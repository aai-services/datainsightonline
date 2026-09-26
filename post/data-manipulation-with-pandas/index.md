---
title: "Introduction to Data Manipulation with pandas"
author: "cathbert busiku"
date: 2021-12-27
description: "you will what the introduction to pandas, how create a DataFrame in pandas and maipulating a pandas DataFrame."
categories: ["Pandas"]
image: images/b895e3_7e45b4d012084b2a94836ff7bdcf0472.webp
wix-url: https://www.datainsightonline.com/post/data-manipulation-with-pandas
---
pandas is a Python package that can be used for manipulation and visualization. pandas is built on top of two essential Python packages, NumPy and Matplotlib. Numpy provides multidimensional array objects for easy data manipulation that pandas uses to store data, and Matplotlib has powerful data visualization capabilities that pandas takes advantage of. Now we are going to dive to explore tools found in pandas.

**1. Introduction to pandas DataFrames:**

In pandas, rectangular data is represented as a DataFrame object. DataFrames can be created from dictionaries or reading from a CSVs file. In python we have to install the pandas package using pip install pandas. Before we can use the pandas package we have to import in our python script for example, import pandas as pd.

a. Creating a DataFrame from dictionaries:

To construct a DataFrame from dictionaries we can use a either a list of dictionaries or dictionaries of list. To create a DataFrame using a list of dictionaries create a list containing one dictionary per row. Each dictionary key is a column name, and each value is the row’s value in that column. Then pass the list to pd.DataFrame(). For example,

List_of_dicts = [

{ “id”:1, “name”: “Mike Banda” , “gender”: “Male”},

{ “id”:2, “name”: “Jennifer Moono” , “gender”: “Female”} ]

names = pd.DataFrame(List_of_dicts)

Print(names)

![](images/b895e3_e9907af7d68947acb79b1d1d9978b34b.webp)

Another way is to build a DataFrame by column, create a dictionary containing a key for each column name. The values for these keys will be a list of row values for that column. Then, pass the dictionary to pd.DataFrame().

Dict_of_lists = { ‘id’ : [1,2],

‘name’:[‘ Mike Banda’, ‘Jennifer Moono’],

‘gender’: [‘Male’,’Female’] }

Name = pd.DataFrame(Dict_of_lists)

**2. Exploring Data Frames**

The good thing about pandas is that it provides methods that aloe you to explore DataFrames without having to view every row and column.

Lets consider the names DataFrame we formed earlier. We use .head() to display the first few observations.

print( names.head() )

![](images/b895e3_ae985a9687a34161bb0ff20e2e703e56.webp)

.info() displays the name, data type, and number of missing values for each column. for example calling [name.info()](http://name.info) produces the following output.

print( [name.info()](http://name.info) )

<class 'pandas.core.frame.DataFrame'>

RangeIndex: 2 entries, 0 to 1

Data columns (total 3 columns):

# Column Non-Null Count Dtype

--- ------ -------------- -----

0 id 2 non-null int64

1 name 2 non-null object

2 gender 2 non-null object

dtypes: int64(1), object(2)

memory usage: 176.0+ bytes

The .shape attribute return a tuple of the number of rows followed by the number of rows followed by the number of columns. Since .shape is an attribute and not a method, it does not require parentheses.

print( names.shape )

(2, 3)

The .describe() method returns summary statistics for numeric columns, including the mean and the median values. Count is the number of non-missing values in the column. calling the describe method produces the following.

print( names.describe() )

![](images/b895e3_1a9d9b2d3f544da9ae55ab19f3a985c5.webp)

**3. Sorting DataFrames on a single and multiple column**

Sorting DataFrame rows can improve the readability of your DataFrame. You can do this with the .sort_values() method, passing the column name to sort by as an argument.

print( names.sort_values(‘name’) )

![](images/b895e3_816463c467134cdb96ee7fe8436a6967.webp)

.sort_values() sorts in ascending order by default. To sort in descending order, set ascending = FALSE.

**4. Subsetting DataFrame columns**

To select a subset of DataFrame columns, follow the DataFrame name with square brackets containing the names of the columns. For example, below to subset gender.

print( names[‘gender’] )

![](images/b895e3_f51dd34f1b9542db8282d9a724377730.webp)

To subset multiple columns, pass a list of column names to the square brackets. For example, to subset id and gender from our names DataFrames.

print( names.[[ ‘id’ , ‘gender’ ]] )

![](images/b895e3_5222b6baed944dbbb03a771a4f63093f.webp)

**5. Adding a new DataFrame column**

To add DataFrame columns derived from existing columns, follow the DataFrame name with square brackets containing the new column name. For example to add age to our names dataframe.

names['age'] = [18,22,10,31]

print(names)

![](images/b895e3_fc19069931b14f28b6e82210b760a28b.webp)

**1. Summarizing numerical data**

Summary statistics are numbers that tell you more about your datasets. Pandas provides DataFrame methods to compute these numbers.

The **mean** is an indication of where the center of data is. To compute the mean of a DataFrame column, subset the column and follow it with .mean() method. For the mean for our names DataFrame can be calculated as follows.

print( names['age'].mean() )

20.25

Other summary statistics include:

.median() , .mode(), .min() , .max(), .var() , .std(), .sum(), .quantile()

These statistics can be used in the same way we used the mean in the previous example.

The Pandas package has a lot of tools that can be used to manipulate data and these mentioned here are just some of the manipulation we can do on DataFrame. There is a lot to learn in pandas.

Happy Hacking.
