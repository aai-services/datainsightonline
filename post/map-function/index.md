---
title: "Map function"
author: "Wilson Waha"
date: 2022-05-06
description: "A simple way to apply a function to each element of an iterator is using the map function. It replaces the for loop which uses a lot of resources and variables and also takes longer to..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/map-function
---
A simple way to apply a function to each element of an iterator is using the map function. It replaces the for loop which uses a lot of resources and variables and also takes longer to execute.

Ilustration: map function that add 2 to each number of a list

```python
from math import sqrt
number = [9,2,20,14,7,8,34,91,43]
even_num = map(lambda x: x+2, number)
even_num = list(even_num)
```

```python
in: even_num
```

```python
out: [11, 4, 22, 16, 9, 10, 36, 93, 45]
```
