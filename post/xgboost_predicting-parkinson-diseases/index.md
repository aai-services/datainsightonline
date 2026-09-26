---
title: "XGBoost Predicting Parkinson Diseases"
author: "adipurnamk"
date: 2020-08-13
description: "Neurodegenerative diseases are a heterogeneous group of disorders that are characterized by the progressive degeneration of the structure and function of the nervous system."
categories: ["Machine Learning"]
image: images/a27d24_a0bb996c29ca49758b93e125d27cc1a1.webp
wix-url: https://www.datainsightonline.com/post/xgboost_predicting-parkinson-diseases
---
![](images/a27d24_af8779560846487abb8c0bbaf28719ff.webp)

## Introduction

Neurodegenerative diseases are a heterogeneous group of disorders that are characterized by the progressive degeneration of the structure and function of the nervous system. They are incurable and debilitating conditions that cause problems with mental functioning also called dementias.

Neurodegenerative diseases affect millions of people worldwide. Alzheimer’s disease and Parkinson’s disease are the most common neurodegenerative diseases. In 2016, an estimated 5.4 million Americans were living with Alzheimer’s disease. An estimated 930,000 people in the United States could be living with Parkinson’s disease by 2020.

The goal of this project is to build a model to accurately predict the presence of a neurodegenerative disease in an individual as early detection of a neurodegenerative disease could be useful for the identification of people who can participate in trials of neuroprotective agents, or ultimately to try and halt disease progression once effective

disease-modifying interventions have been identified.

## Dataset

The dataset was created by Max Little of the University of Oxford, in

collaboration with the National Centre for Voice and Speech, Denver,

Colorado, who recorded the speech signals. The original study published the

feature extraction methods for general voice disorders.

[UCI ML Parkinson’s dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/)

The metadata from this dataset is a file, so we need to open it in a programming way.

```python
# Download the metadata using wget command
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/parkinsons.names

# Read the dataset metadata
with open('/content/parkinsons.names') as txt:
    for t in txt:
        print(t)
```

From existing metadata, we get some important information, such as:

\* Title: Parkinsons Disease Data Set

\* Abstract: Oxford Parkinson's Disease Detection Dataset

\* Data Set Characteristics: Multivariate

\* Number of Instances: 197

\* Number of Attributes: 23

### Dataset Information

This dataset is composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease (PD). Each column in the table is a particular voice measure, and each row corresponds one of 195 voice recording from these individuals ("name" column). The main aim of the data is to discriminate healthy people from those with PD, according to "status" column which is set to 0 for healthy and 1 for PD.

### Attribute Information

Matrix column entries (attributes):

\* name - ASCII subject name and recording number

\* MDVP:Fo(Hz) - Average vocal fundamental frequency

\* MDVP:Fhi(Hz) - Maximum vocal fundamental frequency

\* MDVP:Flo(Hz) - Minimum vocal fundamental frequency

\* MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several

\* measures of variation in fundamental frequency

\* MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude

\* NHR,HNR - Two measures of ratio of noise to tonal components in the voice

\* status - Health status of the subject (one) - Parkinson's, (zero) - healthy

\* RPDE,D2 - Two nonlinear dynamical complexity measures

\* DFA - Signal fractal scaling exponent

\* spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation

## Exploratory Data Analysis

```python
# Download the dataset using wget command
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/parkinsons.data

# Import the dataframe using Pandas
df = pd.read_csv('parkinsons.data')
df
```

Before we step further, we need to explore our dataset first. This EDA's steps include:

1. Using .info() method to examine each column data type and possible missing data

```python
Examine the data type for each columns and possible missing data
df.info()
```

![](images/a27d24_644ce0b7e7da4f899cc8154ece659185.webp)

2. Using .describe() method to see data summary statictic, such as min, median, max, and so on.

```python
# See the statistic summary
df.describe()
```

![](images/a27d24_b8e590f62d444cebba04e9270c0999cf.webp)

3. Using .corr() to see if there is a correlation between a pair of feature.

```python
# See correlation for each feature
df.corr()
```

![](images/a27d24_cd49c7d0236c4667a04523d80b4cd674.webp)

4. Then we draw the heatmap to easily examine the result from step 3.

```python
# Plot heatmap
fig, ax = plt.subplots(figsize=(15,15))
ax = sns.heatmap(df.corr(), annot=True);
```

![](images/a27d24_ea9b4c6b69c44a4f97f901f72815817e.webp)

5. Plot status column using pie chart.

```python
# Plot using pie chart
df.status.value_counts().plot.pie()
```

![](images/a27d24_c7ce0ae535c044609abde97fc8c09b47.webp)

## Data Preparation

Since the status column is located in the middle of dataset, we need to move it to the far right, so we can easily slice the dataset.

```python
# Move status column to the far right
cols = list(df)
cols.insert(24, cols.pop(cols.index('status')))
```

## Reference

'Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection', Little MA, McSharry PE, Roberts SJ, Costello DAE, Moroz IM. BioMedical Engineering OnLine 2007, 6:23 (26 June 2007).

For the repo, you can refer [here](https://github.com/adipurnamk/XGBoost_Predicting-Parkinson-Diseases)
