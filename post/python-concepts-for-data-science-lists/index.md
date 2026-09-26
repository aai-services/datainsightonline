---
title: "Python Concepts for Data Science: Lists"
author: "abdelrahman.shaban7000"
date: 2021-09-22
description: "In this blog we will discuss about \"Lists\" which is important data structure in python to store multiple elements in one variable, also it is mutable so you can change it's elements as you want.Lists..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-lists
---
In this blog we will discuss about **"Lists"** which is important data structure in python to store multiple elements in one variable, also it is mutable so you can change it's elements as you want.

Lists are created using square brackets:

```python
my_list=[1,2,3,4,5]
```

Note that **Lists** can contain different data types like strings, integers, floats and so on.

**List elements**

one characteristic for list items is that they are ordered so each element has certain order number and we can access elements using indices according to that order number. List items are indexed and they begin with zero as follows:

```python
my_list=['banana','apple','orange','cherry']
print(my_list[0])
print(my_list[2])
print(my_list[-1])
```

```python
banana
orange
cherry
```

Also as we saw if we use -1 as index it returns the last element and -2 returns the second to last element and so on.

In addition to that we can use range of indices to specify the start index and where we should stop ( with the start index included but the last index excluded) and the result will be as follows:

```python
my_list=['mango','apple','orange','banana','cherry','melon']
print(my_list[1:4])
print(my_list[:3])
```

```python
['apple','orange','banana']
['mango','apple','orange']
```

In the last example we leave the start index empty and just specified the last index so it will start from the beginning of the list. The same thing also applies if we leave the end index empty, it will include up to the last element.

_____________________________________________

Let's write a simple app using lists for more illustration:

```python
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_nums=[]
even_nums=[]
```

Here we create a list of 20 numbers and 2 other empty lists for odd and even numbers.

```python
for i in nums:
    if i %2==0:
        even_nums.append(i)
    else:
        odd_nums.append(i)
```

In the code above we loop over the previous list **'*****nums*****'** and if the number is odd we add it to the list ***odd_nums.*** If the number is even we add it to ***even_nums***list.

Note that we added the number to the empty lists using the ***append***method*.*

Link to GitHub repo [here](https://github.com/Abdelrahman7000/Python_Concepts_for_data_science_Lists)
