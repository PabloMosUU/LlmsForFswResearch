# Tutorial: *How to handle LLMs in your research*

*For the Department of Development & Education of Youth in Diverse Societies*

**Course coordinators:** Robert Bagheri, Pablo Mosteiro, Laurence Frank, Ozgur Togay (Department of Methodology, Statistics and Data Science)

**Duration:** 1 hour

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

### Example 1: Extract information from an observation {.unnumbered .unlisted}

**Scenario:** You have a short classroom observation about multilingual pupils' participation during a collaborative learning activity.

Copy this prompt to your AI chat:

```default
Extract the key information from the classroom observation below.

Identify:
1. Observable instances of participation and language use.
2. Teacher or peer actions that may be relevant to participation.
3. Ambiguities or missing context.

Support your points with details from the observation. Separate observation from interpretation, and do not infer traits or motives that are not directly supported.

Observation:
"During a small-group science task, the teacher asked pupils to discuss why one object floated and another sank. Lina first discussed her idea quietly in Arabic with Samira. Samira then summarized part of their discussion in Dutch. The teacher told the group that they could use any language while working out the problem, but that the group should present its final explanation in Dutch. Later, Lina raised her hand when the teacher asked groups to report back, but another pupil from the group answered after the teacher called on the group. At the end of the lesson, Lina completed the written explanation independently."
```

