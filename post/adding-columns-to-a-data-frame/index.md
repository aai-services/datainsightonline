---
title: "Adding Columns to a Data Frame"
author: "Ebrima Sise"
date: 2022-05-07
description: "In this tutorial, we will practice adding column(s) to a Data Frame. But first, we need to import pandas and NumPy to be able to demonstrate this.import pandas as pd import numpy as npWe will create..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/adding-columns-to-a-data-frame
---
In this tutorial, we will practice adding column(s) to a Data Frame.

But first, we need to import pandas and NumPy to be able to demonstrate this.

```python
import pandas as pd
import numpy as np
```

We will create a dummy Data Frame for this illustration.

```python
df = pd.DataFrame(np.random.randint(100, 1000, size=(1000, 4)), columns=list('ABCD'))
```

Let's see the first few rows of this Data Frame.

```python
df.head()
```

A B C D

0 933 398 707 576

1 327 659 147 425

2 302 690 426 146

3 460 322 460 236

4 948 629 267 444

The first method we will discuss is called the Direct Column Assignment.

To add a column this way, type the name of the Data Frame and within the square brackets, enter the name of the new column. And set it to the values the new column holds. In this case, the values will be boolean indicating whether the value in column A is less than 600. In some cases, this might be a list of values you already have and can assign to the new column.

```python
df['type1'] = df['A'] < 600
```

If we print the first few rows of the Data Frame, we see that the new column has been added

```python
df.head()
```

A B C D type1

0 933 398 707 576 False

1 327 659 147 425 True

2 302 690 426 146 True

3 460 322 460 236 True

4 948 629 267 444 False

The second method we will discuss is the insert method. This method lets you insert the new column in a specified location.

In the example below, we will insert a column, type2, at column index 3. The values of this column are also boolean values checking a specific condition.

```python
df.insert(3,
         'type2',
         df['C'] > 700)
```

Let's take a quick look at the Data Frame to see the new changes.

A B C type2 D type1

0 933 398 707 True 576 False

1 327 659 147 False 425 True

2 302 690 426 False 146 True

3 460 322 460 False 236 True

4 948 629 267 False 444 False

Indeed, a new column has been added!

For our third and final example, we will use the assign function to add two extra columns (type31 and type32) to our Data Frame. This method is capable of adding one or more new columns to a Data Frame.

```python
df = df.assign(type31 = df['B'] < 500,
              type32 = df['B'] > 600)
```

```python
df.head()
```

A B C type2 D type1 type31 type32

0 933 398 707 True 576 False True False

1 327 659 147 False 425 True False True

2 302 690 426 False 146 True False True

3 460 322 460 False 236 True True False

4 948 629 267 False 444 False False True

I hope you are able to learn something from this tutorial.
