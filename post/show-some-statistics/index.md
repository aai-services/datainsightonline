---
title: "show some statistics"
author: "Ahmed Shebl"
date: 2022-01-23
description: "In this code, I didn't use built in function for statistics.I made two function that takes a list argument: 1 - list_average(lst) --> take a list and return the average.def list_average(lst): total =..."
categories: ["Statistics"]
wix-url: https://www.datainsightonline.com/post/show-some-statistics
---
In this code, I didn't use built in function for statistics.

I made two function that takes a list argument:

1 - list_average(lst) --> take a list and return the average.

```python
def list_average(lst):
    total = 0
    for item in lst:
        total += item

    count_items = len(lst)

    return total / count_items
```

2 - list_max_min(lst) --> take a list and return the max and min items.

```python
def list_max_min(lst):
    max_item = lst[0]
    min_item = lst[0]
    for item in lst:
        if item > max_item:
            max_item = item
        elif item < min_item:
            min_item = item

    return max_item, min_item
```

Then I take the input from user as numbers separated by spaces, and converted it to list

```python
print("Enter numbers separated by space between them: ")
lst = input().split(' ')
```

Then to be sure no error arise, in a for loop I created two lists:

one for numeric values, and the other for wrong values which is not numeric.

```python
for item in lst:
    try:
        lst_numeric.append(float(item))
    except ValueError:
        lst_not_numeric.append(item)
```

Then I call the functions I created to calcualate statistics.

```python
list_count = len(lst_numeric)
list_average = list_average(lst_numeric)
list_max, list_min = list_max_min(lst_numeric)
```

Finally, I print the numeric values and their statistics, and if there are wrong values entered by the user, I print them in separate lines.

```python
print("the numbers: ")
print(lst_numeric)
print("has theses statistics:")
print("---------------------")
print("count:   " + str(list_count))
print("average: " + str(list_average))
print("max:     " + str(list_max))
print("min:     " + str(list_min))
if len(lst_not_numeric) > 0:
    print("Note that you entered these wrong type input:")
    print("---------------------------------------------")
    print(lst_not_numeric)
```

The complete code is here:
