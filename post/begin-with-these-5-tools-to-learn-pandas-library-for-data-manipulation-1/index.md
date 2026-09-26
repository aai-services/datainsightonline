---
title: "Begin with these 5 tools to learn pandas library effectively for data manipulation"
author: "074bex435.ranjan"
date: 2021-11-20
description: "Data is everywhere and not in proper order. Many insights can be taken by proper analysing of data. Here we read some 5 techniques of pandas library.1. Reading CSV files2. Crosstab3. Subsetting with..."
categories: ["Pandas"]
image: images/0e6df6_a5490326a9944a73a39b1d41ca3fb9ab.webp
wix-url: https://www.datainsightonline.com/post/begin-with-these-5-tools-to-learn-pandas-library-for-data-manipulation-1
---
Data is everywhere and not in proper order. Many insights can be taken by proper analysing of data. Here we read some 5 techniques of pandas library.

1. Reading CSV files
2. Crosstab
3. Subsetting with .loc
4. Cleaning empty data
5. Plotting

1. **Reading CSV fies**: To play with the data, we need to import data from many format files, one of the prevalent is csv file. Also some data in the dataframe can be seen by dt.head() command shown as below.

```python
import pandas as pd
data = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv')
data.head()
```

![](images/0e6df6_a5490326a9944a73a39b1d41ca3fb9ab.webp)

**2. Crosstab:** This tool helps to summarize the large datasets by making a crosstab table with row as identifier and the frequency of occurrence of any thing in the columns.

```python
#importing packages
import pandas as pd
import numpy

# creating some arrays
a = numpy.array(["hello", "hello", "hello", "hello","hy", "hy", "hy", "hy","hello", "hello"],
                dtype=object)

b = numpy.array(["one", "one", "one", "two","one", "one", "one", "two","two", "two"],
                dtype=object)

c = numpy.array(["handsome","beautiful","hy", "hy", "beautiful","beautiful", "hy", "beautiful","beautiful", "beautiful"],
                dtype=object)

# form the cross tab
pd.crosstab(a, [b, c], rownames=['greetings'], colnames=['number', 'feature'])
```

![](images/0e6df6_4778008b66564ca2a3b529dcc9a81db7.webp)

Here, 'hello', 'one' and 'beautiful' simulataneously occur only one time in same index. Similarly, other values are interpreted.

3. **Subsetting with .loc**: It accepts index values. When a single argument is passed, it will take a subset of rows.

```python
sample = pd.read_csv('sample.csv',index_col='avg_rating')
sample.head()
```

![](images/0e6df6_01f394e8666f4519ab622d5c0e906363.webp)

```python
here = sample.loc[4.5]
here
```

![](images/0e6df6_a839216cb57f4dcc8923687b2d418b8f.webp)

**4. Cleaning empty cells:** While extracting data, many cells are empty. This may hamper our result. So we should avoid those cells or fill with some value.

```python
data = pd.read_csv('data.csv')
data
```

![](images/0e6df6_27fb10abb58e41c5be34b4a4ec4a7ee2.webp)

```python
new_data = data.dropna()
new_data
```

![](images/0e6df6_ae92a383999c4335a727c25d359f7190.webp)

We can also fill NaN with median as

```python
value = data["Calories"].median()

data["Calories"].fillna(value, inplace = True)
```

![](images/0e6df6_deba79be9d144088a7b107c2c0e381fb.webp)

**5. Plotting:** Picture speaks many things. We can interpret many thing from data looking at the figure like bar diagram, scatter plot, pie-chart, etc.

```python
import matplotlib.pyplot as plt

data.plot()

plt.show()
```

![](images/0e6df6_277c59736160415db30b0b07a99fb894.webp)

We can plot other graph also by placing kind='scatter',kind='hist' as the argument in plot function.

```python
data.plot(kind='hist')
plt.show()
```

![](images/0e6df6_b7c924ef54c84081b5efcf0c877da25b.webp)

Find code on Github: <https://github.com/ranjan435/data-insight-2021/blob/assignment-pandas/pandas.ipynb>
