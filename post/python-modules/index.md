---
title: "Python Modules"
author: "Teresa Rady"
date: 2021-10-04
description: "Have you ever played with Lego or built a house? Both activities have in common the notion that you have building blocks that you utilise to create your masterpiece.Well, now we will add Python to..."
categories: ["Python"]
image: images/8f2ac4_90514f5f388a45558f2bd11912c216cf.webp
wix-url: https://www.datainsightonline.com/post/python-modules
---
![](images/8f2ac4_90514f5f388a45558f2bd11912c216cf.webp)

Have you ever played with Lego or built a house? Both activities have in common the notion that you have building blocks that you utilise to create your masterpiece.

Well, now we will add Python to them through Python modules.

Modules are files that contain pre-defined Python statements and conditions. They form building blocks that one can use to divide the code into small manageable and reusable pieces.

Modules are two types:

1- Built-in : already exists as part of package or library.

2- User-defined : a set of functions and code created by the user for a custom use.

To start using any of the two types we import the module into the code. Let's have an example from a built-in module (math) which has the value of pi stored.

Calculate the circumference of a circle with radius = 5 cm

```python
import math
s = 5
area = math.pi * s * s
print(area)
78.53981633974483
```

Another example : Show the current date and time in your code.(Datetime module)

```python
import datetime
x = datetime.datetime.now()
print(x)
2021-10-04 12:04:34.217884
```

Check out the full list of Python standard modules in this [documentation link](https://docs.python.org/3/py-modindex.html).

Now Let's see how the user generated module works.

In a previous blog article I have written a function for a prank that I can use again as part of creating a game app. Check it out at this [link](https://www.datainsightonline.com/post/functions-in-python-2).

So now I will import the previous notebook with all its contents and then reuse the function that I have already coded before on a different name.

```python
!pip install ipynb
from ipynb.fs.full.Functionstutorialcheckpoint import *
greeter('Joy')
```

And here is the result:

```python
'Hello Joy I wanna play a game!'
```

Note that using an astrisk after import (import \*) means to import all the contents of the notebook. But If I only wanted to import a specific function, the code will be:

```python
from ipynb.fs.full.Functionstutorialcheckpoint import greeter
```

My module name 'greeter is a short name and can be reused, but if my module's name was saw_film_greeter_line i would definitely like to rename it for the ease of handling as follow:

```python
from ipynb.fs.full.Functionstutorialcheckpoint import greeter as gtr
```

We can do the same for pandas module:

```python
import pandas as pd
```

This minimizes the confusion and the typos while calling the functions.

To discover what are all the functions included under a certain module either built-in or user-generated, we use the dir() function.

```python
cr= dir(math)
print(cr)
```

This code snippet gives a list of all functions under the math module:

```python
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```

Now it is your turn to share what exciting modules do you work with in the comments section!
