from __future__ import annotations

import argparse
import copy
import subprocess
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined


ROOT = Path(__file__).resolve().parents[1]

TEMPLATE_NAME = "tutorial_template.md"
DEFAULTS_PATH = ROOT / "tutorial_prompts" / "default.yml"
DEPARTMENTS_DIR = ROOT / "tutorial_prompts" / "departments"
TUTORIALS_DIR = ROOT / "tutorials"

REQUIRED_TOP_LEVEL_FIELDS = [
    "duration",
    "example_1",
    "example_2",
    "example_3",
    "exercise_1",
    "exercise_2",
]

REQUIRED_EXAMPLE_FIELDS = ["title", "scenario", "prompt", "task", "reflection"]
REQUIRED_EXERCISE_FIELDS = ["title", "task", "reflection"]

QUARTO_FRONT_MATTER = """---
format:
  html:
    toc: true
    embed-resources: true
---

```{=html}
<style>
h3 {
  margin-bottom: 0.85rem;
}

h3 + p {
  margin-top: 0;
}
</style>
```
"""

def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping/object.")

    return data


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """
    Recursively merge two dictionaries.

    Values in override replace values in base.
    Nested dictionaries are merged recursively.
    Lists and strings are replaced as complete values.
    """
    result = copy.deepcopy(base)

    for key, override_value in override.items():
        base_value = result.get(key)

        if isinstance(base_value, dict) and isinstance(override_value, dict):
            result[key] = deep_merge(base_value, override_value)
        else:
            result[key] = copy.deepcopy(override_value)

    return result


def validate_slug(slug: str, source: Path) -> None:
    if not isinstance(slug, str) or not slug.strip():
        raise ValueError(f"{source}: slug must be a non-empty string.")

    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789_-")
    unsafe_chars = set(slug) - allowed

    if unsafe_chars:
        raise ValueError(
            f"{source}: slug contains unsafe characters: {sorted(unsafe_chars)}. "
            "Use lowercase letters, numbers, underscores, or hyphens."
        )


def validate_config(config: dict[str, Any], source: Path) -> None:
    missing = [field for field in REQUIRED_TOP_LEVEL_FIELDS if field not in config]
    if missing:
        raise ValueError(f"{source}: merged config is missing fields: {missing}")

    for example_name in ["example_1", "example_2", "example_3"]:
        example = config[example_name]

        if not isinstance(example, dict):
            raise ValueError(f"{source}: {example_name} must be a mapping/object.")

        missing_fields = [
            field for field in REQUIRED_EXAMPLE_FIELDS if field not in example
        ]

        if missing_fields:
            raise ValueError(
                f"{source}: merged {example_name} is missing fields: "
                f"{missing_fields}"
            )

    for exercise_name in ["exercise_1", "exercise_2"]:
        exercise = config[exercise_name]

        if not isinstance(exercise, dict):
            raise ValueError(f"{source}: {exercise_name} must be a mapping/object.")

        missing_fields = [
            field for field in REQUIRED_EXERCISE_FIELDS if field not in exercise
        ]

        if missing_fields:
            raise ValueError(
                f"{source}: merged {exercise_name} is missing fields: "
                f"{missing_fields}"
            )

    if "slug" in config:
        validate_slug(config["slug"], source)


def load_merged_config(slug: str) -> dict[str, Any]:
    defaults = load_yaml(DEFAULTS_PATH)

    department_path = DEPARTMENTS_DIR / f"{slug}.yml"
    if not department_path.exists():
        raise FileNotFoundError(f"No department config found: {department_path}")

    department_overrides = load_yaml(department_path)

    # The file name is the fallback slug.
    department_overrides.setdefault("slug", slug)

    merged = deep_merge(defaults, department_overrides)
    validate_config(merged, department_path)

    return merged


def build_one(slug: str) -> dict[str, Path]:
    config = load_merged_config(slug)

    env = Environment(
        loader=FileSystemLoader(ROOT),
        undefined=StrictUndefined,
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = env.get_template(TEMPLATE_NAME)
    markdown_output = template.render(**config)

    tutorial_dir = TUTORIALS_DIR / config["slug"]
    tutorial_dir.mkdir(parents=True, exist_ok=True)

    md_path = tutorial_dir / "tutorial.md"
    qmd_path = tutorial_dir / "tutorial.qmd"

    md_path.write_text(markdown_output, encoding="utf-8")
    qmd_path.write_text(QUARTO_FRONT_MATTER + markdown_output, encoding="utf-8")

    return {
        "md": md_path,
        "qmd": qmd_path,
    }

def render_html(qmd_path: Path) -> Path:
    subprocess.run(
        ["quarto", "render", str(qmd_path), "--to", "html"],
        check=True,
        cwd=ROOT,
    )

    return qmd_path.with_suffix(".html")

def available_departments() -> list[str]:
    return sorted(path.stem for path in DEPARTMENTS_DIR.glob("*.yml"))


def validate_all() -> None:
    if not DEFAULTS_PATH.exists():
        raise FileNotFoundError(f"Missing defaults file: {DEFAULTS_PATH}")

    if not (ROOT / TEMPLATE_NAME).exists():
        raise FileNotFoundError(f"Missing template file: {ROOT / TEMPLATE_NAME}")

    departments = available_departments()
    if not departments:
        raise FileNotFoundError(f"No department configs found in {DEPARTMENTS_DIR}")

    for slug in departments:
        load_merged_config(slug)

    print("All merged tutorial configs are valid.")


def build_all() -> list[dict[str, Path]]:
    departments = available_departments()
    if not departments:
        raise FileNotFoundError(f"No department configs found in {DEPARTMENTS_DIR}")

    return [build_one(slug) for slug in departments]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--department",
        required=True,
        help="Department slug, e.g. kp, isw, or all.",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate merged configs without writing output files.",
    )
    parser.add_argument(
        "--render",
        action="store_true",
        help="Render generated QMD files to HTML using Quarto.",
    )

    args = parser.parse_args()

    if args.validate_only:
        if args.department == "all":
            validate_all()
        else:
            load_merged_config(args.department)
            print(f"Merged config for {args.department} is valid.")
        return

    if args.department == "all":
        outputs = build_all()
    else:
        outputs = [build_one(args.department)]

    rendered_html = []

    if args.render:
        for output in outputs:
            rendered_html.append(render_html(output["qmd"]))

    print("Built tutorial files:")
    for output in outputs:
        print(f"- {output['md'].relative_to(ROOT)}")
        print(f"- {output['qmd'].relative_to(ROOT)}")

    if args.render:
        print("Rendered HTML files:")
        for html_path in rendered_html:
            print(f"- {html_path.relative_to(ROOT)}")

if __name__ == "__main__":
    main()