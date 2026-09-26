---
title: "Importing Data in Python."
author: "Vanessa Arhin"
date: 2022-02-20
description: "What is Data Importation in Python? Importing data in python is the use of various modules in python to transform different types of file formats into a python readability and interpretation format..."
categories: ["Python"]
image: images/e26853_1490c0f1ea7748d9bb87b12f5ea52bd1.webp
wix-url: https://www.datainsightonline.com/post/importing-data-in-python-7
---
![](images/e26853_1490c0f1ea7748d9bb87b12f5ea52bd1.webp)

##### What is Data Importation in Python?

Importing data in python is the use of various modules in python to transform different types of file formats into a python readability and interpretation format.

Before you start working with a set of data in python, you'll need to import it first. These data may be in different file formats which means each format's importation may differ from the other. In this article, you will learn about how to import:

- Flat files (eg. text file, excel files and csv files)

- Web files

- SQL Database

##### Importing Flat Files.

Text files - To import a text file into python, you will have first have to import the pandas library(as its alias). This will give you access to use all related functions in the library. Importing a text file using pandas will read the file into a DataFrame object.

```python
import pandas as pd
pd.read_table("filelocation/filename.txt")
```

Excel files - Importing an excel file will require you to import python's pandas library. This will give you access to use all related functions in the library. Note that excel files have various file extensions.

```python
import pandas as pd
pd.read_excel("filename.xlsx")
```

CSV files - To import a comma-separated file into python, you will have first have to import the pandas library(as its alias). This will give you access to use all related functions in the library. Importing a CSV file using pandas will read the file into a DataFrame object. Note that the file extension should be **.csv**

```python
import pandas as pd
pd.read_csv("filename.csv")
```

**Importing Web files.**

Getting data from a website is mainly done using the python library **requests**, **urllib**, and **urlretrieve**.

```python
import requests as req
url = "url.of.website"
req.get(url, allow_redirects = True)
```

**Importing SQL Database.**

The required python package to import from SQL Database is pyodbc. Once you import the module, you will need to establish a connection with the database to be able to import or extract the data you need.

```python
import pyodbc
sql_connection = pyodbc.connect("sqlserverpathway")
pd.read_sql_query('type your sql query here', sql_connection)
```
