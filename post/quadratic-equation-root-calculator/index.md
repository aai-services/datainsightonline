---
title: "Finding the Roots of Quadratic Equations using Python"
author: "Isuru Lakshan"
date: 2021-09-21
description: "In mathematics, a Quadratic equation is an equation that has the standard form that follows,where x is the variable and a,b,c are constants. The x values which satisfy the above equation are referred..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/quadratic-equation-root-calculator
---
In mathematics, a Quadratic equation is an equation that has the standard form that follows,

where x is the variable and a,b,c are constants. The x values which satisfy the above equation are referred to as roots of the equation. why roots in plural??? because for quadratic equations there are two values that x can get such that the above equation would be satisfied.

These roots can be obtained using the following two equations,

here, a.b.c are the same constants in the above equation. To obtain roots from these formulas some conditions need to be satisfied

1st condition

This is because divided by zero is undefined in mathematics.

2nd condition

Thus this equation has real roots.

if

The equation does not have real roots instead it has imaginary roots. For this calculator considered only real roots. Therefore entering a,b,c values which satisfy this condition may prompt you to try again.

If the above two conditions are met the root calculated will calculate the relevant roots for you.

Python code is structured in a way that user need to enter the a,b,c values for the intended quadratic equations and if the roots are real, the roots will be displayed in the terminal. then the user will be asked to try again and if the user needs to exit he/she need to enter 'no'

Thank you for Reading

The python code for the calculator,

```python
# import math package to get support of square root
import math

# Welcome the User
print('###  Quadtratic Equation Solver  ###')

# infinite loop to iterate over retries
while(1):
    # get user inputs for corresponding coefficients of quadtratic equation
    a = float(input('enter a value: '))
    b = float(input('enter b value: '))
    c = float(input('enter c value: '))

    # check weather the equation is quadtratic or not if not one root is there
    if a == 0:
        root1 = -c / b
        root2 = -c / b
    else:
        # try to calculate roots
        try:
            root1 = (-b + math.sqrt(b*b-4*a*c)) / 2*a
            root2 = (-b - math.sqrt(b*b-4*a*c)) / 2*a

        # if roots are imaginary abort
        except:
            print('no real roots for this equation')
            usrInput = input('Do you want to retry?? y/n: ')
            #check wether the user need to exit
            if (usrInput == 'n'):
                break
            else:
                continue

    # console out the resulting roots
    print('First Root: ' + str(root1))
    print('Second Root: ' + str(root2))

    usrInput = input('Do you want to restart?? y/n: ')
    #check wether the user need to exit
    if (usrInput == 'n'):
        break

# greet the user
print('### Thank you for using Root calculater ###')
```
