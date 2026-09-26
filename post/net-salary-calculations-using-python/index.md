---
title: "Net Salary Calculations using Python"
author: "Yosef Zeru Seyoum"
date: 2021-10-17
description: "Python has a capacity to conduct various ranges of calculations. Python is an incredibly powerful calculator. By leveraging the math library, numpy, and scipy, Python typically outperforms..."
categories: ["Python"]
image: images/b5f565_02eba2ca5bb84738a09f95dffd8616cc.webp
wix-url: https://www.datainsightonline.com/post/net-salary-calculations-using-python
---
![](images/b5f565_02eba2ca5bb84738a09f95dffd8616cc.webp)

Python has a capacity to conduct various ranges of calculations. Python is an incredibly powerful calculator. By leveraging the math library, numpy, and scipy, Python typically outperforms pre-programmed calculators. Addition, subtraction, multiplication, division, and exponentiation are core operations.

Using this powerful calculator, python, we will see how to calculate net salary of an individual having different types of deductibles and pension.

The 1st step we are expected to do is creating of objects which can be user defined or calculated. Therefore, let us use input() function to allow entry of Employee name as follows.

```python
# Insert Name of the Employee using input() function
NAME = input("Employee Name:")
```

Output

```python
Employee Name:Yosef
```

Like the above let us declare [#Gross](https://www.datainsightonline.com/blog/hashtags/Gross)-Salary and deductible Pension of the Employee as user defined input. What will be different here is that we should change the salary from string to int to help us in our further calculations. To do so we used type() function of python. The Code will looks like the following.

```python
# Insert gross salary of the Employee using input() function
GROSS_SALARY = int(input("Please State your Gross Salary:"))
#Calculate Pension based on the given gross salary
PENSION = GROSS_SALARY * 0.12
```

Output after entering 600 ETB as gross salary.

```python
Please State your Gross Salary:600
```

Finally let us use if…elif …else function and calculate the salary of the employee. When we calculate the net salary in addition to pension tax deductibles should be considered according to predefined salary scale as shown below, pension is 12% of gross salary.

|  |  |  |
| --- | --- | --- |
| S.No | Salary Range | Deductible |
| 1 | < = 600 ETB | 0 |
| 2 | 601 - 1650 ETB | 60 |
| 3 | 1651 - 3200 ETB | 142 |
| 4 | 3201 - 5250 ETB | 303 |
| 5 | 5251 - 7800 ETB | 565 |
| 6 | 7801 - 10900 ETB | 955 |
| 7 | >= 10901 ETB | 1500 |

The python code will look like the following.

```python
#Define the tax, pension and other deductables by salary range
if GROSS_SALARY <= 600:
    Net_Salary = GROSS_SALARY - PENSION
elif GROSS_SALARY >= 601 & GROSS_SALARY <=1650 :
    Net_Salary = GROSS_SALARY - 60 - PENSION
elif GROSS_SALARY >= 1651 & GROSS_SALARY <=3200 :
    Net_Salary = GROSS_SALARY - 142 - PENSION
elif GROSS_SALARY >= 3201 & GROSS_SALARY <=5250 :
    Net_Salary = GROSS_SALARY - 303 - PENSION
elif GROSS_SALARY >= 5251 & GROSS_SALARY <=7800 :
    Net_Salary = GROSS_SALARY - 565 - PENSION
elif GROSS_SALARY >= 7801 & GROSS_SALARY <=10900 :
    Net_Salary = GROSS_SALARY - 955 - PENSION
elif GROSS_SALARY >= 10901:
    Net_Salary = GROSS_SALARY - 1500 - PENSION
else:
    print("Invalid Entry")

print(NAME)
print(GROSS_SALARY)
print(PENSION)
print(Net_Salary)
```

The Output

```python
Yosef
600
72.0
528.0
```

Thank you.
