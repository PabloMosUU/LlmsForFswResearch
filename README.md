# How to handle LLMs in your research

## Building the tutorials

The tutorials are generated from three layers:

1. `tutorial_template.md` defines the shared structure and wording used by all tutorials.
2. `defaults.yml` contains values used across departments unless they are overridden.
3. Each department has its own YAML file containing department-specific examples, prompts, tasks, and reflections.

The build script combines the template, the defaults, and the selected department configuration.

To add a new department, create a new YAML file in the department configuration folder. Use an existing department file as a starting point and give the new department a unique slug (shorthand).

### Build locally

From the repository root, build one department with:

```bash
python scripts/build_tutorial.py --department <department-slug> --render
```

For example:

```bash
python scripts/build_tutorial.py --department iss --render
```

To build all department tutorials:

```bash
python scripts/build_tutorial.py --department all --render
```

The generated Markdown, Quarto, and HTML files are written to the corresponding folders under `tutorials/`.

The `--render` option runs Quarto after generating the tutorial files. Quarto must therefore be installed and available from the command line.

### Build with GitHub Actions

The tutorials can also be built through the GitHub Actions workflow:

1. Open the repository on GitHub.
2. Go to the **Actions** tab.
3. Select the tutorial-building workflow.
4. Click **Run workflow**.
5. Select the branch and, where applicable, the department to build.
6. Start the workflow.

After the workflow finishes, open the completed run and download the generated tutorials from the **Artifacts** section. 
New department slugs need to be added to `.github/workflows/build_tutorial.yml`.

