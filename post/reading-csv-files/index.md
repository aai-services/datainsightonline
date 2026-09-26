---
title: "Reading CSV Files"
author: "Rohit Roy"
date: 2021-10-06
description: "CSV stands for \"Comma Separated Values\" is a simple file format which is used commonly for data science.Each line is a data record which hold information consists of one or more fields, separated by..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/reading-csv-files
---
CSV stands for "Comma Separated Values" is a simple file format which is used commonly for data science.Each line is a data record which hold information consists of one or more fields, separated by commas.

**How to Read a CSV ?**

There are two ways of reading csv files.

1. Using csv.reader
2. Using Pandas
3. Using readlines()

**Using csv.reader**

1.Import the CSV library

```python
import csv
```

2. " .Open()"

.open() will be use to open the file that is" Data.csv"

```python
file=open("Data.csv")
type(file)
```

3. Use csv.reader to read csv file

```python
csvreader=csv.reader(Data.csv)
```

4. Extract Records

To extract records you need to create a list called rows iterated through csv reader object and append by each row to list.

```python
rows=[]
for row in csvreader:
    rows.append(row)
rows
```

5. Close the file

Using ".close()" you can close the opened file. For file Data as shown below.

```python
Data.close()
```

**Using Pandas**

Pandas is an important library when it comes to data science and used in multiple ways . Here are the steps for using to reading a csv file using pandas.

1. Importing Pandas Library

The first step is to import the library in the code as it is used to work with pandas.

```python
import pandas as pd
```

2. Load CSV files to Pandas using read_csv()

The pandas are used here to reading csv is done with the help of command read_csv used over a file named "Data.csv"

```python
data=pd.read_csv("Data.csv")
```

3. Extract The Fields

.columns is used to extract field names form the file and represent it in the form of headers.

```python
data.coloumns
```

4.Extract Rows

All the rows of data can simply be extracted calling the name of the field

attached to filename.

```python
data.field_name
```

**Using readlines()**

.readlines() is used to return all the lines in a file in a common list.Each item of the list row of csv file.Hence the first roe of the readlines() is the header and rest of them are the records.

```python
with open ('Data.csv) as file:
    content= file.readlines()
```

For more information check out the [link](https://github.com/rohitroycanny/adventures/blob/main/Reading%20CSV%20Explained.md).
