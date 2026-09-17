---
title: "Data prep and analysis: Language mixing by parents of children with DLD"
output:
  prettydoc::html_pretty:
    theme: architect
    highlight: github 
    toc: true
---

# Introduction

This markdown contains the data prep and data analysis associated with the manuscript "Parental language mixing and its association with language outcomes of children with (a suspicion of) Developmental Language Disorder".

```{r setup, include = FALSE}
## R Markdown settings
knitr::opts_chunk$set (echo = TRUE)
options (width = 600)

## Load packages
library(tidyr)
library(prettydoc)
library(dplyr)
library(stringr)
library(data.table)
library(formattable)
library(rstatix)
library(ggplot2)
library(Partiallyoverlapping)
library(bain)
library(brms)
library(mice)
library(miceadds)
library(ggmice)
library(parameters)
library(lme4)
```

Reading in the data files:

``` {r read data, warning = FALSE}
## Read in data including Q-BEx and LENA data
Data_Total_QBEx <- read.csv2("DLD_BackgroundQBEx.csv")
LENA <- read.csv2("descriptives_LENA.csv")

Data_Total <- merge(Data_Total_QBEx, LENA, by = "Subject")

## Item level data CLT for glmer analysis
CLT_receptive <- read.csv2("CLT_DLD_Comp_Item.csv")
CLT_productive <- read.csv2("CLT_DLD_Prod_Item.csv")
CLT_productive$Productie_ZN_21_correct <- as.integer(CLT_productive$Productie_ZN_21_correct)

## Create long format for glmer analysis
CLT_receptive <- CLT_receptive %>% 
  pivot_longer(
    cols = `Begrip_ZN_1`:`Begrip_WW_32`, 
    names_to = "Item",
    values_to = "Accuracy")
CLT_receptive$Modality <- "Receptive" # Code modality

CLT_productive <- CLT_productive %>% 
  pivot_longer(
    cols = `Productie_ZN_1_correct`:`Productie_WW_32_correct`, 
    names_to = "Item",
    values_to = "Accuracy")
CLT_productive$Modality <- "Productive" # Code modality

```

```{r, include = FALSE}
rm(Data_Total_QBEx)
rm(LENA)
```

# Statistics reported in methods

## Descriptive statistics Table 1

```{r}
# Descriptives
table1 <- Data_Total %>%
  get_summary_stats(c(Age_Test1, WPPSI_Norm, Qbex_Parental_Education, QBex_Cumulative_Exposure_Dutch, QBex_Cumulative_Use_Dutch), type = "full", show = c("n", "min", "max", "mean", "sd"))

formattable(table1)
```

## Language development score

Descriptives and paired t-test of the language development score in Dutch versus home language.

```{r}
# Select relevant part of the dataset
LangDev <- Data_Total %>%
  select(LanguageDevelopment_Dutch_Score, LanguageDevelopment_HL_Score)

# Transform into long data
LangDev <- LangDev %>%
  gather(key = "Language", value = "Score", LanguageDevelopment_Dutch_Score, LanguageDevelopment_HL_Score)

# Descriptives
tableLangDev <- LangDev %>%
  group_by(Language) %>%
  get_summary_stats(Score, type = "full", show = c("n", "min", "max", "mean", "sd"))

formattable(tableLangDev)
```

```{r}
# Subset Dutch scores
Dutch <- subset(LangDev,  Language == "LanguageDevelopment_Dutch_Score", Score,
                 drop = TRUE)
# Subset HL scores
HL <- subset(LangDev,  Language == "LanguageDevelopment_HL_Score", Score,
                 drop = TRUE)

# Paired t-test
t.test(Dutch, HL, paired = TRUE)
```

## Descriptive statistics Table 2

```{r}
# Descriptives
table2 <- Data_Total %>%
  get_summary_stats(c(length_recording, AWC_FullDay, CVC_FullDay, CTC_FullDay), type = "full", show = c("n", "min", "max", "mean", "sd"))

formattable(table2)
```

## Descriptive statistics Table 3 - QBEX

