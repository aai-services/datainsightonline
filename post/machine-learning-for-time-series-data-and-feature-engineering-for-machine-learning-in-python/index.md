---
title: "Machine Learning for Time Series Data and Feature Engineering for Machine Learning in Python"
author: "Arpan Sapkota"
date: 2022-05-09
description: "Machine Learning for Time Series Data in Python Real-world data sets are essential for developing and testing machine learning models. You might just need some data to play with with an algorithm..."
categories: ["Machine Learning", "Time Series", "Python"]
image: images/a8b2bc_2707ac92713d44159c2459c84f9d3f2d.webp
wix-url: https://www.datainsightonline.com/post/machine-learning-for-time-series-data-and-feature-engineering-for-machine-learning-in-python
---
Machine Learning for Time Series Data in Python

![](images/a8b2bc_2707ac92713d44159c2459c84f9d3f2d.webp)

Real-world data sets are essential for developing and testing machine learning models. You might just need some data to play with with an algorithm. You can also wish to assess your model by creating a benchmark or identifying its flaws using several data sets. You might also want to make synthetic datasets to test your algorithms under controlled conditions by introducing noise, correlations, or redundant data to the data.

Loading Data Using pandas-datareader

Anyone can use the pandas datareader library to get data from a variety of places, including Yahoo Finance for financial market data, the World Bank for global development data, and the St. Louis Fed for economic data. We'll teach you how to load data from several sources in this section.
Pandas datareader gets data from the web in real time and assembles it into a pandas DataFrame behind the scenes. Each data source requires a distinct reader due to the drastically diverse structure of web pages. As a result, pandas datareader can only read from a small number of sources, most of which are connected to financial and economic time series.

Data retrieval is straightforward. Because we know Apple's stock ticker is AAPL, we can collect daily historical Apple stock prices from Yahoo Finance as follows:

```python
import pandas_datareader as pdr
# Reading Apple shares from yahoo finance server
shares_df = pdr.DataReader('AAPL', 'yahoo', start='2021-01-01', end='2021-12-31')
# Look at the data read
print(shares_df)
```

The first argument to DataReader() specifies the ticker, while the second argument specifies the data source.

We can also get stock price history from many firms using a list of tickers:

```python
companies = ['AAPL', 'MSFT', 'GE']
shares_multiple_df = pdr.DataReader(companies, 'yahoo', start='2021-01-01', end='2021-12-31')
print(shares_multiple_df.head())
```

Because of the structure of DataFrames, extracting parts of the data is simple. For example, for some dates, we can plot only the daily close price using the following formula:

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# General routine for plotting time series data
def plot_timeseries_df(df, attrib, ticker_loc=1, title='Timeseries',
                       legend=''):
    fig = plt.figure(figsize=(15,7))
    plt.plot(df[attrib], 'o-')
    _ = plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(ticker_loc))
    plt.title(title)
    plt.gca().legend(legend)
    plt.show()
```

```python
plot_timeseries_df(shares_multiple_df.loc["2021-04-01":"2021-06-30"], "Close",ticker_loc=3, title="Close price", legend=companies)
```

Using pandas-datareader to read from another data source has a similar syntax.

The steps for obtaining two consumer price indices, CPIAUCSL and CPILFESL, and plotting them are as follows:

```python
import pandas_datareader as pdr
import matplotlib.pyplot as plt

# Read data from FRED and print
fred_df = pdr.DataReader(['CPIAUCSL','CPILFESL'], 'fred', "2010-01-01", "2021-12-31")
print(fred_df)

