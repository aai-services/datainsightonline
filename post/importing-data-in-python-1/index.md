---
title: "Importing Data in Python"
author: "Rohit Roy"
date: 2021-12-07
description: "There are three major methods which are used for data science for python. These methods can be used in any juypter notebook provided , by you have pandas library. Pandas library is one of the major..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/importing-data-in-python-1
---
There are three major methods which are used for data science for python. These methods can be used in any juypter notebook provided , by you have pandas library. Pandas library is one of the major library which is used for data analysis.Let's start

1. **Using Filename**

This is the method which is highly popular and easy to use there are only three major things are required in order to achieve this number . We need a csv , juypter notebook and below code. We will import pandas first as a library followed by using the pd.read_csv inside the brackets we will put the file which we want to read . Afterwards, we will check the data.head().

```python
import pandas as pd
data=pd.read_csv("file_name")
data.head()
```

2. **Giving Path**

One of the most efficient and definitive method used by developers and many data scientist is by giving the path of the file and open it with pandas.The idea is to import pandas , and copy the path where the file is present and read it directly. After execution it is easy to ready the data and store the data into the same path or replace it from the old file.

```python
import pandas as pd
data=pd.read_csv(r("Path where file is present"))
data.head() # to check
```

3. **Using URL**

Using URL method is easy but not recommended as it comes under web scraping and all such as data is highly risky especially with compliance and security.However, the process is quite simple , it is similar to the process of what we have already done so far . Import the pandas library used the library by providing the URL link. Open and check the file with data.head().

```python
import pandas as pd
url="URL LINK"
data=pandas.read_csv("URL LINK")
data.head()
```

These are some of the methods which we use to import the csv to do analysis for more information check code [here](https://github.com/rohitroycanny/adventures/blob/main/importing.ipynb).
