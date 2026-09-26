---
title: "Fahrenheit to Celsius Converter"
author: "Mahmoud Abdullah"
date: 2021-10-10
description: "How does it work? Generally to measure the temperature we make use of one of these two popular units i.e. Fahrenheit & Celsius.Converting one into another is usually boring and can be easily..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/fahrenheit-to-celsius-converter-1
---
## How does it work?

Generally to measure the temperature we make use of one of these two popular units i.e. **Fahrenheit** & **Celsius**.

Converting one into another is usually boring and can be easily automated. Today we will be building a simple & short project which will convert Fahrenheit to Celsius for us in seconds.

## Let's Code

So the first thing we are going to do is to ask the user for the temperature in **Fahrenheit** to convert it into the **Celsius**.

```python
temp = input("Enter temperature in Fahrenheit: ")
```

We will convert the temperature into float using **float()** so that we can perform calculations on it.

```python
temp = float(temp)
```

Now finally let's perform calculation and convert the temperature into Celsius.

```python
celsius = (temp - 32) * 5/9
```

This expression you see above is the general formula to convert Fahrenheit into Celsius.

Now finally let's print our temperature in Celsius:

```python
print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")
```

Here we go we are done! Here we have used **f-strings** to directly place the variable within the print statement.

Putting all together in a function:

```python
def fahrenheit_to_celsius():
    temp = input("Enter temperature in Fahrenheit: ")
    temp = float(temp)
    celsius = (temp - 32) * 5/9
    print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")
```

Let's try:

```python
>>> fahrenheit_to_celsius()
Enter temperature in Fahrenheit: 32
32.0 in Fahrenheit is equal to 0.0 in Celsius
```

Perfect!
