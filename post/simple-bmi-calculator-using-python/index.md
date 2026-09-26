---
title: "Simple BMI calculator using Python"
author: "Abhishek Tuladhar"
date: 2021-09-21
description: "Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. It is calculated using a person’s weight in kilograms divided by the square of height in..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/simple-bmi-calculator-using-python
---
Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. It is calculated using a person’s weight in kilograms divided by the square of height in meters. A high BMI can indicate high body fatness.

This post presents a simple BMI calculator created using the python programming language.

**Step 1:** We create a function named 'bodymassindex' with two parameters 'height' and 'weight'. This function returns the calculation of weight in 'kg' divided by the square of the height in 'meters', which is the formula of the Body Mass Index(BMI). The round() function is used in order to round the result to 2 decimal points.

```python
def bodymassindex(height, weight):
    return round((weight / height**2),2)
```

**Step 2:** Using the input() function, we ask the user to enter the height and weight , and assign them to variables 'h' and 'w' respectively. Since the inputs are in string format, we convert them into floats using the float() function. This enables us to perform mathematical calculations using those variables.

```python
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))
```

**Step 3:** Then we make a function call to the function 'bodymassindex' with height 'h' and weight 'w' as the arguments and assign it to the variable 'bmi'. The returned value from the function is the calculated BMI, which is then printed as the result.

```python
bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)
```

**Step 4:** This program can be made further informative by providing information such as if the person is underweight, normal, overweight or obese based on the BMI of the person. For this we use a simple if-else statement as shown below:

```python
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
```

Finally, the full program code:

```python
#Simple BMI calculator using python

def bodymassindex(height, weight):
    return round((weight / height**2),2)

h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))

print("Welcome to the BMI calculator.")

bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
```

Following is the example of the output of the program:

```python
Enter your height in meters: 1.8
Enter your weight in kg: 80
Your BMI is:  24.69
Your weight is normal.
```
