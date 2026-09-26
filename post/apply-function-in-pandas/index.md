---
title: "Apply Function in Pandas"
author: "Ebrima Sise"
date: 2022-05-07
description: "The apply function lets you run a function on all the elements of a pandas series/column. It lets you apply a function on either the rows or columns of a data frame. For us to be able to experiment..."
categories: ["Pandas", "Python"]
wix-url: https://www.datainsightonline.com/post/apply-function-in-pandas
---
The apply function lets you run a function on all the elements of a pandas series/column. It lets you apply a function on either the rows or columns of a data frame.

For us to be able to experiment with the apply method, we'd need to import a few libraries to help us with the data loading. These libraries include the NumPy package and the pandas library.

```python
import numpy as np
import pandas as pd
```

After importing the libraries, we will create a data frame of random integers between 1 and 1000. The data frame will also have 10,000 rows and 5 columns.

```python
df = pd.DataFrame(np.random.randint(1, 1000, size=(10000, 5)), columns=list('LMNOP'))
```

We will now take a look at the first few rows of the data frame.

```python
df.head()
```

L M N O P

0 629 594 412 553 292

1 293 699 963 252 183

2 225 973 665 4 381

3 548 24 731 753 177

4 713 73 747 777 682

Since the apply method runs a function on all the entries in a series, we could use a lambda function to create a function on the fly or create a normal function to use with `apply`. The function we are going to use is going to check every cell in a series and determine whether the value is less than or greater than 500. If greater, it will return big, else it will return small.

```python
def my_func(cell):
    if cell > 500:
        return 'big'
    else:
        return 'small'
```

We will temporarily create a column `Q` that will hold the values returned from using `apply` on column `L`.

```python
df['Q']  = df['L'].apply(my_func)
```

```python
df.head()
```

L M N O P Q

0 629 594 412 553 292 big

1 293 699 963 252 183 small

2 225 973 665 4 381 small

3 548 24 731 753 177 big

4 713 73 747 777 682 big

A quick summary of statistics of the numeric columns of the data frame can be seen below.

```python
df.describe()
```

L M N O P

count 10000.0 10000.0 10000.0 10000.0 10000.0

mean 501.306 501.802 501.6683 496.8143 504.3349

std 286.8483333760824 288.0564945464777 286.70172176468725 289.3895852457632 287.39211326107494

min 1.0 1.0 1.0 1.0 1.0

25% 253.0 253.0 257.0 247.0 256.0

50% 501.0 504.0 500.0 499.0 504.5

75% 750.0 750.0 748.0 747.0 752.25

max 999.0 999.0 999.0 999.0 999.0

You can even use `apply` on a data frame to calculate aggregation across the different axis.

The function below calculates the mean of the given column.

```python
def average(col):
    return round(col.mean())
```

To be able to do this, we have to specify that the axis should be equal to 0. But for this to work, it needs to be applied to numeric columns. Since column Q is not numeric, running apply like this will throw an error. So first, we will need to delete this column.

```python
df.drop(columns='Q', inplace=True)
```

```python
df.apply(average, axis=0)
```

0

L 501

M 502

N 502

O 497

P 504

We can do aggregation row-wise as well. This can be accomplished by setting the axis to 1. The below cell creates a new column, average, that calculates the average row-wise.

```python
df['average'] = df.apply(average, axis=1)
```

L M N O P average

0 629 594 412 553 292 496

1 293 699 963 252 183 478

2 225 973 665 4 381 450

3 548 24 731 753 177 447

4 713 73 747 777 682 598

This is the tip of the iceberg but gives you a solid foundation when getting started with `apply`!
