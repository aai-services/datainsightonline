---
title: "Python Concepts for Data Science: Functions"
author: "Caleb Atiemo - Keseku"
date: 2021-10-03
description: "In programming, as we start to solve more complex programs we start to notice we often have to repeat the same set of steps in many different places in our program.Let us imagine we were building an..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-functions-1
---
In programming, as we start to solve more complex programs we start to notice we often have to repeat the same set of steps in many different places in our program.

Let us imagine we were building an application to help business owners take inventory at the end of the day. Calculating the remaining stock, a simple procedure could look like this:

1. Establish your initial stock and stock sold
2. Calculate the difference
3. Return the remaining stock

These three steps will be executed every time a business owner wants to calculate the remaining stock at the end of the day using our application. In our program, we could rewrite the same procedures over and over (and over) for each time we want to calculate the remaining stock, but there’s a better way. Python gives us a useful concept called *functions*.

Functions are a convenient way to group our code into reusable blocks. A function contains a sequence of steps that can be performed repeatedly throughout a program without having to repeat the process of writing the same code again. In this post, we are going to explore the idea of a function by slowly building out a Python program for our remaining stock calculation steps.

Let’s come back to the remaining stock application. If we were to convert our steps defined earlier into Python code, a very simple version that calculates the remaining stock at the end of each day of a week might look like this:

```python
#Day 1
initial_stock = 50234
stock_sold = 2342
remaining_stock = initial_stock - stock_sold
print('The remaining stock is ' + str(remaining_stock))

#Day 2
initial_stock = 47892
stock_sold = 2142
remaining_stock = initial_stock - stock_sold
print('The remaining stock is ' + str(remaining_stock))

#Day 3
initial_stock = 45750
stock_sold = 2002
remaining_stock = initial_stock - stock_sold
print('The remaining stock is ' + str(remaining_stock))

#Day 4
initial_stock = 43748
stock_sold = 2912
remaining_stock = initial_stock - stock_sold
print('The remaining stock is ' + str(remaining_stock))

#Day 5
initial_stock = 40836
stock_sold = 1942
remaining_stock = initial_stock - stock_sold
print('The remaining stock is ' + str(remaining_stock))
```

Anytime our business friend wants to calculate his remaining stock he would need to run these lines of code over and over again but a function makes things handy here.

A *function* consists of many parts, so let’s first get familiar with its core. Here’s an example of a function definition:

```python
def function_name(parameter):
  # functions tasks go here():
  return result
```

There are some key components we want to note here:

- The def keyword indicates the beginning of a function (also known as a function header). The function header is followed by a name that describes the task the function performs. It’s best practice to give your functions a descriptive yet concise name.
- Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters. Function parameters allow our function to accept data as an input value.
- A colon : to mark the end of the function header.
- One or more valid python statements that make up the function body. The code inside a function must be indented to show that they are part of the function.
- Functions can also *return* a value to the program so that this value can be modified or used later. We use the Python keyword return to do this.

Following this, our function to calculate the daily remaining stock will take this form:

```python
def stock_calculator(initial_stock, stock_sold):
    remaining_stock = initial_stock - stock_sold
    return 'The remaining stock is ' + str(remaining_stock)
```

We utilize the function by calling it. This is done by typing the name of the function and passing an argument in the parenthesis. The argument is assigned to the parameter in the function.

```python
day_1 = stock_calculator(50234, 2342)
print(day_1)
```

Here is a [link](https://github.com/catiemokeseku/Functions.git) to the code on Github
