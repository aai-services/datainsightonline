---
title: "HOW TO IMPORT DATA IN PYTHON"
author: "Nehal Sherif"
date: 2021-12-11
description: "This tutorial explains various methods to read data in Python. Data can be in any of the popular formats - CSV, TXT, XLS/XLSX (Excel)Loading data in python environment is the most initial step of..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/how-to-import-data-in-python
---
This tutorial explains various methods to read data in Python. Data can be in any of the popular formats - CSV, TXT, XLS/XLSX (Excel)

Loading data in python environment is the most initial step of analyzing data.

**Install and Load pandas Package**

**pandas** is a powerful data analysis package. It makes data exploration and manipulation easy. It has several functions to read data from various sources.

If you are using **Anaconda**, pandas must be already installed. You need to load the package by using the following command

```python
import pandas as pd
```

If pandas package is not installed, you can install it by running the following code in **Ipython Console.** If you are using **Spyder,** you can submit the following code in Ipython console within Spyder.

```python
!pip install pandas
```

If you are using **Anaconda**, you can try the following line of code to install pandas

```python
!conda install pandas
```

## 1. Import CSV files

It is important to note that **a singlebackslash does not work** when specifying the file path**.** You need to either **change it to forward slash or add one more backslash** like below

import pandas as pd

```python
import pandas as pd
mydata= pd.read_csv("C:\\Users\\Deepanshu\\Documents\\Salary_Data.csv")
```

## 2. Import File from URL

You don't need to perform additional steps to fetch data from URL. Simply put **URL** in read_csv() function (applicable only for CSV files stored in URL).

```python
mydata = pd.read_csv("http://winterolympicsmedals.com/medals.csv")
```

## 3. Read Text File

We can use read_table() function to pull data from text file. We can also use read_csv() with sep= "\t" to read data from tab-separated file.

```python
mydata = pd.read_table("C:\\Users\\Deepanshu\\Desktop\\example2.txt")
mydata = pd.read_csv("C:\\Users\\Deepanshu\\Desktop\\example2.txt", sep ="\t")
```

## 4. Read Excel File

The read_excel() function can be used to import excel data into Python.

```python
mydata = pd.read_excel("https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls",sheetname="Data 1", skiprows=2)
```
