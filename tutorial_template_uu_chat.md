# Tutorial: *How to handle LLMs in your research*

{% if department is defined %}
*For the Department of {{ department }}*
{% endif %}

**Course coordinators:** Robert Bagheri, Pablo Mosteiro, Laurence Frank, Ozgur Togay (Department of Methodology, Statistics and Data Science)

**Duration:** {{ duration }}

*This tutorial was drafted with assistance from GPT-5.6-Sol. All examples below are AI generated.*

## Learning objectives

By the end of this tutorial, you will be able to:

1. Use **UU AI-Chat** and choose an appropriate way to organise your work using chats, prompts, personas, projects, and groups.
2. Use AI assistants for common research tasks, including:
   - extracting relevant information from text,
   - coding, classifying, or annotating text,
   - summarising or comparing research material.
3. Turn useful one-off prompts into more reusable research workflows.
4. Critically evaluate AI-generated output and recognise important limitations.

---

## Part 1: Get started with UU AI-Chat

For this tutorial, we will use [**UU AI-Chat**](https://aichat.uu.nl/), Utrecht University's generative AI environment. Sign in with your UU account and start a new chat.

UU AI-Chat provides access to several language models and supports files such as PDFs, Word documents, spreadsheets, presentations, and text files. It also includes tools for web search, data analysis, code execution, image generation, and other tasks.

### Choose the right workspace

You do not need to use every feature in this tutorial. The main options in the left sidebar serve different purposes:

| **Feature** | **Useful when...** |
|--|---|
| **Chat** | You want to ask a question, analyse a file, or carry out a one-off task. |
| **Personas** | You want a reusable AI assistant with a consistent role, instructions, or source material for a recurring task. |
| **Projects** | You want to keep related chats, files, instructions, and other material together for an ongoing research task. |
| **Groups** | You want to share reusable resources such as prompts or personas and collaborate with other UU AI-Chat users. |
| **Prompts** | You want to save an instruction that you expect to use again instead of rewriting it each time. |
\
The chat screen also contains ready-made prompts for common tasks. For example, under **Research** you will find prompts for developing hypotheses or engaging with research literature. Treat these as starting points: inspect what the prompt asks the model to do, adapt it to your research question, and evaluate the result critically.

### Choosing a model

For the exercises below, the default model is usually sufficient. You can browse or switch models using the model button in the bottom-right corner of the chat.

Different models may vary in capability, speed, and computing requirements. UU AI-Chat indicates relative computing or energy use in the model selector. Use a more demanding model when the task benefits from it, rather than automatically choosing the largest option.

### Working with files

When an exercise uses research material, you can either paste the relevant text into the chat or upload the source file. When working from an uploaded document, tell the model clearly which document it should use and what information it should base its answer on.

*Throughout the tutorial, remember that the model's output can be incomplete or incorrect even when it is based on an uploaded source.*

---

## Part 2: Example applications in research

### Example 1: {{ example_1.title }} {.unnumbered .unlisted}

**Scenario:** {{ example_1.scenario }}

Copy this prompt to your AI chat:

```default
{{ example_1.prompt }}
```

**Task:** {{ example_1.task }}

*Note: LLMs can also help you build and refine prompts.*

#### Reflection

{{ example_1.reflection }}

If this is a task you expect to repeat, consider saving the instructions as a **Prompt**. A saved prompt is useful when the instructions stay mostly the same but the input changes.

---

### Example 2: {{ example_2.title }} {.unnumbered .unlisted}

**Scenario:** {{ example_2.scenario }}

Copy this prompt to your AI chat:

```default
{{ example_2.prompt }}
```

**Task:** {{ example_2.task }}

*Note: You can include a codebook in the prompt. Clear definitions, decision rules, and output formats can make repeated classifications more consistent.*

#### Reflection

{{ example_2.reflection }}

For a recurring task with stable instructions to the AI assistant, a **Persona** may be more useful than repeatedly pasting the full setup into a new chat.

---

### Example 3: {{ example_3.title }} {.unnumbered .unlisted}

**Scenario:** {{ example_3.scenario }}

Choose an abstract, article excerpt, or paper that you would like to work with. You can either paste the relevant text into the prompt or upload the document directly.

If the prompt contains `[INSERT TEXT HERE]`:

- replace it with your chosen text; or
- if you uploaded a document, replace it with an instruction such as `Use the uploaded document as the source.`

```default
{{ example_3.prompt }}
```

**Task:** {{ example_3.task }}

#### Reflection

{{ example_3.reflection }}

Compare your result with one of the ready-made **Research** prompts in UU AI-Chat. What assumptions does the built-in prompt make? What would you add or change for your own research question?

If you are working on different parts of the same research project, consider creating a **Project**. Chats within a Project can share context, so you can use separate chats for the literature review, methods, analysis, or other parts while keeping them connected.

{% if example_4 is defined and (example_4.enabled | default(true)) %}
---

### Example 4: {{ example_4.title }} {.unnumbered .unlisted}

**Scenario:** {{ example_4.scenario }}

{{ example_4.instructions }}

**Task:** {{ example_4.task }}

{% if example_4.reflection is defined %}
#### Reflection

{{ example_4.reflection }}
{% endif %}
{% endif %}

---

## Part 3: From one-off chats to reusable workflows

A useful prompt is not always the final form of an AI-assisted workflow. After completing the examples above, choose one prompt or task that you found useful and decide how you would reuse it:

- **Save it as a Prompt** if you mainly want to reuse the same instruction.
- **Create a Persona** if the AI should consistently follow a particular role, method, codebook, or set of instructions.
- **Create a Project** if the work involves multiple related chats, files, or recurring context.
- **Use a Group** if prompts or personas should be shared with collaborators.

**Task:** Pick one example from this tutorial and explain which option you would use for a real research workflow and why.

*The purpose is not to use the most features. Use the simplest setup that keeps the task clear, reproducible, and easy to review.*

---

## Part 4: Understanding model limitations
{% set exercise_counter = namespace(value=1) %}
{% if exercise_1.enabled | default(true) %}
### Exercise {{ exercise_counter.value }}: {{ exercise_1.title }} {.unnumbered .unlisted}

**Task:** {{ exercise_1.task }}

#### Reflection

{{ exercise_1.reflection }}

{% set exercise_counter.value = exercise_counter.value + 1 %}
---
{% endif %}

{% if exercise_2.enabled | default(true) %}
### Exercise {{ exercise_counter.value }}: {{ exercise_2.title }} {.unnumbered .unlisted}

**Task:** {{ exercise_2.task }}

#### Reflection

{{ exercise_2.reflection }}

{% set exercise_counter.value = exercise_counter.value + 1 %}
{% endif %}

---

## Wrap-up: Your personal AI-use checklist

Create your own checklist:

- [ ] I will verify AI-generated facts and interpretations.
- [ ] I will check citations and source claims against the original sources.
- [ ] I will follow UU rules for confidential, sensitive, and personal data.
- [ ] I will disclose AI assistance when required.
- [ ] I will keep human oversight over important research decisions.
- [ ] I will use saved prompts, personas, or projects only when they make my workflow clearer or more reproducible.
- [ ] I will choose a level of model capability and computing use appropriate for the task.

## Next steps

For tasks that need to be applied systematically to large amounts of data, API-based workflows may be more appropriate. The Department of Methodology, Statistics and Data Science provides consultation on AI use in research: [Consultation Data Science / AI](https://www.uu.nl/en/organisation/methodology-and-statistics/training-and-support/consultation-data-science-ai)

More information about the university platform is available on the [UU AI platforms page](https://www.uu.nl/en/organisation/ai-policy/ai-platforms-at-uu).

## Quick reference: BRAVE(R) and FACTS {#braver-facts-reference}

Use BRAVE(R) when formulating or improving a prompt. Use FACTS when evaluating an AI-generated response.


### BRAVE(R) {#braver .unnumbered .unlisted}
+--------------------+----------------------------------------------------------+
| **B: Boundaries**  | Set limits on the format, length, or any other           |
|                    | constraints.                                             |
+--------------------+----------------------------------------------------------+
| **R: Role**        | Identify the role or perspective you want the AI tool    |
|                    | to take.                                                 |
+--------------------+----------------------------------------------------------+
| **A: Audience**    | Specify who the output is intended for to determine the  |
|                    | appropriate tone and style.                              |
+--------------------+----------------------------------------------------------+
| **V: Variables**   | Highlight key details, variables, or points that should  |
|                    | be included in the response.                             |
+--------------------+----------------------------------------------------------+
| **E: Expectations**| Clearly state what you expect the AI to accomplish,      |
|                    | including the intended outcome and purpose.              |
+--------------------+----------------------------------------------------------+
| **R: Refine**      | Provide feedback to improve the output and guide future  |
|                    | interactions.                                            |
+--------------------+----------------------------------------------------------+\

\

### FACTS {#facts .unnumbered .unlisted}
+---------------------+---------------------------------------------------------+
| **F: Focus**        | Focus on the AI's response by breaking it down into its |
|                     | main points and arguments.                              |
+---------------------+---------------------------------------------------------+
| **A: Authenticate** | Authenticate the AI's output by verifying it against    |
|                     | current research and empirical data.                    |
+---------------------+---------------------------------------------------------+
| **C: Critique**     | Critique the response's accuracy, relevance, and depth  |
|                     | in the context of the topic.                            |
+---------------------+---------------------------------------------------------+
| **T: Think**        | Think about the response from different perspectives    |
|                     | and consider its potential impact.                      |
+---------------------+---------------------------------------------------------+
| **S: Scrutinise**   | Scrutinise the AI's conclusions by critically           |
|                     | questioning them and exploring alternative hypotheses   |
|                     | or interpretations.                                     |
+---------------------+---------------------------------------------------------+

## Additional resources

### Example from research: LLM-assisted data annotation {#data-annotation-example}

<details>
<summary><strong>View the research prompt</strong></summary>

LLMs are increasingly used for data annotation because they can make large-scale coding faster and cheaper. Performance still depends on the task, but recent work has found that LLMs can match or outperform human annotators on some social-science text classification tasks (Törnberg, 2024).[^annotation-performance]

The example below comes from [Togay et al. (2026)](https://arxiv.org/abs/2603.23531), which used LLMs to identify the political target and stance in Reddit comments across 138 predefined political targets plus an open-ended category. The best-performing models were comparable to highly trained human annotators.[^target-stance-paper]

This is deliberately much longer than the tutorial prompts above. Research annotation prompts can function like codebooks: they define labels, edge cases, output formats, and examples so that the same rules can be applied consistently across many observations. This prompt was also designed for an earlier generation of models; repeated emphasis such as `**...**` was used to reinforce important instructions and is generally not necessary with newer models.

[^annotation-performance]: Törnberg, P. (2024). *Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages*. Social Science Computer Review. https://doi.org/10.1177/08944393241286471
[^target-stance-paper]: Togay, Ö., Garcia-Bernardo, J., Kunneman, F., & Giachanou, A. (2026). *Large Language Models Unpack Complex Political Opinions through Target-Stance Extraction*. arXiv:2603.23531. https://doi.org/10.48550/arXiv.2603.23531

<pre class="annotation-prompt"><code>{{ data_annotation_prompt_example_html }}</code></pre>

</details>
