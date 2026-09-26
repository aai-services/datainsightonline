---
title: "Functions In Python"
author: "aya abdalsalam"
date: 2022-01-19
description: "Function created by keyword called def Add function Name which should be lower case and not python keywords and separate it by underscore"
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/functions-in-python-5
---
A function is a group of statements that performs a specific task and solve a specific problem. Functions help us to break our programs to smaller tasks. As our program grows larger and larger without using functions , functions make it more organized ,easy, small and manageable to be able to add and remove from it. in addition to , it avoids repetition and makes the code reusable. it help us to design or code and make it follow The principle of SOLID so make a function if you need it more than one time or in many places just call it and it will do what you need without repeating code.

## Steps To create function:

1 : Function created by keyword called **def**

2 : Add function Name which should be lower case and not python keywords and separate name with (_)underscore to make it easy to read

3 : Add **()** inside them we will add parameters

### Function should be called to be done
### Function called by its name followed by parenthesis
Let's define small function

```python
#function to add two numbers and return their sum
def add(firstParr, secdParr):
    result = firstParr + secdParr
    print("The sum of " + str(firstParr) +" and "+str(secdParr) + " is "+ str(result) )
#Taking input from user
x = int(input("Enter Your First Number "))
y = int(input("Enter Your Secend Number "))
#call function add with 2 parameters x and y
add(x, y)
```

```python
Enter Your First Number 5
Enter Your Secend Number 4
The sum of 5 and 4 is 9
```

**parameter vs argument**

They are the same ("information that passed to the function to be used in operations)

But their exist a small different between them,

Parameter is exist when declare function and Argument is the value passed to the function when it called

```python
# show difference between argument and parameter
def difference(x):
    print(x)
difference(x = "date")
#here x is the parameter and "date" is the argument
```

output:

```python
date
```

### Return statement
In function you can use return statement which mean you will use it again when call function in another function in the down code we make two functions functions 1: multiply which return multiply of two numbers and not print the result of them just return it 2: use_return function in it we use the return statement from multiply function rather code again or print two statement.

```python
def multiply(num1, num2):
    return num1 * num2

def use_return():
    num1 = int(input("Enter Your First Number "))
    num2 = int(input("Enter Your Secend Number "))
    result = multiply(num1,num2)
    print("The Result Of Multiply " +str(num1)+" and " +str(num2)+ " is " + str(result))
use_return()
```

```python
Enter Your First Number 6
Enter Your Secend Number 7
The Result Of Multiply 6 and 7 is 42
```

## Types of functions

#### Built-in functions
Functions that are built into Python which mean you can use it just by import as **sum, sqrt, ceil ,floor ,round and pow**

#### User-defined functions
Functions defined by the users themselves. this is as any function you type and call in python

```python
def import_biltIn_inUserDefiend_function():
    listA = [1, 2, 3, 4, 5, 7 ,27 , 25]
    print(sum(listA))
call_biltIn_inUserDefiend_function()
```
