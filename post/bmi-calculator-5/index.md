---
title: "BMI Calculator"
author: "ekow.a.indome"
date: 2021-09-22
description: "Body mass index(BMI) is a measure of body fat based on height and weight that applies to adult men and women. To know your bmi, the entries required are height and weight. The formular for bmi with..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/bmi-calculator-5
---
Body mass index(BMI) is a measure of body fat based on height and weight that applies to adult men and women. To know your bmi, the entries required are height and weight. The formular for bmi with height in inches and weight in kilograms is bmi = weight(kg) / (height(m^2))^2. While in when weight is in pounds bmi = weight(pounds) / (height(m^2))^2 \* 703.
The program written below helps to calculate your Body mass index, and informs you which category you belong to.

Here's how the code works:

Initially, you enter you name, move forward to enter you weight(in pounds specifically) and add your height(in inches).

```python
print("A Program to canlculate BMI of an individual")
name = input("Enter your name: ")
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
```

Here, we encounter a function which houses some decision functions. We define our function as BMI, which will take in the arguments weight and height. I then input the formular stated earlier, bmi = weight(kg) / (height(m^2))^2. Then the program checks which of the decision statements it will return the answer to. If bmi is less than 16, it will return severely underweight. Between 16 and18 underweight, between 18.5 and 24 healthy, between 25 and 29 overweight, and above 30 is obese.

```python
def BMI(weight, height):
    bmi = weight / (height ** 2) * 703

    if (bmi < 16):
        return 'severely underweight', bmi
    elif (bmi >= 16 and bmi < 18.5):
        return 'underweight', bmi
    elif (bmi >= 18.5 and bmi < 25):
        return 'healthy', bmi
    elif (bmi >= 25 and bmi < 30):
        return 'overweight', bmi
    elif (bmi >= 30):
        return 'obese', bmi

quote, bmi = BMI(weight, height)
print('your bmi is: {} and your are: {}'.format(bmi, quote))
```
