---
title: "Detect and Impute Missing Values in Pandas"
author: "Ebrima Sise"
date: 2022-05-08
description: "Hardly you will come across a dataset that is free from missing values. Missing values can be encoded in a number of ways. Sometimes when dealing with numeric data, missing data can be encoded with..."
categories: ["Pandas", "Data Cleaning"]
wix-url: https://www.datainsightonline.com/post/detect-and-impute-missing-values-in-pandas
---
Hardly you will come across a dataset that is free from missing values. Missing values can be encoded in a number of ways. Sometimes when dealing with numeric data, missing data can be encoded with Numpy's NaN value. There are times when None or an empty string is used in place of a missing value. In this tutorial, we will first take a look at how to detect missing values and then impute them in the Data Frame.

As usual, we will import Numpy and Pandas for this tutorial. Also, we will import statsmodels to be able to load the mtcars dataset. This is the dataset we will use for the tutorial.

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
```

We will save the loaded dataset in Data Frame called df

```python
df = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
```

Let's take a quick look at the Data Frame

```python
df.head()
```

mpg cyl disp hp drat wt qsec vs am gear carb

Mazda RX4 21.0 6 160.0 110 3.9 2.62 16.46 0 1 4 4

Mazda RX4 Wag 21.0 6 160.0 110 3.9 2.875 17.02 0 1 4 4

Datsun 710 22.8 4 108.0 93 3.85 2.32 18.61 1 1 4 1

Hornet 4 Drive 21.4 6 258.0 110 3.08 3.215 19.44 1 0 3 1

Hornet Sportabout 18.7 8 360.0 175 3.15 3.44 17.02 0 0 3 2

Now that the Data Frame is all set, we need to check if it contains missing values.

```python
df.isnull().sum().sum()
```

```python
output: 0
```

This Data Frame does not have missing values. So we will manually modify it to contain some. We will have `NaN` and `''` in some cells and also create a new column that only has values equal to `None`.

```python
df.iloc[0:4, 3:4] = np.NaN
df.iloc[1:5, 1:2] = ''
df['col_none'] = None
```

Let's now have a quick look at the head of the Data Frame.

```python
df.head()
```

mpg cyl disp hp drat wt qsec vs am gear carb col_none

Mazda RX4 21.0 6 160.0 3.9 2.62 16.46 0 1 4 4

Mazda RX4 Wag 21.0 160.0 3.9 2.875 17.02 0 1 4 4

Datsun 710 22.8 108.0 3.85 2.32 18.61 1 1 4 1

Hornet 4 Drive 21.4 258.0 3.08 3.215 19.44 1 0 3 1

Hornet Sportabout 18.7 360.0 175.0 3.15 3.44 17.02 0 0 3 2

Now we see that their are empty strings in some cells, NaN values in some, and a column with only None values
We will again inspect to see how many na values there are in the Data Frame after the modification.

```python
df.isnull().sum().sum()
```

```python
output: 36
```

We now see that the total is 36!

We will now create a boolean Data Frame for null values, null.

```python
null = pd.isnull(df)
```

A quick peek at the new Data Frame will give us an idea about how this looks.

```python
null.head()
```

mpg cyl disp hp drat wt qsec vs am gear carb col_none

Mazda RX4 False False False True False False False False False False False True

Mazda RX4 Wag False False False True False False False False False False False True

Datsun 710 False False False True False False False False False False False True

Hornet 4 Drive False False False True False False False False False False False True

Hornet Sportabout False False False False False False False False False False False True

We see that the cells with True values are the ones with either NaN or None. But The empty strings are marked False. This is because the isnull() doesn't work on empty strings.

Suppose we thoroughly checked our df and came to the conclusion that only '', NaN, and None encode missing values. We can then have these in a list and create a Data Frame for the missing values.

```python
missing_vals = [np.NaN, '', None]
missing = df.isin(missing_vals)
```

Let's take a look at the head of the new Data Frame.

```python
missing.head()
```

mpg cyl disp hp drat wt qsec vs am gear carb col_none

Mazda RX4 False False False True False False False False False False False True

Mazda RX4 Wag False True False True False False False False False False False True

Datsun 710 False True False True False False False False False False False True

Hornet 4 Drive False True False True False False False False False False False True

Hornet Sportabout False True False False False False False False False False False True

To impute missing NaNs and Nones, the fillna() is enough. Lets take a look.

```python
df.fillna(0).head()
```

mpg cyl disp hp drat wt qsec vs am gear carb col_none

Mazda RX4 21.0 6 160.0 0.0 3.9 2.62 16.46 0 1 4 4 0

Mazda RX4 Wag 21.0 160.0 0.0 3.9 2.875 17.02 0 1 4 4 0

Datsun 710 22.8 108.0 0.0 3.85 2.32 18.61 1 1 4 1 0

Hornet 4 Drive 21.4 258.0 0.0 3.08 3.215 19.44 1 0 3 1 0

Hornet Sportabout 18.7 360.0 175.0 3.15 3.44 17.02 0 0 3 2 0

But to impute/fill missing values for all the occurrences of missing values including empty strings, we will use the pandas mask method. Here, we will replace all missing values with the string '90000'

```python
df = df.mask(missing, '90000')
```

Let's now see the head of the Data Frame.

```python
df.head()
```

mpg cyl disp hp drat wt qsec vs am gear carb col_none

Mazda RX4 21.0 6 160.0 90000 3.9 2.62 16.46 0 1 4 4 90000

Mazda RX4 Wag 21.0 90000 160.0 90000 3.9 2.875 17.02 0 1 4 4 90000

Datsun 710 22.8 90000 108.0 90000 3.85 2.32 18.61 1 1 4 1 90000

Hornet 4 Drive 21.4 90000 258.0 90000 3.08 3.215 19.44 1 0 3 1 90000

Hornet Sportabout 18.7 90000 360.0 175.0 3.15 3.44 17.02 0 0 3 2 90000

But to make sure there are no missing values, let's run the cell below to give us the count of missing values.

```python
df.isnull().sum().sum()
```

```python
0
```

Yaay! Mission accomplished!
