---
title: "Functions of a Python Function"
author: "Joana Owusu-Appiah"
date: 2021-11-13
description: "Have you ever wondered how cavemen managed to do simple activities without the use of tools? I am sure the majority of the cutting and trimming was done with their hands and teeth. Civilization just..."
categories: ["Python"]
image: images/b8e7be_479691b39b1b4d1ba23c52ec201ae361.webp
wix-url: https://www.datainsightonline.com/post/functions-of-a-python-function
---
![](images/b8e7be_479691b39b1b4d1ba23c52ec201ae361.webp)

Have you ever wondered how cavemen managed to do simple activities without the use of tools? I am sure the majority of the cutting and trimming was done with their hands and teeth. Civilization just hands over the knife, which would subsequently **function** just like the teeth or hand, but more conveniently.

The same concept is true for Python functions. The code blocks that you need to utilize repeatedly can be specified explicitly once and then called upon whenever needed. *C'est tres simple!*

Today's post focuses on Python Functions with simple and easy-to-follow code examples. We will cover:

Functions

**Types of Functions**

1. Built-in Functions
2. - User-defined Functions

- Syntax :

- Function name

- Body

- Return statements

- Parameters

- Naming and Calling Functions

- Scope of a Variable

3. Lambda Functions

Stay with me...

A **function** is a named code block designed to perform a specific task. The main essence of a function is to circumvent typing the same blocks of code repetitively, thus making a program easier to read, write, test, and fix. What is the function of a **function** in a code block?

**Functions of a Function**

1. Displays information
2. Processes data and returns a set of values.

**Types of Functions:**

1. Built-in Functions
2. User-Defined functions
3. Empty Functions
4. Lambda Functions\*

Trust me, you started using functions long before you even knew they existed. If the print ('Hello World!') looks familiar? Then that was you using functions!

### 1. Built-in Functions
Built-in functions have their functionalities pre-defined in Python. And so the len() function returns the length of a sequence, and the famous print() function outputs specified strings that have been passed. The help() function outputs information on all the built-in functions once you pass them. For example,

```python
# information on sum() function

help (sum)
```

```python
<output>  Help on built-in function sum in module builtins: sum(iterable, 		      start=0, /)  Return the sum of a 'start' value (default: 0) plus an iterable of numbers  .When the iterable is empty, return the start value.  This function is intended specifically for use with numeric values and may reject non-numeric types.

```

### 2. **User-Defined Functions**

User-defined functions are created by the user. The power of open-source, right? This feature enables users to customize and implement functions. Declaring a user-defined function requires;

*a* ***def*** *keyword*, *function name*, *the body*, and an *optional return statement.*

Syntax of a user-defined function,

```python
 def function_name(parameter):
 """Docstring."""
     Body
     return statement  # this is optional
```

###### **Applying the user-defined concept**, this code defines a function *display_message* and takes a parameter *learning.*

```python
# defining a function display_message

def display_message(learning):
  print('Hello People, I am learning ', learning)
```

### A breakdown of the syntax:

#### - The ***def*** keyword:

The def keyword informs python of your intent to define a function.

#### - The function_name:

The function name identifies the function. To get the most out of functions, there are a few conventions to note on the naming of functions. These concepts apply to naming variables in python too! (FYI);

- Function names should be lowercase, with words separated by underscores as necessary to improve readability.
- Variable names follow the same convention as function names.
- mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backward compatibility. \*

#### - Docstring:

The docstring is your backup note, should you forget the use of the function you defined. It explains the task the function is supposed to execute, and Python uses it to create the documentation for your function.

#### - The body:

The body is the block of code that will be executed. The body is defined by an indentation. Python automatically does the indentation for you if you declare the function name with a colon after the parenthesis.

#### - An optional return statement:

The return statement is used within a function. Every function returns something and in the absence of a return statement, python returns a **None** object. If the return keyword is followed by an expression, the expression is executed first and the value is returned.

What could be the difference between the print statement and the return statement?

