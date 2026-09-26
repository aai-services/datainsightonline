---
title: "Functions in Python"
author: "Marehan Refaat"
date: 2022-02-06
description: "A function is a block of code which only runs when it is called.You can pass data, known as parameters, into a function.A function can return data as a result.Creating a FunctionIn Python a function..."
categories: ["Python"]
image: images/d86598_627afb4622024659a3e8bf6786cd1d5d.webp
wix-url: https://www.datainsightonline.com/post/functions-in-python-7
---
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

## Creating a Function
In Python a function is defined using the def keyword:

```python
def my_function():
  print("Hello from a function")
```

## Calling a Function
To call a function, use the function name followed by parenthesis:

```python
my_function()
Hello from a function
```

## Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

```python
def my_function(input_sample):
  print(input_sample + " Office")
my_function("Big")
my_function("Small")
```

```python
Big Office
Small Office
```

The terms *parameter* and *argument* can be used for the same thing: information that are passed into a function.

## Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

```python
def my_function(input_1,input_2):
  print(input_1 + " " + input_2)

my_function("Big", "Office")
```

```python
Big Office
```

## Arbitrary Arguments, \*args
If you do not know how many arguments that will be passed into your function, add a \* before the parameter name in the function definition.

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Ahmed", "Ali", "Manar")
The youngest child is Manar
```

**Keyword Arguments**

You can also send arguments with the *key* = *value* syntax.

```python
This way the order of the arguments does not matter

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Ahmed", child2 = "Ali", child3 = "Manar")
The youngest child is Manar
```

## Arbitrary Keyword Arguments, \*\*kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: \*\* before the parameter name in the function definition.

```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Mohamed", lname = "Ali")
His last name is Ali
```

## Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

I am from Sweden
I am from India
I am from Norway
I am from Brazil
```

## Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
apple
banana
cherry
```

## Return Values
To let a function return a value, use the return statement:

```python
def my_function(input_sample):
  return 10*input_sample

print(my_function(2))
print(my_function(7))
print(my_function(5))
20
70
50
```

## The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

```python
def myfunction():
  pass
```

You can refer to the code from [here](https://github.com/MarehanRefaat/Python_Functions/blob/main/Python_Functions.ipynb)
