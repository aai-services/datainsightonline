---
title: "Simple Python Program for Calculating BMI"
author: "Teresa Rady"
date: 2021-09-20
description: "Albert Einstein said \" If you can't explain it to a six year old, you don't understand it yourself\". This matches the same philosophy of learning in Data Insight scholarship, that is why as part of..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/simplest-program-for-bmi-calculator
---
> Albert Einstein said " If you can't explain it to a six year old, you don't understand it yourself".

This matches the same philosophy of learning in Data Insight scholarship, that is why as part of the process I was required not only to create a simple in python (the BMI calculator) but also to walk the reader through every step of the code.

BMI is the acronym for body mass index which is one of the known measures of obesity. According to the [CDC website](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#Interpreted) the formula to calculate the BMI is by dividing weight in kg by height squared.

So the first two lines of code focus on asking the user about their height in centimetres and accepting an input which represents the height. Then store this input in a variable named cm so as to use in the formula. Note that the code has int() so as to make sure the input is treated as integer not as string.

```python
print('what is your height in centimetres ?')
cm = int(input())
```

Repeat the same concept with the weight of the user.

```python
print('what is your weight in kilograms ?')
kg = int(input())
```

Then, comes the formula that calculates the BMI. Please note that multiplying by 10000 is to convert the cm input to metres as in the original formula.

```python
BMI = kg * 10000/(cm*cm)
print('Your BMI is ' + str(BMI))
```

The last piece of code concentrates on interpreting the output to give a health status based on the ranges on the CDC site.

```python
if BMI < 18.5:print("Status: Underweight")
elif BMI >= 18.5 and BMI < 25:print("Status: Normal weight")
elif BMI >= 25 and BMI < 30:print("Status: Overweight")
else:print("Status: Obese")
```

Here is a a worked example using the calculator and the output.

```python
print('what is your height in centimetres ?')

what is your height in centimetres ?
cm = int(input())

155

print('what is your weight in kilograms ?')

what is your weight in kilograms ?
kg = int(input())

57

BMI = kg * 10000/(cm*cm)
print('Your BMI is ' + str(BMI))

Your BMI is 23.72528616024974

if BMI < 18.5:print("Status: Underweight")elif BMI >= 18.5 and BMI < 25:print("Status: Normal weight")elif BMI >= 25 and BMI < 30:print("Status: Overweight")else:print("Status: Obese")

Status: Normal weight
```
