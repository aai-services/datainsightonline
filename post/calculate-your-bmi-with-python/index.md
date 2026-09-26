---
title: "Calculate Your BMI with Python"
author: "Sadekeen"
date: 2021-09-26
description: "Writing a program in python is easy yet confusing. The simpler the language the complex it is sometimes to handle. But simply python is more of a language for everyone and it's sometimes easier to..."
categories: ["Python"]
image: images/6f95f0_2bc98b3c91984e0eb2f8bb765d6a47bd.webp
wix-url: https://www.datainsightonline.com/post/calculate-your-bmi-with-python
---
![](images/6f95f0_2bc98b3c91984e0eb2f8bb765d6a47bd.webp)

Writing a program in python is easy yet confusing. The simpler the language the complex it is sometimes to handle. But simply python is more of a language for everyone and it's sometimes easier to decode.

"

I did programming with C, C++ basically. I find python understandable but difficult to write. Thanks to the huge community of python, there's always solution available. "

For calculating BMI the first thing to notice is the input of the value. By default the input type is str, so the typecasting was required .

```python
#check the input type
x=input()
print(type(x)) #<class 'str'>
```

```python
h = float(input("Enter an Height in (m): "))
w = float(input("Enter an Weight in kg: "))
```

Secondly the formula was written and lastly I had to compare the result for the condition of the health.

![](images/6f95f0_a0c20b67aa2544438e693bb834a95f18.webp)

```python
BMI= w/(h*h)
```

```python
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
```
