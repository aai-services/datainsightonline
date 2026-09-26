---
title: "IMPORTING, CLEANING AND VISUALIZING DATA"
author: "ukaegbu daniel"
date: 2022-06-16
description: "Importing, cleaning, and visualizing data are important aspects of a data science project workflow as they determine the outcome of the data science tool or project that has been carried out. Hence..."
categories: ["Visualization", "Data Cleaning"]
wix-url: https://www.datainsightonline.com/post/importing-cleaning-and-visualizing-data
---
Importing, cleaning, and visualizing data are important aspects of a data science project workflow as they determine the outcome of the data science tool or project that has been carried out. Hence every data science project meticulously undergo these three process as a form of quality assurance.

One mistake in one of these concepts can affect the others leading to a huge problem. Therefore crucial steps are taken to ensure that a set of data is correctly imported, cleaned with extreme precision, and then visualized to tell good stories.

**Importing Data in python**

Working with data is a very important task and python has just the right tools and modules to help us do that. Python is a powerful programming language to work with datasets as it helps us import external datasets in various formats such as CSV, excel, hdf5, SAS, and even databases, etc. Although python has a very efficient module called open() that allows us to work with files, python's data science module pandas an even more powerful library for working with datasets as it efficiently helps us import and manipulation data in various formats. This can be done by simply importing pandas and importing the dataset using the specific panda's importation functions eg pf.read_csv('file'), pd.read_excel('file'). Below is a code example to help you understand better.

```python
#first we import pandas
import pandas as pd
#Since we are working with Google colab and not Jupiter notebook we need to import our dataset from our machine or computer into colab
from google.colab import files
#the file imported above is a CSV file we are going to load it using pandas in order to get a Dataframe
df=pd.read_csv('students_adaptability_level_online_education.csv')
#we can see the dataset using the head method
df.head()
#We just uploaded an excel file from the machine into the Google collab environment
df2=pd.read_excel('CAS Chem Name SMILES Data Set CID.5.9.22.xlsx')
df2.head()
```

**Cleaning data in python**

Data cleaning is a very important part of a data science project workflow and also an important skill every data scientist should have. Not only does it aid data visualization it helps fit data in a machine learning and statistical model. Data cleaning involves the process of observing and correcting dirty or inaccurate datasets. It usually entails modifying, changing, and sometimes entirely deleting dirty data. Some major data issues in data science include:

Missing data

Redundant and unnecessary data

Irregular and inconsistent data etc.

Some pythonic data cleaning techniques used in data science include:

Handling missing data: missing data is a common problem in data science as most models cannot handle it. This problem can be detected using the ISNA()function or it can be visualized using the menu python module which enables users to have a better understanding of the extent to which data is missing from the dataset. some ways missing data can be addressed are:

Dropping the missing data. This can be done using the drop() function

Replace or inputs missing data: Replacing missing data is common and good practice in data science, especially when dealing with numerical data. This is usually done by replacing the mean data or values with statistical measures related to the data such as(Mean, median, and mode). it is done using the Fill()method.

Dropping duplicate: Duplicate data is a major problem in data analysis. This can easily be addressed by dropping this duplicate data using the dropna() pandas method. Using the kaggle titanic challenge dataset we are going to illustrate some simple data cleaning using python

```python
#using kaggles titanic data set we are doing some column that will not be necessary
df = df.drop(['ticket','cabin'], axis=1)
#we can also NAN rows in the data set using the dropna() method
df = df.dropna()
#We can specifically clean a specific column and will empty rows with a values just like we did below
data.drop('PassengerId', axis=1, inplace=True)
survived = data['Survived'].dropn()
data['Survived'].fillna(-1, inplace=True)
```

**Visualizing Data in python**

Data is essential for telling stories and giving insight into anything at all through visualization. These visualizations help data scientist and njn data scientist understand correlations, trends, and charts to communicate risk which aid in making the right decision.

Python has some amazing modules used for effective data visualization. Matplotlib and seaborne are some of python's most prominent visualization libraries. Matplotlib allows for visualization using scatter plots, graphs, line plots, histograms, bar charts, etc. The seaborne library is built on the matplotlib library. However, seaborne gives more options and flexibility as it allows us to perform discreet statistical visualization on a dataset. Both matplotlib band seaborne are exceptional visualization libraries as they also allow the customization of our plots and charts.

Below is a code tutorial on data visualization using both matplotlib and seaborn.

```python
#first import matplotlib
import matplotlib.pyplot as plt
#we are going to Visualize the age distribution that exists in our student adaptability dataset using histogram.
#First we isolate the column in a Dataframe called age
Age=df['Age']

Age.head()
#using the mat matplotlib module we are going to create a histogram that helps understand the age distribution in the dataset.
plt.hist(Age)
plt.show()
```
