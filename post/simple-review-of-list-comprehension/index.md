---
title: "Simple Review of List Comprehension"
author: "Roshan Gyawali"
date: 2021-10-06
description: "The list comprehension feature is one of the most effective methods among several list creating methods provided by python. List Comprehensions are one-liners code, allowing to create lists from..."
categories: ["Python"]
image: images/d42fcb_4dc15f663e024901a55f22d432a1d295.webp
wix-url: https://www.datainsightonline.com/post/simple-review-of-list-comprehension
---
![](images/d42fcb_4dc15f663e024901a55f22d432a1d295.webp)

The list comprehension feature is one of the most effective methods among several list creating methods provided by python. List Comprehensions are one-liners code, allowing to create lists from Iterables. It really minimizes the line of code; let us understand from the below code:

###### Using traditional for loop for updating the content of list

```python
nums =[1,2,3,4,5]
squared_nums = []
for num in nums:
    squared_nums.append(num ** 2)

squared_nums
```

###### Generated Output: [1, 4, 9, 16, 25]

Now, lets see a one-liner code implementation: List Comprehensions.

###### Using one-liners code technique: List Comprehensions

```python
squared_nums = [num ** 2 for num in nums]
squared_nums
```

###### Generated Output: [1, 4, 9, 16, 25]

From the both techniques, we can be insightful, how efficient and powerful is list comprehension technique than the primitive for loop method, for updating the elements of list.

It was a quick preview of, why or how should we use list comprehensions. Now let's briefly talk about the syntax of it, using about example:

[*output expression*for *iterator variable* in *iterable*if *predicate expression*]

- *output expression:* *It determines the output expression that we are going to obtain from the operation.*
- for *iterator variable* in *iterable: It is the for loop expression that is similar to primitive foor loop expression.*
- if *predicate expression:* *It is a conditional statement for producing desired output.*

*Now let's discuss some advanced concept of the List Comprehension.*

**List comprehension with a condition:**

```python
# List Comprehension with a Condition
nums_list = [1, 2, 3, 4, 5]
squared_nums = [num ** 2 for num in nums_list if num % 2 == 0]
squared_nums
```

###### Genearated Output: [4, 16]

Here in this example, we have added a condition after the for loop expression. The condition states that, only square of those numbers will be calculated which are even. Furthermore, we can use more than a single condition to match with out expectation.

**List comprehension with multiple condition:**

```python
nums = [1, 2, 3, 4, 5]
squared_nums = [num * 2 for num in nums if num % 2 == 0 and num > 3]
squared_nums
```

###### Genearated Output: [8]

In this example we have added two conditions that, only squares of those numbers will be calculated which are greater than 3 and are even numbers.

List Comprehensions can also be used with strings and manipulated accordingly:

**List comprehension with strings:**

```python
given_string = 'list-comprehension'
single_letter = [letter for letter in string]
single_letter
```

###### Generated Output:

###### ['l', 'i', 's', 't', '-', 'c', 'o', 'm', 'p', 'r', 'e', 'h', 'e', 'n', 's', 'i', 'o', 'n']

**List comprehension with dictionaries:**

```python
numbers_dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
squared_keys = [k ** 2 for (k,v) in numbers_dictionary.items()]
squared_keys
```

###### Generated Output: [1, 4, 9, 16, 25]

List Comprehension can also be use with dictionaries like with strings. Here in the code we have our numbrs_dictionary which stores from number 1 to 5, with key value pair, key as a number and value as a string of those numbers in words. Finally The code above creates a list that consists of all dictionary keys, as a square.

In as nutshell, List Comprehension can be used in many more concepts. Here in this blog, we have discussed about some simple concepts as well as advanced use of List Comprehension.
