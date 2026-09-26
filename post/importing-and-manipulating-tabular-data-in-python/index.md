---
title: "Importing and manipulating tabular data in python:"
author: "imene.maallem"
date: 2021-12-09
description: "Data science by its name and nature requires us to have access to data. We have learned that images, sounds, files texts, and other pieces of information can be represented as data.Tabular data is..."
categories: ["Python"]
image: images/a8e214_aa9f13348e5d4a1f8b3393ff259622e2.webp
wix-url: https://www.datainsightonline.com/post/importing-and-manipulating-tabular-data-in-python
---
![](images/a8e214_aa9f13348e5d4a1f8b3393ff259622e2.webp)

Data science by its name and nature requires us to have access to data. We have learned that images, sounds, files texts, and other pieces of information can be represented as data.

Tabular data is data in rows and columns, either extracted from an image, a database, or similar structures and represented in an array. An array is a set of values in rows and columns.As in the case of color images, it

The pandas package has much to do with the success of Python as a programing language for Data Science It is an enormous package and is used to importdata,manipulate data,to docalculations with data, and even create graphs and plots using the data

We are going to take a glimpse into the usefulness of the pandas package by importing some data captured in a spreadsheet file and apply some function on it.

We are going to work on a data related to some people categorized by smokers, non smokers and smokers long time ago

**Pakckage used in this tutorial : (pandas):**

It is useful to import all packages from the start :

Import pandas as pd # Package to work with data.

Import numpy as np # numerical analysis package

We can import our data either from a spreadsheet localized in our pc or from a google drive by which we need a special function and this is not required when running python on a local system

From jupyter Notebook we can import drive # connecting to google drive or using pandas ' read_csv() function preeceded with the pandas abbreviation pd :

```python
df= pd.read.read_csv(' smokers and non smokers.csv') # import spreadsheet file
```

We use the "type" function to show that the object assigned to the df computer variable is a Dataframe object

```python
type(df) # Type of the object held in the computer variable df
```

We can look at the attributes and methods of dataframe objects using pythons dir function. Another function called head which returns the first five rows of a dataframe object

```python
df.head()
```

The shape attribute shows the number of rows and columns, returned as tuple. An attribute like shape has no parentheses

```python
df.shape #number of rows (subjects) and columns (statistical variables)
```

The columns property list all the column header names called labels

```python
df.columns  # list statistical variables
```

There is also stype attribute which returns python data type of the values in each of the columns

**b. Extracting rows and columns :**

In order to analyse data, we need to extract certain values and this is a very skillful skills

Pandas refers to a single column in a data frame object as a Series object. We can also create standalone series objects, but in the context of analyzing data, a standalone series object is perhaps not as useful. Below, we extract just the Age column ( statistical variable)and save it as a series object. The notation uses square brackets with the column name represented as a string

```python
Age_column = df['Age'] # Note the use of square brackets
Our new object is a series object
Type (age_column)
```

We can display the first few rows in the series object with the head method

```python
Age_column.head()
```

c. Filtring Data :

Filtring Data is one of the most useful things that we can do with datain a dataframe object.Wewill see how to filter data by extracting numpy array objects based on criteria that we want to investigate by creating brand new dataframes

a. Finding unique vaues in a column : When looking at categorical variable.The unique method is used to find all the sample space elements n a column :

```python
df.smoke.unique() # Data entries encoded 0,1,2
```

The smoke column contain information about the smoking habitsofthe respondants in the data sets ours ample contains 3 integers : 0 for not smoking, 1 for smoking and 2 for previous smoking

Let's say we are interested in creating an array that contain ages of only patients who don’t smoke in the dataframe.To do so, we use indexing directly

```python
Non_smoker_age = df[df.Type == 0] ['Age'].to_numpy()
Non_smoker_age # Print the values to the screen
```

As an alternative, we can use the loc indexing , passing a row and a column specification as arguments.The row interrogates the Smoke column and includes only those with a 0 entry. The column is then specified to the age column .

```python
df.loc[df.Smoke == 0, 'Age']. to_numpy ()
```

