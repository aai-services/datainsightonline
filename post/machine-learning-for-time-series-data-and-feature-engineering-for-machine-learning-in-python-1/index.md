---
title: "Machine Learning for Time Series Data And Feature Engineering for Machine Learning in Python"
author: "Tanushree Nepal"
date: 2022-06-08
description: "Time series data is ubiquitous. Whether it be stock market fluctuations, sensor data recording climate change, or activity in the brain, any signal that changes over time can be described as a time..."
categories: ["Machine Learning", "Time Series", "Python"]
image: images/79946d_ab4f2be6b5ac4e5187249cd5755237a9.webp
wix-url: https://www.datainsightonline.com/post/machine-learning-for-time-series-data-and-feature-engineering-for-machine-learning-in-python-1
---
![](images/79946d_ab4f2be6b5ac4e5187249cd5755237a9.webp)

Time series data is ubiquitous. Whether it be stock market fluctuations, sensor data recording climate change, or activity in the brain, any signal that changes over time can be described as a time series. Machine learning has emerged as a powerful method for leveraging complexity in data in order to generate predictions and insights into the problem one is trying to solve.

Most organizations generate time-series data. The generation of sales and financial data are the primary components of all organizations’ business. This data is a form of time series data. Time series data consists of any data that carries a temporal component. Time series data is recorded across time, not always in consistent intervals, but across time nonetheless. Understanding time series data allows us the avenue of what the future may hold. As such, most forecasting problems involve some flavor of time series analysis. The forecast model seeks to use knowledge of the past to explain what should be expected in the future at various time periods.

There are many methods that are great at solving time series problems. Traditionally, these methods fell well within the realm of statistical modeling. Auto-Regressive Integrated Moving Average (ARIMA), Exponential Smoothing, and Fourier Transforms have all proven successful at modeling time series data. Many of these methods are univariate in nature. Univariate methods may leave a gap in understanding of the time series. In situations for which a greater understanding of the influence on the time series is required, we can turn to multivariate methods. One of these multivariate approaches is through using machine learning methods to build time series models that are both accurate in their forecast and allow for the inclusion of influential features on the time series.

**Feature Engineering for Machine Learning in Python**

Feature Engineering is the process of transforming data to increase the predictive performance of machine learning models. Every day we read about the amazing breakthroughs in how the newest applications of machine learning are changing the world. Often this reporting glosses over the fact that a huge amount of data munging and feature engineering must be done before any of these fancy models can be used.

Feature engineering is both beneficial and necessary because of the following reasons:

- Feature engineering approaches like standardization and normalization typically result in the better weighting of variables, which increases accuracy and, in certain cases, speeds up convergence.
- Improved interpretability of data relationships: When we create new features and understand how they connect to our desired outcome, we have a better comprehension of the data. We may still acquire a high assessment score if we skip the feature engineering step and utilize complicated models (which to a significant extent automate feature engineering), but at the cost of a deeper grasp of our data and its relationship with the goal variable.

The first step of Featuring engineering is getting to know our data Fo this blog we will be using [**Stackoverflow survey response data**](https://insights.stackoverflow.com/survey/2018/#overview)**.**

Pandas is one of the most popular packages used to work with tabular data in Python. It is generally imported using the alias pd and can be used to load a CSV (or other delimited files) using read_csv().

```python
# Create subset of only the numeric columns
so_numeric_df = so_survey_df.select_dtypes(include=['int','float'])

# Print the column names contained in so_survey_df_num
print(so_numeric_df.columns)
```

To use categorical variables in a machine learning model, we first need to represent them in a quantitative way. The two most common approaches are to one-hot encode the variables using or to use dummy variables

- One-hot encode the Country column, adding "OH" as a prefix for each column.

```python
# Convert the Country column to a one hot encoded Data Frame
one_hot_encoded = pd.get_dummies(so_survey_df, columns=['Country'], prefix='OH')

# Print the columns names
print(one_hot_encoded.columns)
```

- Creating dummy variables for the Country column, adding "DM" as a prefix for each column.

```python
# Create dummy variables for the Country column
dummy = pd.get_dummies(so_survey_df, columns=['Country'], drop_first=True, prefix='DM')

# Print the columns names
print(dummy.columns)
```

The difference we see when using these two encoding processes is that a column named "France" is missing when using the Dummy variable.

**Dealing with uncommon categories**

Some features can have many different categories but a very uneven distribution of their occurrences. For example Data Science's favorite languages to code in, some common choices are Python, R, and Julia, but there can be individuals with bespoke choices, like FORTRAN, C etc. In these cases, you may not want to create a feature for each value, but only the more common occurrences.

```python
# Create a series out of the Country column
countries = so_survey_df['Country']

# Get the counts of each category
country_counts = countries.value_counts()

# Print the count values for each category
print(country_counts)
```

## How sparse is my data?
Most datasets contain missing values, often represented as NaN (Not a Number). If you are working with Pandas you can easily check how many missing values exist in each column.

```python
# Subset the DataFrame
sub_df = so_survey_df[['Age', 'Gender']]

# Print the number of non-missing values
print(sub_df.info())
```
