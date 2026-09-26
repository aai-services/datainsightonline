---
title: "Universal Gravitation Calculator"
author: "James Owusu-Appiah"
date: 2022-04-18
description: "Newton's Law Of Universal Gravitation CalculatorThe law entails that objects with mass feel an attractive force that is proportional to their masses and inversely proportional to the square of the..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/universal-gravitation-calculator
---
## Newton's Law Of Universal Gravitation Calculator
The law entails that objects with mass feel an attractive force that is proportional to their masses and inversely proportional to the square of the distance. Mathematically given as;

**F = GMm/(r^2)**

where **F** represents the force in Newtons, **M** and **m** represent the two masses in kilograms, and **r** represents the separation in meters. **G** represents the gravitational constant, which has a value of **6.674x10^-11N(m/kg)^2**. Because of the magnitude of **G**, the gravitational force is very small unless large masses are involved.

```python
G = 6.674e-11
#Taking the values of the masses involved
M = float(input('Enter the mass of the first object in kilograms: '))
m = float(input('Enter the mass of the second object in kilograms: '))

#Taking the input of the distance of separation between the two masses
r = float(input('Enter the distance of separation between the two masses in meters: '))

#Calculating the force
F = (G*M*m)/r**2

#Printing the force in newtons
print(f'The force that exists between the two objects is {F} Newtons'.format(F))
```

The code initializes a value for G. It takes the input of the masses of the two objects involved and converts them into float values. It then takes the distance between the two masses and converts that into a float value as well. It then computes the force between them. It then prints the value obtained to the user.

**LINK TO GITHUB REPOSITORY WITH CODE:**

<https://github.com/Jegge2003/universal-gravitation-calculator/blob/main/gravitation_calculator.ipynb>
