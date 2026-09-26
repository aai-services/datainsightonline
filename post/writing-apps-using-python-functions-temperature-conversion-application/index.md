---
title: "Writing Apps Using Python Functions: Temperature Conversion Application"
author: "Ochuole Ogbeche"
date: 2022-01-21
description: "Python Functions:In Python, a function is a piece of reusable code. It eliminates the need to write code repetitively, thereby following the PEP8 standard of DRY (Don’t Repeat Yourself).A function in..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/writing-apps-using-python-functions-temperature-conversion-application
---
**Python Functions**:

In Python, a function is a piece of reusable code. It eliminates the need to write code repetitively, thereby following the PEP8 standard of DRY (Don’t Repeat Yourself).

A function in python is written using the def keyword followed by the function name, a bracket containing the argument(s) for the function, and ending in a colon. A function depends on indentions, therefore, the block of code, that is the code to be executed, is indented.

Python functions have to be called with parameters that equal the arguments in the function bracket before the function can run. The function is usually called at the end of all the blocks of code needed by the function.

**Temperature Conversion App**

Like all functions, it begins with the def keyword followed by the name of the function, temperature_converter, a name that clearly states what the function does and follows variable naming conventions in Python. The blocks of code to be executed are indented. The first and second lines show the standard conversion of Celsius to Fahrenheit and Fahrenheit to Celsius, respectively.

Underneath this initial block of code, there is a block of code (if…elif…else block) which verifies the input for the temperature calculation. This block of code begins with an if statement that specifies that the input for the degree is equal to “C” for Celsius or "F" for Fahrenheit, and the float entered for the temperature to be converted is equal to greater than or equal to zero, or less than or equal to zero. Thereafter, there is a display saying the temperature inputted is being converted to Fahrenheit of Celsius, depending on the initial unit specified, after which the temperature converted is displayed on the screen, along with the inputted value and unit.

def convert_temperature(unit, temp):

temp_convert_celsius = ((float(temp) - 32) \* 5 / 9)

temp_convert_fahrenheit = ((float(temp) \* 1.8) + 32)

if unit == "C" and (float(temp) >= 0 or float(temp) <= 0):

print("Converting to Fahrenheit...")

print("The temperature in Celsius is " + str(temp) + " and the
 temperature in Fahrenheit is " + str(

temp_convert_fahrenheit) + ".")

elif unit == "F" and (float(temp) >= 0 or float(temp) <= 0):

print("Converting to Celsius...")

print("The temperature in fahrenheit is " + str(float(temp)) + " and the
 temperature in Celsius is " + str(

temp_convert_celsius) + ".")

else:

print("Invalid Unit")

The second block of code is another if block beginning with the while True statement. This if…elif…else block simply verifies the inputted unit for the temperature, ensuring that the correct alphabets (c or f) are inputted, and instructs the user to enter either if the input doesn’t match. If the input matches, the block of code that matches the input for both unit and temperature, that is either the if, elif, or else statement in the previous if…elif…else block is executed. The capitalize method is used to capitalize the inputted alphabet to ensure all inputs for "f" or "c" match no matter if the user uses lower or upper case.

while True:

unit = str(input("Input Degree: 'C' for Celsuis or 'F' for Fahrenheit
 \n")).capitalize()

if unit == "C":

print("Unit is Celsius.")

break;

elif unit == "F":

print("Unit is Fahrenheit.")

break;

else:

print("Invalid Unit.\nEnter either 'c' for Celsius or 'f' for Fahrenheit")

The third code block simply verifies the inputted value for the temperature to be an integer that can be converted into a float, throws an exception when a ValueError is caught, and instructs the user to enter an integer. If there is no error, the block of code that matches either input for both unit and temperature in the if, elif, or else statement in the first if…elif…else block is executed.

while True:

temp = input("Input the temperature to be converted \n")

try:

val = float(temp)

print("Input number is: ", val)

break;

except ValueError:

print("This is not a Integer.\nPlease enter a valid Number")

The function is called at the end with the validated parameters (unit and temp) supplied into it.

convert_temperature(unit, temp)