```{r}
# Numeric
Data_Total$QBex_OneWord_Parents <- as.numeric(Data_Total$QBex_OneWord_Parents)
Data_Total$QBex_TwoThreeWord_Parents <- as.numeric(Data_Total$QBex_TwoThreeWord_Parents)
Data_Total$QBex_BetweenSentences_Parents <- as.numeric(Data_Total$QBex_BetweenSentences_Parents)
Data_Total$QBex_BetweenSpeakers_Parents <- as.numeric(Data_Total$QBex_BetweenSpeakers_Parents)
Data_Total$QBex_DutchL1_Parents <- as.numeric(Data_Total$QBex_DutchL1_Parents)
Data_Total$QBex_L1Dutch_Parents <- as.numeric(Data_Total$QBex_L1Dutch_Parents)

# Calculate overall mixing score and mean within speakers mixing 
Data_Total <- Data_Total %>%
  rowwise() %>%
  mutate(QBex_WithinSpeakers_Parents = mean(c(QBex_OneWord_Parents, QBex_TwoThreeWord_Parents, QBex_BetweenSentences_Parents)),
         QBex_Overall_Mixing_Parents = sum(c(QBex_OneWord_Parents, QBex_TwoThreeWord_Parents, QBex_BetweenSentences_Parents, QBex_BetweenSpeakers_Parents)))

Data_Total$QBex_WithinSpeakers_Parents <- round(Data_Total$QBex_WithinSpeakers_Parents, 1)

# Descriptives QBEX
table3QBEx <- Data_Total %>%
  get_summary_stats(c(QBex_Overall_Mixing_Parents, QBex_DutchL1_Parents, QBex_L1Dutch_Parents, QBex_BetweenSpeakers_Parents, QBex_WithinSpeakers_Parents, QBex_OneWord_Parents, QBex_TwoThreeWord_Parents, QBex_BetweenSentences_Parents), type = "full", show = c("n", "min", "max", "mean", "sd"))

formattable(table3QBEx)
```

## Descriptive statistics Table 3 - LENA

```{r}
# Descriptives LENA
table3LENA <- Data_Total %>%
  get_summary_stats(c(Mixing_Parents_LENA_PerHour, Mixing_Parents_IntoHome_LENA_PerHour, Mixing_Parents_IntoDutch_LENA_PerHour, Mixing_Parents_BetweenSpeaker_LENA_PerHour, Mixing_Parents_WithinSpeaker_LENA_PerHour, Mixing_Parents_Insertion_LENA_PerHour, Mixing_Parents_Alternation_LENA_PerHour, Mixing_Parents_Intersentential_LENA_PerHour), type = "full", show = c("n", "min", "max", "mean", "sd"))

formattable(table3LENA)
```

Hypothesis 1 is borne out: all parents mix to some extent, although substantial differences between families are observed.

Here, we also check the correlation between the LENA overall mixing score used in the manuscript with a LENA overall mixing score corrected for adult word count (AWC) for selected 5-minute segments.

```{r}
# Create new variable 
Data_Total <- Data_Total %>%
  mutate(Mixing_Parents_Corrected = (Mixing_Parents_LENA_PerHour/AWC_selection)*100)

# Correlation
correlation_LENA_measures <- cor.test(Data_Total$Mixing_Parents_LENA_PerHour, 
                                      Data_Total$Mixing_Parents_Corrected, 
                                      method = 'pearson',
                                      use = "complete.obs")

correlation_LENA_measures
```


# Research question 1

## Direction of mixing

Hypothesis 2: Parents mix more from the minority language into the majority language Dutch than vice versa (Gross & Kaushanskaya, 2022; Smolak et al., 2020). 

First, the frequentist approach: the partially overlapping t-test (due to missing data) with QBEx data and a paired t-test for LENA data.

```{r}
# Partially overlapping paired t-test QBEX
direction_QBEx <- Partover.test(Data_Total$QBex_DutchL1_Parents, Data_Total$QBex_L1Dutch_Parents, stacked = TRUE, conf.level = 0.975)

direction_QBEx

# Paired t-test LENA
direction_LENA <- bain::t_test(Data_Total$Mixing_Parents_IntoHome_LENA_PerHour, Data_Total$Mixing_Parents_IntoDutch_LENA_PerHour, paired = TRUE, conf.level = 0.975)

direction_LENA
```

Second, the Bayes Factor. 

