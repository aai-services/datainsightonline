---
title: "Body Mass Index (BMI) Calculator"
author: "James Owusu-Appiah"
date: 2022-04-18
description: "Body Mass Index (BMI) CalculatorBody Mass Index is an approximate measure of whether someone is over or underweight, calculated by dividing their weight in kilograms by the square of their height in..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/writing-simple-apps-with-python
---
## Body Mass Index (BMI) Calculator
Body Mass Index is an approximate measure of whether someone is over or underweight, calculated by dividing their weight in kilograms by the square of their height in meters. BMI is an inexpensive and easy screening method for weight categories - underweight, healthy weight, overweight, and obesity. BMI does not measure body fat directly, but BMI is moderately correlated with more direct measures of body fat. Mathematically;

**BMI = Weight (kg) / (Height (m) ^2).**

```python
#Taking the weight input of the individual
weight = float(input('Enter your weight in kilograms: '))

#Taking the height input of the individual
height = float(input('Enter your height in metres: '))

#Calculating the Body Mass Index (BMI)
BMI = weight/height**2

#Printing out the BMI value
print(f'Your BMI is {BMI} kg/m^2'.format(BMI))
```

This code takes the weight input of the individual in kilograms and converts it into a float value. It then takes the height input of the individual in meters and converts it into a float value. The BMI is then calculated and then later printed for the individual.

**LINK TO GITHUB REPOSITORY WITH CODE:**

<https://github.com/Jegge2003/simple-bmi-calculator-app/blob/main/BMI_calculator.ipynb>
