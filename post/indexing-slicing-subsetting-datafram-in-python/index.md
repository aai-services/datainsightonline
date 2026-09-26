---
title: "Indexing , Slicing & Subsetting DataFram in Python"
author: "Amr Mohamed Salama"
date: 2022-02-05
description: "1. IntroductionThe Python and NumPy indexing operators [ ] and attribute operator ‘.’ (dot) provide quick and easy access to pandas data structures across a wide range of use cases. The index is like..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/indexing-slicing-subsetting-datafram-in-python
---
**1.** **Introduction**

The Python and NumPy indexing operators [ ] and attribute operator ‘.’ (dot) provide quick and easy access to pandas data structures across a wide range of use cases. The **index** is like an address, that’s how any data point across the data frame or series can be accessed. Rows and columns both have **indexes.**

**The axis labeling information in pandas objects serves many purposes:**

**·** **Identifies data (i.e. provides metadata) .**

**·** **Enables automatic and explicit data alignment.**

**·** **Allows intuitive getting and setting of subsets of the data.**

**2.** **Indexing in terms of analytics**

· implicit (numeric values)

· explicit ( label type)

**3.** **Indexing in terms of programming**

3.1.label-based indexing(.loc)

3.1.1. A single label, e.g. **5 or 'a'** (5 is interpreted as a *label* of the index, **not** an integer position index).

3.1.2. A list or array of labels **['a', 'b', 'c'].**

3.1.3. A slice object with labels **'a':'f'** (**both** the start and the stop are included)

3.1.4. A boolean array (any NA values will be treated as False).

3.1.5. A **callable** function with one argument).

```python
# a single label
df1=df.loc['a', '5']
# a list / array of labels
df2=df.loc[['a', 'b', 'c'], ]
# a slice object with labels
df3=df.loc['a':'b',]
# a boalean array
df4=df.loc['a']>5
# a callabel function
df5=df.loc[lambda df: df['A'] > 0, :]
```

3.2. Integer/position-based indexing (.iloc)

3.2.1. An integer e.g. **5**.

3.2.2. A list or array of integers **[4, 3, 0].**

3.2.3. A slice object with ints **1:7.**

3.2.4. A boolean array (any NA values will be treated as False).

3.2.5. A callable function with one argument.

```python
 a single label
df6=df.iloc[5]
# a list / array of labels
df7=df.iloc[[3, 4, 5],]
# a slice object with labels
df8=df.iloc[7:1,]
# a boalean array
df9=df.iloc[5]>5
# a callabel function
df10=df.iloc[:, lambda df: [0, 1]]
```
