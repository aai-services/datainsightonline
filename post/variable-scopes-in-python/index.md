---
title: "Variable Scopes in Python"
author: "Ebrima Sise"
date: 2022-05-04
description: "In python, a variable is only accessible from inside the area it has been created in. The term `Scope` is used to describe this logic.A variable can be in one of these types of scopes:- Local Scope-..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/variable-scopes-in-python
---
In python, a variable is only accessible from inside the area it has been created in. The term `Scope` is used to describe this logic.

A variable can be in one of these types of scopes:

- Local Scope

- Global Scope

- Built-in Scope

## Local Scope

In this case, the variable can only be accessible within the code block it's declared

For example, take a look at the variable `a` in the following function.

```python
def func():
    a = 10
    print(a)
```

`a` is only accessible from within this function. If you try to access `a` outside this function, the program is going to throw a NameError.

## Global Scope

If a variable is created in the main body of the python code, it is considered to have a global scope. This makes it accessible from anywhere in the program.

For example, the code below illustrates this logic.

```python
x = 10

def test_func():
    print(x)

test_func()
print(x)
```

```python
output:
10
10
```

From the results above, it is evident that indeed variable `x` is accessible from anywhere in the program.

## Built-in Scope
This is actually considered the widest scope in the python programming language. All reserved names in python have a built-in scope. Variables/names in this scope can be accessed from anywhere in the program without the need to declare them.

Maybe an example will go a long way in explaining this.

```python
b = 99.9
b = int(b)
print(type(b))
print(b)
```

output:

```python
<class 'int'>
99
```

In the example above, the functions int(), print() and type() all have built in scope.

If we declare variables with the same name in different scopes. The local scope will use the local variable instead of the global one.

We can use the `global` keyword before the variable name if we want the opposite of the above.

We can use the `nonlocal` keyword to accomplish something similar to the `global`.
