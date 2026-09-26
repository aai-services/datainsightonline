---
title: "Data Preprocessing and Dimension Reduction"
author: "Gaurab Awal"
date: 2022-04-24
description: "Data Preprocessing in Machine LearningReal-world data generally contains noises, and missing values, and maybe in an unusable format that cannot be directly used for machine learning models. Data..."
categories: ["Data Cleaning"]
wix-url: https://www.datainsightonline.com/post/data-preprocessing-and-dimension-reduction
---
#### Data Preprocessing in Machine Learning
Real-world data generally contains noises, and missing values, and maybe in an unusable format that cannot be directly used for machine learning models. Data preprocessing is a required task for cleaning the data and making it suitable for a machine learning model which also increases the accuracy and efficiency of a machine learning model.

It involves the below steps:

1. Finding Missing Data

If our dataset contains some missing data, then it may create a huge problem for our machine learning model. Hence it is necessary to handle missing values present in the dataset.

2. Treating the outliers

Outliers can have a huge impact on data analysis results. For example, if you're averaging test scores for a class, and one student didn’t respond to any of the questions, their 0% could greatly skew the results.

3.Encoding Categorical Data

Handling categorical variables is another integral aspect of Machine Learning. Categorical variables are basically the variables that are discrete and not continuous. For example, the color of an item is a discrete variable whereas its price is a continuous variable.

4. Feature Scaling

Feature scaling is the final step of data preprocessing in machine learning. It is a technique to standardize the independent variables of the dataset in a specific range. In feature scaling, we put our variables in the same range and in the same scale so that no variable dominates the other variable.

#### Dimension Reduction
If your data is represented using rows and columns, such as in a spreadsheet, then the input variables are the columns that are fed as input to a model to predict the target variable. Input variables are also called features.

Having a large number of dimensions in the feature space can mean that the volume of that space is very large, and in turn, the points that we have in that space (rows of data) often represent a small and non-representative sample.

This can dramatically impact the performance of machine learning algorithms fit on data with many input features, generally referred to as the “curse of dimensionality.”

Dimensionality reduction could be done by both feature selection methods as well as feature engineering methods.

Feature selection is the process of identifying and selecting relevant features for your sample. Feature engineering is manually generating new features from existing features, by applying some transformation or performing some operation on them.

**Advantages of Dimensionality Reduction**

- It helps in data compression, and hence reduced storage space.
- It reduces computation time.
- It also helps remove redundant features, if any.

**Disadvantages of Dimensionality Reduction**

- It may lead to some amount of data loss.
- PCA tends to find linear correlations between variables, which is sometimes undesirable.
- PCA fails in cases where mean and covariance are not enough to define datasets.
- We may not know how many principal components to keep- in practice, some thumb rules are applied.
