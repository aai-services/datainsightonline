---
title: "Fahrenheit to Celsius Conversion"
author: "Arpan Sapkota"
date: 2021-09-21
description: "For the conversion of temperature from Fahrenheit to Celsius first thing we are going to do is to ask the user for the temperature in Fahrenheit.We will convert the temperature into float using..."
categories: ["General"]
image: images/a8b2bc_de7fe529bbb3426fb96dbfac79d80d49.webp
wix-url: https://www.datainsightonline.com/post/fahrenheit-to-celsius-conversion
---
![](images/a8b2bc_de7fe529bbb3426fb96dbfac79d80d49.webp)

For the conversion of temperature from Fahrenheit to Celsius first thing we are going to do is to ask the user for the temperature in Fahrenheit.

We will convert the temperature into float using float() so that we can perform calculations on it.

```python
temp = float(input("Enter Temperature in Fahrenheit:"))
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

Here we go we are done! Here we have used f-strings to directly place the variable within the print statement.
