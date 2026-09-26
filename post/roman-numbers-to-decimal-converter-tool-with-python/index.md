---
title: "Roman numbers to decimal converter tool with Python"
author: "Abdi Tolesa"
date: 2021-09-21
description: "This article explains how we can build a tool than helps converting a Roman number to its equivalent decimal representation. Lets first see what the function look like and then chunk it down into..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/roman-numbers-to-decimal-converter-tool-with-python
---
This article explains how we can build a tool than helps converting a Roman number to its equivalent decimal representation. Lets first see what the function look like and then chunk it down into pieces and look at them in depth.

```python
    def roman_to_int(s):
        romans_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and romans_int[s[i]] > romans_int[s[i - 1]]:
                int_val += romans_int[s[i]] - 2 * romans_int[s[i - 1]]
            else:
                int_val += romans_int[s[i]]
        return int_val
```

The function accepts as an argument the roman number representation and returns the decimal equivalent by computing it.

First, the roman numbers are defined in a python dictionary as a {key: value} pair. The value of a particular dictionary can be accessed as dict[key], where key represents the position of the element in the dictionary. The python *range(n)* function creates a collection of numbers on the fly, from 0 to n-1. Using the python dictionary data structure and the built-in python functions like range() and len() - a function that returns the length of a value, the above code implements the logic behind the calculation of an integer representation for a given roman number.
