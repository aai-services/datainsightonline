---
title: "Importing Data in Python"
author: "Arpan Sapkota"
date: 2021-12-08
description: "Doing any data-related operations in Python, such as data cleansing, data aggregation, data transformation, and data visualisation, First we have to load data into Python. Depends on the types of..."
categories: ["Python"]
image: images/a8b2bc_7f91cc56fb054981a60fb2b888e7d07f.webp
wix-url: https://www.datainsightonline.com/post/importing-data-in-python-2
---
![](images/a8b2bc_7f91cc56fb054981a60fb2b888e7d07f.webp)

Doing any data-related operations in Python, such as data cleansing, data aggregation, data transformation, and data visualisation, First we have to load data into Python. Depends on the types of data files (e.g. .csv, .txt, .tsv, .html, .json, Excel spreadsheets, relational databases etc.) and their size, different methods should be applied to deal with this initial operation accordingly. Some common methods for importing data in Python are discussed here.

1. Python build-in functions (read(), readline(), and readlines())

In general, a text file (.txt) is the most common file we will deal with. Text files are structured as a sequence of lines, where each line includes a sequence of characters. Let’s assume we need to import in Python the following text file (sample.txt).

To import its content to Python, we need to first open it. This step is just like double-clicking a file to open it in our computer system. However, in Python, this is done by calling the open() built-in function. open() has a required argument that is the path to the file and an optional argument to indicate the mode (i.e. default argument ‘r’: open for reading; ‘w’: open for writing). With those set, open() then returns us a file object.

There are three methods to read content (i.e. read(), readline(), and readlines()) that can be called on this file object either by one or in combination.

- read(size=-1): this reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
- readline(size=-1): this reads the entire line if no arguments are passed or None or -1 is passed. Or if passed with size, this reads the size number of characters from the line. Moreover, multiple readline() functions can be called sequentially, in which the next readline() function will continue from the end position of last readline() function. Note that output of the third readline() appends an extra newline character(\n, displayed as a new line). This can be avoided by using print(reader.readline(5), end=’’).
- readlines(): this reads all the lines or remaining lines from the file object and returns them as a list

```python
file = open("sample.txt")
data = file.read()
print(data)
file.close()
```

As it is very easy to forget to close the file, we should always use with statement. This also provides better syntax and exceptions handling.

2. Python csv library

The sample.txt we just processed had only one field per line, which make it handy to process using just build-in function (read(), readline(), and readlines()). However, more frequently we will work with a file that has multiple fields on each line (aka tabular data)

As we can see that every field on each line is comma-separated, indicating where one field ends and the next field starts. We call this type of file the delimited file. These files are often either comma-separated (.csv)or tab-separated (.tsv or .txt). In rare cases, you may also encounter other delimiters like colon (:), semi-colon (;), and characters.
Even though the build-in function can still process these files, it is highly likely to mess up, especially when there are hundreds of fileds per line in some cases. Alternatively, we can use Python’s csv library designed to read delimited files. Here let’s learn two common functions from this module.

- csv.reader(): this reads all lines in the given file and returns a reader object. Then each line can be returned as a list of strings.

- csv.DictReader(): if the file has headers (normally the first row that identifies each filed of data), this function reads each line as a dict with the headers as keys. We then can access data of each column by calling its fieldname

```python
import csv
with open("Sample.csv",'r') as samfile:
    rows=csv.reader(samfile,delimiter=',')
    for r in rows:
        print(r)
```

3. Import data using Pandas

Another very popular option in importing data in Python must go to Pandas, especially when the data size is big (like several hundred MBs). We won’t delve into the specifics of how pandas works or how to use it. There are many excellent tutorials and books (e.g. Python for Data Analysis, by Wes McKinney, creator of pandas). Here we just show some of the power of pandas in reading csv and excel files.

- pd.read_csv(): this reads a csv file into DataFrame object. An important point here is that pandas is smart enough to automatically tell the header row and data type of each field, which make the downstream analyse more efficient.

- pd.read_excel(): this reads an excel file (.xls, .xlsx, .xlsm, .xlsb, and .odf file extensions) into a pandas DataFrame. By default, it only import the first data sheet within the excel file (sample.xlsx has multiple sheets)

To be able to access a specific sheet within the excel file, we can first import the whole excel file using pd.ExcelFile() and then specify the sheet name when calling pd.read_excel()
Moreover, to be handier in accessing all sheets, instead of calling pd.read_excel() multiple times, we can store all sheets as dataframe objects inside a dict.

```python
import pandas as pd
df = pd.ExcelFile('Sample.xlsx')
print(df)
```
