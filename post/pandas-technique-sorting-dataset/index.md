---
title: "Pandas Technique: Sorting Dataset"
author: "Abu Bin Fahd"
date: 2021-11-26
description: "import pandas as pd import numpy as npRead Datasetdf = pd.read_csv('Srt_dta.csv') dfSortingPandas sort_values() function sorts a data frame in Ascending or Descending order of passed Column. It's..."
categories: ["Pandas"]
image: images/7db382_061765f637434b479d057ec7f9d018de.webp
wix-url: https://www.datainsightonline.com/post/pandas-technique-sorting-dataset
---
![](images/7db382_061765f637434b479d057ec7f9d018de.webp)

```python
import pandas as pd
import numpy as np
```

## Read Dataset
```python
df = pd.read_csv('Srt_dta.csv')
df
```

![](images/7db382_451f2aee6e734e19ae670ad24b78f86d.webp)

## Sorting
Pandas sort_values() function sorts a data frame in Ascending or Descending order of passed Column. It's different than the sorted Python function since it cannot sort a data frame and particular column cannot be selected.

```python
df.sort_values('Weight(kg)')
```

![](images/7db382_cb5281ea55634cd78de63ae9c612607f.webp)

## Sorting in** descending **value
To sort in descending order, we need to specify ascending=False

```python
df.sort_values('Weight(kg)', ascending=False)
```

![](images/7db382_568fe255ad064b969bc85b792ccc0fbc.webp)

## Sorting by multiple variables
Call pandas.DataFrame.sort_values(by, ascending) with by as a list of column names to sort the rows in the DataFrame object based on the columns specified.

```python
df.sort_values(['Weight(kg)', 'Height(cm)'])
```

![](images/7db382_b0c55f9650b64658a9bb2c7eb262ece8.webp)

## Sorting by multiple variables
Call pandas. DataFrame. sort_values(by, ascending) with by as a list of column names to sort the rows in the DataFrame object based on the columns specified in by . Set ascending to a tuple of booleans corresponding to the columns in by , where True sorts in ascending order and False sorts in descending order.

```python
df.sort_values(['Weight(kg)', 'Height(cm)'], ascending=[True, False])
```

![](images/7db382_b8a9d1570d66499c8552467e7a220716.webp)

## [GitHub Link](https://github.com/abubinfahd/Data-Insight/blob/main/Assignments/Pandas%20Technique/PandasTechnique-Sorting%20DataFrame.ipynb)
