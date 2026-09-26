---
title: "Python Classes"
author: "Omnia Sayed"
date: 2021-10-07
description: "Python is an “object-oriented programming language.” This means that almost all the code is implemented using a special construct called classes. Programmers use classes to keep related things..."
categories: ["Python"]
image: images/a9799b_06722c952aa94f6c832b70d4ceeba40a.webp
wix-url: https://www.datainsightonline.com/post/python-classes
---
![](images/a9799b_06722c952aa94f6c832b70d4ceeba40a.webp)

Python is an “object-oriented programming language.” This means that almost all the code is implemented using a special construct called classes. Programmers use classes to keep related things together. This is done using the keyword “class,” which is a grouping of object-oriented constructs.

**Define What is Class**

A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.

```python
Instance = class(arguments)
```

## How to create a class

The simplest class can be created using the class keyword. For example, let's create a simple, empty class with no functionalities.

```python
class ClassName:
    # Statement-1
    .
    .
    .
    # Statement-N
```

Example

Create a class named MyClass, with a property named x:

```python
class MyClass:
  x = 5
```

## Create Object

Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:

```python
p1 = MyClass()
print(p1.x)
```

## The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

## Accessing Attributes

You access the object's attributes using the dot operator with object. Class variable would be accessed using class name

Instead of using the normal statements to access attributes, you can use the following functions −

- The **getattr(obj, name[, default])** − to access the attribute of object.
- The **hasattr(obj,name)** − to check if an attribute exists or not.
- The **setattr(obj,name,value)** − to set an attribute. If attribute does not exist, then it would be created.
- The **delattr(obj, name)** − to delete an attribute.

```python
hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
delattr(empl, 'age')    # Delete attribute 'age'
```

## Built-In Class Attributes
Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −

- **__dict__** − Dictionary containing the class's namespace.
- **__doc__** − Class documentation string or none, if undefined.
- **__name__** − Class name.
- **__module__** − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
- **__bases__** − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
