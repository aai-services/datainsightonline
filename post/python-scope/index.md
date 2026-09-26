---
title: "Python Scope"
author: "Mohamed Adel"
date: 2021-10-10
description: "A variable is only available from inside the region it is created. This is called scope.Local Scope A variable created inside a function belongs to the local scope of that function, and can only be..."
categories: ["Python"]
image: images/90add5_d66a6a3b53594cea8c6284b3a5558af3.webp
wix-url: https://www.datainsightonline.com/post/python-scope
---
A variable is only available from inside the region it is created. This is called **scope**.

![](images/90add5_d66a6a3b53594cea8c6284b3a5558af3.webp)

**Local Scope**

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

### Example

A variable created inside a function is available inside that function:

```python
def myfunc():
  x = 300
  print(x)
​
myfunc()

#output
300
```

## Function Inside Function

As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

### Example

The local variable can be accessed from a function within the function:

```python
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
​
myfunc()

#output
300
```

## Global Scope

A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local

### Example

A variable created outside of a function is global and can be used by anyone:

```python
x = 300
​
def myfunc():
  print(x)
​
myfunc()
​
print(x)

#outputs
300
300
```

## Naming Variables

If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

### Example

The function will print the local x, and then the code will print the global x:

```python
x = 300
​
def myfunc():
  x = 200
  print(x)
​
myfunc()
​
print(x)

#outputs
200
300
```

## Global Keyword

If you need to create a global variable but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

### Example

If you use the global keyword, the variable belongs to the global scope:

```python
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#output
300
```

Also, use the global keyword if you want to make a change to a global variable inside a function.

### Example

To change the value of a global variable inside a function, refer to the variable by using the global keyword:

```python
x = 300

def myfunc():
global x
  x = 200

myfunc()

print(x)

#output:
300
200
```
