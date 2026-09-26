---
title: "Begin with these 5 tools to learn pandas library for data manipulation"
author: "074bex435.ranjan"
date: 2021-11-20
description: "Data is everywhere and not in proper order. Many insights can be taken by proper analysing of data. Here we read some 5 techniques of pandas library.1. Reading CSV files2. Crosstab3. Subsetting with..."
categories: ["Pandas"]
image: images/0e6df6_78bf526e88af4df2be9f68d3b83a078e.webp
wix-url: https://www.datainsightonline.com/post/begin-with-these-5-tools-to-learn-pandas-library-for-data-manipulation
---
Data is everywhere and not in proper order. Many insights can be taken by proper analysing of data. Here we read some 5 techniques of pandas library.

1. Reading CSV files
2. Crosstab
3. Subsetting with .loc
4. Cleaning empty data

1. **Reading CSV fies**: To play with the data, we need to import data from many format files, one of the prevalent is csv file. Also some data in the dataframe can be seen by dt.head() command shown as below.

```python
import pandas as pd
data = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv')
data.head()
```

![](images/0e6df6_78bf526e88af4df2be9f68d3b83a078e.webp)

**2. Crosstab:** This tool helps to summarize the large datasets by making a crosstab table with row as identifier and the frequency of occurrence of any thing in the columns.

```python
#importing packages
import pandas as pd
import numpy

# creating some arrays
a = numpy.array(["hello", "hello", "hello", "hello",
                 "hy", "hy", "hy", "hy",
                 "hello", "hello"],
                dtype=object)

b = numpy.array(["one", "one", "one", "two",
                 "one", "one", "one", "two",
                 "two", "two"],
                dtype=object)

c = numpy.array(["handsome","beautiful",
                 "hy", "hy", "beautiful",
                 "beautiful", "hy", "beautiful",
                 "beautiful", "beautiful"],
                dtype=object)

# form the cross tab
pd.crosstab(a, [b, c], rownames=['greetings'], colnames=['number', 'feature'])
```

![](images/0e6df6_f5e078c88e5548f5b9906873cd556c65.webp)

Here, 'hello', 'one' and 'beautiful' simulataneously occur only one time in same index. Similarly, other values are interpreted.

3. **Subsetting with .loc**: It accepts index values. When a single argument is passed, it will take a subset of rows.

```python
sample = pd.read_csv('sample.csv',index_col='avg_rating')
sample.head()
```

![](images/0e6df6_ba3ad8b534474fa09c4d05ad981feb47.webp)

```python
here = sample.loc[4.5]
here
```

![](images/0e6df6_0db88f85b2fd4042be4278eba7417807.webp)

**4. Cleaning empty cells:** While extracting data, many cells are empty. This may hamper our result. So we should avoid those cells or fill with some value.
