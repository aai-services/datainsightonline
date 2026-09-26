---
title: "PANDAS DATA MANIPULATION TECHNIQUES"
author: "ukaegbu daniel"
date: 2022-06-17
description: "Pandas have unarguably got to be the best thing that has happened to data analysis in python as it makes data manipulation so easy. With pandas, we can iterate over thousands and thousands of rows..."
categories: ["Pandas"]
wix-url: https://www.datainsightonline.com/post/pandas-data-manipulation-techniques
---
Pandas have unarguably got to be the best thing that has happened to data analysis in python as it makes data manipulation so easy. With pandas, we can iterate over thousands and thousands of rows and columns of data with ease. Pandas give us the power to understand and prepare our data for analysis and not only is it highly efficient to use and learn has it has an impressive community of developers and users.

Five important pandas data manipulation techniques that may interest you include:

**Merging Dataframes:** The pandas merge function merge()helps combine rows of the dataset that share the same data. The two key variants of the merge function are the many-to-one merge and the many-to-many merge. In the many-to-one join, one column of the dataset will have many rows in the merged column, while in the many-to-many both merged columns will have repeated values

```python
#First we import the pandas module
import pandas as pd
#because we are using the Google colab code notebook it is important we import our dataset
from google.colab import files
Upload=files.uploaded()
```

```python
df=pd.read_csv('INC 5000 Companies 2019.csv')

df.head()
#for the purpose of this tutorial we are going to create a Dataframe, so that we merge to the old
#using this dataset we are going to create a data frame for the percentage of previous workers
Previous_workers_percentage= df['previous_workers']/100

Previous_workers_percentage.head()
#lets convert it into a Dataframe into the variable C
C=pd.DataFrame(Previous_workers_percentage)
C.head()
#we have converted our data into a Dataframe next is that we merge into our imported Dataframe
df['Previous_workers_percentage']=C
#lets see if our new Dataframe got merged with our odd dataframe
df.head()
```

**Working with Time:** Working with time data can be quite tricky and challenging for data scientists However pandas make it easy to manipulate time data effectively. It is important to know that most time data are presented in a dataset as strings. Therefore it is important to clean them before use by converting them to the python standard datetime object or format before use. This can be done using the PD. to_datetime() function. Using this function use convert a DateTime string into valid dates and times, and extract days, weeks, hours, on the, etc from the dataset. You can even perform advanced DateTime analysis with the panda's module like converting GMT to UTC.

```python
DT_data.head()
#let convert the data time format
DT=pd.to_datetime(DT_data['datetime'])
#we can now convert MIT to a dataframe
DT2=pd.DataFrame(DT)
DT2
```

**Sorting Dataframe with python:** one amazing feature that makes the panda's library highly efficient is its ability to perform categorical sorting on a dataset using the .sort_values() method. It also allows for sorting data based on certain criteria and conditions such as the column of interest or by increasing and decreasing order, this can be done by passing the specific arguments into the sort value function

```python
#we are going to sort our Dataframe using specific criteria.
#we sorted our data based on those industry that are into Advertising and marketing
D=df['city'].unique()
A_and_M=df[df['industry'] == 'Advertising & Marketing']
A_and_M.head()
#we can also sort company based on year founded
Year_founded=df[df['founded'] == 2015]
Year_founded
```

**Loading data in pandas:** pandas no doubt is one of the most versatile data manipulation tools as it allows loading data in various formats such as CSV,hdf5, excel, and even databases, etc. Using the PD.read_csv, PD.read_excel, etc.

```python
#the file imported above is a CSV file we are going to load it using pandas in order to get a Dataframe
df=pd.read_csv('students_adaptability_level_online_education.csv')
#we can see the dataset using the head method
df.head()
#We just uploaded an excel file from the machine into the Google colab environment
df2=pd.read_excel('CAS Chem Name SMILES Data Set CID.5.9.22.xlsx')
df2.head()
```

**Slicing data with pandas:**Pandas also helps data scientist slice data. Data slicing is simply done using the [ ] operator to select a set of rows or columns in a data frame. Slicing has a very simple syntax which is[start:stop ] or [start :steps: stop]. This operator takes 2 or 3 values, the first value tells the operator which row to start and the second tells the operation where to stop slicing. Sometimes there is a value between the first and last values, these steps tell to operator the number 9f steps to take when slicing the data. Data slicing can be done using the iloc[ ] method for numbers and loc[ ] for strings.

```python
#data slicing is an important aspect of data science. It is used to segment a dataset based on the indexed rolls
#we can slice the first 50 rows of our dataset
First_50=df[:50]
First_50
#we can also slice the from 1500th row to 2500th row
Second=df[1500:2500]
Second
#We can also use iloc and loc for data slicing
```
