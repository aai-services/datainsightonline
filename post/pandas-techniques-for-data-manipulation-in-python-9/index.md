---
title: "Pandas Techniques for Data Manipulation in Python"
author: "cheikhbadiane99"
date: 2022-06-08
description: "In this blog post, we are going to talk about two technics of the python pandas library for sorting DataFrame and Imputing missing values.Sorting Dataframe in PythonHere is the dataset we are going..."
categories: ["Pandas", "Python"]
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-manipulation-in-python-9
---
In this blog post, we are going to talk about two technics of the python pandas library for sorting DataFrame and Imputing missing values.

## Sorting Dataframe in Python

Here is the dataset we are going to use in this blog post.

In pandas we can sort DataFrame by values or index based on what we want to do.

**Sorting by values: .sort_values()**

Here we sorted our dataset based on the Year column. By default when we do not specify the sorting order, pandas sort in ascending order. But we can change this by specifying the sorting order we want the DataFrame to sorted on.

Seting the ascending parameter to false means we want to sort the DataFrame in descending order.

We can add one of the pandas sorting algorithm wich are quicksort, heapsort and mergesort. But we are going to use just mergesort algorithm wich the only stable know today.

### Sorting multiples columns

We can also sort multiple columns in pandas.

We can sort different columns and add different sorting order in pandas as you can see below.

### Sorting by index: .sort_index()

Now let's use these sorted columns as a new DataFrame called sort_df and sort it by index and see how it looks like.

## Imputing missing values in pandas

For this part, we are going to use the same dataset and let's see if it contains missing values and if yes, we will use some pandas imputation technics to deal with the missing values.

We can see there are missing values in columns: Engine Fuel Type, Engine HP, Engine Cylinders, Number of Doors, Market Category.

Let's print out the percentage of missing values for each columns.

We can see that market Category column has the heighest percentage of missing values over 31%.

Pandas gives us many technics to deal with missing values.

We can fill missing values or just drop them using fillna or drop functions.

### Imputing missing values with zero

We can see that there are no more missing values in the dataset, because all missing values are imputed (replaced) by 0.

### Fill NA Forward / Backward
We can imput for each row with NA values, the values of the intermediate row at the top or the bottom.

### Fill NA forward: pad/fill

For each row with NA values, the values of the intermediate row at the top have been used for filling in pad method.

### Fill NA backward: bfill/backfill

### Dropping missing values
In other situations, we can just drop missing values in the dataset. For example, when the percentage of missing values is very small, we can think dropping missing values from the dataset or for just some columns, using the dropna() function.

In the real life projects, we use a specific imputation method for each column based on the problem and the reason on missing values.

Thanks for reading.
