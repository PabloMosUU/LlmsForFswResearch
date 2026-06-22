# Tutorial: *How to handle LLMs in your research*

*For the Department of Clinical Child & Family Studies*

**Course coordinators:** Ayoub Bagheri, Pablo Mosteiro (Department of Methodology and Statistics)

**Duration:** 1 hour

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

**Why HuggingChat?** Hosts open models such as Llama, Mistral, and Qwen, and does not train models on your conversations.

---

## Part 2: Example applications in research

### Example 1: Extract information from text

**Scenario:** You have a short case description and want to extract information relevant to your research.

Copy this prompt to HuggingChat:

```default
Extract the key information from the case below.

Case:
A 12-year-old child has recently become more withdrawn at school. A teacher reports that the child avoids group activities and has had several conflicts with classmates. The parent says that the child has been sleeping poorly since the parents separated six months ago. The child says, "I do not want to pick sides, but everyone keeps asking me what I want." The school is considering whether extra support is needed, but no formal assessment has been conducted.

Provide:
1. The main issue in one sentence.
2. The child-level, family-level, school-level, and peer-level factors mentioned in the text.
3. Exact words or phrases from the case that support each point.
4. Any uncertainty, ambiguity, or missing context.
5. What would need manual verification before this could be used in research, assessment, or policy advice.

Stay close to the text. Do not diagnose the child. Do not infer abuse, disorder, trauma, or risk level unless the text explicitly supports it. Use cautious language.
```

**Task:** Use the [BRAVE(R)](#braver) framework to analyze the prompt, then use the [FACTS](#facts) framework to analyze the response. Discuss your evaluation with a classmate.

*Note: LLMs can also help you build and refine prompts.*

#### Reflection

1. Did the model separate child, family, school, and peer factors clearly?
2. Did it quote evidence from the case?
3. Did it avoid diagnosis or unsupported risk claims?
4. What information would a researcher or practitioner still need to check manually?

---

### Example 2: Code, annotate or classify text

**Scenario:** You need to code an interview response using a codebook.

Copy this prompt to HuggingChat:

```default
Code the following interview excerpt using the codebook below.

Interview question:
"What has changed for the child or family in the past few months?"

Response:
"Since the move, he gets angry much faster. At school they say he interrupts other children and walks out when things get too much. At home he wants to stay close to me all the time. I try to keep routines stable, but I am also stressed and sometimes I just give in because I do not want another argument."

Codebook:
- Child emotional or behavioural difficulties: signs of distress, anger, withdrawal, anxiety, impulsivity, or problems with regulation.
- Parenting stress or coping: parent reports of stress, exhaustion, uncertainty, inconsistent responses, or attempts to manage the situation.
- School or peer functioning: references to classroom behaviour, peer relationships, teacher concerns, or school participation.
- Family transition or environmental stressor: references to divorce, bereavement, illness, moving, poverty, migration, family conflict, or other contextual stressors.
- Protective factor or support: references to routines, supportive relationships, help-seeking, services, or strategies that may support the child or family.
- Ambiguous or insufficient evidence: use this when the excerpt does not clearly support a code.

Provide a table with:
1. Text segment.
2. Assigned code or codes.
3. Exact supporting words.
4. Confidence: high, medium, or low.
5. Alternative possible code.
6. Brief justification.

Do not force a code when the evidence is weak. Do not diagnose. Mark ambiguity explicitly.
```

**Task:** Use the [FACTS](#facts) framework to analyze the response. Discuss your evaluation with a classmate.

*Note: You can include a codebook in the prompt. Clearer definitions lead to more consistent outputs, and current LLMs can follow detailed instructions and output schemas.*

#### Reflection

1. Did the model apply the codebook consistently?
2. Did it separate child behaviour, parenting stress, school functioning, and contextual stressors?
3. Did it over-interpret the excerpt or imply diagnosis?
4. Would the coding be reproducible if another researcher used the same prompt?

---

### Example 3: Summarize or compare research

**Scenario:** You need to quickly understand whether an article is relevant to your research.

Find an abstract or a short article excerpt that you would like to summarize. Copy the prompt below into HuggingChat, replace `[INSERT TEXT HERE]` with your chosen text, and then send it.

```default
Summarize the research abstract below for a Clinical Child & Family Studies researcher deciding whether the article is relevant to their research.

Abstract:
[INSERT ABSTRACT TEXT HERE]

Provide:
1. The main research question.
2. The target group or population studied.
3. The study design and method.
4. The main findings.
5. Any findings relevant to child development, parenting, family context, school or peer environment, assessment, prevention, or intervention.
6. Limitations explicitly mentioned in the abstract.
7. Claims that require reading the full paper before trusting.
8. Three search terms for finding related work.

Use only information from the abstract. Do not invent sample details, measures, effect sizes, mechanisms, clinical implications, or policy implications. Mark uncertain points clearly.
```

**Task:** Use the [FACTS](#facts) framework to analyze the response. Discuss your evaluation with a classmate.

#### Reflection

1. Did the model distinguish research question, method, findings, and limitations?
2. Did it avoid adding implications that were not in the abstract?
3. Did it identify what would require reading the full paper?
4. Would this help you decide whether the article is relevant to your work?

---

## Part 3: Understanding model limitations

### Exercise 1: Identifying hallucinations

**Task:** Ask the model to review recent literature in a specific field. For example:

What are the latest validated AI-based screening tools for detecting psychosocial problems in children and families, published in 2026?

Then check the answer against reliable external sources such as Google Scholar, PubMed, Web of Science, Scopus, or official project pages.

#### Reflection

1. Do the named studies, tools, or interventions actually exist?
2. Are the authors, publication years, journals, and institutions correct?
3. Does the model confuse proposed tools with validated instruments?
4. Does it imply clinical usefulness or diagnostic validity without evidence?
5. What wording would make the prompt safer and more precise?

Document any fabricated, unverifiable, or overstated claims.

---

### Exercise 2: Bias detection

**Task:** Compare responses to these two prompts:

Prompt A: Describe the typical profile of a high-risk family.

Prompt B: Describe how risks and protective factors in child development can vary across family structures, socioeconomic contexts, cultures, schools, peer groups, and service systems.

Pay attention to what the model treats as normal, risky, problematic, or protective.

#### Reflection

1. What assumptions does the model make about families, parents, children, or social background?
2. Does it stereotype particular family structures, cultures, or socioeconomic groups?
3. Does it balance risk factors with protective factors?
4. Does it distinguish individual, family, school, peer, and policy-level factors?
5. How could the prompt be revised to reduce stigmatizing or overgeneralized output?

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

|---|---|
| **B: Boundaries** | Set limits on the format, length, or any other constraints. |
| **R: Role** | Identify the role or perspective you want the AI tool to take. |
| **A: Audience** | Specify who the output is intended for to determine the appropriate tone and style. |
| **V: Variables** | Highlight key details, variables, or points that should be included in the response. |
| **E: Expectations** | Clearly state what you expect the AI to accomplish, including the intended outcome and purpose. |
| **R: Refine** | Provide feedback to improve the output and guide future interactions. |

### FACTS {#facts}

|---|---|
| **F: Focus** | Focus on the AI's response by breaking it down into its main points and arguments. |
| **A: Authenticate** | Authenticate the AI's output by verifying it against current research and empirical data. |
| **C: Critique** | Critique the response's accuracy, relevance, and depth in the context of the topic. |
| **T: Think** | Think about the response from different perspectives and consider its potential impact. |
| **S: Scrutinise** | Scrutinise the AI's conclusions by critically questioning them and exploring alternative hypotheses or interpretations. |

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