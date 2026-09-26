---
title: "Where Function in Pandas"
author: "Ebrima Sise"
date: 2022-05-08
description: "The where() in pandas and NumPy is used to filter Data Frames based on a condition. We will discuss this important topic in this tutorial. First, we will need to import our libraries that will help..."
categories: ["Pandas", "Python"]
wix-url: https://www.datainsightonline.com/post/where-function-in-pandas
---
The where() in pandas and NumPy is used to filter Data Frames based on a condition. We will discuss this important topic in this tutorial.

First, we will need to import our libraries that will help us work with a Data Frame.

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
```

Now that the libraries are imported, we will load the mtcars dataset from statsmodels into a Data Frame and name it as df.

```python
df = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
```

Let's take a quick glance at the newly created Data Frame.

```python
df.head()
```

mpg cyl disp hp drat wt qsec vs am gear carb

Mazda RX4 21.0 6 160.0 110 3.9 2.62 16.46 0 1 4 4

Mazda RX4 Wag 21.0 6 160.0 110 3.9 2.875 17.02 0 1 4 4

Datsun 710 22.8 4 108.0 93 3.85 2.32 18.61 1 1 4 1

Hornet 4 Drive 21.4 6 258.0 110 3.08 3.215 19.44 1 0 3 1

Hornet Sportabout 18.7 8 360.0 175 3.15 3.44 17.02 0 0 3 2

Our tutorial will start by first getting the indices of all the cars in the Data Frame which has four cylinders. We will store these indices in a variable called four_cyl_ind.

```python
four_cyl_ind = np.where(df.cyl == 4)
```

Since the dataset is not very big, we can assume that the four-cylinder cars will not be too many. That being the case, we will print the indices below.

```python
four_cyl_ind
```

```python
output: (array([ 2,  7,  8, 17, 18, 19, 20, 25, 26, 27, 31]),)
```

Now, we can subset the Data Frame and get data on only the four-cylinder cars.

```python
four_cylinder_cars = df.iloc[four_cyl_ind]
```

To confirm that only four-cylinder cars are in the new Data Frame, we will check the unique values in the cyl column. If it is more than one, then our assertion is incorrect.

```python
four_cylinder_cars['cyl'].unique()
```

```python
output: array([4])
```

And yes! We were right.
But let's look at the first few rows of the new Data Frame.

```python
four_cylinder_cars.head()
```

mpg cyl disp hp drat wt qsec vs am gear carb

Datsun 710 22.8 4 108.0 93 3.85 2.32 18.61 1 1 4 1

Merc 240D 24.4 4 146.7 62 3.69 3.19 20.0 1 0 4 2

Merc 230 22.8 4 140.8 95 3.92 3.15 22.9 1 0 4 2

Fiat 128 32.4 4 78.7 66 4.08 2.2 19.47 1 1 4 1

Honda Civic 30.4 4 75.7 52 4.93 1.615 18.52 1 1 4 2

We can use the where() to also create a new column in a Data Frame. It checks a condition, if true, the second argument is returned. Otherwise, the third one is returned. We will create a new column called consumption based on this.

```python
df['consumption'] = np.where(df['mpg'] > 25,
        'High MPG',
        'Low MPG')
```

Finally, we will see the new column added to Data Frame.

mpg cyl disp hp drat wt qsec vs am gear carb consumption

Mazda RX4 21.0 6 160.0 110 3.9 2.62 16.46 0 1 4 4 Low MPG

Mazda RX4 Wag 21.0 6 160.0 110 3.9 2.875 17.02 0 1 4 4 Low MPG

Datsun 710 22.8 4 108.0 93 3.85 2.32 18.61 1 1 4 1 Low MPG

Hornet 4 Drive 21.4 6 258.0 110 3.08 3.215 19.44 1 0 3 1 Low MPG

Hornet Sportabout 18.7 8 360.0 175 3.15 3.44 17.02 0 0 3 2 Low MPG
