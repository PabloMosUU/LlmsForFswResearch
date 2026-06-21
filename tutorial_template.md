# Tutorial: *How to handle LLMs in your research*

{% if department is defined %}
*For the Department of {{ department }}*
{% endif %}

**Course coordinators:** Robert Bagheri, Pablo Mosteiro, Ozgur Togay (Department of Methodology and Statistics)

**Duration:** {{ duration }}

*Parts of this tutorial were drafted with assistance from Qwen/Qwen2.5-7B-Instruct and moonshotai/Kimi-K2-Instruct-0905 via HuggingChat, using Together and Groq as providers. The examples are fictional and were generated with GPT-5.5.*

## Learning objectives

By the end of this tutorial, you will be able to:

1. Set up an account on a privacy-conscious LLM platform.
2. Use LLMs for common research tasks, including:
   - extracting relevant information from text,
   - coding, classifying, or annotating text,
   - summarizing or comparing research material.
3. Understand model limitations through exercises.

---

## Part 1: Setting up HuggingChat

1. Go to [HuggingChat](https://huggingface.co/chat/models/Qwen/Qwen3.6-27B).
2. Click **Sign in with Hugging Face**.
3. Create a free account or sign in with an existing account.
4. If you are redirected to the HuggingFace homepage after creating your account, open the link in step 1 again to start a chat with Qwen3.6-27B. You can select a different model by clicking the model name at the top of the chat.
5. Click **Settings** in the bottom-left menu and enable **Paste text directly**.
6. For each activity below, copy the prompt from the text box and paste it into your HuggingChat conversation. If the prompt contains a placeholder such as `[INSERT TEXT HERE]`, replace it before sending.

**Why HuggingChat?** Hosts open models such as Llama, Mistral, and Qwen, and does not train models on your conversations. If you already use another chat-based GenAI system, feel free to use that one instead.

---

## Part 2: Example applications in research

### Example 1: {{ example_1.title }}

**Scenario:** {{ example_1.scenario }}

Copy this prompt to HuggingChat:

```default
{{ example_1.prompt }}
```

**Task:** {{ example_1.task }}

*Note: LLMs can also help you build and refine prompts.*

#### Reflection

{{ example_1.reflection }}

---

### Example 2: {{ example_2.title }}

**Scenario:** {{ example_2.scenario }}

Copy this prompt to HuggingChat:

```default
{{ example_2.prompt }}
```

**Task:** {{ example_2.task }}

*Note: You can include a codebook in the prompt. Clearer definitions lead to more consistent outputs, and current LLMs can follow detailed instructions and output schemas.*

#### Reflection

{{ example_2.reflection }}

---

### Example 3: {{ example_3.title }}

**Scenario:** {{ example_3.scenario }}

Find an abstract or a short article excerpt that you would like to summarize. Copy the prompt below into HuggingChat, replace `[INSERT TEXT HERE]` with your chosen text, and then send it.

```default
{{ example_3.prompt }}
```

**Task:** {{ example_3.task }}

#### Reflection

{{ example_3.reflection }}

---

## Part 3: Understanding model limitations

### Exercise 1: {{ exercise_1.title }}

**Task:** {{ exercise_1.task }}

#### Reflection

{{ exercise_1.reflection }}

---

### Exercise 2: {{ exercise_2.title }}

**Task:** {{ exercise_2.task }}

#### Reflection

{{ exercise_2.reflection }}

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

The Department of Methodology and Statistics provides consultation on AI use in research: [Consultation Data Science / AI](https://www.uu.nl/en/organisation/methodology-and-statistics/training-and-support/consultation-data-science-ai)

## Quick reference: BRAVE(R) and FACTS {#braver-facts-reference}

Use BRAVE(R) when formulating or improving a prompt. Use FACTS when evaluating an AI-generated response.


### BRAVE(R) {#braver}
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

### FACTS {#facts}
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

## Troubleshooting HuggingChat {#troubleshooting}

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

You can also open [HuggingChat with Qwen3.6-27B](https://huggingface.co/chat/models/Qwen/Qwen3.6-27B) directly.

</details>

<details>
<summary><strong>The model remains stuck on “Reasoning,” becomes unavailable, or stops responding</strong></summary>

Try the following steps in order:

1. Stop the response, if the stop button is available, and send the prompt again.
2. Refresh the page or start a new conversation.
3. Select a different model by clicking the model name at the top of the chat.
4. If the problem continues, use one of the alternative platforms listed below.

Copy your prompt before refreshing the page or changing platforms.

</details>

<details>
<summary><strong>HuggingChat says that a usage or rate limit has been reached</strong></summary>

You can complete the exercises on another platform. Free alternatives include:

- [Duck.ai](https://duck.ai/) hosts several models, GPT-OSS-120B is recommended for these exercises.
- [Qwen Chat](https://chat.qwen.ai/) hosts Qwen models.
- [Z.ai Chat](https://chat.z.ai/) hosts GLM models.
- [Le Chat by Mistral AI](https://chat.mistral.ai/chat) provides access to its basic model without an account.

You can also use a proprietary chat assistant:

- [Gemini](https://gemini.google.com/app)
- [ChatGPT](https://chatgpt.com/)

</details>

<details>
<summary><strong>How should I choose a model?</strong></summary>

As a rule of thumb, newer and larger models tend to perform better. Open models often report their size in the model name. For example, the **27B** in Qwen3.6-27B means that the model has approximately 27 billion parameters.

Version numbers can also indicate recency, but only within the same model family. For example, GLM-5.2 is newer than GLM-5. However, version numbers are not comparable across families: GLM-4 is not older than Qwen3.6. Models from the same generation and size range often perform similarly on general tasks, although some are stronger in particular languages, coding, reasoning, or multimodal tasks. You can search online for benchmarks on various tasks.

These are some of the established current open model families:

* Alibaba's **Qwen 3.6**
* Z.ai's **GLM 5**
* Google's **Gemma 4**

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

When using HuggingChat, you generally do not need to choose a quantization yourself. This becomes more relevant when running it locally.

</details>
