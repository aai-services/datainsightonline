---
title: "PANDAS TECHNIQUES FOR DATA MANIPULATION"
author: "James Owusu-Appiah"
date: 2022-03-21
description: "Merge DataFramesWhen there are 2 or more datasets or DataFrames that need to be analyzed as a single dataset or DataFrame, then there is the need to merge them together to make analysis very simple..."
categories: ["Pandas"]
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-manipulation-5
---
## Merge DataFrames
When there are 2 or more datasets or DataFrames that need to be analyzed as a single dataset or DataFrame, then there is the need to merge them together to make analysis very simple and more intuitive.

The pandas' ***merge*** method allows us to carry out this function of joining different datasets together as one to aid in analysis. The syntax for the ***merge*** method is given as:

***DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x','_y'), copy=True, indicator=False, validate=None)***

***right:*** object to merge with.

***how:*** {'left','right','inner','outer','cross'}, default 'inner'

*'****left':*** use only keys from left frame

*'****right':*** use only keys from right frame

*'****outer':*** use union keys from both frames

*'****left':*** use only keys from left frame

*'****cross':*** creates cartesian product from both frames

***on:*** column or index level to join on.

***left_on:*** Column or index level names to join on in the left DataFrame.

***right_on:*** Column or index level names to join on in the right DataFrame.

***left_index:*** Use the index from the left DataFrame as the join key.

***right_index:*** Use the index from the right DataFrame as the join key

***suffixes:*** to distinguish between two data frame columns if there exist the same names.

Code showing merging to two different DataFrames using ***right_on*** and ***left_on***.

```python
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],                   'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],                    'value': [5, 6, 7, 8]})
df1.merge(df2, left_on='lkey', right_on='rkey')
#right and left on
```

Output:

```python
    lkey    value_x    rkey    value_y
 0  foo           1    foo           5
 1  foo           1    foo           8
 2  foo           5    foo           5
 3  foo           5    foo           8
 4  bar           2    bar           6
 5  baz           3    baz           7
```

Code showing merging of two different DataFrame using ***inner***.

```python
df1 = pd.DataFrame({'a': ['foo', 'bar'],                   'b': [1, 2]})
df2 = pd.DataFrame({'a': ['foo','baz'],                    'b': [3, 4]})
df1.merge(df2, how='inner', on='a')
```

Output:

```python
    a    b_x    b_y
0   foo    1      3
```

Code showing merging of two different DataFrames using ***left***.

```python
df1 = pd.DataFrame({'a': ['foo', 'bar'],                   'b': [1, 2]})
df2 = pd.DataFrame({'a': ['foo','baz'],                    'b': [3, 4]})
df1.merge(df2, how='left', on='a')
```

Output:

```python
    a    b_x    b_y
0   foo    1      3
1   bar    2    NaN
```

## Apply Function
**Pandas.Series.apply** allow the users to pass a function and apply it on every single value of the Pandas series. It comes as a huge improvement for the pandas library as this function helps to segregate data according to the conditions required due to which it is efficiently used in data science and machine learning.

The syntax is as follows:

***Series.apply(func,convert_dtype=True,args=(),\*\*kwargs)***

***func:***.apply takes a function and applies it to all values of pandas series.

***convert_dtype:***Convert dtype as per the function’s operation.

***args=():***Additional arguments to pass to function instead of series.

***Return Type:***Pandas Series after applied function/operation.

Code to show how this function works:

```python
#Importing the necessary libraries and loading the data
import pandas as pd
import numpy as np
df3 = pd.DataFrame([[1,2,3,4,5]], columns=['A', 'B','C','D', 'E'])
df3.apply(np.sqrt)
```

Output:

```python
    A          B           C        D           E
0   1.0  1.41421    1.732051      2.0    2.236068
```

## Pandas.Series.drop_duplicates
This helps to get rid of duplicate values in a dataset. It returns Series with duplicate values removed.

The syntax for this method is:

***Series.******drop_duplicates******(******keep='first'******,*** ***inplace=False******)***

***keep:*** {'first', 'last', False}, default 'first'

Method to handle dropping duplicates:

- **'first'**: Drop duplicates except for the first occurrence
- **'last':** Drop duplicates except for the last occurrence
- **False:** Drop all duplicates.

***inplace:*** bool, default False

If True, performs operation inplace and returns None.

***Returns:*** Series or None

Series with duplicates dropped or None if inplace=True

Code showing how ***pandas.series.drop_duplicates*** work:

```python
s = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo', 'lion', 'frog', 'lion'], name='animal')
s.drop_duplicates()
```

Output:

```python
0      lama
1       cow
3    beetle
5     hippo
6      lion
7      frog
```

## Pandas.Series.append
Pandas***series.append()*** function is used to append rows of other dataframe to the end of the given dataframe, returning a new dataframe object or concatenating two or more series. Columns which are not in the original dataframes are added as new columns and the new cells are populated with NaN value.

The syntax of the append function is given as:

***Series.append(to_append, ignore_index=False, verify_integrity=False)***

***'to_append':*** Series to append with self.

***'ignore_index':*** If True, the resulting axis will be labelled 0... n-1

***'verity_integrity':*** If True, raise Exception on creating index with duplicates

***Returns:*** Concatenated Series

Code showing how the append function is used:

```python
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s1.append(s2)
```

Output:

```python
0    1
1    2
2    3
0    4
1    5
2    6
```

## Pandas.Series.truncate
Truncates a Series or DataFrame before and after some index value. This is a useful shorthand for boolean indexing based on index values above or below certain thresholds.

The syntax is given as:

***Series.truncate(before=None, after=None, axis=None, copy=True)***

***'before':*** Truncate all rows before this index value

***'after':*** Truncate all rows after this index value

***'axis':*** Axis to truncate. Truncates the index(rows) by default

***'copy':*** Return a copy of the truncated section

***Returns:*** Truncated Series or DataFrame

Code to demonstrate the use of truncate:

```python
df = pd.DataFrame({'A': ['y', 'u', 'c', 'd', 'e'],
                   'B': ['f', 'g', 'h', 'i', 'j'],
                   'C': ['k', 'l', 'm', 'n', 'o']},
                  index=[1, 2, 3, 4, 5])
df.truncate(before=2, after=4)
```

Output:

```python
    A    B    C
2   u    g    l
3   c    h    m
4   d    i    n
```
