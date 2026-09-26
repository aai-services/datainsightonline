---
title: "Importing Data in Python"
author: "Tahani Reesh"
date: 2021-12-18
description: "Introduction There are always essential things we do before running any python programs which are extremely simple. And the program starts by getting the data into the Python environment. After..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/importing-data-in-python-6
---
## Introduction

There are always essential things we do before running any python programs which are extremely simple. And the program starts by getting the data into the Python environment. After importing the data we can visualize , wrangle and clean it.

In this blog, you'll learn some important methods to import data into Python. We will start with various files formats, including **.txt** , **.xlsx** and **.csv** files, which are simple formats for data storage.

## CSV Files

The **CSV** format is one of the common data type. Which is comma-separated, indicating where one field ends and the next field starts. First. We need to capture the full path where your **CSV** file is stored. And then import our **CSV** file with the pandas library as we do in the next code.

```python
import pandas as pd
path = "/content/drive/MyDrive/addresses.csv"
df_bonus = pd.read_csv(path)
```

## Text Files
The **text** file is another common data type, which contains textual data. Importing **text** file is so similar to **cvs** where we will also use pandas but with different function. In our example we use a simple text file which contains several sentences.

```python
text_path = "/content/drive/MyDrive/sample3.txt"
text = pd.read_table(text_path)
print(text)
```

## Excel Data
we can import excel file is simple way using pandas and to do that we have to use **ExcelFile** function.

```python
excel_path= "/content/drive/MyDrive/ir211wk12sample.xls"
excel= pd.ExcelFile(excel_path)
print(excel)
```

## URL

The data is often available on a website and can be downloaded into a local device. So we can load the data directly by a website URL into Python.

And to do that, firstly we have to import the **urllib** library for performing this task. Then we save the loaded file in the local python environment using the **urlretrieve** function. Finally we can simply read the file using the **pandas** library as we did in the previous examples.

```python
import urllib
from urllib.request import urlretrieve

url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'

urlretrieve(url, 'airtravel.csv')

df_web = pd.read_csv('airtravel.csv')

print(df_web)
```

## SQL Database

In order to import data SQL, we have to import In order to import data into an[SQLite](https://www.stuartsplace.com/computing/software/databases/sqlite) llibrary. The next step is to establish the connection with the database as we do in our example.

```python
import sqlite3
conn = sqlite3.connect('my_data.db')
c = conn.cursor()
Data = c.execute('''SELECT * FROM username''').fetchall()
print(Data)
```

Finally thank you so much for reading. As always, I welcome feedback. And this is my [GitHub](https://github.com/tahanijaber/Importing-data-in-python) link.
