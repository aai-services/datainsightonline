---
title: "BMI calculator"
author: "Prativa Bhatta"
date: 2021-10-24
description: "Body Mass Index(BMI) is a measure of body fat based on height and weight that applies to adult men and women. On this basis, a persons BMI value can be categorized as follows:Underweight =..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/bmi-calculator-6
---
Body Mass Index(BMI) is a measure of body fat based on height and weight that applies to adult men and women. On this basis, a persons BMI value can be categorized as follows:

Underweight = <18.5

Normal weight = 18.5–24.9

Overweight = 25–29.9

Obesity = BMI of 30 or greater

Formula to calculate BMI is:

BMI = Body weight/ Body height\*\*2

As the weight is measured in kilograms and height is measured in metres, the unit of BMI is written as kilograms per metre square.

First, let's prompt the user to enter their data

```python
weight = float(input("Weight in kilograms: "))
height = float(input("Height in metres: "))
```

Now, we will calculate the BMI using our formula. We used abs() method if the user accidentally input negative numbers. Also we are using except in case the user inputs invalid values.

```python
bmi = 0
try:
    bmi = abs(weight / height ** 2)
except:
    print("Please enter a valid weight and height before proceeding!")
```

```python
Finally, we can display a BMI category of the user according to their input using a simple  if...elif...else  structure.
```

```python
if bmi <= 18.5:
    print("You are underweight. Are you taking nutrient rich food and enough meal?")
elif bmi < 25:
    print("Congratulations! You're normal weight. Keep up your healthy diet :)")
elif bmi < 30:
    print("You are overweight. Try to maintain a balanced diet with some physical exercises.")
else:
    print("You are obese. Obesity has many detrimental health implications.")
```

With this you can easily calculate your BMI. But beside this make sure to take proper care of your health.
