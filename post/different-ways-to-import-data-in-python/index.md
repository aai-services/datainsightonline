---
title: "Different ways to import data in Python"
author: "Gaurab Awal"
date: 2021-12-09
description: "For data analysis, we have to collect different kinds of data from different sources. So we have to know about the different file types and the ways to import data for the data analysis process.We..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/different-ways-to-import-data-in-python
---
For data analysis, we have to collect different kinds of data from different sources. So we have to know about the different file types and the ways to import data for the data analysis process.

We are going to explore each data type and ways to import it.

1. Reading files like text file, CSV file

We can import the file in the following way. First, we are assigned a filename and open the file, then read data from the text file and then close the file.

```python
filename = 'file.txt'
file = open(filename,mode='r')
text = file.read()
file.close()
```

2. Read files with Numpy

We can read a simple text file with the help of NumPy also. First we need to import numpy and use the .loadtxt method to read a text files using numpy. We can also add skiprows = 1 to skip header line of the data file.

```python
import numpy as np
filename = 'file.txt'
data = np.loadtxt(filename,delimiter=',')
```

3. When we need to import data with mixed data types using Numpy

We use .genfromtxt to import data with contains multiple data types.

```python
import numpy as np
filename = 'file.csv'
data = np.genfromtxt(filename,delimiter=',',names = True, dtypes=None)
```

4. Import files using pandas

We can use the pandas library to read data. To do so we have import pandas library first as follows. For now, we are reading the CSV file so that we have used read_csv. If we want to read an excel file then we use read_excel. The nrows= 5 means we are going to read only five rows data.

```python
import pandas as pd
pd.read_csv('titanic.csv',nrows= 5)
```

5. Pickle file

Pickle can be used to serialize python object structures, which refers to the process of converting an object in the memory to a byte stream that can be stored as a binary file on disk.

import pickle

```python
with open("pickle_file.pkl","rb") as file:
    data = pickle.load(file)
```

6. Importing SAS/Stata files using pandas

from sas7bdat import SAS7BDAT

```python
with SAS7BDat('dataset.sas7bdat') as file:
    df_sas = file.to_datadata_frame()
```

7. Read data from relational databases

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(''sqlite:///Chinook.sqlite')
con = engine.connect()
rs = con.execute("Select * from dataset)
df = pd.DateFrame(rs.fetchall())
```