```{r}
# QBEX
# Set SE and N
SE <- (15.52722989-7.782328)/1.96
SE <- SE**2
cov <- list(matrix(SE, nrow = 1, ncol = 1))
N <- 30
estimate <- direction_QBEx$estimate
names(estimate) <- "difference"

# Bain BF
# set a seed value
set.seed(100)
# test hypotheses with bain. 
results.direction_QBEx <- bain(estimate, "difference < 0", n = N, Sigma = cov, group_parameters = 1, joint_parameters = 0)
# display the results
results.direction_QBEx

# LENA
# Set SE and N
SE <- (25.290338-15.36667)/1.96
SE <- SE**2
cov <- list(matrix(SE, nrow = 1, ncol = 1))
N <- 30
estimate <- direction_LENA$estimate
names(estimate) <- "difference"

# Bain BF
# set a seed value
set.seed(100)
# test hypotheses with bain. 
results.direction_LENA <- bain(estimate, "difference < 0", n = N, Sigma = cov, group_parameters = 1, joint_parameters = 0)
# display the results
results.direction_LENA
```

## Type of mixing

Hypothesis 3: 3.	Parents mix more between speakers than within speakers (Bail et al., 2015; Blom et al., 2024; Gross & Kaushanskaya, 2022; Kremin et al., 2022).

First, the frequentist approach: paired t-tests for QBEx and LENA data.

```{r}
#QBEX
# Select relevant part of the dataset
Type <- Data_Total %>%
  select(QBex_BetweenSpeakers_Parents, QBex_WithinSpeakers_Parents)

# Transform into long data
Type <- Type %>%
  gather(key = "Type", value = "Frequency", QBex_BetweenSpeakers_Parents, QBex_WithinSpeakers_Parents)

# Subset between mixing
Between <- subset(Type,  Type == "QBex_BetweenSpeakers_Parents", Frequency,
                 drop = TRUE)
# Subset within mixing
Within <- subset(Type,  Type == "QBex_WithinSpeakers_Parents", Frequency,
                 drop = TRUE)

# Paired t-test
type_QBEx <- bain::t_test(Between, Within, paired = TRUE, conf.level = 0.975)

type_QBEx

#LENA
# Select relevant part of the dataset
Type_LENA <- Data_Total %>%
  select(Mixing_Parents_BetweenSpeaker_LENA_PerHour, Mixing_Parents_WithinSpeaker_LENA_PerHour)

# Transform into long data
Type_LENA <- Type_LENA %>%
  gather(key = "Type", value = "Frequency", Mixing_Parents_BetweenSpeaker_LENA_PerHour, Mixing_Parents_WithinSpeaker_LENA_PerHour)

Type_LENA <- as.data.frame(Type_LENA)

# Subset between mixing
Between_LENA <- subset(Type_LENA,  Type_LENA == "Mixing_Parents_BetweenSpeaker_LENA_PerHour", Frequency,
                 drop = TRUE)
# Subset within mixing
Within_LENA <- subset(Type_LENA,  Type_LENA == "Mixing_Parents_WithinSpeaker_LENA_PerHour", Frequency,
                 drop = TRUE)

# Paired t-test
type_LENA <- bain::t_test(Between_LENA, Within_LENA, paired = TRUE, conf.level = 0.975)

type_LENA
```

Second, the Bayes Factor.

```{r}
# QBEX
# Set SE and N
SE <- (14.393236-6.783333)/1.96
SE <- SE**2
cov <- list(matrix(SE, nrow = 1, ncol = 1))
N <- 30
estimate <- type_QBEx$estimate
names(estimate) <- "difference"

# set a seed value
set.seed(100)
# test hypotheses with bain. 
results.type_QBEx <- bain(estimate, "difference > 0", n = N, Sigma = cov, group_parameters = 1, joint_parameters = 0)
# display the results
results.type_QBEx

# LENA
# Set SE and N
SE <- (19.5668239-10.092)/1.96
SE <- SE**2
cov <- list(matrix(SE, nrow = 1, ncol = 1))
N <- 30
estimate <- type_LENA$estimate
names(estimate) <- "difference"

# set a seed value
set.seed(100)
# test hypotheses with bain. 
results.type_LENA <- bain(estimate, "difference > 0", n = N, Sigma = cov, group_parameters = 1, joint_parameters = 0)
# display the results
results.type_LENA
```

