---
title: "Preparing Your Data : Import ,Read and Clean Data"
author: "Teresa Rady"
date: 2021-12-07
description: "The first step to data analysis is to have a look on your data before working on it, that is why you always should start with Exploratory data analysis.Exploratory data analysis means to have an..."
categories: ["Data Cleaning"]
wix-url: https://www.datainsightonline.com/post/preparing-your-data-import-read-and-clean-data
---
The first step to data analysis is to have a look on your data before working on it, that is why you always should start with Exploratory data analysis.

Exploratory data analysis means to have an insightful look into your data before working with it. It starts withstep 1: importing your data .

Import Data

Sometimes not all data you need to work with is in csv format. So Python provides a great opportunity to import data from various other formats to work with.

First of all we import Pandas as the known alias pd.

```python
import pandas as pd
```

Then after that we type the code that reads the specific file of the data. There are different types of files:

- flat files: which are plain text files or tables with no relational databases

some of the commands are found in the following table:

|  |  |
| --- | --- |
| Data format | command |
| CSV file(from a location on your drive) | *data= pd.read_csv("C:\\Users\\Someplace\\Documents\\file1.csv")* |
| CSV file (from a website) | data = *pd.read_csv("http://winterolympicsmedals.com/medals.csv")* |
| .txt file | *data = pd.read_table("C:\\Users\\Someplace\\Desktop\\example2.txt")* |
| Excel file | data = *pd.read_excel("https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls")* |
| SAS file | data = *pd.read_sas('meows.sas7bdat')* |
| STATA file | data = *pd.read_stata('films.dta')* |

- Relational databases: such as SQL

```python
from sqlalchemy import create_engine
engine = create_engine('sqlite://name.sqlite' )
```

or using pandas:

```python
df = pd.read_sql_query("SELECT  *  FROM  Orders " , engine)
```

- Pickled files:

```python
import pickle
with open('pickledname.pkl', 'rb') as file:
    pickled_data = pickle.load(file)
```

- HDF5 files:

```python
import h5py
filename = 'name_file.hdf5'
data = h5py.file(filename, 'r')
```

- MATLAB files:

```python
import scipy.io
filename = 'name.mat'
mat = scipy.io.loadmat(filename)
```

There is also a way to get the data from an HTML file called web scraping. Web scraping works through BeautifulSoup

```python
import request
from bs4 import BeautifulSoup
```

```python
url = ' www.something.html '
r = request.get(url)
html.doc = r.text
Soup = BeautifulSoup(html.doc)
Pretty_Soup = Soup.pretty()print(pretty_Soup)
```

After importing the data here comes the step of reading and cleaning it.

firstly we start by having a general look on the data after importing it through the known commands of pandas.

```python
df.head()
df.describe()
```

This step aims at understanding what is your data about and have an idea if there is any missing or duplicate data.

There are various ways to deal with missing or duplicate data. You can read a hint about them in the blog post named [Pandas Manipulation Techniques](https://www.datainsightonline.com/post/pandas-manipulation-techniques).

There is another important step in reading your data which is visualizing it. It gives an idea about outlier data and you can find any inconsistencies that might hinder your data analysis process.

Now after you have done all those steps your data is ready for work!
