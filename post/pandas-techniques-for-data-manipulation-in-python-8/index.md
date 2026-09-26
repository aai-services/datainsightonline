---
title: "Pandas Techniques for Data Manipulation in Python"
author: "Wilson Waha"
date: 2022-05-13
description: "Pandas is a great library for data Manipulation, it offers many tools to analyse data. Pandas is made up by numpy and matplotlib, so it use the power of numpy to perfom some task on a large scale of..."
categories: ["Pandas", "Python"]
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-manipulation-in-python-8
---
Pandas is a great library for data Manipulation, it offers many tools to analyse data. Pandas is made up by numpy and matplotlib, so it use the power of numpy to perfom some task on a large scale of data.

Pandas use two dimensionnal array call DataFrame. There are many technics that we can use to analyse data using pandas.

1. **Sorting DataFrame:**

Sorting is a great operation, it can be useful on many situation. we can change the order of data.It is useful when we want to extract the most interesting data and to put them at the top of the dataFrame.

l example

using our sale_price dataset, we can sort weekly_sale from the highest to the smallest

```python
#load Dataset
in: df = pd.read_csv('sales_subset.csv')
    df.head()
```

```python
#sorting weekly_sales in descending order to see the department which make the biggest sale
df.sort_values('weekly_sales', ascending=False)
```

The complete notebook is available [**here**](https://github.com/wilson-programmer/DataInsight/blob/main/Sorting_DataFrame.ipynb)

**2. Subsetting**

When we need to get a specific part of a DataFrame, we use subsetting. We can extract a

- specific rows and all columns
- specific column and all rows
- specific row and specific column

Example: here we are using a dataframe of temperatures to subset the country with the highest and the smallest temperature after each four years, from 2000-01-01 to 2013-09-01

```python
# import module
import pandas as pd
import numpy as np

# Load the DataSet
temp = pd.read_csv('temperatures.csv')
```

```python
in: temp1 = temp['date']<= "2004-01-01"
    avg_temp1 = temp[temp1]
```

```python
# Subset the country with the highest and smallest temperature
in: avg_temp1["avg_temp_c"].max()
```

```python
out: 38.283
```

```python
in: avg_temp1[avg_temp1['avg_temp_c']==38.283]
```

The complete notebook is available [**here**](https://github.com/wilson-programmer/DataInsight/blob/main/Subsetting_DataFrame.ipynb)

**3. Grouped summary statistic**

We can apply some statistic operations like mean, median, sum, mode, minimum, maximum, quantile, standard deviation.

Here we have you use grouped summary statistic to see the factors that influences the performances of student.

```python
#load Data
df = pd.read_csv('StudentsPerformance.csv')
df.head()
```

```python
in: df.groupby('parental level of education')['math score'].mean()
```

```python
in: df.groupby('parental level of education')['reading score'].mean()
```

```python
in: df.groupby('parental level of education')['writing score'].mean()
```

## It can therefore be seen that the level of education of the parents influences the performance of the learners.

## The marks of children whose parents have a high level of education are higher than those of others.

The complete notebook is available [**here**](https://github.com/wilson-programmer/DataInsight/blob/main/Grouped_Summary_statistic.ipynb)

**4. Iterating over rows of DataFrame**

Sometime we need to iterate over a DataFrame. There are several method to do it:

- iterrows(): here we use two variable to iterate over rows, the first is get the index and the second produse a pandas Series

e.g:

[#Iterating](https://www.datainsightonline.com/blog/hashtags/Iterating) over each rows using iterrows

for index, row in df.iterrows():

print(index, row['OSName'], row['Type '])

- itertuples(): we only use one variable.

example:

```python
in:		#Iterating over rows using itertuples
		for row in df.itertuples():
    			print(row)
```

```python
out: Pandas(Index=0, OSName='Windows 10 64 bit', PercApr22=73.55, ChangeApr22=-1.14, _4='Windows')
```

we can remove index, and set a custom name for the yielded namedtuples

```python
in: for row in df.itertuples(name='OS'):
    print(row)
```

```python
out: OS(OSName='Windows 10 64 bit', PercApr22=73.55, ChangeApr22=-1.14, _4='Windows')
```

**2. Create pandas DataFrame**

**There are many ways to create a pandas dataFrame**

- **Creating pandas DataFrame from list of list**

example:

```python
list_data = [['Adama',17],['Clinton',12],['Kemogne',15],['John',13],['Ntep',18],['Bodo',14],['Abdou',9]]
data = pd.DataFrame(list_data, columns=['Name','Math score'])
```

- **Creating pandas DataFrame using zip() function**

```python
math_score = [17,12,15,13,18,14,9]
data = pd.DataFrame(zip(name,math_score), columns=['Name','Math score'])
data
```

- **Creating pandas DataFrame from dictionnary of list**

```python
dict_data = {'Name':['Adam',"Clinton","Kemogne","John","Ntep","Bodo","Abdou"], 'Math score':[17,12,15,13,18,14,9]}
data = pd.DataFrame(dict_data)
data
```

- Creating DataFrame from Dicts of series.

```python
data={'Name':pd.Series(['Adam',"Clinton","Kemogne","John","Ntep","Bodo","Abdou"]),
        'Math score':pd.Series([17,12,15,13,18,14,9])}
data = pd.DataFrame(data)
data
```

- Create pandas DataFrame from lists of dictionaries

```python
data = [{'Name':'Adam','Math score':17},{'Name':'Clinton','Math score':12 },{'Name':'Kemogne','Math score': 15},
        {'Name':'John','Math score':13 },{'Name':'Ntep','Math score':18 },
        {'Name':'Bodo','Math score':14 }, {'Name':'Abdou','Math score': 9}]
data = pd.DataFrame(data)
data
```