The different ways to interact with pandas adds to its power and you can find a way to achieve your data analysis goals that best first your way of work

Since this is now a numpy array object, we can use methods such as the mean method to calculate the average age of all non smoking participants

```python
Non_smoker_age.mean ()
```

Non _smoker ages where survey choice is 3 :

We want to filter by 2 criterias (two columns) , Age and Survey. The filtering can either refer to **and** or **or** . In the first , we require all the criteria t obe met and in the second, only one of the criteria need be met ( return a True value).

The symbol for and is and for or is I. Below we use since we want both criteria to be met. Each filter is created in a set of paranthese.The code uses the row, column notation

```python
Non_smoker_satisfied_age = df.loc[ ( df.Smoke == 0) l (df.sex == F) ,  'Age']. To_numpy()
```

In literature terms: Take the df dataframe object and look down the rows of the smoke and survey columns . Return only the rows where Smoke is 0 And sex is F .Then return the Age column for all these rows fulfilling both criteria.

Never smoked or satisfaction score greater than 3

We are interested in those participants who never smoked Or those that have a satisfaction score of more than 3. Here our filtering criteria requires only one of the two criteria to return True. A clearer way to build these filtering criteria , is tosave them as a computer variable first.

# saving the filtering criteria as a computer variable

```python
Crit = (df.smoke == 0) I (df.sex == F)
```

**d. Sorting:**

Storing can be a useful way to interact with our data.Below, we change the dataframe object bysorting the lastnames alphabetically. All the corresponding column will change as well, so that each row still pertains to the same patient

```python
df.sort_values(by='Last_name')
```

the alphabetical order can be reversed by using ascending=False argument

```python
df.sort( by'Last_name' , ascending=False)
```

We can sort by more than one column at a time. This is done by passing a list of column names.Below,we sort byAge and sBP.With default values, numerical and values will be from smaller to larger values and from earlier to later dates and categorical variables will be alphabetical

```python
e. Missing values :
Then Numpy nan value
```

It is very often that datasets contain missing data.The numpy library has a specific entity called a nan value.This stands for not a number .Below, we see it by itself and also as an element in a Python list.

```python
np.nan
my_list = [1, 2, 3, np.nan]
my_list
```

The list object, my_list, above, cannt be used as argument to functions such as sum, since python does not know how to deal with this missing data.Below , we use the numpy sum function.The results is a nan value

```python
np.sum(my_list)
```

**f. Deleting missing data :**

The first way of dealing with missing data, to simply remove all the rows that contain any missing data.This is done with the .dropna() method.To make the changes permanent, we would have to use the inplace=True argument.Instead of permanent removal, we create a newdataframe object.

Complete_data_df = missing_df.dropna() # Non permanent removal

Complete_dta_df

To find out how many rows contain missing data, we can make use of the fact that True and False are represented by 1 and 0 and can thus be added.The isna method will return Boolen values depending on whether the data is missing

```python
Missing_df.age.isna ()
```

We can sum over these Booelean values using the sum method.Since True values are saved internally to Python as the value 1 ,. The sum will be thenumber of values marked as True when missing, which as we saw, is what isna method returns

**g. Replacing missing values:**

The process of creating values to fill in missing data is called data imputation and is a separate and complicated subject.The pandas library provides a fillna method for fillignin the missing data with simple calculations.Below we use the argument and value method=ffill which simply fill empty values with previous value.There is also a method=bfill argument setting that fills the missing data with the next availabele data down the column.

```python
Missing_df.age.fillna(method='ffill')
```

**h. Default missing data**

It is common to use default values when data is not available at the time of capture.If we know what theses are, we can interpret them as missing data when spreadsheet file is imported

Below, we import a spread sheet file that uses 999, nil and Missing for missing values instead of leaving the cell blank

```python
default_missing_df = pd.read_csv ('DefaultMissingData.csv')
default_missing_df
```

We can replace the missing values or specify allthe words and numbers used for coding missing datawhen we import the data file

Those values are now NAN

```python
Default_missing_df = pd.read_csv('DEfaultMissingData.csv', na_values=(999, 'Nil', 'Missing'])
Default_missing_df
```