# Show in plot the data of 2019-2021
fig = plt.figure(figsize=(15,7))
plt.plot(fred_df.loc["2019":], 'o-')
plt.xticks(rotation=90)
plt.legend(fred_df.columns)
plt.title("Consumer Price Index")
plt.show()
```

For analyzing and forecasting time-based data, time series algorithms are widely employed. Machine learning has developed as an effective tool for recognizing hidden complexities in time series data and making reasonable forecasts, given the complexity of other elements outside time.

Feature Engineering for Machine Learning in Python

![](images/a8b2bc_d041c08e36904bb891362686dfd2d1ab.webp)

The most crucial, yet often underestimated, talent in predictive modeling is feature engineering. We use it without even realizing it in our daily lives!
Lets imagine you're a bartender and someone approaches you and requests a vodka tonic. When you ask for identification, you notice the person's birthday is "09/12/1998." This information isn't particularly useful, but you can tally up the years with some rapid mental math and discover that the person is 22 years old (which is above the legal drinking age). What happened there, exactly? To answer the question "Is this individual authorized to drink?" you took a piece of data ("09/12/1998") and translated it into another variable (age).

This is exactly what feature engineering is for machine learning models. We alter and manipulate our data to provide our model(s) the best possible representation of our data in order to better forecast our desired outcome. If this isn't completely evident right now, it will be when we go through real-life instances in this essay.

For the following reasons, feature engineering is both beneficial and necessary:

- Feature engineering approaches like as standardization and normalization typically result in better weighting of variables, which increases accuracy and, in certain cases, speeds up convergence.
- Improved interpretability of data relationships: When we create new features and understand how they connect to our desired outcome, we have a better comprehension of the data. We may still acquire a high assessment score if we skip the feature engineering step and utilize complicated models (which to a significant extent automate feature engineering), but at the cost of a deeper grasp of our data and its relationship with the goal variable.

Because most models cannot accept specific data forms, feature engineering is required. Missing values cannot be handled by models like linear regression on their own; they must be imputed (filled in). In the next part, we'll examine some examples of this.

Exploratory Data Analysis (EDA), or the initial analysis of our data, is the first step in every data science pipeline. As we gain a better understanding of what features we need to create/modify, EDA is a critical pre-cursor stage. Depending on how unstructured or chaotic the data is, the following stage is usually data cleaning/standardization.
The following step is feature engineering, which begins with an evaluation of the data's baseline performance. Then, using a feature selection method, we iteratively create features and continuously evaluate model performance (and compare it to the baseline performance) until we are satisfied with the findings.

For most tabular datasets, there are two major ways to feature engineering:

- The checklist approach: create features using proven and true approaches.
- The domain-based approach: involves using domain knowledge about the dataset's subject matter to build additional features.

We'll now take a closer look at these methods using real-world data. Note that these examples are procedural in nature and are intended to demonstrate how to implement it in Python. The case study that follows this part will show you a real-world end-to-end scenario application of the practices discussed here.
Before loading the dataset, we need to import the dependencies listed below.

```python
# dependencies

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_palette(sns.color_palette(['#851836', '#edbd17']))
sns.set_style("darkgrid")

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
```

We'll use a dataset on grocery sales to demonstrate the checklist approach.

The Checklist Approach

Numeric Aggregations

For longitudinal or panel data, when individuals are repeated, numerical aggregation is a typical feature engineering strategy. We have categorical variables with repeated observations in our dataset (for example, we have multiple entries for each supermarket branch).

Numeric aggregation involves three parameters:

- Categorical column
- Numeric column(s) to be aggregated
- Aggregation type: Mean, median, mode, standard deviation, variance, count etc.

  Three instances of numeric aggregations based on mean, standard deviation, and count are shown in the code chunk below.

```python
# Numeric aggregations

grouped_df = df.groupby('Branch')

df[['tax_branch_mean','unit_price_mean']] = grouped_df[['Tax 5%', 'Unit price']].transform('mean')

df[['tax_branch_std','unit_price_std']] = grouped_df[['Tax 5%', 'Unit price']].transform('std')