**Task:** Use the [BRAVE(R)](#braver) framework to analyze the prompt, then use the [FACTS](#facts) framework to analyze the response. Discuss your evaluation with a classmate.

*Note: LLMs can also help you build and refine prompts.*

#### Reflection

1. Did the model distinguish observation from interpretation?
2. Did it support its claims with details from the excerpt?
3. What would you need to know before drawing broader conclusions about participation or inclusion?

If this is a task you expect to repeat, consider saving the instructions as a **Prompt**. A saved prompt is useful when the instructions stay mostly the same but the input changes.

---

### Example 2: Code qualitative data {.unnumbered .unlisted}

**Scenario:** You want to code an interview excerpt about digital learning, access, and participation using a small predefined codebook.

Copy this prompt to your AI chat:

```default
Code the interview excerpt below using the codebook.

Codebook:
- DIGITAL_ACCESS: Access to devices, software, internet, or opportunities to use digital tools.
- PEDAGOGICAL_ADAPTATION: Teaching practices or materials are changed in response to pupils' needs or circumstances.
- SOCIAL_PARTICIPATION: Interaction, collaboration, help-seeking, or participation with others.
- LEARNER_PREFERENCE_OR_AGENCY: A pupil expresses a preference or choice in how they engage with learning.
- EQUITY_CONCERN: Differences in circumstances or resources that may affect opportunities to participate or learn.
- DATA_OR_ALGORITHM_USE: Digital scores or other data-driven outputs are considered in educational decisions.
- AMBIGUOUS_OR_INSUFFICIENT: The excerpt does not clearly support another code.

Provide a table with:
- text segment;
- assigned code or codes;
- brief justification with supporting words;
- confidence: high, medium, or low.

Multiple codes may apply. Mark ambiguity explicitly and do not add assumptions that are not supported by the excerpt.

Interview excerpt:
"We started using an online practice platform because pupils can work at their own pace. Some children finish the exercises on a tablet at home, but a few have told me that they share one device with brothers or sisters. I now give everyone time to use the platform during class and I keep a paper version available. One pupil told me she prefers the paper version because she can sit next to a classmate and ask for help. The platform scores are useful, but I do not want them to decide by themselves who needs extra support."
```

**Task:** Use the [FACTS](#facts) framework to analyze the response. Discuss your evaluation with a classmate.

*Note: You can include a codebook in the prompt. Clear definitions, decision rules, and output formats can make repeated classifications more consistent.*

#### Reflection

1. Were the codes applied consistently and supported by the text?
2. Did the model handle overlapping or ambiguous cases appropriately?
3. Did it introduce assumptions about disadvantage, achievement, or causality that were not present in the excerpt?
4. Which code definitions would you refine before using them on real data?

For a recurring task with stable instructions to the AI assistant, a **Persona** may be more useful than repeatedly pasting the full setup into a new chat.

---

### Example 3: Assess the relevance of research {.unnumbered .unlisted}

**Scenario:** You need to quickly assess whether a paper is relevant to research on children's development, learning, participation, or educational contexts.

Choose an abstract, article excerpt, or paper that you would like to work with. You can either paste the relevant text into the prompt or upload the document directly.

If the prompt contains `[INSERT TEXT HERE]`:

- replace it with your chosen text; or
- if you uploaded a document, replace it with an instruction such as `Use the uploaded document as the source.`

```default
Summarize the research abstract below for a researcher deciding whether the study is relevant to their work on child or youth development and education.

Provide:
1. The research question, population, and setting.
2. The study design and main concepts or outcomes.
3. The main findings.
4. Any stated limitations or boundary conditions.
5. What would require reading the full paper.

If relevant, note how diversity, inequality, social context, or participation is addressed. Use only information from the abstract and mark uncertainty clearly.

Abstract:
[INSERT ABSTRACT TEXT HERE]
```

**Task:** Use the [FACTS](#facts) framework to analyze the response. Discuss your evaluation with a classmate.

#### Reflection

1. Did the model stay within what the abstract actually supports?
2. Did it avoid overstating causality or generalisability?
3. Would the summary help you decide whether to read the full paper?

**Try a platform feature:** Compare your result with one of the ready-made **Research** prompts in UU AI-Chat. What assumptions does the built-in prompt make? What would you add or change for your own research question?

If you are working on different parts of the same research project, consider creating a **Project**. Chats within a Project can share context, so you can use separate chats for the literature review, methods, analysis, or other parts while keeping them connected.

---

### Example 4: Optimize and verify R code {.unnumbered .unlisted}

**Scenario:** You have R code used in a research workflow and want to improve it without changing the analysis or results.

Use **your own R code**, another piece of R code you are interested in, or the example below.

Give the AI enough context to understand what the code is intended to do, then adapt this prompt:

```default
Review and optimize the R code below for a scientific research workflow.

Context:
[WHAT SHOULD THE CODE DO? WHAT ARE THE IMPORTANT INPUTS AND OUTPUTS?]


Improve the code where useful, focusing on readability and efficiency while preserving the analysis and its output.

Explain the main changes, flag any assumptions or new package dependencies, and suggest a simple way to check that the revised code gives equivalent results. Do not claim performance improvements unless they are actually measured.

R code:
[PASTE R CODE HERE]

```

**If you need example code**, use this:

```r
schools <- unique(df$school_id)
result <- data.frame()

for (i in seq_along(schools)) {
  this_school <- schools[i]
  tmp <- df[df$school_id == this_school & !is.na(df$score), ]

  result <- rbind(
    result,
    data.frame(
      school_id = this_school,
      n = nrow(tmp),
      mean_score = if (nrow(tmp) == 0) NA_real_ else mean(tmp$score)
    )
  )
}

result <- result[order(result$school_id), ]
```

Assume `df` contains a school identifier and a numeric `score` that may be missing. The output should contain one row per school, including schools with only missing scores, and should remain ordered by `school_id`.

**Task:** Compare the original and revised code. Check whether the behaviour that matters for the analysis is preserved, and run the suggested checks in R if possible. Ask at least one follow-up question about a change or assumption you do not fully understand.

#### Reflection

1. Did the revised code preserve the intended analysis and important edge cases?
2. Were the main changes and assumptions clear?
3. What would you test before using the revised code in a real analysis?

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
### Exercise 1: Verify generated literature {.unnumbered .unlisted}

**Task:** Ask the model:

```default
Find three peer-reviewed empirical studies published in 2026 about digital technologies and social participation, learning, or development among children or adolescents. For each study, provide the title, authors, journal, DOI, study population, and one-sentence main finding.
```

Verify the references and findings using reliable external sources such as journal websites, Crossref, Google Scholar, or another academic database.

#### Reflection

1. Do the publications and bibliographic details exist as given?
2. Do the reported findings match the original sources?
3. What would make this literature-search workflow more reliable?

---

### Exercise 2: Detect assumptions in a research question {.unnumbered .unlisted}

**Task:** Compare responses to these two prompts:

**Prompt A:**
```default
Explain why multilingual children participate less in classroom discussions than monolingual children.
```

**Prompt B:**
```default
Discuss factors that may be associated with variation in classroom participation among multilingual and monolingual children. Do not assume that a group difference exists. Distinguish empirical evidence from possible explanations.
```

Compare how the framing affects what the model treats as established.

#### Reflection

1. Did Prompt A encourage the model to accept an unsupported assumption?
2. Did either response overgeneralise or rely on stereotypes?
3. How could you phrase your own research questions to reduce leading assumptions?


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

### Example from research: LLM-assisted data annotation {#data-annotation-example}

<details>
<summary><strong>View the research prompt</strong></summary>

LLMs are increasingly used for data annotation because they can make large-scale coding faster and cheaper. Performance still depends on the task, but recent work has found that LLMs can match or outperform human annotators on some social-science text classification tasks (Törnberg, 2024).[^annotation-performance]

The example below comes from [Togay et al. (2026)](https://arxiv.org/abs/2603.23531), which used LLMs to identify the political target and stance in Reddit comments across 138 predefined political targets plus an open-ended category. The best-performing models were comparable to highly trained human annotators.[^target-stance-paper]

This is deliberately much longer than the tutorial prompts above. Research annotation prompts can function like codebooks: they define labels, edge cases, output formats, and examples so that the same rules can be applied consistently across many observations. This prompt was also designed for an earlier generation of models; repeated emphasis such as `**...**` was used to reinforce important instructions and is generally not necessary with newer models.

[^annotation-performance]: Törnberg, P. (2024). *Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages*. Social Science Computer Review. https://doi.org/10.1177/08944393241286471
[^target-stance-paper]: Togay, Ö., Garcia-Bernardo, J., Kunneman, F., & Giachanou, A. (2026). *Large Language Models Unpack Complex Political Opinions through Target-Stance Extraction*. arXiv:2603.23531. https://doi.org/10.48550/arXiv.2603.23531

<pre class="annotation-prompt"><code>You will be provided with a Reddit comment and the title of the submission under which it was posted&#46;&#13;&#10;&#13;&#10;Your task is to identify the &#42;&#42;target&#42;&#42; and the &#42;&#42;stance&#42;&#42; expressed toward it in the Comment&#44; using the predefined list of political targets at the end&#46;&#13;&#10;&#13;&#10;Only classify stances related to a target from the list&#46; If the Comment refers to a similar target with different wording&#44; select the exact matching entry from the list&#46;  &#13;&#10;&#42;&#42;Do not rename&#44; paraphrase&#44; or invent new target names&#46;&#42;&#42;  &#13;&#10;&#45; If the post refers to a target not on the list&#44; label it &#42;&#42;&#34;Other&#34;&#42;&#42;&#46;  &#13;&#10;&#45; If no political target is mentioned&#44; label it &#42;&#42;&#34;None&#34;&#42;&#42;&#46;  &#13;&#10;&#13;&#10;Use the Submission &#42;&#42;only&#42;&#42; to resolve ambiguity &#40;e&#46;g&#46;&#44; resolving pronouns or vague references&#41;&#46; &#42;&#42;Do not infer stance from the Submission&#46;&#42;&#42;&#13;&#10;&#13;&#10;&#45;&#45;&#45;&#13;&#10;&#13;&#10;&#35;&#35; Classification Steps&#13;&#10;&#13;&#10;1&#46; &#42;&#42;Identify the Political Target&#42;&#42;  &#13;&#10;   &#45; Choose a target from the predefined list at the end&#46;  &#13;&#10;   &#45; If the post refers to a target not on the list&#44; label it &#42;&#42;&#34;Other&#34;&#42;&#42;&#46;  &#13;&#10;   &#45; If no target is mentioned&#44; label it &#42;&#42;&#34;None&#34;&#42;&#42; and skip stance classification&#46;&#13;&#10;&#13;&#10;2&#46; &#42;&#42;Determine the Stance&#42;&#42; &#40;only if a target is identified&#41;  &#13;&#10;   &#45; &#42;&#42;Positive&#42;&#42;&#58; clear support or praise  &#13;&#10;   &#45; &#42;&#42;Neutral&#42;&#42;&#58; mention without a clear stance  &#13;&#10;   &#45; &#42;&#42;Negative&#42;&#42;&#58; criticism or disapproval&#13;&#10;   &#45; &#42;&#42;None&#42;&#42;&#58; no stance can be identified&#13;&#10;&#13;&#10;3&#46; &#42;&#42;Return the classification&#42;&#42;&#13;&#10;&#13;&#10;&#45;&#45;&#45;&#13;&#10;&#13;&#10;&#35;&#35; Output Format&#13;&#10;&#13;&#10;Your response must be a JSON object with the following fields&#58;&#13;&#10;&#45; &#34;target&#34; &#40;string&#41;&#58; The identified political target&#44; from the list of Predefined Targets&#46;&#13;&#10;&#45; &#34;stance&#34; &#40;string&#41;&#58; The determined stance&#46; Must be one of&#58; &#34;Positive&#34;&#44; &#34;Neutral&#34;&#44; &#34;Negative&#34;&#44; or &#34;None&#34;&#46;&#13;&#10;&#45; &#34;confidence&#34; &#40;float&#41;&#58; A confidence score between 0&#46;0 and 1&#46;0 &#40;inclusive&#41; representing how certain the model is about its classification&#46;&#13;&#10;&#13;&#10;Example JSON output if a target and stance are identified&#58;&#13;&#10;&#96;&#96;&#96;json&#13;&#10;&#40;&#13;&#10;  &#34;target&#34;&#58; &#34;Donald Trump&#34;&#44;&#13;&#10;  &#34;stance&#34;&#58; &#34;Positive&#34;&#44;&#13;&#10;  &#34;confidence&#34;&#58; 0&#46;95&#13;&#10;&#41;&#13;&#10;&#13;&#10;&#35;&#35; Examples&#13;&#10;&#13;&#10;&#35; Example 1&#13;&#10;Input&#58;&#13;&#10;&#9;Submission Title&#58; New York Primary Results Megathread&#9;&#13;&#10;&#9;Comment&#58; Didn&#39;t Sanders vote for that crime bill too&#63; Has he evolved on that position or does he still support it&#63;&#9;&#13;&#10;Output&#58;&#13;&#10;&#96;&#96;&#96;json&#13;&#10;&#40;&#13;&#10;  &#34;target&#34;&#58; &#34;Bernie Sanders&#34;&#44;&#13;&#10;  &#34;stance&#34;&#58; &#34;Neutral&#34;&#44;&#13;&#10;  &#34;confidence&#34;&#58; 0&#46;8&#13;&#10;&#41;&#13;&#10;&#13;&#10;&#35; Example 2&#13;&#10;Input&#58;&#13;&#10;&#9;Submission Title&#58; Flat&#45;tax in the U&#46;S&#46; &#45; a good idea&#63;&#9;&#13;&#10;&#9;Comment&#58; I&#39;d say it&#39;s a good thing&#44; but the reason for existing tax breaks is to encourage people to live in a way that is good for society&#59; get educated&#44; own property&#44; have kids&#44; etc&#46;&#9;&#13;&#10;Output&#58;&#13;&#10;&#96;&#96;&#96;json&#13;&#10;&#40;&#13;&#10;  &#34;target&#34;&#58; &#34;Tax cuts &#40;general&#41;&#34;&#44;&#13;&#10;  &#34;stance&#34;&#58; &#34;Positive&#34;&#44;&#13;&#10;  &#34;confidence&#34;&#58; 0&#46;90&#13;&#10;&#41;&#13;&#10;&#13;&#10;&#35; Example 3&#13;&#10;Input&#58;&#13;&#10;&#9;Submission Title&#58; Is drug legalization&#47;decriminalization sound policy&#63; &#13;&#10;&#9;Comment&#58; &#34;Treating drug abuse as a medical problem instead of a criminal problem has been successful in European countries and has been a conclusion by various studies&#46;&#13;&#10;&#9; &#13;&#10;&#9; &#40;let&#39;s make the AutoMod happy&#58; &#41;&#13;&#10;&#9; &#13;&#10;&#9; https&#58;&#47;&#47;www&#46;drugabuse&#46;gov&#47;about&#45;nida&#47;noras&#45;blog&#47;2014&#47;03&#47;unodc&#45;recommends&#45;treating&#45;addiction&#45;health&#45;not&#45;legal&#45;issue&#13;&#10;&#9; &#13;&#10;&#9; https&#58;&#47;&#47;www&#46;ncbi&#46;nlm&#46;nih&#46;gov&#47;pmc&#47;articles&#47;PMC2681083&#47;&#34;&#9;&#13;&#10;Output&#58;&#13;&#10;&#96;&#96;&#96;json&#13;&#10;&#40;&#13;&#10;  &#34;target&#34;&#58; &#34;War on Drugs&#34;&#44;&#13;&#10;  &#34;stance&#34;&#58; &#34;Negative&#34;&#44;&#13;&#10;  &#34;confidence&#34;&#58; 0&#46;90&#13;&#10;&#41;&#13;&#10;&#13;&#10;&#35; Example 4&#13;&#10;Input&#58;&#13;&#10;&#9;Submission Title&#58; What are the benefits and costs of the federal hiring freeze&#63;&#9;&#13;&#10;&#9;Comment&#58; I will note you didn&#39;t call out the dude who cited a government agency to show government agency hiring shouldn&#39;t be frozen&#46;&#9;&#13;&#10;Output&#58;&#13;&#10;&#40;&#13;&#10;  &#34;target&#34;&#58; &#34;None&#34;&#44;&#13;&#10;  &#34;stance&#34;&#58; &#34;None&#34;&#44;&#13;&#10;  &#34;confidence&#34;&#58; 1&#46;0&#13;&#10;&#41;&#13;&#10;&#13;&#10;&#45;&#45;&#45;&#13;&#10;&#13;&#10;&#35;&#35; Predefined Targets&#13;&#10;&#13;&#10;&#123;predefined&#95;targets&#125;&#13;&#10;Target&#59; Explanation&#13;&#10;Republican Party&#59; Republican Party as an organization&#13;&#10;Republican politicians&#59; Republican politicians as a group&#44; including representatives&#44; senators and governors&#13;&#10;Republican politician &#40;generic&#41;&#59; a Republican politician not on the list&#46; &#13;&#10;Republicans&#59; Republican party supporters&#46; A comment about both the Republican politicians and Republican party supporters would fall here&#46; If it is only about Republican politicians&#44; use the Republican politicians label&#46;&#13;&#10;Conservatives&#59; Conservative people and&#47;or ideology&#13;&#10;Right&#45;wingers&#59; right&#45;wing people and&#47;or ideology&#13;&#10;Alt&#45;right&#59; alt&#45;right people and&#47;or ideology&#13;&#10;Independents&#59; independent people &#40;often used for voters without a party affiliation&#41;&#13;&#10;Democratic Party&#59; Democratic Party as an organization&#13;&#10;Democratic politicians&#59; Democratic politicians as a group&#44; including representatives&#44; senators and governors&#13;&#10;Democratic politician &#40;generic&#41;&#59; a Democratic politician not on the list&#13;&#10;Democrats&#59; Democratic party supporters&#46; A comment about both the Democratic politicians and Democratic party supporters would fall here&#46; If it is only about Democratic politicians&#44; use the Democratic politicians label&#46;&#13;&#10;Centrists&#59; Centrist people and&#47;or ideology&#13;&#10;Liberals&#59; Liberal people and&#47;or ideology&#13;&#10;Leftists&#59; Leftist people and&#47;or ideology&#13;&#10;Greens&#59; Green people and&#47;or ideology&#13;&#10;Socialists&#59; Socialist people and&#47;or ideology&#13;&#10;Antifa&#59; Antifa political group and its supporters&#13;&#10;Abortion&#59; Planned Parenthood also almost always fall under here&#44; unless they specifically focus on Planned Parenthood as a public healthcare organization&#46;&#13;&#10;Gun Control&#59;&#13;&#10;LGBTQ rights&#59;&#13;&#10;Vaccination&#59;&#13;&#10;Belief in Institutional Racism&#59;&#13;&#10;Belief in Climate Change&#59;&#13;&#10;Immigration&#59;&#13;&#10;Affirmative Action for Racial Equality&#59;&#13;&#10;Affirmative Action for Gender Equality&#59;&#13;&#10;Muslims&#59;&#13;&#10;Jews&#59;&#13;&#10;Catholics&#59;&#13;&#10;Protestants&#59;&#13;&#10;Christians&#59;&#13;&#10;Atheists&#59;&#13;&#10;Whites&#59;&#13;&#10;Blacks&#59;&#13;&#10;Hispanics&#59;&#13;&#10;Asians&#59;&#13;&#10;Indians&#59;&#13;&#10;Government spending&#59; Fiscal policies that favor an increased government budget  Use the specific label if it refers to a higher budget for education&#44; healthcare&#44; military&#44; security&#44; or any other item on the list&#46;&#13;&#10;Tax cuts &#40;general&#41;&#59; Tax cuts that apply to everyone&#13;&#10;Tax cuts &#40;for rich&#41;&#59; Tax cuts that apply to the rich&#13;&#10;Tax cuts &#40;for low&#45;middle classes&#41;&#59; Tax cuts that apply to the low and&#47;or middle class&#13;&#10;Higher corporate tax&#59; A comment calling for lower corporate tax rate would be labelled as Anti &#40;so &#45;1&#41; Higher Corporate Tax&#44;&#13;&#10;Higher taxes for the rich&#59;&#13;&#10;Minimum wage&#47;Higher minimum wage&#59; establishing a minimum wage&#44; or increasing it&#13;&#10;Social spending&#59; social spending&#44; except healthcare&#44; education&#44; Coronavirus stimulus checks and security  Examples&#58; unemployment or childcare benefits&#44; public funding of parks etc&#46;&#13;&#10;Universal basic income&#59; Universal Basic Income &#40;UBI&#41; in which people regularly receive a minimum income without any checks on conditions&#46;&#13;&#10;Public healthcare&#59; public healthcare&#44; including Affordable Care Act &#40;Obamacare&#41;&#44; Medicare&#44; Medicaid&#44; healthcare reforms that would require more government funding&#13;&#10;Private healthcare&#59; private healthcare&#46; Examples include calls for more privatization&#44; removal of existing social security programs &#40;ACA&#47;Medicaid etc&#46;&#41;&#13;&#10;Public education&#59; public education&#46; Examples include calls for more government funding for schools&#13;&#10;Private education&#59; private education&#46; Examples include calls for more privatization&#13;&#10;Student loan forgiveness&#59; whether student loans and debt should be forgiven&#46;&#13;&#10;Government bailouts&#59; government bailout of private corporations&#44; a common example would be bank bailouts during the 2008 financial crisis&#46;&#13;&#10;Military spending&#59; the US military spending&#47;budget&#13;&#10;Police spending&#59; the US police&#47;law enforcement spending&#47;budget&#46; This is often referred within the state level&#44; but covers both state and federal budgets&#46;&#13;&#10;International Trade&#59; International Trade&#46; Examples include Trans&#45;Pacific Partnership&#44; US trade with China&#44; US trade with Canada and Mexico &#40;NAFTA&#41;&#44; World Trade Organization etc&#46;&#13;&#10;Protectionism&#59; protectionist international trade policies&#44; such as Tariffs and trade barriers&#46;&#13;&#10;Nuclear Energy&#59;&#13;&#10;Renewable&#47;Green Energy&#59;&#13;&#10;Fossil fuels&#59;&#13;&#10;Trust in the US government &#40;general&#41;&#59; the Trust the US government as an organization that do not mention a party&#47;president&#13;&#10;Trust in the Biden administration&#59;&#13;&#10;Trust in the Trump administration&#59;&#13;&#10;Trust in the Obama administration&#59;&#13;&#10;Trust in the G&#46;W&#46; Bush administration&#59;&#13;&#10;Trust in the US Military&#59;&#13;&#10;Trust in the US Law Enforcement&#59;&#13;&#10;Trust in the US electoral system&#59; the US electoral system&#44; including electoral college&#44; two&#45;party system&#44; first past the post voting&#44; electoral districts&#44; campaign donations and funding &#40;political action comittes&#44; SuperPACs&#41;&#13;&#10;Restrictions on Voting Access&#59; the regulations that make voting less accessible&#46; Examples include registration or ID checks&#46; Counter examples&#44; i&#46;e&#46; cases that make voting easier&#44; would include mail&#45;in ballots&#44; ways to reduce voting queues&#44; or helping those waiting in the voting queue&#46;&#13;&#10;Trust in the US judicial system&#47;courts&#59; the US judicial system and courts in general&#46; Examples include fair sentencing&#44; costly court cases where corporations can outspend individuals&#13;&#10;Trust in the US Supreme Court&#59; Specifically refering to the US Supreme Court&#13;&#10;Coronavirus stimulus checks&#59;&#13;&#10;Discrimination based on Political Beliefs or Activities&#59;&#13;&#10;Capital Punishment&#59;&#13;&#10;Diversity&#44; equity&#44; and inclusion initiatives&#59; DEI initiatives that seek to promote the fair treatment and full participation of all people&#44; particularly groups who have historically been underrepresented or subject to discrimination&#46; Criticized by Conservatives on the basis that it creates preferential treatment of minorities&#44; forgoes merit as the basis of quality&#44; and restricts freedom of speech&#46;&#13;&#10;Critical Race Theory&#59; CRT&#44; which focuses on the relationships between social conceptions of race and ethnicity&#44; social and political laws&#44; and mass media&#46; CRT also considers racism to be systemic in various laws and rules&#44; not based only on individuals&#39; prejudices&#46; It is criticisized by &#40;often&#41; Conservatives for being anti&#45;American and anti&#45;White&#44; for undermining American history and traditions&#46; Mostly referred in the context of right&#45;wing backlash and censure of CRT in schools&#46;&#13;&#10;Multiculturalism&#59; multiple cultures living together or interacting&#13;&#10;Cannabis legalization&#59;&#13;&#10;Environmental Protections&#59;&#13;&#10;Trust in the scientific community&#59; the scientific community&#46; Examples include the academia&#44; advisory organizations such as World Health Organization&#44; Centers for Disease Control and Prevention &#40;CDC&#41;&#13;&#10;Pornography&#59;&#13;&#10;Euthanasia&#59;&#13;&#10;AI&#45;driven surveillance&#59; whether the government should use AI technologies in surveillance&#46;&#13;&#10;Social Media Regulations&#59; whether social media platforms and the associated companies should be regulated more &#13;&#10;Cryptocurrencies&#59; cryptocurrencies&#44; decentralized finance&#44; and financial use of blockchain technology&#46; A positive stance would favor those&#44; a negative stance would be against or would call for more regulations&#46;&#13;&#10;AI Regulations&#59; the general attitudes toward AI regulation or ethics&#13;&#10;Use of AI in the workplace&#59; the use of AI &#44; often referred in the context of AI replacing human workers&#46;&#13;&#10;Religion &#40;general&#41;&#59; religion that speak on general terms without referring to a specific belief system&#13;&#10;Net Neutrality&#59; Net Neutrality&#44; the principle that Internet service providers &#40;ISPs&#41; must treat all Internet communications equally&#46;&#13;&#10;Zoning Laws&#59; &#40;the US&#44; and often state or city level&#41; Zoning Regulations&#44; that divide land in a municipality into zones in which certain land uses are permitted or prohibited&#46; Often referred in the context of certain municipalities blocking new constructions to keep house&#47;land values higher&#44; which exacerbate housing crisis&#46;&#13;&#10;Whistleblowing&#47;Leaks&#59; whistleblowing or journalistic practice of leaking&#46; Examples include Wikileaks&#44; Panama Papers&#44; Boeing whistleblowers&#44; and often discussed through people such as Julian Assange&#44; Edward Snowden&#44; Chelsea Manning&#13;&#10;Censorship&#59; censorship by an administrative or regulative body &#40;the government&#44; the state&#44; and also municipal education boards&#41;&#46; Often referred in the context of some US schools banning certain books&#46;&#13;&#10;War on Drugs&#59; the War on Drugs&#44; the policy of a global campaign led by the United States federal government&#44; of drug prohibition&#44; foreign assistance&#44; and military intervention&#44; with the aim of reducing the illegal drug trade in the US&#46; This is often referred in discussion of whether repression or legalization is better to reduce social harms caused by drugs&#46;&#13;&#10;War on Terror&#59; the War on Terror&#44; a global campaign led by the US against militant Islamist movements&#44; such as Al&#45;Qaeda&#44; Taliban&#44; ISIS and offshoots&#46; Does not include the 2003 invasion of Iraq&#13;&#10;Invasion of Iraq &#40;2003&#41;&#59; the invasion and occupation of Saddam&#39;s Iraq&#46;&#13;&#10;NATO&#47;US Allies&#59; the NATO and other US Allies&#46; Mainly referred within the context of the US&#39; bases abroad&#44; and whether the Allies are doing enough &#40;financially or militarily&#41;&#13;&#10;United Nations&#59;&#13;&#10;European Union&#59;&#13;&#10;Foreign military interventions by the US&#59; the US military involvement in foreign conflicts&#46; Examples include US involvement in the Syrian Civil War against Assad&#46; Does not include Invasion or Iraq&#44; War on Terror or War on Drugs&#46;&#13;&#10;US Support for Israel&#59;&#13;&#10;Israel&#59;&#13;&#10;Palestine&#59; Palestinian people&#46; A pro&#45;Palestinian stance would stress the rights of Palestinians to self&#45;governance and highlight Israeli oppresion&#44; an anti&#45;Palestinian stance would focus more on Hamas&#39; leadership of Palestine&#44; or poor governance by the Palestinian Authority over the West Bank&#46;&#13;&#10;Black Lives Matter movement&#59;&#13;&#10;Blue Lives Matter movement&#59; Blue Lives Matter movement was a counter&#45;movement against Black Lives Matter and stressed the dangers the law enforcement faces&#13;&#10;MeToo movement&#59; &#34;the MeToo movement&#44; and the practices employed or popularized by it&#44; such as public exposures&#44; social media campaigns against sexual harrasment and discrimination&#44; and also &#34;&#34;cancelling&#34;&#34; of accused figures&#46;&#34;&#13;&#10;Donald Trump&#59;&#13;&#10;Joe Biden&#59;&#13;&#10;Barack Obama&#59;&#13;&#10;G&#46;W&#46; Bush&#59;&#13;&#10;Bill Clinton&#59;&#13;&#10;Ronald Reagan&#59;&#13;&#10;Richard Nixon&#59;&#13;&#10;Franklin D&#46; Roosevelt&#59;&#13;&#10;Theodore Roosevelt&#59;&#13;&#10;Abraham Lincoln&#59;&#13;&#10;Hillary Clinton&#59;&#13;&#10;Bernie Sanders&#59;&#13;&#10;Alexandria Ocasio&#45;Cortez&#59;&#13;&#10;Elizabeth Warren&#59;&#13;&#10;George Soros&#59;&#13;&#10;Elon Musk&#59;&#13;&#10;Ted Cruz&#59;&#13;&#10;Marco Rubio&#59;&#13;&#10;Mitt Romney&#59;&#13;&#10;Ron Paul&#59;&#13;&#10;Newt Gingrich&#59;&#13;&#10;John McCain&#59;&#13;&#10;Trump supporters&#59; Specifically referring to Trump supporters&#44; rather than Republicans&#44; Conservatives&#44; or Right&#45;wingers&#13;&#10;Biden supporters&#59; Specifically referring to Biden supporters&#44; rather than Democrats&#44; Centrists&#44; Liberals etc&#46; &#13;&#10;Obama supporters&#59; Specifically referring to Obama supporters&#44; rather than Democrats&#44; Centrists&#44; Liberals etc&#46; &#13;&#10;Bush supporters&#59; Specifically referring to G&#46;W&#46;Bush supporters&#44; rather than Republican&#44; Conservatives&#44; or Right&#45;wingers&#13;&#10;Hillary Clinton supporters&#59; Specifically referring to H&#46;Clinton supporters&#44; rather than Democrats&#44; Centrists&#44; Liberals etc&#46; &#13;&#10;Sanders supporters&#59; Specifically referring to Sanders supporters&#44; rather than Democrats&#44; Leftists&#44; Socialists etc&#46; &#13;&#10;N&#47;A&#59; When target cannot be identified&#13;&#10;Other&#59; When there&#39;s an explicit target but is not listed&#13;&#10;Belief in Trump&#45;Russia Collusion&#59; Regarding alleged collusion between Donald Trump and Russian authorities for political gain&#44; including influencing elections&#13;&#10;Belief in Russian Interference in Elections&#59; Regarding attempts by Russia to influence US elections&#44; without asserting whether this was intended to support Trump&#13;&#10;Increased Surveillance&#59; the increase in state or law enforcement surveillance activities&#46; If the main focus is on the use of AI in surveillance&#44; categorize under &#39;AI&#45;Surveillance&#39;&#13;&#10;&#13;&#10;&#40;Use the exact wording&#46; Do not rename&#44; paraphrase&#44; or invent targets&#46;&#41;</code></pre>

</details>