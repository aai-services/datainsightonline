---
title: "Pandas Technique: Pivot Table"
author: "Abu Bin Fahd"
date: 2021-11-26
description: "Pivot table in pandas is an excellent tool to summarize one or more numeric variable based on two other categorical variables. Pivot tables in pandas are popularly seen in MS Excel files. In python..."
categories: ["Pandas"]
image: images/7db382_52cde11cd7a744329f6c4082057bfb01.webp
wix-url: https://www.datainsightonline.com/post/pandas-technique-pivot-table
---
Pivot table in pandas is an excellent tool to summarize one or more numeric variable based on two other categorical variables. Pivot tables in pandas are popularly seen in MS Excel files. In python, Pivot tables of pandas dataframes can be created using the command: pandas. pivot_table.

```python
import pandas as pd
import numpy as np
```

## Read Dataset
```python
df = pd.read_csv('Srt_dta.csv')
df
```

![](images/7db382_52cde11cd7a744329f6c4082057bfb01.webp)

## Pivot Table
Here we calculated the mean of individual weight(kg) with color
**values: column to aggregate, optional**
(If an array is passed, it must be the same length as the data.
The list can contain any of the other types (except list). Keys to group by on the pivot table index. If an array is passed, it is being used as the same manner as column values.)
**index: column, Grouper, array, or list of the previous**

```python
df.pivot_table(values='Weight(kg)', index='Color')
```

![](images/7db382_8de5811bac0b485ca369020e6a4798ba.webp)

## Different Statistics
```python
df.pivot_table(values='Weight(kg)', index='Color', aggfunc=np.median)
```

![](images/7db382_4911d1ce576745078bd4f7cce3453ce9.webp)

## Multiple Statistics
**aggfunc : function, list of functions, dict, default numpy.mean**

If list of functions passed, the resulting pivot table will have hierarchical columns whose top level are the function names (inferred from the function objects themselves) If dict is passed, the key is column to aggregate and value is function or list of functions.

```python
df.pivot_table(values='Weight(kg)', index='Color', aggfunc=[np.mean, np.median])
```

![](images/7db382_183a367e0c224f8b86bd34da53537eb2.webp)

## Pivot on two variable
**columns: column, Grouper, array, or list of the previous**

If an array is passed, it must be the same length as the data. The list can contain any of the other types (except list). Keys to group by on the pivot table column. If an array is passed, it is being used as the same manner as column values.

```python
df.pivot_table(values='Weight(kg)', index='Color', columns='Breed')
```

![](images/7db382_d5b80d31c29b4091ac85aa4958bb7c98.webp)

## Filling missing values in pivot tables
**fill_value: scalar, default None**

Value to replace missing values with (in the resulting pivot table, after aggregation).

```python
df.pivot_table(values='Weight(kg)', index='Color', columns='Breed', fill_value=0)
```

![](images/7db382_d9fd83d4330b41e397910f13f0ac19f0.webp)

## Summing with pivot tables
**margins: bool, default False**

Add all row / columns (e.g. for subtotal / grand totals)

```python
df.pivot_table(values='Weight(kg)', index='Color', columns='Breed', fill_value=0, margins=True)
```

![](images/7db382_4583f7e6f59c4e4cbeb26bd287837c88.webp)

## [GitHub](https://github.com/abubinfahd/Data-Insight/blob/main/Assignments/Pandas%20Technique/Pandas%20Technique-Pivot%20Table.ipynb)
