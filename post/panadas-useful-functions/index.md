---
title: "Panadas Useful Functions"
author: "Umme Rubaiyat Chowdhury"
date: 2021-11-21
description: "1. Creating a Data Frame A Data Frame is a data collection with two dimensions.It's a data structure that stores data in a tabular format.Datasets are organized in rows and columns, and the data..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/panadas-useful-functions
---
1. **Creating a Data Frame**

A Data Frame is a data collection with two dimensions.

It's a data structure that stores data in a tabular format.

Datasets are organized in rows and columns, and the data frame can hold numerous datasets.

We can add column/row selection and columns/rows in the data frame, among other arithmetic operations.

We can import DataFrames from external storage, which can be described as a SQL Database, a CSV file, or an Excel file.

We can also employ lists, dictionaries, and dictionaries from a list, among other things.

We'll learn how to construct a data frame in Pandas in this blog.

```python
# Create a dataframe from a list of dictionaries
rectangles = [
    { 'height': 40, 'width': 10 },
    { 'height': 20, 'width': 9 },
    { 'height': 3.4, 'width': 4 }
]

rectangles_df = pd.DataFrame(rectangles)
rectangles_df
```

2. **Apply**

Pandas.apply allows users to pass a function and have it applied to each and every value in the Pandas series.

This is a significant improvement for the pandas library since it allows data to be separated according to the aspects required, which is essential in data science and machine learning.

```python
# Use the height and width to calculate the area
def calculate_area(row):
    return row['height'] * row['width']

rectangles_df.apply(calculate_area, axis=1)
```

3. **Read csv**

One of the first things you should do when you start wrangling and cleaning your data is to simply acquire your data.

Your data will most likely come from an external data source, and one of the most popular sources is.csv files (comma separated text files).

As a result, you should be familiar with Pandas' read csv() method and how to use it.

```python
df=pd.read_csv("PoliceKillingsUS.csv")
```

4.**Fillna**

Null values appear as NaN in Data Frame when a csv file contains null values.

fillna() controls NaN values and allows the user to replace them with their own.

```python
#clean the dataset of column 'armed' and replace the No values with 'other'

df['armed'].fillna(value='other', inplace=True)
df.armed
```

5.**sort**

ou may need to arrange the rows based on some criteria when cleaning, inspecting, or analyzing the data.

For example, if you have a dataset with a variety of persons, you could wish to sort the data rows by age.

The sort values() method in Pandas can be used to accomplish this.

This is a regular occurrence in data inspection.

However, it's also widely used in data visualization and analysis.

This is the tool you need if you've ever required to display your data in a certain, sorted order.

```python
#now let us create our own datasets and perform the operations

students = [ ('Jack', 34, 'Sydney') ,

             ('Riti', 31, 'Delhi' ) ,

             ('Aadi', 16, 'New York') ,

             ('Riti', 32, 'Delhi' ) ,

             ('Riti', 33, 'Delhi' ) ,

             ('Riti', 35, 'Mumbai' ),

             ('Ajay', 21, 'Hyderabad')

             ]
```

```python
#create a dataframe object
df3=pd.DataFrame(students,columns=['Name','Marks','City'], index=['b','a','f','e','d','c','g'])
df3
```

```python
#observe the difference between below 3 operations on sort function

#let us perform the sort by index
df3.sort_index()
```

Find out the code at - <https://github.com/ummerubaiyat/data_insight/blob/main/python/Pandas/Functions%20In%20Pandas.ipynb>
