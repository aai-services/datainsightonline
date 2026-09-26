---
title: "Beginners guide to starting python programming language"
author: "Blessing Oludele"
date: 2021-11-14
description: "While there are several programming languages available, python is considered very beginner-friendly which is why it is widely used. This tutorial will focus on introducing the readers to the basics..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/beginners-guide-to-starting-python-programming-language
---
While there are several programming languages available, python is considered very beginner-friendly which is why it is widely used. This tutorial will focus on introducing the readers to the basics in python; downloading the software, editors to use, data types, and creating simple functions.
A little disclaimer before proceeding; I have in no way explored all the options available, everything in this tutorial is what works for me and what I have learned from other tutorials and classes I have taken.

**Downloading the python software**: you can download the python software by clicking this link <https://www.python.org/downloads/>and then selecting the download appropriate for your system. After the download is complete, open the downloads folder and install it.

**Using python:** to use the python software you can work with the command-line interface or a graphic interface. A graphic interface will require you to download visual studio or some other software. For the sake of this tutorial, I will be exploring the command line interface.

To use python on the command line, open up windows cmd or Mac's terminal, change the directory to where you installed python by using 'cd', once you have gotten to the directory type python then press enter you'd see a little prompt '>>>' where you can enter python codes directly or run python scripts.

Just so you confirm python works you can type a simple mathematical operation after the prompt and press enter, the correct answers will be displayed. To close python-mode on the terminal you can type close() then press enter and it will return to the normal command-line interface.

**To write a script or not:** As I already mentioned the command line can run python code directly or run a python script, but why write a python script? A Python script is a file saved with '.py' Which contains a sequence of related statements to perform a specific task. So basically what this means is that if we want to execute several actions after one another we can combine them into a python script and run it at once. A script is used when processes need to be repeated to avoid typing out code severally into the python terminal. To write a python script we need an editor. Notepad and Microsoft word generally don't do the trick because python works with indentation and it is strenuous to manually add those indents. An editor that I found works well is the atom editor. It changes the python keywords to a different color and gives indentation to a new block of code. To download the atom editor visit the link <https://atom.io/>

**Basics of python**

**Data types:** python has several built-in data types which are as follows;

|  |  |  |
| --- | --- | --- |
| datatype | ​ | example |
| Text | String | x="Hello" |
| Numeric | int | x=5 |
| ​ | float | x=21.5 |
| ​ | complex | x=3j |
| Sequence | list | x=["people", "ball", "sherry"] |
| ​ | tuple | x=("people", "ball", "sherry") |
| ​ | range | x= range(10) |
| Mapping | dictionary | x={"name" : "Joan", "age" : 36} |
| Set | set | x={"people", "ball", "sherry"} |
| ​ | frozenset | x=frozenset({"people", "ball", "sherry"}) |
| Boolean | bool | x=True |

**Variables and Data Structures:** variables are like containers that can store a value, this value may be of any data type. In other programming languages like C, C++, variables have to be declared stating the types of value they will store before assigning a value but in Python, we don’t need to do that, Just assign a value to the variable then it will automatically know whether the value given would be an int, float, or char or even a String.

example assigning a value to a variable;

# Python program to declare variables

myvariable = 2

myvariable2 = 4.3

myvariable3 ="hello-world"

so automatically python knows that myvariable is an integer, myvariabler2 is a float and myvariable3 is a string, so anytime you refer to myvariable python automatically replaces it with 2 and so on. A variable can be changed at any point of the code by assigning another value to it and from that point in the code the variable value changes.

Python has 4 major built-in Data Structures which are; List, Dictionary, Tuple, and Set. They are briefly explained below;

A **list** is the most basic Data Structure in python. Items can be added to a list after the list has been created. The append() function is used to add data to the list. the list is accessed by the index of the item to be retrieved, the first item is the index 0 in python.

For example, to retrieve people in the list example we simple type print(x[0])

A **Dictionary** consists of key-value pairs. The values of a dictionary can be accessed by the specific key assigned to that value in the dictionary. For example, to retrieve Joan from the dictionary example we simply type print(x['name']).

A **tuple** is a sequence of immutable (in changeable); Python objects. Tuples are just like lists except tuples cannot be changed once declared. Tuples are usually faster than lists. A tuple is usually written within a parenthesis can be retrieved just as a list is.

A **Set** is a collection of data without a specific order, which is mutable and has no duplicate elements. The major advantage of using a set over a list is that it has a more efficient method for checking whether a specific element is contained in the set. unlike a list, set items cannot be accessed by referring to an index because their items are unordered. But you can loop through the set items using a ‘for’ loop, we can also check if a specified value is present in a set, by using the in keyword

**Simple python functions**

A function is a block of related statements designed to perform a specific task. The idea is to put some commonly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse the code contained in it over and over again.

Functions can be both built-in or user-defined. It helps the program to be concise, non-repetitive, and organized.

**examples of built-in functions are;**

|  |  |
| --- | --- |
| function | description |
| print() | it is used to display information to a screen |
| Len() | It provides the length of the object as an output |
| max() | It returns the largest number in the given iterable object |
| min() | It returns the minimum value from the values defined as arguments |
| list() | It is used to convert an object to a list object |
| round() | It gives an approximate/rounded value for a number. |
| ​abs(x) | It returns the absolute value of a number of the magnitude of a complex number. |

**user-defined functions**

When creating functions we use the ‘def‘ keyword.

the syntax is:

```python
def function-name(arguments):
            #function body
```

the arguments are values that the function may require to carry out the specific task. e.g. if you need to calculate the average age of some students you may require the list of the ages as an argument.

the function body contains the code to carry out the task.

example of a function to tell a user hello;

def hello():

print("hello user")

# this function has no argument.

to use a function in a script simply type out the function name providing argument if any. example calling the hello function.

hello()

the # symbol is used to add comments in between code to explain what the code is all about and make it generally more understandable. Python generally ignores everything written on the line after the # symbol.

I hope you feel more confident to dive deeper into python as this was a very basic introduction :), good luck!

**References**

- [W3schools python tutorial](https://www.w3schools.com/python/)

- [Python for everybody crash course](https://www.youtube.com/watch?v=8DvywoWv6fI)

- [Python 3 basics - GeeksforGeeks](https://www.geeksforgeeks.org/python-3-basics/?ref=rp)