```{r}
# Clear environment
rm(table1)
rm(table2)
rm(table3LENA)
rm(table3QBEx)
rm(direction_LENA)
rm(direction_QBEx)
rm(Type_LENA)
rm(type_LENA)
rm(type_QBEx)
rm(LangDev)
rm(cov)
rm(results.direction_LENA)
rm(results.direction_QBEx)
rm(results.type_LENA)
rm(results.type_QBEx)
rm(Type)
rm(tableLangDev)
```

# Research question 2: the association between parental language mixing and child langauge outcomes

Hypothesis 4: The frequency of parental language mixing relates negatively to performance on both vocabulary and grammar, because children with DLD’s problems with language uptake and processing (e.g., Jackson et al., 2021) may enhance the potential processing costs associated with language mixing in the input (e.g., Byers-Heinlein et al., 2017; Morini & Newman, 2019; Potter et al., 2019). 

## Descriptive statistics Table 4 - Language outcomes

```{r}
# Calculate overall receptive and productive vocab
Data_Total <- Data_Total %>%
  rowwise() %>%
  mutate(
    Vocab_Receptive = sum(c(Receptive_Nouns_Raw, Receptive_Verbs_Raw)),
    Vocab_Productive = sum(c(Productive_Nouns_Raw, Productive_Verbs_Raw)))

# Descriptives language outcomes
table4 <- Data_Total %>%
  get_summary_stats(c(Vocab_Receptive, Vocab_Productive, CELF_SR_Raw, CELF_SR_Norm), type = "full", show = c("n", "min", "max", "mean", "sd"))

formattable(table4)
```

## Imputation of missing data

Missing data are imputed using a subset of the data: children's age and their available scores on the language outcome measures (i.e., receptive vocabulary nouns, receptive vocabulary verbs, productive vocabulary nouns, productive vocabulary verbs and grammar).

```{r, warning = FALSE, results = "hide"}
# Set components for imputation
init = mice(Data_Total, maxit=0) 
meth = init$method
predM = init$predictorMatrix

# Remove variables from imputation
predM[, c("Subject", "Gender", "HomeLanguage", "HomeLanguage_2", "Receptive_Nouns_Percentile", "Receptive_Verbs_Percentile", "Productive_Nouns_Percentile", "Productive_Verbs_Percentile", "CELF_SR_Norm", "WPPSI_Raw", "WPPSI_Norm", "LanguageDevelopment_Dutch_Score", "LanguageDevelopment_HL_Score", "QBex_Cumulative_Exposure_Dutch", "QBex_Cumulative_Exposure_HL", "QBex_Cumulative_Use_Dutch", "QBex_Cumulative_Use_HL", "Qbex_Parental_Education", "QBex_OneWord_Parents", "QBex_TwoThreeWord_Parents", "QBex_BetweenSentences_Parents", "QBex_BetweenSpeakers_Parents", "QBex_DutchL1_Parents", "QBex_L1Dutch_Parents", "AWC_FullDay", "CVC_FullDay", "CTC_FullDay", "all_data_row", "Remaining_silence", "proportion_remaining", "length_recording", "length_remaining", "AWC_selection", "CVC_selection", "CTC_selection", "N_missing", "Proportion_Media", "Segments_Dutch", "Segments_L1", "Segments_Mixed", "Segments_Total", "Proportion_Dutch", "Proportion_L1", "Proportion_Mixed", "Overall_Mixing_Parents_LENA", "Mixing_Parents_LENA_PerHour", "IntoDutch", "IntoHome", "Mixing_Parents_IntoDutch_LENA_PerHour", "Mixing_Parents_IntoHome_LENA_PerHour", "Between_Speaker", "Within_Speaker", "Mixing_Parents_BetweenSpeaker_LENA_PerHour", "Mixing_Parents_WithinSpeaker_LENA_PerHour", "Alternation", "Insertion", "Intersentential", "Mixing_Parents_Insertion_LENA_PerHour", "Mixing_Parents_Alternation_LENA_PerHour", "Mixing_Parents_Intersentential_LENA_PerHour", "QBex_WithinSpeakers_Parents", "QBex_Overall_Mixing_Parents", "Vocab_Receptive", "Vocab_Productive")]=0

# Run the multiple (m = 20) imputation
set.seed(103)
imputed = mice(Data_Total, method=meth, predictorMatrix=predM, m=20)
```

