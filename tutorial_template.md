# Tutorial: *Working with LLMs in your research*

{% if department is defined %}
*For {{ department }}*
{% endif %}

**Course coordinators:** Robert Bagheri, Pablo Mosteiro, Ozgur Togay (Department of Methodology and Statistics)

**Duration:** {{ duration }}

*Partly generated with help of Qwen/Qwen2.5-7B-Instruct and moonshotai/Kimi-K2-Instruct-0905 via together and groq, respectively (HuggingChat).*

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

1. Go to https://huggingface.co/chat.
2. Click "Sign in with Hugging Face".
3. Create a free account or sign in with an existing account.
4. Once logged in, open a new chat. You can now access various open-source models.
5. For each activity below, copy the prompt from the text box and paste it into your HuggingChat conversation. If the prompt contains a placeholder such as `[INSERT TEXT HERE]`, replace it before sending.

**Why HuggingChat?** Uses open-source models such as Llama, Mistral, and Qwen, does not train models on your conversations. If you already use another chat-based GenAI system, feel free to use that one instead.

---

## Part 2: Example applications in research

### Example 1: {{ example_1.title }}

**Scenario:** {{ example_1.scenario }}

Copy this prompt to HuggingChat:

```text
{{ example_1.prompt }}
```

***NOTE***: Sometimes HuggingChat gets stuck "thinking". If that happens, do one of the following (or try both):
1. Open up the "thinking" window and read the last bit that is written down before the end of the box
1. Ask the model to provide you with an answer

**Task:** {{ example_1.task }}

#### Reflection

{{ example_1.reflection }}

---

### Example 2: {{ example_2.title }}

**Scenario:** {{ example_2.scenario }}

Copy this prompt to HuggingChat:

```text
{{ example_2.prompt }}
```

**Task:** {{ example_2.task }}

#### Reflection

{{ example_2.reflection }}

---

### Example 3: {{ example_3.title }}

**Scenario:** {{ example_3.scenario }}

Copy this prompt to HuggingChat:

```text
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