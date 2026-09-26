---
title: "Temperature Conversions using Python"
author: "mairajsaleem92"
date: 2021-09-21
description: "OVERVIEW:In this blog post, we will learn the conversion of temperature in different scales. The three most common temperature scales are Celsius, Fahrenheit and Kelvin. Each scale has its uses, so..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/temperature-conversions
---
**OVERVIEW:**

In this blog post, we will learn the conversion of temperature in different scales. The three most common temperature scales are Celsius, Fahrenheit and Kelvin. Each scale has its uses, so if you encounter them and need to convert between them, the conversion formula is as shown below:

|  |  |
| --- | --- |
| ​Celsius to Fahrenheit | F = (9/5) \* C + 32 |
| Kelvin to Fahrenheit | F = (9/5) \* (K – 273.15) + 32 |
| Fahrenheit to Celsius | ​C = (5/9) \* (F - 32) |
| ​Celsius to Kelvin | ​K = C + 273.15 |
| ​Kelvin to Celsius | ​C = K – 273.15 |
| ​Fahrenheit to Kelvin | ​K = (5/9) \* (F - 32) + 273.15 |

**EXPLANATION OF CODE:**

First define a function name **temp_conversion** include all the conversion by using if, elif and else statements. The **temp_conversion** have taken three inputs, first is **temp** which is the temperature to be convert , second is **current_unit** which shows the current scale of temperature and last is **to_be_convered** define the scale in which we want to convert the temperature. The formula of all conversion shown above in the overview section. The code of the function shown below:

```python
# Temperature Conversion
# Define a function for conversion

def temp_conversion(temp,current_unit,to_be_convered):
# Use "F" for Fahrenheit, "C" for Celsius and "K" for Kelvin
### Conversion from Celsius to Fahrenheit ###
    if to_be_convered == "F" and current_unit == "C":
        new_temp = round(9 / 5 * temp + 32, 3)
        print("The converted temperature in Fahrenheit scale
        is " + str(new_temp) + " degrees")

### Conversion from Fahrenheit into Celsius ###
    elif to_be_convered == "C" and current_unit == "F":
        new_temp = round(5 / 9 * (temp - 32), 3)
        print("The converted temperature in Celsius scale is
        " + str(new_temp) + " degrees")

### Conversion from Celsius to Kelvin ###
    elif to_be_convered == "K" and current_unit == "C":
        new_temp = round(temp + 273.15, 3)
        print("The converted temperature in Kelvin scale
        is " + str(new_temp) + " degrees")

### Conversion from Kelvin to Celsius ###
     elif to_be_convered == "C" and current_unit == "K":
         new_temp = round(temp - 273.15, 3)
         print("The converted temperature in Celsius scale is
         " + str(new_temp) + " degrees")

### Conversion from Kelvin to Fahrenheit ###
    elif to_be_convered == "F" and current_unit == "K":
        new_temp = round(9 / 5 * (temp - 273.15) + 32, 3)
        print("The converted temperature in Fahrenheit scale
        is " + str(new_temp) + " degrees")

### Conversion from Fahrenheit to Kelvin ###
    else:
        new_temp = round(5 / 9 * (temp - 32) + 273.15, 3)
        print("The converted temperature in Kelvin scale
        is " + str(new_temp) + " degrees")
```

**EXAMPLES:**

Now, we apply this function to convert the temperature in different scales.

In first example, we convert temperature of Celsius into Fahrenheit.

```python
temp_conversion(108,"C","F")
```

The converted temperature in Fahrenheit scale is 226.4 degrees

Let's take another example to convert temperature from Kelvin to Fahrenheit.

```python
temp_conversion(235.685,"K","F")
```

The converted temperature in Fahrenheit scale is -35.437 degrees

**CONCLUSION:**

By using the above function, you can easily convert temperature into three different scales and vice versa. I hope this article is helpful for you.

Here is the [link](https://github.com/MuhammadMairajSaleem92/Projects/blob/main/Temperature%20Conversions.ipynb) Git hub repository.