## Data preparations 

Here, we create the overall receptive and productive vocabulary scores and select variables for correlations.

```{r}
# Create complete dataset from imputed data
imputed_Data_Total <- complete(imputed, action = "long", include = TRUE)

# Calculate overall vocabulary scores
imputed_Data_Total <- imputed_Data_Total %>%
  rowwise() %>%
  mutate(
    Vocab_Receptive = sum(c(Receptive_Nouns_Raw, Receptive_Verbs_Raw)),
    Vocab_Productive = sum(c(Productive_Nouns_Raw, Productive_Verbs_Raw)))

# Subject as character, not integer
imputed_Data_Total$Subject <- as.character(imputed_Data_Total$Subject)

# Centering and scaling continuous predictors
imputed_Data_Total$Age_Test1_Scaled <- as.numeric(scale(imputed_Data_Total$Age_Test1, center = TRUE, scale = TRUE))
imputed_Data_Total$CELF_SR_Scaled <- as.numeric(scale(imputed_Data_Total$CELF_SR_Raw, center = TRUE, scale = TRUE))
imputed_Data_Total$Qbex_Parental_Education_Scaled <- as.numeric(scale(imputed_Data_Total$Qbex_Parental_Education, center = TRUE, scale = TRUE))
imputed_Data_Total$QBex_Cumulative_Exposure_Dutch_Scaled <- as.numeric(scale(imputed_Data_Total$QBex_Cumulative_Exposure_Dutch, center = TRUE, scale = TRUE))
imputed_Data_Total$QBex_Overall_Mixing_Parents_Scaled <- as.numeric(scale(imputed_Data_Total$QBex_Overall_Mixing_Parents, center = TRUE, scale = TRUE))
imputed_Data_Total$LENA_Overall_Mixing_Parents_Scaled <- as.numeric(scale(imputed_Data_Total$Mixing_Parents_LENA_PerHour, center = TRUE, scale = TRUE))
imputed_Data_Total$QBex_BetweenSpeakers_Parents_Scaled <- as.numeric(scale(imputed_Data_Total$QBex_BetweenSpeakers_Parents, center = TRUE, scale = TRUE))
imputed_Data_Total$QBex_WithinSpeakers_Parents_Scaled <- as.numeric(scale(imputed_Data_Total$QBex_WithinSpeakers_Parents, center = TRUE, scale = TRUE))
imputed_Data_Total$LENA_BetweenSpeakers_Parents_Scaled <- as.numeric(scale(imputed_Data_Total$Mixing_Parents_BetweenSpeaker_LENA_PerHour, center = TRUE, scale = TRUE))
imputed_Data_Total$LENA_WithinSpeakers_Parents_Scaled <- as.numeric(scale(imputed_Data_Total$Mixing_Parents_WithinSpeaker_LENA_PerHour, center = TRUE, scale = TRUE))


# Make selection for correlation matrix
Corr_Data <- imputed_Data_Total %>%
  select(c(.imp, .id, Vocab_Receptive, Vocab_Productive, CELF_SR_Raw, Age_Test1, Qbex_Parental_Education, QBex_Cumulative_Exposure_Dutch, QBex_Overall_Mixing_Parents, LENA_Overall_Mixing_Parents_Scaled))

# Convert back to mids format for further analysis on imputed datasets
imputed_Data_Total <- as.mids(imputed_Data_Total)
Corr_Data <- as.mids(Corr_Data)
```

## Correlations

Covariates (SES, cumulative proportion of exposure to Dutch, and children’s age) are included in the models below. Here, we present the relationship between the potential covariates and outcome measures.

```{r}
micombine.cor(Corr_Data, variables=NULL, conf.level=0.975,
     method="pearson", nested=FALSE, partial=NULL )
```

### Correlation plots

Correlations between the overall parental mixing score from Q-BEx and LENA on the one hand and children's langauge outcomes are plotted using the original dataset. Missing data is explicitly shown in red.

