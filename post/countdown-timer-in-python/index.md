---
title: "Countdown timer in Python"
author: "Abdi Tolesa"
date: 2021-09-22
description: "In this article, we are going to see how we can write a countdown timer with python. Lets first review the whole bunch of code and look deeper into each piece.import time def countdown(time_sec)..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/countdown-timer-in-python
---
In this article, we are going to see how we can write a countdown timer with python. Lets first review the whole bunch of code and look deeper into each piece.

```python
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")
```

So basically, the first statement imports the [time](https://docs.python.org/3/library/time.html) module which is shipped with Python. This module provides various time-related functions.

The function accepts an integer which is the time in seconds the functions starts counting down from. Out of the module's methods, the time.sleep function is used in this function to add an interval of 1 second before the next iteration is executed in the loop.

The other python built-in method used here is the [divmod()](https://docs.python.org/3/library/functions.html) function, which takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder. In our code, it is specifically used to calculate the minutes and second part of the function's output at each iteration.
