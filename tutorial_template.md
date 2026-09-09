# Tutorial: *How to handle LLMs in your research*

{% if department is defined %}
*For the Department of {{ department }}*
{% endif %}

**Course coordinators:** Robert Bagheri, Pablo Mosteiro, Ozgur Togay (Department of Methodology, Statistics and Data Science)

**Duration:** {{ duration }}

*This tutorial was drafted with assistance from GPT-5.6-Sol. All examples below are AI generated.*

## Learning objectives

By the end of this tutorial, you will be able to:

1. Choose an AI chat platform and model appropriate for your task.
2. Use LLMs for common research tasks, including:
   - extracting relevant information from text,
   - coding, classifying, or annotating text,
   - summarizing or comparing research material.
3. Understand model limitations through exercises.

---

## Part 1: Choose an AI chat platform and model

For the exercises below, choose one of the privacy-conscious platforms in the table. If you are working in a pair or group, try different models and compare the outputs. If you already use another chat-based GenAI system, such as ChatGPT or Claude, feel free to use that instead.

*When comparing outputs from different platforms, keep in mind that differences may come from the platform as well as the underlying model.*

| **Feature** | [**HuggingChat**](#use-huggingchat) | [**Duck.ai**](#use-duckai) | [**Lumo**](#use-lumo) |
|---|---|---|---|
| **Sign-up** | Free account required | Not required | Not required |
| **Model choice** | Many open models | Few open and proprietary models | Automatic model assignment |
| **Privacy** | No training on user data; retention policies may vary | No training on user data; no retention | No training on user data; no retention, hosted in the EU |
| **File support** | No PDFs; text and images vary by model | PDFs up to 15 pages, text and images | PDFs, large documents, text and images |

<details id="use-huggingchat">
<summary><strong>Use HuggingChat</strong></summary>

1. Choose one of the suggested models:
   - **Small:** [Qwen 3.5 9B](https://huggingface.co/chat/models/Qwen/Qwen3.5-9B), [IBM Granite 4.2 3B](https://huggingface.co/chat/models/ibm-granite/granite-4.2-3b) (*XSmall*), [Llama 3.1 8B](https://huggingface.co/chat/models/meta-llama/Llama-3.1-8B-Instruct) (*outdated*)
   *Llama 3.1 is included as an older example to show how quickly models have advanced.*
   - **Medium:** [Qwen 3.8 27B](https://huggingface.co/chat/models/Qwen/Qwen3.8-27B) (*Great baseline, can be run locally*), [Muse Glimmer 30B](https://huggingface.co/chat/models/meta-models/Muse-Glimmer-30B), [Gemma 4 31B](https://huggingface.co/chat/models/google/gemma-4-31B-it)
   - **State-of-the-art:** [GLM 5.3 744B](https://huggingface.co/chat/models/zai-org/GLM-5.3), [Kimi K3](https://huggingface.co/chat/models/moonshotai/Kimi-K3), [DeepSeek V4 Flash](https://huggingface.co/chat/models/deepseek-ai/DeepSeek-V4-Flash-0731) (Note: These models will consume your usage limits quickly, but they provide performance akin to flagship proprietary models such as GPT-5.6-Sol and Claude Opus)
2. Click **Sign in with Hugging Face**.
3. Create a free account or sign in with an existing account.
4. If you are redirected to the Hugging Face homepage after creating your account, return to chat with the model link above.
5. Click **Settings** in the bottom-left menu and enable **Paste text directly**.
6. You can change models at any time by clicking the model name at the top of the chat.

</details>

<details id="use-duckai">
<summary><strong>Use Duck.ai</strong></summary>

1. Go to [Duck.ai](https://duck.ai/). No account is required.
2. Click the current model name in the sidebar to select a model. For this tutorial, you could try:
   - **Open medium:** Gemma 4 31B
   - **Large open:** gpt-oss 120B, Mistral Small 4
   - **Efficient proprietary:** GPT-5.4 mini
   - **Large proprietary:** GPT-5.6 Luna
3. You can attach a PDF or other supported file directly to the conversation.

*Most proprietary models do not share their parameter sizes, so size-based comparisons are less straightforward.*

</details>

<details id="use-lumo">
<summary><strong>Use Lumo</strong></summary>

1. Go to [Lumo](https://lumo.proton.me/). You can start a chat as a guest without creating an account.
2. Click the current version name in the bottom-right to change between Lite and Max processing, which automatically changes the backend model.
3. You can upload PDFs and other supported documents directly to the conversation.

</details>

As a rule of thumb, newer and larger models tend to perform better, but they also use more computing resources and may reach usage limits faster. When working in a group, comparing models of different sizes or from different developers can help you see how much the choice of model affects the result. More detail is available in the [model-selection reference](#model-selection-reference).

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

---

### Example 2: {{ example_2.title }} {.unnumbered .unlisted}

**Scenario:** {{ example_2.scenario }}

Copy this prompt to your AI chat:

```default
{{ example_2.prompt }}
```

**Task:** {{ example_2.task }}

*Note: You can include a codebook in the prompt. Clearer definitions lead to more consistent outputs, and current LLMs can follow detailed instructions and output schemas.*

#### Reflection

{{ example_2.reflection }}

---

### Example 3: {{ example_3.title }} {.unnumbered .unlisted}

**Scenario:** {{ example_3.scenario }}

Find an abstract or a short article excerpt that you would like to summarize. Copy the prompt below into your AI chat, replace `[INSERT TEXT HERE]` with your chosen text, and then send it.

```default
{{ example_3.prompt }}
```

**Task:** {{ example_3.task }}

#### Reflection

{{ example_3.reflection }}

{% if example_3.extension is defined %}
#### {{ example_3.extension.title }} {.unnumbered .unlisted}

{{ example_3.extension.text }}
{% endif %}

---

## Part 3: Understanding model limitations
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

- [ ] I will verify AI-generated facts.
- [ ] I will not input sensitive, confidential, or personally identifiable information.
- [ ] I will disclose AI assistance in my work.
- [ ] I will check citations and source claims manually.
- [ ] I will choose open-source models when possible.
- [ ] I will keep human oversight over critical decisions.

## Next steps

The tasks in this tutorial can also be applied and automated at larger scale through API-based workflows.

The Department of Methodology, Statistics and Data Science provides consultation on AI use in research: [Consultation Data Science / AI](https://www.uu.nl/en/organisation/methodology-and-statistics/training-and-support/consultation-data-science-ai)

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
| **C: Critique**     | Critique the response's accuracy, relevance, and depth   |
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

### Choosing a model {#model-selection-reference}

<details>
<summary><strong>How do model size and architecture affect model choice?</strong></summary>

As a rule of thumb, newer and larger models tend to perform better. Open models often report their size in the model name. For example, the **27B** in Qwen3.8-27B means that the model has approximately 27 billion parameters.

Version numbers can also indicate recency, but only within the same model family. For example, GLM-5.2 is newer than GLM-5. However, version numbers are not comparable across families: GLM-4 is not newer than Qwen3.8. Models from the same generation and size range often perform similarly on general tasks, although some are stronger in particular languages, coding, reasoning, or multimodal tasks. You can search online for benchmarks on various tasks.

These are some of the established current open model families:

* Alibaba's **Qwen**
* Z.ai's **GLM**
* Google's **Gemma**

The newest and largest models perform the best, but they are not always the right tool for every task. They generally respond more slowly, require a lot more computing power, and use more of your token budget when accessed through platforms such as HuggingChat. A practical approach is to decide on the acceptable level of performance for your task and use the smallest model that meets it. 

**A note on Mixture-of-Experts models**

Not every number in a model name refers to the same thing. A conventional, or *dense*, model uses approximately all of its parameters when generating each token. A **Mixture-of-Experts (MoE)** model contains several specialised groups of parameters, called experts, but activates only a subset of them at a time. This reduces the computation needed for each response, although the complete model still has to be stored in memory.

For example:

* **Llama-4-Scout-17B-16E** has 16 experts, approximately 17 billion active parameters, and 109 billion parameters in total.
* **Qwen3.6-35B-A3B** has 35 billion parameters in total but activates approximately 3 billion at a time. Here, **A3B** means 3 billion active parameters.

Developers are constantly experimenting with different architectures, for example, in **Gemma 4 E2B**, the **E** means *effective*. The model has approximately 2.3 billion effective parameters, but around 5.1 billion parameters when its embedding tables are included. This is an efficiency technique rather than a Mixture-of-Experts architecture.

The naming conventions are not fully standardised, so check the model card when the numbers are unclear.

**A note on quantization**

Open models are also frequently modified to make them smaller and easier to run. The most common method is **quantization**, which stores model weights at a lower numerical precision.

Models are commonly released in formats such as **floating point 32 (FP32**), **FP16**, or **BF16**. Quantized versions may instead use **FP8**, **INT8**, **INT4**, or labels such as **Q4**, **Q5**, **Q6**, and **Q8**. These numbers refer roughly to how many bits are used to represent each weight.

Lower-bit quantization reduces memory use and may make the model faster, but more aggressive quantization can also reduce output quality. Eight-bit and FP8 versions often remain close to the original model, while six-bit and four-bit versions can still work well depending on the model and task. Very low-bit versions involve a greater trade-off.

When using HuggingChat, you generally do not need to choose a quantization yourself. This becomes more relevant when running it ***locally***.

</details>


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

## Troubleshooting {#troubleshooting}

<details>
<summary><strong>A pasted prompt appears as “clipboard content” or cannot be sent</strong></summary>

HuggingChat may treat a long pasted prompt as an attached file. To paste it directly into the message box:

1. Click **Settings** in the bottom-left menu.

![Open Settings from the bottom-left menu.](../../tutorial_assets/images/settings.png){width=50% fig-align="center"}

2. Enable **Paste text directly** under **Application Settings**.

![Enable Paste text directly.](../../tutorial_assets/images/app_settings.png){width=95% fig-align="center"}

Paste the prompt again after enabling the setting.

</details>

<details>
<summary><strong>You are redirected to the HuggingFace homepage after signing in</strong></summary>

Open the menu in the top-right corner and select **HuggingChat**.

![Open the Hugging Face menu and select HuggingChat.](../../tutorial_assets/images/huggingface_to_chat.png){width=100% fig-align="center"}

You can also use the links under [Use Hugging Chat](#use-huggingchat) to navigate to chat directly.

</details>

<details>
<summary><strong>The model remains stuck on “Reasoning,” becomes unavailable, or stops responding</strong></summary>

Try the following steps in order:

1. Stop the response, if the stop button is available, and send the prompt again.
2. Refresh the page or start a new conversation.
3. Select a different model by clicking the model name at the top of the chat.
4. If the problem continues, return to [Part 1](#part-1-choose-an-ai-chat-platform-and-model) and continue with Duck.ai or Lumo.

Copy your prompt before refreshing the page or changing platforms.

</details>

<details>
<summary><strong>HuggingChat says that a usage or rate limit has been reached</strong></summary>

Try selecting a different model. If the limit continues, return to [Part 1](#part-1-choose-an-ai-chat-platform-and-model) and continue the exercises with Duck.ai or Lumo instead.

Copy your prompt before changing platforms.

</details>