#### Q-BEx overall mixing

```{r, warning = FALSE, message = FALSE}
# PLOT
ggmice(Data_Total, aes(Vocab_Receptive, QBex_Overall_Mixing_Parents)) +
  geom_point() +
  geom_smooth(method = "lm") +
  xlab("Dutch receptive vocabulary score") + ylab("Q-BEx overall mixing score") 
```


```{r, warning = FALSE, message = FALSE}
# PLOT
ggmice(Data_Total, aes(Vocab_Productive, QBex_Overall_Mixing_Parents)) +
  geom_point() +
  geom_smooth(method = "lm") +
  xlab("Dutch productive vocabulary score") + ylab("Q-BEx overall mixing score") 
```

```{r, warning = FALSE, message = FALSE}
# PLOT
ggmice(Data_Total, aes(CELF_SR_Raw, QBex_Overall_Mixing_Parents)) +
  geom_point() +
  geom_smooth(method = "lm") +
  xlab("Dutch grammar score") + ylab("Q-BEx overall mixing score") 
```
#### LENA overall mixing

```{r, warning = FALSE, message = FALSE}
# PLOT
ggmice(Data_Total, aes(Vocab_Receptive, Mixing_Parents_LENA_PerHour)) +
  geom_point() +
  geom_smooth(method = "lm") +
  xlab("Dutch receptive vocabulary score") + ylab("LENA overall mixing score") 
```


```{r, warning = FALSE, message = FALSE}
# PLOT
ggmice(Data_Total, aes(Vocab_Productive, Mixing_Parents_LENA_PerHour)) +
  geom_point() +
  geom_smooth(method = "lm") +
  xlab("Dutch productive vocabulary score") + ylab("LENA overall mixing score") 
```

```{r, warning = FALSE, message = FALSE}
# PLOT
ggmice(Data_Total, aes(CELF_SR_Raw, Mixing_Parents_LENA_PerHour)) +
  geom_point() +
  geom_smooth(method = "lm") +
  xlab("Dutch grammar score") + ylab("LENA overall mixing score") 
```

## Language mixing and vocabulary

First, we center and scale continuous predictors.

```{r}
# Combine CLT data on item level
data_vocabulary <- rbind(CLT_receptive, CLT_productive) 

# Combine CLT and Data_Total data
data_vocabulary <- merge(data_vocabulary, Data_Total, by = "Subject")

# Center and scale continuous predictors
data_vocabulary$Age_Test1_Scaled <- as.numeric(scale(data_vocabulary$Age_Test1, center = TRUE, scale = TRUE))
data_vocabulary$Qbex_Parental_Education_Scaled <- as.numeric(scale(data_vocabulary$Qbex_Parental_Education, center = TRUE, scale = TRUE))
data_vocabulary$QBex_Cumulative_Exposure_Dutch_Scaled <- as.numeric(scale(data_vocabulary$QBex_Cumulative_Exposure_Dutch, center = TRUE, scale = TRUE))
data_vocabulary$QBEx_Overall_Mixing_Parents_Scaled <- as.numeric(scale(data_vocabulary$QBex_Overall_Mixing_Parents, center = TRUE, scale = TRUE))
data_vocabulary$LENA_Overall_Mixing_Parents_Scaled <- as.numeric(scale(data_vocabulary$Mixing_Parents_LENA_PerHour, center = TRUE, scale = TRUE))
data_vocabulary$QBex_BetweenSpeakers_Parents_Scaled <- as.numeric(scale(data_vocabulary$QBex_BetweenSpeakers_Parents, center = TRUE, scale = TRUE))
data_vocabulary$QBex_WithinSpeakers_Parents_Scaled <- as.numeric(scale(data_vocabulary$QBex_WithinSpeakers_Parents, center = TRUE, scale = TRUE))
data_vocabulary$LENA_BetweenSpeakers_Parents_Scaled <- as.numeric(scale(data_vocabulary$Mixing_Parents_BetweenSpeaker_LENA_PerHour, center = TRUE, scale = TRUE))
data_vocabulary$LENA_WithinSpeakers_Parents_Scaled <- as.numeric(scale(data_vocabulary$Mixing_Parents_WithinSpeaker_LENA_PerHour, center = TRUE, scale = TRUE))

# Contrast code modality
data_vocabulary$Modality <- as.factor(data_vocabulary$Modality)
contrast1 <- cbind (c(1/2,-1/2))
colnames (contrast1) <- c("-receptive+productive")
contrasts (data_vocabulary$Modality) <- contrast1
contrasts (data_vocabulary$Modality)
```