> The print statement shows the user a string representing what the computer is running. The string at that point is of no use to the computer. The return statement, on the other hand, gives back a value that is typically unseen by the user but will be used by the computer in subsequent computations.

How can functions be used after their initial declaration? We simply call them!

### Calling Functions

During a function call, what happens is that Python runs your call through the function you have defined and applies the task specified in the body of the code. The syntax of a function call is,

```python
function_name(‘argument’)
```

Let's call our function *display_message* and specify an argument *'Introduction to Data Visualisation with Seaborn'*

```python
display_message('Introduction to Data Visualisation with Seaborn')
```

```python
<output> Hello People, I am learning  Introduction to Data Visualisation with Seaborn
```

Notice I have not spoken about **parameters** in the defined function's parenthesis...

#### - Parameters

The parameter specifies the information the function needs to execute the block of code. The new input that the user specifies when calling the function is an **argument**. (Some people use the parameter and argument interchangeably, but we define a function with a parameter and pass **arguments** through the function call).

A function could have multiple parameters. In that case, there has to be a **way** of calling the functions with arguments to ensure a smooth-running code. We will find out about the methods but let's look at how a function with multiple parameters would look like.

```python
def make_shirt(size, shirt_inscription):
  print('You chose a', size, '-sized shirt', 'with the inscription: ', shirt_inscription )
```

Function *make_shirt* accepts two parameters, the *size*, and *shirt_inscription*

Now we learn how to call the functions with multiple parameters. through:

##### 1. Positional arguments:

Calling functions using positional arguments considers the order in which the parameters were declared and follows suit. If either of the arguments is positioned wrongly, the program will return a wrong output or in instances where the parameters have different data types, Python will throw an error message. Let's pass arguments to the function *shirt,*

```python
def shirt(size, shirt_inscription):
  print('Your shirt size is, ', size, 'with the inscription: ')
```

```python
<output> You chose a medium-sized shirt with the inscription:  They that wait
```

##### 2. Keyword argument:

The keyword argument solves the need for order when passing arguments, as in the positional method. A keyword argument is a name-value pair that is passed to a function. The name is the parameter and the value is the argument. Although the order does not matter here, the user must remember the exact name of the parameter defined originally.

Using the keyword argument would look like this,

```python
# using the keyword argument
make_shirt(size='Medium', shirt_inscription='They That Wait')
```

```python
<output> You chose a Medium-sized shirt with the inscription:  They That Wait
```

##### 3. Default values:

Defining functions with few parameters is ideal as it limits the occurrence of errors. A good way to limit errors even with multiple parameters is to use default values. Some arguments may recur in a program, the user could set the parameter to that value while defining the function.

For context, we define another function *making_shirt.* This company of interest, presumably in a Python Community has almost all its clients requesting large shirts as well a common inscription professing their love for the language... we set the parameters to '*large*' and 'I love python' when declaring the function making_shirt. And it looks like this,

```python
# using default values
def making_shirt(size='Large', inscription='I love Python'):
  print('You chose a', size, '-sized shirt', 'with the inscription:', inscription)
```

We call the function *making_shirt()* with,

```python
making_shirt()
```

and it outputs,

```python
You chose a Large-sized shirt with the inscription: I love Python
```

A few things to note:

***NB****: the parameters that would require default values should come after the parameters without the default values. Within a program, if there is a need to deviate from the default value stated in the definition, you only have to reassign it.*

*For the first part of the note, the parameters without default values should* precede *the ones with default values.*

```python
def get_formated_names(first, surname, middle_name=' '):
```

Second part,

```python
# here we print a medium shirt but with the default inscription
# specified with the making_shirt function

making_shirt(size='Medium')
```

### Flexible Arguments

When we are not sure of the number of arguments a user would want to pass, we define functions with flexible parameters. Python supports the concept of any number of arguments or keyword arguments. There are two of these special function elements:

**- ( \*args)**: Represents an arbitrary number of arguments, it turns all the arguments passed to a function call into a tuple called ***args*** in the function body.

Check out this use case,

