---
title: "Number Sum"
author: "Ebrima Sise"
date: 2022-05-03
description: "In this blog, I will write about a simple but interesting program I wrote to calculate the sum of all the numbers within a given range.I named the function `number_sum`. The function takes in a..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/number-sum
---
In this blog, I will write about a simple but interesting program I wrote to calculate the sum of all the numbers within a given range.

I named the function `number_sum`. The function takes in a positive integer and calculates the sum of all the numbers within that range.

Here is a quick glance at the function.

```python
def number_sum(num):
    '''
        A program that returns the sum of all the
        numbers within a given range
    '''

    # implement a try except block to catch errors for
      non integers

    try:

        if((num >= 1) & (type(num) == int)):

          numbers = [number for number in range(1, num + 1)]
          return sum(numbers)
        else:
          return 'Error: number provided should be 1 or greater'
     except:
       print("Only integers are allowed!")
```

The function first checks if the provided number is an integer and also greater than or equal to 1. If that is the case, it uses list comprehension

to store all the numbers in that range in a list. It then uses the python sum method to calculate the sum of all the numbers in the list.

If the value provided is a boolean, less than 1, or float, it returns an error message saying you should provide a number greater than 1 and an integer type.

If the value provided is not a number, the except block will throw an error message saying only integers are allowed!

The complete code with examples can be found on GitHub [here](https://github.com/siseebrima/DataInsight/blob/main/sum_number.ipynb).
