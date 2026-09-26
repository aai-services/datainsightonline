---
title: "Data Importing in Python"
author: "mairajsaleem92"
date: 2021-12-10
description: "Introduction:Before doing any data cleaning, wrangling and visualizing, we need to know how to get data into Python. Data is available in many formats as used in many industries like in .csv, .txt..."
categories: ["Python"]
image: images/b581a2_362c6b6400e34f68be54a1e8fc210933.webp
wix-url: https://www.datainsightonline.com/post/data-importing-in-python
---
![](images/b581a2_362c6b6400e34f68be54a1e8fc210933.webp)

**Introduction:**

Before doing any data cleaning, wrangling and visualizing, we need to know how to get data into Python. Data is available in many formats as used in many industries like in .csv, .txt, .mat many more. In this blog, we learn how to import data in Python from various formats of files.

**From flat file:**

Flat files are usually considered plain text files in which fields can be separated by a delimiter such as commas or tab characters. Generally, flat-file load in two formats of the file is .txt and .csv. Let's discuss it one by one.

**a) .txt files:**

The .txt file is known as a text file. We import this file in many ways. In the first method, we import with the open() method, first open the file and apply mode to 'r' which is for reading then used file.read() method to read the file after reading we close the file with file.close(). Code is shown below:

```python
# first import the necessary libraries
import numpy as np
import pandas as pd
```

```python
filename = r'C:\Users\Mairaj-PC\Downloads\text.txt'
file = open(filename, mode = 'r')
text = file.read()
file.close()
print(text)
```

Output is :

```python
The 5-Second Rule (2017) is a top-notch guide on overcoming self-doubt and living a more fulfilled life. It
gives you a simple strategy that counteracts most of your brain's psychological defenses against action,
allowing you to delay less, live happier, and achieve your goals.
Mel Robbins, the author, is a motivational speaker and television broadcaster from the United States. She offers a straightforward and efficient one-size-fits-all answer to the problem of holding yourself back. You'll discover that the key isn't knowing what to do, but rather how to force oneself to do it.
```

We also import line by line text with a .txt file. For this, we use with command and file.readline() to read a single line of text.

```python
# import the text file by using 'with' command
with open (filename, 'r') as file:
    print(file.readline())
```

Output is:

```python
The 5-Second Rule (2017) is a top-notch guide on overcoming self-doubt and living a more fulfilled life. It
```

Another way to import text files is by using the NumPy library. With the use of np.loadtxt() command, we easily import the text file as separated by any delimiter. Let's check this example to understand the coding of this command.

```python
new_file = r'C:\Users\Mairaj-PC\Downloads\np_del_data.txt'
np_data = np.loadtxt(new_file, delimiter = ',')
print(np_data[100:150])
```

Output is:

```python
[  0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0. 188. 255.  94.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.]
```

**b) .csv files:**

The .csv stands for Comma Separated Values. It is a simple text file in which a comma is used to separate the values. This file is also imported with many methods. The first method is through the NumPy library. We use np.genfromtxt() command to import csv file. This command has several arguments including delimiter for separated values, names for any column header or names and dtype for the data type. Let's look the example:

```python
csv_file = r'C:\Users\Mairaj-PC\Downloads\data.csv'
np_data_new = np.genfromtxt(csv_file, delimiter = ',', names = True, dtype = None)
print(np_data_new[1:5])
```

Output shows the first four rows of dataset:

```python
[(2001,  9.8, 6.4, nan, 5.7, 7.2, 4.7, 5.3, 4.8, 4.6, 4. , nan, 4.3, nan)
 (2002, 10.5, 7.1, nan, 6.3, 8. , 5.4, 5.8, 5.3, 5.1, 4.2, nan, 4.6, nan)
 (2003, 11.8, 7.8, nan, 7.1, 8.9, 6.2, 6.5, 6. , 5.5, 4.9, nan, 5. , nan)
 (2004, 13.4, 8.5, nan, 7.9, 9.9, 6.8, 7.1, 6.4, 5.9, 5.4, nan, 5.5, nan)]
```

Another way to import CSV files is by using pd.readcsv() command through the Pandas library. Let's import the above data from the command of the Pandas library.

```python
# from pandas
from_pd = pd.read_csv(csv_file, index_col = 0)
print(from_pd.head(3))
```

Output shown the first three rows of dataset:

```python
       CMU  MIT  UW  Stanford  Berkeley  Illinois  San Diego  Maryland  \
Date
2000   8.9  5.8 NaN       5.1       6.3       4.3        4.7       4.4
2001   9.8  6.4 NaN       5.7       7.2       4.7        5.3       4.8
2002  10.5  7.1 NaN       6.3       8.0       5.4        5.8       5.3

      Georgia Tech  Cornell  Michigan  Columbia  Texas
Date
2000           4.4      NaN       NaN       4.1    3.7
2001           4.6      4.0       NaN       4.3    NaN
2002           5.1      4.2       NaN       4.6    NaN
```

**2) SAS files:**

