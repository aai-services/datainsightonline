---
title: "BMI Calculator by python"
author: "Alaa Mohamed"
date: 2021-09-20
description: "What is the BMI?Body Mass Index (BMI) is a person’s weight in kilograms divided by the square of height in meters. A high BMI can indicate high body fatness. BMI screens for weight categories that..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/bmi-calculator-by-python
---
**What is the BMI?**

Body Mass Index (BMI) is a person’s weight in kilograms divided by the square of height in meters. A high BMI can indicate high body fatness. BMI screens for weight categories that may lead to health problems, but it does not diagnose the body fatness or health of an individual.

so in the program I start by taking the height and the weight from user :

```python
w=float(input("Please Enter your Weight"))
h=float(input("Please Enter your Height"))
```

then I calculated the BMI :

BMI=w/(h/100)\*\*2

then I converted the result from float to string to concatenate it print sentence:

```python
bmi=str(BMI)
```

the program detect if person's BMI is normal is not so I used if Condition to print the BMI value and the Person status as shown:

```python
if BMI <= 18.4:
print("Your BMI is" +bmi+"You are underweight.")
elif BMI <= 24.9:
print("Your BMI is" +bmi+"You are healthy.")
elif BMI <= 29.9:
print("Your BMI is" +bmi+" You are over weight.")
elif BMI <= 34.9:
print("Your BMI is" +bmi+" You are severely over weight.")
elif BMI <= 39.9:
print("Your BMI is" +bmi+" You are obese.")
else:
print("Your BMI is" +bmi+" You are severely obese.")
```

program code :

```python
print("Welcome In BMI Calculator Program")
w=float(input("Please Enter your Weight"))
h=float(input("Please Enter your Height"))
BMI=w/(h/100)**2
bmi=str(BMI)
if BMI <= 18.4:
print("Your BMI is" +bmi+"You are underweight.")
elif BMI <= 24.9:
print("Your BMI is" +bmi+"You are healthy.")
elif BMI <= 29.9:
print("Your BMI is" +bmi+" You are over weight.")
elif BMI <= 34.9:
print("Your BMI is" +bmi+" You are severely over weight.")
elif BMI <= 39.9:
print("Your BMI is" +bmi+" You are obese.")
else:
print("Your BMI is" +bmi+" You are severely obese.")
```