```python
def add_all(*args):
  """ Sum all values in *args together. """

  # initiate the sum
  sum_all = 0

  # accumulate the sum
  for num in args:
    sum_all += num

  return sum_all
```

Calling the function add_all here,

```python
add_all(1)
```

we get the output,

```python
<output> 1
```

- (\*\*kwargs): Represents an arbitrary number of keyword arguments preceded by identifiers. **\*\*kwargs** turns the identifier keyword-pairs into a dictionary within the function body. For example,

```python
# ** Kwargs

def print_all(**kwargs):
  """ Print out the key-value pairs"""
  print(kwargs)
```

We call the \*\*kwarg defined function here.

```python
print_all(one=1, two=2, three=3)
```

```python
<output> {'one': 1, 'two': 2, 'three': 3}
```

The most important thing to note is that with flexible arguments, you only need to declare the parameter with \* or \*\*, the args and kwargs are just arbitrary keywords by convention.

### Scope
The scope specifies the part of a project that a name, an object, or a variable may be accessed. There exist a **global**, **local**, and **built-in** scope.

- **Local scope**: A local scope variable is defined inside the body of a function and only accessible within the function. Once the execution of the code is over, the variables cease to exist.

- **Global scope**: The global scope variable is defined in the **main body** of a script and can be accessed anywhere within the program

The code snippet below gives a case scenario of the global and local variables.

```python
age = 30 # Global variable

def get_full_name(first, surname):
  full_name = first + ' ' + surname  # fullname is a local variable
  print("Age: " , age)
  print("Full name is: " , full_name) # prints the statements within the function
```

When the function get_full_name is called,

```python
get_full_name('Joana', 'Owusu-Appiah') # both the age would be printed
```

```python
<output>
Age:  30
Full name is:  Joana Owusu-Appiah
```

However, when we decide to call both of the variables full_name and age outside the function get_full_name, let's see what happens.

```python
print("Age: " , age)
print("Full name is : " , full_name)
```

An error message is thrown...

```python
Age:  30
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-19-c9d93c003ac3> in <module>()      1 print("Age: " , age)----> 2 print("Full name is : " , full_name)
NameError: name 'full_name' is not defined
```

it could not print *full_name* because it is a local variable and cannot be called outside the function.

### 3. Lambda Functions

Lambda functions provide a quick way and potentially dirty way of writing functions using the keyword **lambda.** It follows the syntax,

```python
lambda args1, args2: expression
```

Potentially dirty because the Zen of python is heavy on code readability and so when there are a lot of arguments, it makes the code messy. Use lambda functions only when you need to quickly use a function perhaps just once. Example,

```python
# defined without names

raise_power = lambda x,y : x**y
```

Calling the function *raise_power,*

```python
raise_power(2, 3)
```

```python
<output> 8
```

However, there is a very useful function called the **map** function which takes two arguments, a **function**, and a **sequence**, and applies the function over all the elements in the sequence.

```python
nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num**2, nums)
print(square_all)
```

The above would show that the variable *square_all* is a map object.

```python
output:
<map object at 0x7f88611a1690>
```

we now convert the map object into a list and print it.

```python
print(list(square_all))
```

```python
<output> [2304, 36, 81, 441, 1]
```

I used code examples to demonstrate my understanding of Python functions throughout this post. I hope it helps you appreciate working with user-defined python functions.

Keep Learning!

**Reference materials**

1. Python 101 - Michael Driscoll
2. Python Crash course - Eric Matthes
3. https://www.dummies.com/programming/python/how-to-name-functions-in-python/
4. <https://www.python.org/dev/peps/pep-0008/#naming-conventions> - PSF(Python Software Foundation) Style Guide for Python Code
5. <https://www.datacamp.com/community/tutorials/functions-python-tutorial>
6. Check out the [Datacamp Data Science Toolbox (Part 1) course](https://campus.datacamp.com/courses/python-data-science-toolbox-part-1/writing-your-own-functions?ex=1)
7. Access the entire notebook with additional code samples on [my](https://github.com/Joana-Mansa/tutorial_functions) Github.