SAS stands for Statistical Analysis System. SAS is used for advanced analytics, Multivariate analysis, Business Intelligence and Predictive Analytics. The extension of the SAS file is .sas7bdat which is a dataset file and .sas7bcat is for catalogue files. To import data from SAS, we need to import SAS7BDAT function sas7bdat library. We first used SAS7BDAT function with the command to save data as a file then convert it into a data frame to easily analyze in python.

```python
from sas7bdat import SAS7BDAT

with SAS7BDAT(r'C:\Users\Mairaj-PC\Downloads\sales.sas7bdat') as file:
    df_sas = file.to_data_frame()
print(df_sas.head())
```

Output is:

```python
   YEAR     P           S
0  1950.0  12.9  181.899994
1  1951.0  11.9  245.000000
2  1952.0  10.7  250.199997
3  1953.0  11.3  265.899994
4  1954.0  11.2  248.500000
```

3) STATA files:

Stata is a combination of Statistics and data. It is used to analyze, manage and produce graphical visualization of data. it is generally used by researchers in the field of economics, biomedicine and political science to examine data patterns. The extension of Stata is .dta. To import data from Stata, we need the pd.read_stata() command from the Pandas library.

```python
# stata file
stata_data = pd.read_stata(r'C:\Users\Mairaj-PC\Downloads\disarea.dta')
print(stata_data.head(2))
```

Output shows the first three rows of data set.

```python
 wbcode      country  disa1  disa2  disa3  disa4  disa5  disa6  disa7  disa8  \
0    AFG  Afghanistan   0.00   0.00   0.76   0.73    0.0    0.0   0.00    0.0
1    AGO       Angola   0.32   0.02   0.56   0.00    0.0    0.0   0.56    0.0

   ...  disa16  disa17  disa18  disa19  disa20  disa21  disa22  disa23  \
0  ...     0.0     0.0     0.0    0.00     0.0     0.0    0.00    0.02
1  ...     0.0     0.4     0.0    0.61     0.0     0.0    0.99    0.98

   disa24  disa25
0    0.00     0.0
1    0.61     0.0
```

**4) HDF5 files:**

The HDF5 stands for Hierarchical Data Format version 5. It is an open-source file format that supports large, complex and heterogeneous data. The HDF5 data scales to exabytes. The extension of this source file is .hdf5 and we need to import h5py library to extract data from this source file into Python. For importing, we use h5py.File() command .

```python
import h5py
h5py_file = r'C:\Users\Mairaj-PC\Downloads\L-L1_LOSC_4_V1-1126259446-32.hdf5'

# Now read the file
data = h5py.File(h5py_file, 'r')
print(type(data))
```

Output show the data type of source file.

```python
<class 'h5py._hl.files.File'>
```

To see the structure of HDF5 file, we use data.keys() method relates with the dictionary approach.

```python
for key in data.keys():
    print(key)
```

The output shows the data has three keys, each of these is HDF group. The LIGO documentation tells us the **meta** contain the metadata for the file, **quality** contains information about data quality and **strain** contain strain data from the interferometer.

```python
meta
quality
strain
```

**5) MATLAB files:**

Matlab is a short form of Matrix Laboratory. This software has powerful linear algebra and matrix calculation capabilities. This software is used by engineers and scientists to solve complex mathematical problems. The extension of Matlab is .mat. To import data from Matlab, we need to import the scipy library. We used scipy.io.loadmat() command to read the Matlab data into Python.

```python
import scipy.io
# from matlab
mat_file = r'C:\Users\Mairaj-PC\Downloads\ja_data2.mat'
data = scipy.io.loadmat(mat_file)
print(type(data))
```

```python
<class 'dict'>
```

The data stored is in dictionary format, we see the columns of the data by data. keys() method .

```python
for key in data.keys():
    print(key)
```

Output is:

```python
__header__
__version__
__globals__
rfpCyt
rfpNuc
cfpNuc
cfpCyt
yfpNuc
yfpCyt
CYratioCyt
```

By using the same method for values, we also see the values of each column of data.

**6) JSON files:**

JSON stands for Javascript Object Notation. It is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute-value pairs and arrays. The extension of this file is .json. To load data from JSON files, we first need to import json library. After that, we use the json.load() command to load the JSON data into Python.

```python
import json
file = r'C:\Users\Mairaj-PC\Downloads\iris.json'
with open(file, 'r') as json_file:
    json_data = json.load(json_file)
print(json_data[1:3])
```

Output is:

```python
[{'sepalLength': 4.9, 'sepalWidth': 3.0, 'petalLength': 1.4, 'petalWidth': 0.2, 'species': 'setosa'}, {'sepalLength': 4.7, 'sepalWidth': 3.2, 'petalLength': 1.3, 'petalWidth': 0.2, 'species': 'setosa'}]
```

**Conclusion:**

In this blog, we learn to load data from different data file formats. I believe this will help you with data importing in Python. My Github repository is **https://github.com/MuhammadMairajSaleem92/imorting-data-in-python/blob/main/Introduction%20to%20Data%20Importing%20in%20Python.ipynb**
