---
title: "building an Fahrenheit to Celsius Converter"
author: "Nehal Sherif"
date: 2021-09-22
description: "today we will be building a Fahrenheit to Celsius Converter in Python.Generally to measure the temperature we make use of one of these two popular Fahrenheit & Celsius.Converting one into another is..."
categories: ["General"]
image: images/472975_d605f43530984f4f9d9cb691b39db924.webp
wix-url: https://www.datainsightonline.com/post/building-an-fahrenheit-to-celsius-converter
---
today we will be building a Fahrenheit to Celsius Converter in Python.

Generally to measure the temperature we make use of one of these two popular Fahrenheit & Celsius.

Converting one into another is usually boring and can be easily automated. Today we will be building a simple & short project which will convert Fahrenheit to Celsius for us in seconds.

So the first thing we are going to do is to ask the user for the temperature in Fahrenheit to convert it into the Celsius.

```python
temp = float(input("Enter temperature in Fahrenheit: "))
```

We will convert the temperature into float using float() so that we can perform calculations on it.

```python
celsius = (temp - 32) * 5/9
```

This expression you see above is the general formula to convert Fahrenheit into Celsius.

let's print our temperature in Celsius:

```python
print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")
```

user input is 6:

```python
Enter temperature in Fahrenheit: 6
```

output:

```python
6.0 in Fahrenheit is equal to -14.444444444444445 in Celsius
```
