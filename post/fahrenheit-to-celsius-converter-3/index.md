---
title: "Fahrenheit to Celsius Converter"
author: "Ebrima Sise"
date: 2022-05-03
description: "According to Wikipedia, the Fahrenheit scale is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit. It uses the degree Fahrenheit as the unit.It also states..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/fahrenheit-to-celsius-converter-3
---
According to Wikipedia, the Fahrenheit scale is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit. It uses the degree Fahrenheit as the unit.

It also states that the degree Celsius is a unit of temperature on the Celsius scale, a temperature scale originally known as the centigrade scale. The degree Celsius can refer to a specific temperature on the Celsius scale or a unit to indicate a difference or range between two temperatures.

There are times when the scale Fahrenheit is used to measure temperature but the end-user wants to know the measurement in the Celsius scale. In those instances, the formula to convert the temperature is used.

```python
celsius = (fahrenheit − 32) × 5/9
```

This formula is not hard to understand and the calculations are a bit straightforward. But for an end-user who only cares about the equivalent in Celsius, this is too technical. That's why I created this program with the end-user in mind.

```python
def fahrenheit_to_celsius_converter(temp):
    '''this function prints the converted temperature
       measurement from fahrenheit to celsius
    '''
    # formula to convert the temperature from
    # fahrenheit to Celsius
    celsius = (temp - 32) * (5/9)

    # round the result to 2 decimal places
    celsius =    round(celsius, 2)

    # print the results for the user
    print(str(temp) + ' degrees Fahrenheit is equal to
          ' + str(celsius) + ' degrees Celsius')
```

The program takes the formula above and takes care of the calculations and conversions in the background. All the user need is the name of the function and she/he can provide the temperature to be converted and the program prints the result instantly without hassle.

The complete program with examples can be found on my GitHub [here](https://github.com/siseebrima/DataInsight/blob/main/temperature_converter(fahrenheit_celsius).ipynb).
