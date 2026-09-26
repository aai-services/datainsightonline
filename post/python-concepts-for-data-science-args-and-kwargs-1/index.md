---
title: "Python Concepts for Data Science: *args and **kwargs"
author: "074bex435.ranjan"
date: 2021-10-06
description: "Function is an inevitable part in programming which reduces the redundant task to be performed. If the number of variables to be passed as function argument, then we can do it in normal way as:def..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-args-and-kwargs-1
---
Function is an inevitable part in programming which reduces the redundant task to be performed. If the number of variables to be passed as function argument, then we can do it in normal way as:

```python
def func(a,b,c):
    print("The statement is "+a+ " " + b + " " + c)
func("Data","Insight","Online")

Output
The statement is Data Insight Online
```

But if we don't know the number of function arguments, then we use special symbols as:

- \*args(Non-keyword argument)
- \*\*kwargs(Keyword argument)

## \*args
Keyword is not required while passing arguments. The arguments are passed as a tuple and these passed arguments make tuple inside the function with same name as the parameter excluding asterisk \*.

```python
def withArgs(*args):
    print(args)
withArgs(3,4,5)

Output
(3, 4, 5)
```

Here \*args is used but we can use anything instead of args but \* should be present before it. Example, \*num, \*dummy, etc.

## \*\*kwargs
If we want to pass keyword along with arguments, the \*\*kwargs is used. The arguments are passed as dictionary.

```python
def withKwargs(**foo):
    print(foo)
    for key, value in foo.items():
        print("Key={},Value={}".format(key,value))
withKwargs(name="abc",surname="def",gender="M")

Output
{'name': 'abc', 'surname': 'def', 'gender': 'M'} Key=name,Value=abc Key=surname,Value=def Key=gender,Value=M
```

As similar to \*args, we can use any dummy value after double asterisk(\*\*). Due to the dictionay nature, we accessed the values as key, value pair.

Code in github: <https://github.com/ranjan435/data-insight-2021/blob/assignment-2(Python-Concepts-for-Data-Science)/args%20and%20kwargs.ipynb>
