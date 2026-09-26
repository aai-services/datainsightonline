---
title: "Data Manipulation in Pandas."
author: "Vanessa Arhin"
date: 2021-11-20
description: "Pandas is an open-source python library used for data analysis and manipulation. With pandas, one can get lots of information from a dataset and also make adjustments to a dataset. In this article..."
categories: ["Pandas"]
image: images/e26853_a220ca4ac60147178309afc9db51e55f.webp
wix-url: https://www.datainsightonline.com/post/data-manipulation-in-pandas
---
![](images/e26853_a220ca4ac60147178309afc9db51e55f.webp)

Pandas is an open-source python library used for data analysis and manipulation. With pandas, one can get lots of information from a dataset and also make adjustments to a dataset. In this article, we will learn about some techniques used in pandas used for data manipulations.

#### Sorting DataFrames.
Sorting a DataFrame helps you put various parts of your data into various sections you want. The two major sort functions in pandas are:

- **Sort_values()**: It is used to sort columns of a DataFrame in an ascending or descending order. To sort a particular column in DataFrame, you will have to pass the name(s) of the column(s) to the function.

```python
#sorting one column
df.sort_values('age')

#sorting two or more columns
df.sort_values(['age', 'weight'])
```

Inside of the sort_value() function, you can add parameters to make your data look the way you want. For instance, the order in which you want your data, either ascending or descending.

```python
#sorting in ascending order
df.sort_values('age', ascending = True)

#sorting in descending order
df.sort_values('age', ascending = False)
```

- **Sort_index()**: This method is used to sort a DataFrame by index.

df.sort_index()

You can also sort by order or sort by axis.

```python
#.SORT_INDEX()
df.sort_index()

#sort along row
df.sort_index(axis=0)

#sort along column
df.sort_index(axis=1)

#sort in ascending order
df.sort_index(ascending=True)

#sort in descending order
df.sort_index(ascending=False)
```

#### Merging DataFrames.
The merge() method in pandas is used to merge two DataFrames. This is normally done if the two DataFrames have one or more columns in common. Before merging two DataFrame, you should check if they have any columns in common. Here are some parameters used in the merge method:

**on**: column(s) to join in the two DataFrames. Column(s) must be

found in both DataFrames.

**how**: specifies which keys are to be included in the results. The

default setting is 'inner', but you can set it to 'outer', 'left' or 'right'.

```python
pd.merge(dataframe_1, dataframe_2, on='column_name', how='inner')
```

#### Viewing a DataFrame.
It is important to know what a DataFrame looks like and what it entails before you start working with it. There are some functions to help you with that and they are **.head()**, **.tail()**, **.shape**, and **.info()**.

- **.head():** It is used to view the first few rows of a DataFrame. The

default number of rows is five, but you can change the number of

rows to view to a number of your choice by setting the parameter n

to a number(integer).

```python
#first few rows
df.head()

#viewing a number of rows(from the top)
df.head(7)
```

- **.tail():** It is used to view the last few rows of a DataFrame.The

default number of rows is five, but you can change the number of

rows to view to a number of your choice by setting the parameter n

to a number(integer).

```python
#last few rows
df.tail()

#viewing a number of rows(from the bottom)
df.tail(4)
```

- **.shape**: It returns the number of rows and columns in a

DataFrame. These values are returned as a tuple, that is

(number_of_rows, number_of_columns). You can also check only

the number of rows or columns, by setting the index to 0 for rows

and 1 for columns.

```python
#shape of a DataFrame
df.shape
#number of rows
df.shape[0]
#number of columns
df.shape[1]
```

- **.info()**: It returns information or summary about the DataFrame.

Examples of information returned include index type, columns,

non-null values and memory usage.

```python
df.info()
```

#### Selecting Rows and Columns in a DataFrame.
Whiles working with a DataFrame you might need to select some specific data within the DataFrame, to do so you will need to know the location of that specific data. Pandas uses **.iloc**, **.loc** and **.ix** for data selections.

- **.iloc**: Used to select or get data in a specified position using the

index, specifying two arguments to iloc that is row selection and

column selection. ( df.iloc[row_selection,column_selection] )

```python
df.iloc[2,3]
```

- **.loc**: Used to select data by specifying the row and/or column label

(name)

```python
df.loc['row_name', 'column_name']
```

- **.ix**: It uses both .loc and .iloc interchangeably, which is both label

index selection.

```python
#using index
df.ix[1,4]

#using label
df.ix['row','column']

#using both index and label
df.ix[3, 'column']
```

#### Summary Statistics.
Working DataFrames in python might require you to some statistical information about your DataFrame. There are lots of statistical methods in pandas module to help you get the information you need. Some of these statistical functions are **.mean()**, **.mode()**, **.median()**, **.min()**, **.max()**, **.std() and .var()**

```python
#calculates the mean
df.mean()

#find the median
df.median()

#find the mode
df.mode()

#find minimum value
df.min()

#find maximum value
df.max()

#calculate the standard deviation
df.std()

#calcuate the variance
df.var()
```
