---
title: "Python App to Convert temperature in Fahrenheit to Celsius."
author: "Ahmed Shebl"
date: 2022-01-23
description: "I made a function that takes one argument (fah) which is the degree in Fahrenheitdef fah_to_cel(fah): # (32°F − 32) × 5/9 = 0°C cel = (fah -32) * 5 / 9 return celI used the equation of converting..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-app-to-convert-temperature-in-fahrenheit-to-celsius
---
I made a function that takes one argument (fah) which is the degree in Fahrenheit

```python
def fah_to_cel(fah):
    # (32°F − 32) × 5/9 = 0°C
    cel = (fah -32) * 5 / 9

    return cel
```

I used the equation of converting Fahrenheit to Celsius in the above function.

Then, I use **input()** funtion to get the temperature degree in Fahrenheit from user and and **flaot()** function to convert it from string to float, so I can use it in calculation in the function.

I put my code in **try...except** to check if the user input can be converted to float or not, and not crashed by wrong input data, if it can converted the program continue executing, if not it will print a message to the user.

Then I call my function with the user input to get the temperature in Celsius.

Finally I return the result which is the temperature degree in Celsius.

```python
print("Enter temperature in Fahrenheit")
try:
    fah = float(input())

    cel = fah_to_cel(fah)

    print("The temperature " + str(fah) + " in Fahrenheit = " + str(cel) + " in Celsius.")

except ValueError:
    print("The temperature degree you entered not a number")
```

The complete code is here:

```python
def fah_to_cel(fah):
    # (32°F − 32) × 5/9 = 0°C
    cel = (fah -32) * 5 / 9

    return cel

print("Enter temperature in Fahrenheit")
try:
    fah = float(input())

    cel = fah_to_cel(fah)

    print("The temperature " + str(fah) + " in Fahrenheit = " + str(cel) + " in Celsius.")

except ValueError:
    print("The temperature degree you entered not a number")
```
