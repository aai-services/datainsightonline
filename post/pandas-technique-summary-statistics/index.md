---
title: "Pandas Technique: Summary Statistics"
author: "Abu Bin Fahd"
date: 2021-11-26
description: "Summary statistics is a part of descriptive statistics that summarizes and provides the gist of information about the sample data. Statisticians commonly try to describe and characterize the..."
categories: ["Pandas", "Statistics"]
image: images/7db382_97e616c6259f41d89520616ff9c0f765.webp
wix-url: https://www.datainsightonline.com/post/pandas-technique-summary-statistics
---
Summary statistics is a part of descriptive statistics that summarizes and provides the gist of information about the sample data. Statisticians commonly try to describe and characterize the observations by finding: a measure of location, or central tendency, such as the arithmetic mean.

```python
import pandas as pd
import numpy as np
```

```python
# read dataset
df = pd.read_csv('Srt_dta.csv')
df
```

![](images/7db382_97e616c6259f41d89520616ff9c0f765.webp)

## Summarizing numerical data
```python
df['Height(cm)'].mean()
```

```python
'2011-12-11'
```

```python
df['Date of Birth'].max()
```

```python
'2018-02-27'
```

## The .agg() method
agg() is used to pass a function or list of function to be applied on a series or even each element of series separately. In case of list of function, multiple results are returned by agg() method.

```python
def pct30(column):
    return column.quantile(0.3)

df['Weight(kg)'].agg(pct30)
```

```python
21.0
```

## Summaries on multiple columns
```python
df[['Height(cm)', 'Weight(kg)']].agg(pct30)
```

```python
Height(cm)    45.4
Weight(kg)    21.0
dtype: float64
```

## Multiple summaries
```python
def pct40(column):
    return column.quantile(0.4)

df['Height(cm)'].agg([pct30, pct40])
```

```python
pct30    45.4
pct40    47.2
Name: Height(cm), dtype: float64
```

## Cumulative sum
```python
df['Weight(kg)'].cumsum()
# another method
# .cummax()
# .cumprod()
# .cummin()
```

```python
0     25
1     48
2     70
3     87
4    116
5    118
6    192
Name: Weight(kg), dtype: int64
```
