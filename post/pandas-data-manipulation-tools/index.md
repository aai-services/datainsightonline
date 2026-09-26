---
title: "Pandas Data Manipulation Tools"
author: "Rashidat Sikiru"
date: 2021-11-22
description: "Author: Rashidat SikiruIntroductionPandas is an open-source python library for highly specialized data analysis. It is a perfect tool for anyone who wants to perform data analysis using python as a..."
categories: ["Pandas"]
wix-url: https://www.datainsightonline.com/post/pandas-data-manipulation-tools
---
Author: Rashidat Sikiru

**Introduction**

Pandas is an open-source python library for highly specialized data analysis. It is a perfect tool for anyone who wants to perform data analysis using python as a programming language. In this article, I will be taking us through the pandas techniques for data manipulation. There are several data manipulation tools, but this article will we be discussing five powerful pandas data manipulation tools. These are:

1. Merging

2. Mapping

3. Removing Duplicates

4. Binning

5. Sorting

**1. Merging**

Merging also referred to as joining consists of a combination of data frames through the connection of rows using one or more keys. It can be likened to the “JOIN” operation for those who are familiar with the Structured Query Language(SQL) and merge() is the function to perform this kind of operation.

Let’s import the pandas library and define two data frames that will serve as examples for this section:

```python
# import pandas and numpy
import numpy as np
import pandas as pd

# define the first dataframe
data1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
                      'price': [12.33,11.44,33.21,13.23,33.62]})
data1
```

```python
   id     price
0  ball    12.33
1  pencil  11.44
2  pen     33.21
3  mug     13.23
4  ashtray 33.62
```

```python
# define the second dataframe
data2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'], 'color': ['white','red','red','black']})
data2
```

```python
    id      color
0   pencil  white
1   pencil  red
2   ball    red
3   pen    black
```

Now we can carry out merging by applying the merge() function to the two data frame objects.

```python
pd.merge(data1,data2)
```

```python
    id     price    color
0   ball   12.33    red
1   pencil 11.44    white
2   pencil 11.44    red
3   pen    33.21    black
```

We can see from the result, the returned data frame consists of all rows that have an ID in common. In addition to the common column, the columns from the first and the second data frame are added. In this case, we used the merge() function without specifying any column explicitly.

However, we will come across cases where we need to decide which column on which to base the merging. To do this, we need to add the ON option with the column name as the key for the merging.

Let's do this by adding another column named "brand" to the two data frames so that we can have two similar columns on each data frame.

```python
data1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
                      'color':  ['white','red','red','black','green'],
                      'brand': ['OMG','ABC','ABC','POD','POD']})
data1
```

```python
     id       color     brand
0    ball     white     OMG
1    pencil   red       ABC
2    pen      red       ABC
3    mug      black     POD
4    ashtray  green     POD
```

```python
data2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
                     'brand': ['OMG','POD','ABC','POD']})
data2
```

```python
     id     brand
0  pencil   OMG
1  pencil   POD
2  ball     ABC
3  pen      POD
```

Now that we have two data frames having columns with the same name, let us use our merge() function.

```python
pd.merge(data1,data2)
```

```python
id color  brand
```

We can see that our code returns an empty data frame because it does not know which of the columns it should carry out the merging.

So let's try to explicitly define the criteria for merging by specifying the name of the key column in the ON option.

```python
# merging using id
pd.merge(data1,data2,on='id')
```

```python
   id    color   brand_x   brand_y
0 ball   white   OMG       ABC
1 pencil red     ABC       OMG
2 pencil red     ABC       POD
3 pen    red     ABC       POD
```

```python
# merging using brand
pd.merge(data1, data2, on="brand")
```

id_xobjectcolorobjectbrandobjectid_yobject

0

ball

white

OMG

pencil

1

pencil

red

ABC

ball

2

pen

red

ABC

ball

3

mug

black

POD

pencil

4

mug

black

POD

pen

5

ashtray

green

POD

pencil

6

ashtray

green

POD

pen
