---
title: "Convert temperature in Fahrenheit to Celsius."
author: "amrali150"
date: 2022-01-23
description: "Fahrenheit to CelsiusIn order to convert Fahrenheit to Celsius, we use the formula, °C = (°F - 32) × 5/9, in which the value of the temperature in Fahrenheit is placed and we get the value in..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/convert-temperature-in-fahrenheit-to-celsius-1
---
## Fahrenheit to Celsius
In order to convert **Fahrenheit to Celsius**, we use the formula, °C = (°F - 32) × 5/9, in which the value of the temperature in Fahrenheit is placed and we get the value in Celsius. Fahrenheit and Celsius are the scales that are used to measure temperature. In this lesson, we will be learning about the Fahrenheit to Celsius formula and the method by which we convert Fahrenheit to Celsius.

Where,

- C = Measure of temperature in degree Celsius (°C).
- F = Measure of temperature in degree Fahrenheit (°F).

now we will start by taking an input from user, we will ask for the temperature in Fahrenheit.

```python
f = input("Write the temperature in Fahrenheit\n")
```

Output is:

then, the variable " f " is a string as we will convert it to float so we can apply the law of conversion.

```python
f = float(f)
```

then, we will apply the law to convert Fahrenheit to Celsius.

```python
c = (f - 32) * 5/9
```

finally print the result in Celsius

```python
print("the temperature in Celsius is ", c)
```

Output is:

```python
the temperature in Celsius is  5.0
```
