---
title: "pandas techniques for data manipulation in python"
author: "Nehal Sherif"
date: 2021-11-23
description: "pandas is an open-source python library that implements easy, high-performance data structures and data analysis tools. The name comes from the term ‘panel data’, which relates to multidimensional..."
categories: ["Pandas", "Python"]
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-manipulation-in-python-3
---
pandas is an open-source python library that implements easy, high-performance data structures and data analysis tools. The name comes from the term ‘panel data’, which relates to multidimensional data sets found in statistics and econometrics.

To install pandas, just run pip install pandas inside Python environment. Then we can import pandas as pd.

```python
pip install pandas
```

```python
import pandas as pd
```

pd.read_csv loads this data into a DataFrame. This can be considered as essentially a table or spreadsheet. Once loaded we can take a quick glimpse of the dataset by calling head() on the data frame.

```python
df = pd.read_csv('gapminder_full.csv')
```

```python
df.head()
```

### 1.**Pivot Table**

Pandas can be practised to produce MS Excel style pivot tables. For example, in a table, a key column which has missing values. We can impute it using mean amount of other groups.

```python
df.pivot(index="year",columns="country")
```

2.**Boolean Indexing**

Boolean Indexing is used if user wants to filter the values of a column based on conditions from another set of columns. For instance, we want a list of all students who are not scholars and got a loan. Boolean indexing can support here.

```python
0==False
c=10
(c>1)+(c<20)+(c==12)
#Boolean index can be used as an index for an array or tuple
state=True
state=(True,False)[state]
state
```

### 3.Crosstab

This function is used to get an original view of the data. The function provides scope to validate some fundamental hypothesis. For instance, one column is expected to affect the other column.

```python
pd.crosstab(df.year,df.life_exp)
```

## 4.Merge DataFrames
Merging data frames is vital when a user has data coming from various sources to be related.

```python
mydataset1 = pd.DataFrame({'cars': ["BMW", "Volvo", "Ford"],'passings': [3, 7, 2]})
```

```python
mydataset2 = pd.DataFrame({'cars': ["BMW", "Volvo", "Ford"], "speed": [50, 70, 80]})
```

```python
data=pd.merge(mydataset1,mydataset2)
```

## 5.Sorting DataFrames

When we want to sort Pandas data frame in a particular way. When a user wants to sort pandas data frame based on the values of one or more columns or sort based on the contents of row index or row names of the panda’s data frame. Pandas data frame has two useful functions

1. sort_values(): this command is used to sort pandas data frame by one or more columns
2. sort_index(): this command is used to sort pandas data frame by row index

```python
sort_by_life=df.sort_values('life_exp')
```
