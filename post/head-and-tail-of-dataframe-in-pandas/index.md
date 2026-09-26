---
title: "Head and Tail of DataFrame in Pandas"
author: "Arpan Sapkota"
date: 2021-11-22
description: "To view a small sample of a Series or DataFrame object, use the head() and tail() methods. The default number of elements to display is five, but you may pass a custom number. head() returns the..."
categories: ["Pandas"]
image: images/a8b2bc_9e9e436c2be646f0880c8d2dca378f03.webp
wix-url: https://www.datainsightonline.com/post/head-and-tail-of-dataframe-in-pandas
---
![](images/a8b2bc_9e9e436c2be646f0880c8d2dca378f03.webp)

To view a small sample of a Series or DataFrame object, use the head() and tail() methods. The default number of elements to display is five, but you may pass a custom number.

head() returns the first n rows(observe the index values). The default number of elements to display is five, but you may pass a custom number.

tail() returns the last n rows(observe the index values). The default number of elements to display is five, but you may pass a custom number.

Lets start with importing the pandas and numpy

```python
import pandas as pd
```

```python
import numpy as np
```

Create a series with random numbers

```python
long_series = pd.Series(np.random.randn(1000))
```

The first five rows of the data series:

```python
long_series.head()
```

Output:

```python
0    0.580156
1    0.469914
2   -0.744791
3   -2.381032
4    0.954909
```

The last three rows of the data series:

long_series.tail(3)

```python
997    0.294750
998   -1.108673
999    0.013724
```