### Frequentist analyses

*Q-BEx model*

```{r}
# Run QBEx model
Model_vocab_QBEx <- glmer (Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + QBEx_Overall_Mixing_Parents_Scaled + (1|Subject) + (1|Item),
                      data = data_vocabulary, 
                   control = glmerControl(calc.derivs = FALSE), 
                   na.action = na.omit,
                   family = binomial)

# Summary and CI
model_parameters(Model_vocab_QBEx, ci = 0.975)
```

*LENA model*

```{r}
# Run LENA model
Model_vocab_LENA <- glmer (Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + LENA_Overall_Mixing_Parents_Scaled + (1|Subject) + (1|Item),
                      data = data_vocabulary, 
                   control = glmerControl(calc.derivs = FALSE), 
                   na.action = na.omit,
                   family = binomial)

# Summary and CI
model_parameters(Model_vocab_LENA, ci = 0.975)
```

### Bayesian analyses

Here, we use the brm function from the brms package to calculate the Bayes Factor for the effect of the Q-BEx and LENA overall mixing score on children's receptive vocabulary scores.

*Q-BEx model*

```{r fit bmrs vocab qbex model, cache = TRUE}

# set generic weak priors
priors = prior(normal(0, 1), class = 'b')

# Run QBEx model
model_vocab_QBEx_BF <- brm(Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + QBEx_Overall_Mixing_Parents_Scaled + (1|Subject) + (1|Item),
                           data = data_vocabulary, 
                           warmup = 1000,
                           prior = priors,
                           iter = 2000, 
                           chains = 4,
                           cores = 4,
                           seed = 123)

summary(model_vocab_QBEx_BF)
```

```{r}
hypothesis(model_vocab_QBEx_BF, "QBEx_Overall_Mixing_Parents_Scaled < 0")
```

*LENA model*

```{r fit bmrs vocab LENA model, cache = TRUE}
# Run LENA model
model_vocab_LENA_BF <- brm(Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + LENA_Overall_Mixing_Parents_Scaled + (1|Subject) + (1|Item), 
                           data = data_vocabulary, 
                           warmup = 1000,
                           prior = priors,
                           iter = 2000, 
                           chains = 4,
                           cores = 4,
                           seed = 123)

summary(model_vocab_LENA_BF)
```

```{r}
hypothesis(model_vocab_LENA_BF, "LENA_Overall_Mixing_Parents_Scaled < 0")
```


## Language mixing and grammar

### Frequentist analyses

*Q-BEx model*

```{r}
# Fit model on imputed datasets
model_grammar_QBEx <- with(imputed_Data_Total, exp = lm (CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + QBex_Overall_Mixing_Parents_Scaled))

# Pool models on imputed datasets and get 97.5% CI's for estimates
model_parameters(model_grammar_QBEx, ci = 0.975)
```

*LENA model*

```{r}
# Fit model on imputed datasets
model_grammar_LENA <- with(imputed_Data_Total, exp = lm (CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + LENA_Overall_Mixing_Parents_Scaled))

# Pool models on imputed datasets and get 97.5% CI's for estimates
model_parameters(model_grammar_LENA, ci = 0.975)
```

### Bayesian analyses

*Q-BEx model*

```{r fit bmrs grammar Q-BEx model, cache = TRUE}
# Run QBEx model
model_grammar_QBEx_BF <- brm_multiple(CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + QBex_Overall_Mixing_Parents_Scaled, 
                           data = imputed_Data_Total, 
                           warmup = 1000,
                           prior = priors,
                           iter = 2000, 
                           chains = 4,
                           cores = 4,
                           seed = 123)

summary(model_grammar_QBEx_BF)
```

```{r}
hypothesis(model_grammar_QBEx_BF, "QBex_Overall_Mixing_Parents_Scaled < 0")
```

