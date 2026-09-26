---
title: "Most Effective Pandas Techniques In Python For Data Manipulation"
author: "Mahmoud Morsy"
date: 2021-11-21
description: "Python is the most preferred language for data scientists. It provides the greater ecosystem of a programming language and the insight of good scientific computation libraries.Pandas is an..."
categories: ["Pandas", "Python"]
image: images/0cda06_3db62628d7f4479e877a606407dc4e60.webp
wix-url: https://www.datainsightonline.com/post/most-effective-pandas-techniques-in-python-for-data-manipulation
---
**Python** is the most preferred language for data scientists. It provides the greater ecosystem of a programming language and the insight of good scientific computation libraries.

**Pandas** is an open-source python library that implements accessible, high-performance data structures and data analysis tools. The name comes from the term ‘panel data’, which relates to multidimensional data sets found in statistics and econometrics.

![](images/0cda06_3db62628d7f4479e877a606407dc4e60.webp)

**Install Pandas:**

To install pandas, just run pip install pandas inside the Python environment.

```python
pip install pandas
```

Then we can import pandas as pd.

```python
import pandas as pd
```

**Pandas DataFrame creation:**

The fundamental Pandas object is called a DataFrame. It is a 2-dimensional size-mutable, potentially heterogeneous, tabular data structure.

A DataFrame can be created in multiple ways. It can be made by passing in a dictionary or a list of lists to the pd.DataFrame() method, or by reading data from a CSV file.

```python
# Ways of creating a Pandas DataFrame
# Passing in a dictionary:
data = {'name':['Anthony', 'Maria'], 'age':[30, 28]}
df = pd.DataFrame(data)

# Passing in a list of lists:
data = [['Tom', 20], ['Jack', 30], ['Meera', 25]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])

# Reading data from a csv file:
df = pd.read_csv('students.csv')
```

**Selecting Pandas DataFrame rows using logical operators:**

In pandas, specific rows can be selected if they satisfy certain conditions using Python’s logical operators. The result is a DataFrame that is a subset of the original DataFrame.

Multiple logical conditions can be combined with OR (using |) and AND (using &), and each condition must be enclosed in parentheses.

```python
# Selecting rows where age is over 20
df[df.age>20]

# Selecting rows where name is not John
df[df.name!= "John"]

# Selecting rows where age is less than 10
# OR greater than 70
df[(df.age<10) | (df.age>70)]
```

**Pandas apply() function:**

The Pandas apply() function can apply a function on every value in a column or row of a DataFrame, and transform that column or row to the resulting values.
By default, it will apply a function to all values of a column. To perform it on a row instead, you can specify the argument axis=1 in the apply() function call.

```python
# This function doubles the input value
def double(x):
return2*x

# Apply this function to double every value in a specified column
df.column1 = df.column1.apply(double)

# Lambda functions can also be supplied to `apply()`
df.column2 = df.column2.apply(lambdax : 3*x)

# Applying to a row requires it to be called on the entire DataFrame
df['newColumn'] = df.apply(lambdarow:
row['column1'] * 1.5 + row['column2'],
axis=1
)
```

**Pandas DataFrames adding columns:**

Pandas DataFrames allow for adding columns after the DataFrame has already been created, by using the format df['newColumn'] and setting it equal to the new column’s value.

```python
# Specifying each value in the new column:
df['newColumn'] = [1, 2, 3, 4]

# Setting each row in the new column to the same value:
df['newColumn'] = 1

# Creating a new column by doing a
# calculation on an existing column:
df['newColumn'] = df['oldColumn'] * 5
```

**String Operations in Pandas:**

Often, we’ll need to manipulate string data that are formatted incorrectly. Pandas provide vectorized string operations. For most string operations, you’ll need to be familiar with [regular expressions](https://docs.python.org/3/library/re.html#module-re). Let’s perform an example extract operation by smushing some of our existing data together.

```python
companies_smushed = pd.DataFrame()
companies_smushed['sector_employees'] = companies['sector']+ \companies['employees'].astype(str)

print(companies[['sector','employees']].head())
print(companies_smushed.head())

companies_smushed=companies_smushed['sector_employees'].str.extract(r'(\D+)(\d+)')companies_smushed.head()
```

**Transformation:**

Transformation returns manipulated data in the same size as the passed data. There are many methods and functions at your disposal to transform data, as shown below. In the below example, we pass a defined function find_percent and return the transformed series.

```python
def find_percent(column):
   return column / float(column.sum())
companies.groupby('sector').agg({'employees':'sum'}).transform(find_percent)
```

**Filtration:**

Filter returns a subset of the original data. It works similar to boolean indexing except instead of working on individual rows and individual groups. The filter must return a True or False value for the group as a whole. The services sector is the only sector that has more than 1,000,000 employees.

```python
companies.groupby('sector').filter(lambdax:x['employees'].sum()>1000000)[['name','employees']]
```

**Pivot Tables:**

We can produce the same data in a different format by using pandas.pivot_table.

```python
companies.pivot_table(columns='sector', values='employees', aggfunc='sum')
```
