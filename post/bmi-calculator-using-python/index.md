---
title: "BMI calculator using python"
author: "074bex435.ranjan"
date: 2021-09-19
description: "Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. It is a measure for the healthiness of the body in terms of physical body calculation..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/bmi-calculator-using-python
---
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. It is a measure for the healthiness of the body in terms of physical body calculation. Furthermore, it also clarify about the obesity.

First, we require the height and weight of the person. Here we have input the height and weight in python and convert it into number.

```python
#take height in feet and inches format as input from user
print('Enter your height in feet and inches')
print('Feet=')
feet = float(input())
print('Inches=')
inches = float(input())
height = feet*12+inches
```

```python
# Take weight as input in pound
print('Enter your weight in pounds')
print('Weight = ')
weight = float(input())
```

Then we calculate the bmi using formula.

```python
#Calculate BMI using formula
bmi = (weight/(height*height))*703
print('Your BMI is ',round(bmi,2))
```

Finally we also show the remarks according to the output of bmi.

```python
#Check for under, normal, over weight or obesity
if bmi<=18.5:
    print('Underweight')
elif bmi>18.5 and bmi<=24.9:
    print('Normal weight')
elif bmi>=25 and bmi>=29.9:
    print('Over weight')
else:
    print('Obesity')
```

Github: https://github.com/ranjan435/data-insight-2021/blob/main/bmi.ipynb
