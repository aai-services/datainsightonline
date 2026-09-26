---
title: "FUNCTIONS AND LOOPS IN PYTHON"
author: "ukaegbu daniel"
date: 2022-06-17
description: "Functions are vital concepts for all programming languages and sure python good list. Functions make your work as a programmer and data scientist easy saving you vital time and memory space..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/functions-and-loops-in-python
---
Functions are vital concepts for all programming languages and sure python good list. Functions make your work as a programmer and data scientist easy saving you vital time and memory space. Functions can be written by anyone and one function can be used by everybody so long as it serves such a programming purpose. This is what makes them very important in programming.

Functions are programs written to solve specific problems or tasks. Functions can take a single input or multiple inputs as arguments which may return or may not return a value once the task is completed. Python has two types of functions and they include:

**Built-in functions:** These are the types of functions that are integrated into the python programming language itself. You do not require to write them, you call them and they perform the task they were inscribed for. Examples of some of these functions are the max() which gets the maximum number in a list or tuple of numbers, and the sum() which gets the sum of numbers in a list or tuple.

**User- defined-function:**While some functions are built-in python, it may also excite you to know that you can write your functions and also modify them in a way that suits your programming needs. To understand this type of function, we will be working through writing a user-defined function at the end of this post but before we further let's understand the part of a function.

**A function Technically has 7 parts they are :**

1. The def Keyword: the def Keyword serves as a function header, it signifies that you are writing a function
2. The function name: every function has its unique name as no two function shares the same name. This helps in identifying a function and gives insight into the type of task the function performs. So do choose your function name carefully.
3. Parameters: the parameters are also known as arguments. They are the medium by which we pass Values or inputs into our functions. These arguments may be strings, booleans, numbers in form of args which are tuples, or awards which are direct objects.
4. The colon: This is used to signify and define the end of a function header.
5. Documentation: Also called docstrings they are optional but I do consider them necessary as they are an essential part of a function. The docstrings are written just after declaring the function. The doc string gives you vital information about the function. It tells you what specific task the function performs and the kind of input it accepts.
6. Statement: This is just the body of the function. It consists of indented lines of code that make up the function itself.
7. Return statement: the return statement returns some values when the function has performed its task and this is option

```python
      #First we import pandas
import pandas as pd
#next we define the function name using the def Keyword while signifying our parameter.
def load_data(file,num):
#we write a docstrings that gives us insight into the function
    """This function helps us load a CSV data and also helps us see the number of rolls of the data we want to see.its accepts two parameter({file:name of file,num:number of rolls we did like to see.})"""
#statment
    df=pd.read_csv(file)
    return df.head(num)
    # let's see if our function works.
df1=load_data('students_adaptability_level_online_education.CSV,10)

df1
#As you can see our function works perfectly fine.it has helped us load the data and also see 10 rolls of our dataset.
```

**LOOPS IN PYTHON**

Loops are a very important programming concept in python. Data science loops are very powerful tools for executing part of a data science project workflow such as data cleaning, data analysis, visualization, and even modeling. For loops are iterable Objects such as tuples, list Dictionaries, and sets which allow a similar action to be performed on every entity of the iterable object one at a time while returning them one after the other. The benefits of loops in data science cannot be over-emphasized they can help us iterate through voluminous columns and rolls of datasets to help us clean Visualize and analyze this data.

```python
#Here we created a list we can iterate over using for loops.
List=[1,2,3,5,6,9,12,16,11,4,8,10,15]
#using the for loop statement we can access every item in the list
for nums in List:
    print(nums)

#Using for loops we can print out all the number in the list

 9#We can multiply and  every item in the list by two
#but this expression has to be in the loop.
for nums in List:
    print(nums*2)
for nums in List:
#Here we tried dividing every item in the list by two
    print(nums/2)
```
