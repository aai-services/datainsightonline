---
title: "Multiplying all elements in list"
author: "Rawda Rumaieh"
date: 2021-10-10
description: "since “A Journey of a Thousand Miles Begins with a Single Step” understanding how to basically reach every element in a list and using it can be a salient step in many applications.it is not about..."
categories: ["Python"]
image: images/d96e14_0c2e74df75bd466ba2be51c71a79537d.webp
wix-url: https://www.datainsightonline.com/post/multiplying-all-elements-in-list
---
![](images/d96e14_0c2e74df75bd466ba2be51c71a79537d.webp)

since “A Journey of a Thousand Miles Begins with a Single Step”

understanding how to basically reach every element in a list and using it can be a salient step in many applications.

it is not about how simple a task is .. it is all about how can I use this task to build a masterpiece out of it.

here in my simple application I take a list and multiply every element of it then return the result

here is the code snippet

```python
#defining a function that takes a list
def multiply_all (my_list):
#defining the result as 1 so it gets multiplied by the first element
     product=1
 #looping over my list
    for i in my_list:
#multiplying the product with the current element in the list
   product=product*i
#returning the product
    return product
```
