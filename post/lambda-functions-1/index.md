---
title: "Lambda functions"
author: "stella tchoutcha"
date: 2022-05-06
description: "They are very useful when it is necessary to perform small tasks with less code, they promote the readability of the codeexample : power = lambda x, y: x ** y power(2, 3)8 Lambdas show us their great..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/lambda-functions-1
---
They are very useful when it is necessary to perform small tasks with less code, they promote the readability of the code

example :

```python
 power = lambda x, y: x ** y
power(2, 3)
```

```python
8
```

Lambdas show us their great power when we need to use functions that take another function as an argument. An example of such a function in python could be: apply(), map() or reduce().

```python
nums = [48, 6, 9, 21, 1]
square = map(lambda num: num ** 2, nums)
print(square)
```

apply to a dataset

```python
import pandas as pd

train = pd.read_csv("dataset/train.csv") # load the dataset
```

The first thing to do is to deal with the missing value , lets check first how many there are for each variable avec Lambda function

```python
train.apply(lambda x: sum(x.isnull()),axis=0)
```

here is the [notebook](https://github.com/Tchoutcha/Data-insight-sandjong/blob/main/assigmentLambda.ipynb)
