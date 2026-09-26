---
title: "Body Mass Index Calculator Using Python"
author: "Isuru Lakshan"
date: 2021-09-21
description: "Body Mass Index (BMI) is a commonly used indicator that gives information about how healthy your body is. It is given as a ratio between your weight and height. There is a simple formula to calculate..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/body-mass-calculator-using-python
---
Body Mass Index (BMI) is a commonly used indicator that gives information about how healthy your body is. It is given as a ratio between your weight and height. There is a simple formula to calculate BMI.

The formula is,

Note to make the equation valid, you have to substitute weight and height according to the given SI units.

This BMI value is then used to check your body fat level. The fat level is categorized into five categories and the considered ranges of BMI into those categories are shown in the following table.

|  |  |
| --- | --- |
| BMI Category | BMI range |
| Under weight | <18.5 |
| Normal weight | 18.5 - 24.9 |
| Over weight | 25 - 29.9 |
| Obesity | >30 |

Here I used python language to calculate your BMI and show you the BMI and to which category you belong from the table.

Basically what I did was I created an infinite loop where once you go in it will calculate mode until the user terminates the program typing exit. then in each loop, I prompt the user to enter weight in kilograms and height in meters specifically because I do not implement any unit conversions in my code. After the user enters weight and height it will calculate give output the BMI and the category th

at particular user belongs to and prompt the user wether he/she need to exit or redo the calculation. Typing 'yes' would reiterate the loop and Typing 'no' breaks the loop and exits.

Thank you all for reading.

This is the entire code

```python
# Welcome the User
print('###  BMI Calculater  ###')

# infinite loop where user enters and get the BMI values
while(1):
    # Prompt the user to enter weight and height
    weight = float(input('Enter your Weight in Kilograms: '))
    height = float(input('Enter your height in meters: '))

    #the formula to calculate the BMI
    BMI = (weight) / ((height) * (height))

    # Write the value to the console
    print('Your BMI is :' + str(BMI))

    # deciding which category the user belongs
    if BMI < 18.5:
        print('Alert!! You are underweight')
    elif 18.5 < BMI & BMI < 24.9:
        print('Great! You are Normal weight')
    elif 18.5 < BMI & BMI < 24.9:
        print('Alert! You are over weight')
    else:
        print('Warning! You have obesity')
    usrInput = input('Do you want to restart?? y/n: ')
    #check wether the user need to exit
    if (usrInput == 'n'):
        break

# greet the user
print('### Thank you for using BMI calculater ###')
```
