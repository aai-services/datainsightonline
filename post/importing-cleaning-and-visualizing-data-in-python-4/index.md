---
title: "Importing, Cleaning and Visualizing Data in Python"
author: "Prativa Bhatta"
date: 2022-03-25
description: "Examples of the Data Files;Excel file, CSV file, Text file, HDF5 file, MATLAB files, RDBMS, etc.Using these different files you import them differently,One popular option for importing data is to use..."
categories: ["Visualization", "Data Cleaning", "Python"]
wix-url: https://www.datainsightonline.com/post/importing-cleaning-and-visualizing-data-in-python-4
---
***Examples of the Data Files;***

Excel file, CSV file, Text file, HDF5 file, MATLAB files, RDBMS, etc.

Using these different files you import them differently,

One popular option for importing data is to use the **pandas,**

especially for a huge dataset. I have already discussed some pandas functions [here](https://t.co/avhVctqq31)

In that regard, before you can import the dataset, we also need to import pandas

```python
# Importing needed library
```

```python
import pandas as pd
```

Now, we can load the data needed.

Here we will discuss the common and basic data files i.e. Excel file and CSV file.

**Excel File**

Importing an excel file, the common way normally used is **pd.read_excel()**

**pd.read_excel()** : loads an excel file with the extensions; xls, xlsx, etc. into a DataFrame for further analysis using python

**STEPS TO LOAD**

*> Copy the excel file path.*

Suppose this is the file path that includes the file name and the file extension

"C:\Users\HP\Desktop\data analysis sheet.xlsx"

*> Apply the code.*

df = pd.read_excel(r"C:\Users\HP\Desktop\data analysis sheet.xlsx")

```python
df
```

The r before the file path string .... r"c because of the special character \ in the path.

or,

df = df.read_excel("r"C:\Users\HP\Desktop\data analysis sheet.xlsx")

*> Run the codes*

Runthe code by calling if

After this code has run, it loads the excel file into the pandas DataFrame.

```python
 df.head()
```

**CSV file**

Another data file is a CSV file (comma-separated values) which is a delimited text file that uses a comma to separate values.

You can import a csv by calling

pd.read_csv()

pd.read_csv() : This loads a csv file into a DataFrame.

It follows the same steps as loading an excel file but here the file extension differ

Looks like this,

data =pd.read_csv(r"C:\Users\HP\Desktop\data analysis sheet.csv")

data.head()

**Note that with the excel file you use pd.read_excel and with the CSV file you used pd.read_csv**

Now, we know some basics of importing data in Python.

There are other ways you can also import data once that data is not on your laptop like web scraping using HTML, which I am not going to dive deeper into. But we extract from the websites by importing BeautifulSoup and request.

```python
import request
```

```python
from bs4 import BeautifulSoup
```

```python
url = '' example "
```

```python
r = request.get(url)
```

```python
html.doc = r.text
```

```python
Soup = BeautifulSoup(html.doc)
```

```python
Pretty_Soup = Soup.pretty()
```

```python
print(pretty_Soup)
```

Now import some basic files.

**2.** **DATA CLEANING**

What is Data Cleaning?

From [Wikipedia](https://en.wikipedia.org/wiki/Data_cleansing),

**Data cleansing** or **data cleaning** is the process of detecting and correcting (or removing) corrupt or inaccurate records from a recordset, table, or database and refers to identifying incomplete, incorrect, inaccurate, or irrelevant parts of the data and then replacing, modifying, or deleting the dirty or coarse data.

After the data has been imported, you can now explore the data. First and foremost you need to clean the data.

*Why do you need to clean the data?*

You need to clean the data because you can not make meaningful insights from messy and dirty data. As the saying goes - "Garbage In, Garbage Out".

Using messy and dirty data for analysis, predictions, and making inferences will not cause only wrong outcomes but also bad decisions. Hence the need to clean data.

*How to clean the data*

Using a dataset from the Kwame Nkrumah University of Science and Technology. About the less endowed students(High School students in the deprived communities).

You can clean a data by

1. Checking for Missing Values

2. Dropping Irrelevant Features

3. etc.

You need to import the needed libraries;

```python
import pandas as pd
```

```python
import numpy as np
```

Load the necessary dataset. We have already discussed how to;

data =pd.read_csv(r"C:\Users\HP\Desktop\data analysis sheet.csv")

data.head()

Running head() gives the top five from the dataset.

***Checking for Missing Values***

Missing Values are values that were not recorded in a dataset. They can be a single missing value in a cell or missing values in the entire observation (rows or columns).

To know the distinct items within a column per count use value_counts

```python
df['data'].value_counts()
Dropping Missing Values
```

But in an instance where there are missing you can deal with them by dropping the entire row or column.

*Dropping column*

```python
df.drop['example', axis = 1]
```

*Dropping row*

```python
df.drop['example', axis = 0]
```

This drops the entire column or row with the name example. With this approach, you lose some essential information in the data that can be useful.

Hence not a best practice.

**Replacing Missing Values**

On the other hand, you can input values to replace these null values. Replacing helps you to overwrite the data.

Example:

```python
df['example'].replace('x', 'y', inplace = True)
```

With inplace = True, any change is done permanently. To avoid this and have the original dataset, you can assign a variable name

```python
df.['example'] = df.['example'].replace('x', 'y')
```

**Replacing NAN values**

You will use the python code *df.isnull().sum()* to check for the "null" values in the dataset.

From the dataset, we are using;

```python
knust.isnull().sum()

when we have null values and you want fill them
```

```python
df['example'] = df[;example'].fillna(' ')
```

You need not to replace all the null values at once. You can replace them with the mean, median, the highest occurring value, or the lowest occurring value.

**3. Data Visualization**

Clean and well-structured data is ready for analysis. One best way to make meaningful insight from data is to visualize it.

**\*\***Good visualization allows you to communicate your data to other consumers for easy understanding.

Before you Visualize, you need to import the necessary libraries. Commonly used libraries are the matplotlib and seaborn but there are others that you can explore

```python
import matplotlib.pyplot as plt
```

```python
%matplotlib notebook
```

```python
import seaborn as sns
```

**Matplotlib**

This is one popular library in python for plotting. It is low leveled as compared to seaborn. Before you can use it you need to install it i.e.

```python
pip install matplotlib
```

Matplotlib is essentially used for creating basic and popular graphs which include the bar chart, histogram, line chart, and others.

*Bar Chart*; To plot a bar chart, you use

```python
df.plot(kind='bar')
```

```python
plot.bar()
Now you can import, clean and visualize data!!
```
