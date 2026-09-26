---
title: "Pandas Techniques for Data Analysis"
author: "Fatma Ali"
date: 2021-11-21
description: "Introduction:Pandas is a Python module for working with tabular data (i.e., data in a table with rows and columns). Tabular data has a lot of the same functionality as SQL or Excel, but Pandas adds..."
categories: ["Pandas", "Projects"]
image: images/f5d020_0fec4e4259604b60ad15082f39b26f74.webp
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-analysis
---
![](images/f5d020_0fec4e4259604b60ad15082f39b26f74.webp)

## Introduction:
Pandas is a Python module for working with tabular data (i.e., data in a table with rows and columns). Tabular data has a lot of the same functionality as SQL or Excel, but Pandas adds the power of Python. In order to get access to the Pandas module, we’ll need to install the module and then import it into a Python file.

The pandas module is usually imported at the top of a Python file under the alias pd.

```python
import pandas as pd
```

we’ll be working with datasets that already exist. One of the most common formats for big datasets is the *CSV*. *CSV (*comma-separated *values)* is a text-only spreadsheet format. You can find CSVs in lots of places. Our dataset is an open-source dataset and you can download it from [this link](https://www.kaggle.com/PromptCloudHQ/imdb-data).

In this article, I will explain some Pandas techniques for data analysis.

1- Inspect a Dataframe

2- Data selection

3-Groupby operations

4-sorting operations

5- Apply functions

**Inspect a DataFrame**

When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv():

```python
df = pd.read_csv('IMDB-Movie-Data.csv')
df
```

In the example above, the .read_csv() method is called. The CSV file called my-csv-file is passed in as an argument.

```python
df.head()
df.head(10)
```

When we load a new DataFrame from a CSV, we want to know what it looks like. If it’s a small DataFrame, you can display it by typing print(df). If it’s a larger DataFrame, it’s helpful to be able to inspect a few items without having to look at the entire DataFrame. The method .head() gives the first 5 rows of a DataFrame. If you want to see more rows, you can pass in the positional argument n. For example, df.head(10) would show the first 10 rows.

```python
df.info()
```

The method **df.info()** gives some statistics for each column.

## Selecting Data

**Select Columns:**

Now we know how to create and load data. Let’s select parts of those datasets that are interesting or important to our analyses.

```python
#Select Columns
director = df[['Director']]
director
```

### Selecting Multiple Columns
When you have a larger DataFrame, you might want to select just a few columns.

```python
multi_col = df[['Rank', 'Title']]
```

**Select Rows**

We want to select this single row of data.

DataFrames are zero-indexed, meaning that we start with the 0th row and count up from there.

```python
df.iloc[[2]]
```

**Select Rows with Logic**

You can select a subset of a DataFrame by using logical statements:

```python
#Select Rows with Logic
genre=df[df['Genre']== 'Horror']
genre
```

## Groupby Operation
A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.

```python
df.groupby('Genre')['Votes'].mean().head()
```

**Sorting operation**
***sort_values( )*** method is used to perform sorting operations

on a column or a list of multiple columns.

```python
df.groupby('Genre')[['Votes']].mean().sort_values(['Votes']).head()
```

## Apply Function
Pandas.apply allow the users to pass a function and apply it on every single value of the Pandas series. It comes as a huge improvement for the pandas library as this function helps to segregate data according to the conditions

```python
# Classify movies based on ratings
def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'
```

```python
# creating a new variable in the dataset to hold the rating category
df['Rating_category'] = df['Rating'].apply(rating_group)
df[['Title','Director','Rating','Rating_category']].head(10)
```

The full code [here](https://github.com/fatmtly892/Pandas-Techniques-for-Data-Analysis)
