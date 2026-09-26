---
title: "Converting Fahrenheit to Celsius with Python"
author: "Alberta Johnson"
date: 2021-09-22
description: "Looking to change Fahrenheit to Celsius or Celsius to Fahrenheit? I'm going to talk on how to Covert Temperature that is from Fahrenheit to Celsius. The Fahrenheit scale is a temperature scale based..."
categories: ["Python"]
image: images/1fa3fb_ad30d302385644db837318a20bc9bddc.webp
wix-url: https://www.datainsightonline.com/post/converting-fahrenheit-to-celsius
---
![](images/1fa3fb_ad30d302385644db837318a20bc9bddc.webp)

Looking to change **Fahrenheit to Celsius** or **Celsius to Fahrenheit**?

I'm going to talk on how to Covert Temperature that is from Fahrenheit to Celsius.

The **Fahrenheit scale** is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit (1686–1736). It uses the **degree Fahrenheit** (symbol: **°F**) as the unit. In the Fahrenheit scale, water freezes at 32 degrees, and boils at 212 degrees.

The **degree Celsius** is a unit of temperature on the **Celsius scale**, a temperature scale originally known as the **centigrade scale.** The degree Celsius (symbol: **°C**) can refer to a specific temperature on the Celsius scale or a unit to indicate a difference or range between two temperatures. It is named after the Swedish astronomer Anders Celsius (1701–1744), who developed a similar temperature scale.

### F° TO C°: FAHRENHEIT TO CELSIUS CONVERSION FORMULA

To convert temperatures in degrees Fahrenheit to Celsius, subtract 32 and multiply by .5556 (or 5/9).

- Example: (50°F - 32) x .5556 = 10°C

Now let's consider a simple converter app, written in Python language.

# A function to convert Fahrenheit to degree Celsius

def temperature converter(Fahrenheit):

Input the temperature to convert to Celsius

Fahrenheit to Celsius

°C = (°F – 32) x 5/9

Celsius to Fahrenheit

Fahrenheit = 9.0/5.0 \* Celsius + 32

```python
Celsius = (Fahrenheit - 32) * 5.0/9.0
```

```python
 Celsius = np.round(Celsius,2)
```

```python
return '{} Fahrenheit is equivalent to {} Degree Celsius'.format(Fahrenheit,Celsius)
```

# Invoke the function

```python
temperature_converter(2)
```

Output displayed

```python
'2 Fahrenheit is equivalent to -16.67 Degree Celsius'
```

In conclusion, the above approach is used to convert temperature Fahrenheit to Celsius.
