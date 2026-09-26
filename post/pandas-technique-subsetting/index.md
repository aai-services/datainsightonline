---
title: "Pandas Technique-Subsetting"
author: "Abu Bin Fahd"
date: 2021-11-19
description: "import pandas as pd import numpy as npRead Datasetdf = pd.read_csv('Srt_dta.csv')dfSubsetting columnsTo select a single column, use square brackets [] with the column name of the column of..."
categories: ["Pandas"]
image: images/7db382_cbb0257afb5a462aae974b96e94f80e5.webp
wix-url: https://www.datainsightonline.com/post/pandas-technique-subsetting
---
```python
import pandas as pd
import numpy as np
```

**Read Dataset**

```python
df = pd.read_csv('Srt_dta.csv')df
```

![](images/7db382_cbb0257afb5a462aae974b96e94f80e5.webp)

## Subsetting columns
To select a single column, use square brackets [] with the column name of the column of interest.

```python
df['Name']
```

![](images/7db382_6b15962a6d144f909911f0cea867ecfc.webp)

## Subsetting multiple columns
```python
# method 1
df[["Breed","Height(cm)"]]
```

![](images/7db382_8ba1f95935f049dd9bb33f7bc36c6c4e.webp)

```python
# method 2
cols_to_subset = ["Breed","Height(cm)"]
df[cols_to_subset]
```

![](images/7db382_cf785d0f4bd44e898378d576fc3b8e81.webp)

## Subsetting rows
This return boolean value.

```python
df["Height(cm)"] > 50
```

![](images/7db382_be772a98be8647f7ae123c24ee707740.webp)

```python
# This return numeric value
df[df["Height(cm)"] > 50]
```

![](images/7db382_9157b361828b4e149c622d434b7b412c.webp)

## Subsetting based on text data
```python
df[df["Breed"] > '2015-01-01']
```

![](images/7db382_f76f4ac8ca544df1b9dab4518420b3c9.webp)

## Subsetting based on multiple conditions
```python
is_lab = df['Breed'] == 'Labrador'
is_black = df['Color'] == 'Black'
df[is_lab & is_black]
```

![](images/7db382_32d62f76d6b24bd99365088e32e74ca2.webp)

## Subsetting using .isin()
Pandas isin() method is used to filter data frames. isin() method helps in selecting rows with having a particular(or Multiple) value in a particular column. Parameters: values: iterable, Series, List, Tuple, DataFrame or dictionary to check in the caller Series/Data Frame.

```python
is_black_or_brown = df['Color'].isin(['Black', 'Brown'])
df[is_black_or_brown]
```

![](images/7db382_e4559f68a4104b6bba236d7d5cf977f1.webp)

<https://github.com/abubinfahd/Data-Insight/blob/main/Assignments/Pandas%20Technique/Pandas%20Tecnique-Subsetting.ipynb>