df[['product_count','gender_count']] = grouped_df[['Product line', 'Gender']].transform('count')
```

And here are the new features we've added.

```python
df[['Branch', 'tax_branch_mean', 'unit_price_mean', 'tax_branch_std','unit_price_std', 'product_count', 'gender_count']].head(10)
```

There appear to be duplicate rows because we're viewing a column subset of the whole df. When you see the rest of the columns, you'll discover that while there are no duplicate rows, there are duplicate values. This is intentional.

Choosing numeric aggregation parameters

```python
df[['Tax 5%', 'Unit price', 'Branch', 'tax_branch_mean', 'unit_price_mean']]
```

Indicator Variables

- To signify the absence or availability of some information, indicator variables only take on the values 0 or 1.

Interaction Terms

- The presence of interaction effects between two or more variables leads to the creation of interaction terms. Although statistical methods can help detect them, subject expertise plays a key role (which is beyond the scope of this article). Free shipping, for example, may affect customer rating, but free shipping combined with quantity may have a different effect, which would be important to encode (assuming customer rating is the target variable in this case). The variable unit price 50 \* qty is defined to be exactly that.

```python
df['unit_price_50'] = np.where(df['Unit price'] > 50, 1, 0)
```

```python
df['unit_price_50 * qty'] = df['unit_price_50'] * df['Quantity']
```

Numeric Transformations

Numeric transformations are not considered feature engineering by some data scientists. This is due to the fact that many models, particularly newer ones such as tree-based models (decision trees, random forests, and so on), are unaffected by these modifications. To put it another way, completing these modifications has no effect on predictive performance. However, because other models, such as linear regression, are sensitive to the scale of their variables, these changes can make a huge impact.

To account for the right skew in the variable cogs, we create a new variable log cogs. The result is depicted in the graphs below the code portion.
If we feel the relationship between a predictor and target variable is not linear, but quadratic in nature, we can perform different adjustments such as squaring a variable (seen in the code chunk below) (as a predictor variable changes, target variable changes by an order of 2).
It's up to your decision and domain knowledge whether we use cubed variables or any n degree polynomial term.

```python
# numeric transformations

df['log_cogs'] = np.log(df['cogs'] + 1)
df['gross income squared'] = np.square(df['gross income'])
```

As can be seen, the log transformation made the Cost of Goods Sold (cogs) distribution more regularly distributed (or less right-skewed). Outliers that generated the initial skewness will have less of an impact on the weights/coefficients of models like linear regression.

Simillary in checklist approach we can do :

- Numeric Scaling
- Categorical Variable Handling
- Missing Value Handling
- Date-Time Decomposition

Domain-based Approach

The line between domain-based and checklist-based approaches to feature engineering is blurry. I believe the distinction is purely subjective; with domain-based features, you still use many of the techniques we've already discussed, but with a strong focus on domain knowledge.
Many ad-hoc measures, such as ratios and formulas, will be used in domain-based features. In the case study example below, we'll see examples of this.

Example - Movie Box Office Data

We'll be using movie box office data for our case study. More information on the dataset can be found by going here.
Normally, we would begin by performing exploratory data analysis on the dataset, but as this is a feature engineering post, we will concentrate on that. Note that many of the feature engineering techniques shown below were inspired by a Kaggle kernel found here.

Filling missing values

Let's start with missing values. We use Seaborn to display them and then use the median and mode to fill in numeric and categorical missing values.

```python
plt.figure(figsize=(15, 15))
sns.heatmap(df.isnull(), cbar=False);
```

The median will be used to fill in the missing numeric variables, and the mode will be used to fill in the blank category column. After we finish feature engineering the other columns, we'll address the categorical missing data (at the very end).
There is no clear and fast rule for deciding which missing value imputation method to use. Most practitioners evaluate several missing value imputation strategies before selecting the one with the highest evaluation score.

Decomposing Date

We can now break down the date column into its constituent characteristics. Because there is no quantitative relationship between month and day, we encode them as string variables. Days and months have set boundaries (the month cannot exceed 12 and the day cannot exceed 31). The days 10 and 31 are just different (think of them as categories).
Let's separate the year, month, and day columns in the dataframe:

```python
df['release_date'] = pd.to_datetime(df['release_date'])

# decomposition
df['Year'] = df['release_date'].dt.year
df['Month'] = df['release_date'].dt.month.astype(str)
df['Day'] = df['release_date'].dt.day.astype(str)

df[['Year','Month','Day']].head()
```

Adjusting budget

We use the logarithm of the budget to account for the right-skewed nature of the budget. Because many movies have a budget of $0, we use the logarithm of the budget Plus 1 instead of the logarithm of 0.

```python
df['log_budget'] = np.log(df['budget'] + 1)

plot_hist(df['budget'], df['log_budget'])
```

Prediction

We can develop a simple regression model to forecast movie income to show that feature engineering works and improves model performance.
Normally, we choose which features to utilize using a process called feature selection, but since this post is about feature engineering, we'll use a simpler method: correlation analysis.

We can see that most of the variables we produced aren't very predictive of revenue by plotting the correlation matrix (below). Most of the time, this is what happens: you design a lot of features, but only a few of them are useful - but the ones that are valuable make a difference.
