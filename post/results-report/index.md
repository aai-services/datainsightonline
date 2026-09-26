---
title: "Results report"
author: "sefako dorlote djaman"
date: 2021-09-04
description: "You have given a test to the students in your class. Now, you want to display their results. The first thing you need to do is to know the grade of each student. In input, this function will allow..."
categories: ["General"]
image: images/d10d7c_a48b247518ad455da2b07e3b8a46d7ac.webp
wix-url: https://www.datainsightonline.com/post/results-report
---
![](images/d10d7c_a48b247518ad455da2b07e3b8a46d7ac.webp)

You have given a test to the students in your class. Now, you want to display their results. The first thing you need to do is to know the grade of each student. In input, this function will allow you to see the results.

```python
# display results
def results():
    x = int(input("please insert your grade : "))
    if x > 20 :
        print('error')
    elif x < 10 :
        print('achievement level : failure')
    elif x <= 12 :
        print('achievement level : passable')
    elif x <=14 :
        print('achievement level : satisfactory')
    elif x <= 16 :
        print('achievement level : good')
    elif x <= 18 :
        print('achievement level : very good')
    else :
        print('achievement level : excellent')
```

To set the variable x, the student will have to insert his grade. The results will then be displayed.

This is an example of a test performed using the code above for an student :

```python
# input
results()
```

After writing the results function, a line appears to indicate the score. Then we will have the output below:

```python
# output
please insert your grade : 15
achievement level : good
```

So this student has**good** as achievement level.
