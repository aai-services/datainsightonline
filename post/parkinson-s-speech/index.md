---
title: "Parkinson's Speech?"
author: "Blessing Oludele"
date: 2022-11-11
description: "Dealing with any form of disease is traumatizing enough. From history early detection have proven to have a huge impact on patients and Parkinson's disease is no exemption.Parkinson's disease usually..."
categories: ["General"]
image: images/c58e2f_3982e1be1ef6471bbaf4b87f8f03a0ae.webp
wix-url: https://www.datainsightonline.com/post/parkinson-s-speech
---
Dealing with any form of disease is traumatizing enough. From history early detection have proven to have a huge impact on patients and Parkinson's disease is no exemption.

Parkinson's disease usually develop gradually and are mild at first. The order of the symptoms and their severity are normally peculiar based on the individual case. Some of the main symptoms are:

- Tremor: This the shaking which occurs mostly at the limbs and is visible when relaxing or at rest.

- Slowness of movement (bradykinesia): physical movements for people with Parkinson's are usually much slower.

- Muscle stiffness (rigidity): stiffness and tension in the muscles, which can make it difficult to move around and make facial expressions, and can result in painful muscle cramps.

They are other symptoms including cognitive and psychiatric.

In the paper 'Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection' by Little MA, et. al. in 2007 it was suggested that audio signals could be analyzed and used for early detection of some neurodegenerative diseases. The data set is provided on the UCL ML dataset repository for Parkinson's disease and this blog shows the process of creating a classification model.

Reading in the data and import necessary modules.

![](images/c58e2f_3982e1be1ef6471bbaf4b87f8f03a0ae.webp)

Inspecting the dataset

![](images/c58e2f_adca68a876d644c2b37fb4b3aaa09355.webp)

There are no null values in the dataset, columns are in the correct data type apart from the target column ('status') that can be represented as a categorical variable so it's considerably clean.

Separating the features and target

Visualizing correlation

![](images/c58e2f_a011a8ea09324fddbacd525f2250ab26.webp)

We have 24 columns which is considerably a lot compared to the rows (195) so dimensionality reduction is needed.

![](images/c58e2f_38b4f61ff8ac400a88152492939a2a26.webp)

![](images/c58e2f_f3a40e20c6314d2994f14e9218441cb0.webp)

![](images/c58e2f_8a861d341ce84949a94ea181a6a14f84.webp)

![](images/c58e2f_458d77276f3e4496936b55b0bea669ca.webp)

**Questions:**

1. what are the features necessary in building the model

- MDVP:Fo(Hz) - Average vocal fundamental frequency

- MDVP:Fhi(Hz) - Maximum vocal fundamental frequency

- MDVP:Flo(Hz) - Minimum vocal fundamental frequency

- MDVP:Jitter(%) - measures of variation in fundamental frequency

- MDVP:Jitter(Abs) - measures of variation in fundamental frequency

- MDVP:Shimmer - measures of variation in fundamental amplitude

- NHR - measures of ratio of noise to tonal components in the voice

- HNR - measures of ratio of noise to tonal components in the voice

- RPDE - nonlinear dynamical complexity measures

- DFA - Signal fractal scaling exponen

- spread1 - nonlinear measures of fundamental frequency variation

- spread2 - nonlinear measures of fundamental frequency variation

- D2 - nonlinear dynamical complexity measures

2. what features are the most important

![](images/c58e2f_5483bce9ef7743f4932085037209ea07.webp)

3. What type of algorithms can you try:

this is a classification problem so good classifiers are suitable e.g random forest classifiers, logistic regressors and boosting algorithmns

References

'Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection', Little MA, McSharry PE, Roberts SJ, Costello DAE, Moroz IM. BioMedical Engineering OnLine 2007, 6:23 (26 June 2007)

Max A. Little, Patrick E. McSharry, Eric J. Hunter, Lorraine O. Ramig (2008), 'Suitability of dysphonia measurements for telemonitoring of Parkinson's disease', IEEE Transactions on Biomedical Engineering (to appear).

[Parkinson's disease - Symptoms - NHS (www.nhs.uk)](https://www.nhs.uk/conditions/parkinsons-disease/symptoms/) (checked 11/11/2022)
