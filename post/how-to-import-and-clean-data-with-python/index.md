---
title: "How to import and Clean Data with Python"
author: "Fatma Ali"
date: 2021-12-08
description: "Importing DataLoading and Saving CSVs:When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv():df= pd.read_csv('IMDB_Movies.csv') dfCleaning DataDiagnose the Data:We..."
categories: ["Data Cleaning", "Python"]
image: images/f5d020_9f098edefbde4a5598564e89a7f7e901.webp
wix-url: https://www.datainsightonline.com/post/how-to-import-and-clean-data-with-python
---
![](images/f5d020_9f098edefbde4a5598564e89a7f7e901.webp)

**Importing Data**

**Loading and Saving CSVs:**

When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv():

```python
df= pd.read_csv('IMDB_Movies.csv')
df
```

**Cleaning Data**

**Diagnose the Data:**

We often describe data that is easy to analyze and visualize as “tidy data”. What does it mean to have tidy data? For data to be tidy, it must have:

- Each variable as a separate column
- Each row as a separate observation

**df.info()** gives some statistics for each column.

```python
df.info()
```

**Dealing with Duplicates:**

Often we see duplicated rows of data in the DataFrames we are working with. This could happen due to errors in data collection or in saving and loading the data. To check for duplicates, we can use the pandas function .duplicated(), which will return a Series telling us which rows are duplicate rows.

```python
df.duplicated()
```

We can use the pandas .drop_duplicates() function to remove all rows that are duplicates of another row.

```python
df.drop_duplicates(subset=['director_name'])
df
```

**Missing Values:**

We often have data with missing elements, as a result of a problem with the data collection process or errors in the way the data was stored. The missing elements normally show up as NaN (or Not a Number) values.

```python
df.isnull().sum()
```

If we wanted to remove every row with a NaN value in the *director_name* column only, we could specify a subset:

```python
df = df.dropna(subset=['director_name'])
df
```

**Looking at Types:**

Each column of a DataFrame can hold items of the same *data type* or *dtype*. The dtypes that pandas uses are: float, int, bool, datetime, timedelta, category and object. Often, we want to convert between types so that we can do better analysis.

To see the types of each column of a DataFrame, we can use:

```python
print(df.dtypes)
```

You can check the full code [here](https://github.com/fatmtly892/Importing-and-Cleaning-Data)
