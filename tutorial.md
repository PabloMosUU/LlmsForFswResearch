# Tutorial for *How to handle LLMs in your research*

**Course Coordinators**: Ayoub Bagheri, Pablo Mosteiro (Department of Methodology and Statistics)

**Duration**: 1 hour

*Partly generated with help of Qwen/Qwen2.5-7B-Instruct and moonshotai/Kimi-K2-Instruct-0905 via together and groq, respectively (HuggingChat).*

## Learning Objectives
By the end of this tutorial, you will be able to:

1. Set up accounts on privacy-focused LLM platforms
2. Apply LLMs to a common NLP task
3. Use LLMs for literature review and summarization
4. Understand model limitations through practical exercises

## Part 1: Setting Up Accounts on Privacy-Focused Platforms

### HuggingChat (Open-source alternative)

1. Navigate to https://huggingface.co/chat
2. Click "Sign in with Hugging Face" 
3. Create a free account or sign in
4. Once logged in, you can access various open-source models

**Why HuggingChat?** Uses open-source models like Llama, Mistral, and Qwen - no data training on your conversations.

## Part 2: Example Usage from NLP

### Task 1: Sentiment Analysis of Therapy Session Transcripts

**Scenario**: You have transcripts from therapy sessions and want to understand emotional patterns.

Copy this prompt to HuggingChat:

```
Analyze the following therapy session excerpt for emotional tone and therapeutic indicators:

Client: "I've been feeling really anxious about going to work lately. It's like my stomach is in knots every Sunday night."
Therapist: "Can you tell me more about what happens in your body when you think about work?"
Client: "I feel tense, and I start worrying about everything that could go wrong."

Provide:
1. Overall emotional sentiment (scale 1-10, with 10 being most distressed)
2. Key therapeutic themes present
3. Therapeutic alliance indicators
4. Suggestions for therapeutic focus

Use clinical psychology terminology and maintain professional objectivity.
```

**Task**: Use the BRAVE(R) framework to analyze the prompt, then use the FACTS framework to analyze the response. Discuss this with a classmate.

### Task 2: Coding Qualitative Interview Data

**Scenario**: You need to code open-ended responses from participants about their mental health experiences.

Copy this prompt to HuggingChat:

```
Code the following interview response using thematic analysis:

Interview question: "How has anxiety affected your daily life?"
Response: "Well, it's like I'm constantly on edge. I can't concentrate at work because I'm worried something bad will happen. My partner says I seem distant, but I just feel overwhelmed all the time. Sometimes I can't sleep because my mind won't stop racing."

Provide:
1. Main themes (3-5 themes)
2. Sub-themes for each main theme
3. Relevant quotes for each theme
4. Brief description of each theme's meaning

Use psychology research terminology and maintain confidentiality.
```

**Task**: Use the FACTS framework to analyze the response. Discuss this with a classmate.

## Part 3: Using LLMs for Literature Review and Summarization

### Task 3: Summarizing Research Articles

**Scenario**: You need to quickly understand key findings from multiple papers.

Use this prompt with a real abstract from PubMed or Google Scholar:

```
Summarize this research article abstract in 3 bullet points:

[INSERT ABSTRACT TEXT HERE]

Provide:
1. Main research question and methodology
2. Key findings relevant to clinical practice
3. Limitations and implications for future research

Focus on information that would help a clinical psychologist decide whether to read the full paper.
```

**Task**: Use the FACTS framework to analyze the response. Discuss this with a classmate.

## Part 4: Understanding Model Limitations

### Exercise 1: Identifying Hallucinations

**Task**: Ask a model: ```What are the latest studies on virtual reality therapy for PTSD published in 2026?```

Then check:

1. Do the studies actually exist? (look up the titles in a search engine)
2. Are the journal names real?
3. Do the author names match real researchers in the field?

Document any fabricated information.

*Note: HuggingChat is especially open about not having information, so if you don't find any hallucinations, you may consider using a commercial tool for comparison.*

### Exercise 2: Bias Detection

**Task**: Compare responses to these two prompts:

Prompt A: ```Describe the typical profile of someone with depression```

Prompt B: ```Describe how depression manifests across different cultures and genders```

What differences do you notice? What assumptions does the model make?

## Wrap-Up and Next Steps

### Your Personal AI Use Guidelines

Create your own checklist:

- [ ] I will verify all AI-generated facts
- [ ] I will not input personally identifiable information
- [ ] I will disclose AI assistance in my work
- [ ] I will choose open-source models when possible
- [ ] I will maintain human oversight of critical decisions