*LENA model* 

```{r fit bmrs grammar LENA model, cache = TRUE}
# Run LENA model
model_grammar_LENA_BF <- brm_multiple(CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + LENA_Overall_Mixing_Parents_Scaled, 
                           data = imputed_Data_Total, 
                           warmup = 1000,
                           prior = priors,
                           iter = 2000, 
                           chains = 4,
                           cores = 4,
                           seed = 123)

summary(model_grammar_LENA_BF)
```

```{r}
hypothesis(model_grammar_LENA_BF, "LENA_Overall_Mixing_Parents_Scaled < 0")
```

## Exploratory research question 2a

Is the association the same for vocabulary and grammar? For this, we compare the 85% CIs.

```{r}
### Q-BEx
model_parameters(Model_vocab_QBEx, ci = 0.85)
model_parameters(model_grammar_QBEx, ci = 0.85)

### LENA
model_parameters(Model_vocab_LENA, ci = 0.85)
model_parameters(model_grammar_LENA, ci = 0.85)
```

## Exploratory research question 2b

Is the association the same for between and within speakers mixing?

First, we must run the separate models.

```{r}
### Q-BEx vocab
### Between speakers mixing
Model_vocab_betweenQBEx <- glmer (Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + QBex_BetweenSpeakers_Parents_Scaled + (1|Subject) + (1|Item),
                      data = data_vocabulary, 
                   control = glmerControl(calc.derivs = FALSE), 
                   na.action = na.omit,
                   family = binomial)

### Within speakers mixing 
Model_vocab_withinQBEx <- glmer (Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + QBex_WithinSpeakers_Parents_Scaled + (1|Subject) + (1|Item),
                      data = data_vocabulary, 
                   control = glmerControl(calc.derivs = FALSE), 
                   na.action = na.omit,
                   family = binomial)

### LENA vocab
### Between speakers mixing
Model_vocab_betweenLENA <- glmer (Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + LENA_BetweenSpeakers_Parents_Scaled + (1|Subject) + (1|Item),
                      data = data_vocabulary, 
                   control = glmerControl(calc.derivs = FALSE), 
                   na.action = na.omit,
                   family = binomial)

### Within speakers mixing 
Model_vocab_withinLENA <- glmer (Accuracy ~  1 + Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + Modality + LENA_WithinSpeakers_Parents_Scaled + (1|Subject) + (1|Item),
                      data = data_vocabulary, 
                   control = glmerControl(calc.derivs = FALSE), 
                   na.action = na.omit,
                   family = binomial)

### Q-BEx grammar
### Between speakers mixing
model_grammar_betweenQBEx <- with(imputed_Data_Total, exp = lm (CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + QBex_BetweenSpeakers_Parents_Scaled))

### Within speakers mixing 
model_grammar_withinQBEx <- with(imputed_Data_Total, exp = lm (CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + QBex_WithinSpeakers_Parents_Scaled))

### LENA grammar
### Between speakers mixing
model_grammar_betweenLENA <- with(imputed_Data_Total, exp = lm (CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + LENA_BetweenSpeakers_Parents_Scaled))

### Within speakers mixing 
model_grammar_withinLENA <- with(imputed_Data_Total, exp = lm (CELF_SR_Scaled ~  Age_Test1_Scaled + QBex_Cumulative_Exposure_Dutch_Scaled + Qbex_Parental_Education_Scaled + LENA_WithinSpeakers_Parents_Scaled))

```

Second, we compare the 85% CIs.

```{r}
### Q-BEx vocab
model_parameters(Model_vocab_betweenQBEx, ci = 0.85)
model_parameters(Model_vocab_withinQBEx, ci = 0.85)

### LENA vocab
model_parameters(Model_vocab_betweenLENA, ci = 0.85)
model_parameters(Model_vocab_withinLENA, ci = 0.85)

### Q-BEx grammar
model_parameters(model_grammar_betweenQBEx, ci = 0.85)
model_parameters(model_grammar_withinQBEx, ci = 0.85)

### LENA grammar
model_parameters(model_grammar_betweenLENA, ci = 0.85)
model_parameters(model_grammar_withinLENA, ci = 0.85)
```
