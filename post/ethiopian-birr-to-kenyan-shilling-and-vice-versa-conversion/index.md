---
title: "Ethiopian Birr to Kenyan Shilling and Vice Versa Conversion"
author: "Yosef Zeru Seyoum"
date: 2021-10-15
description: "IntroductionEthiopia and Kenya neighboring East African countries who shared border, culture, and language. Both countries are members of IGAD and have different bilateral trade and military..."
categories: ["General"]
image: images/b5f565_0ac14fe09ce143e8935c78f427ae207d.webp
wix-url: https://www.datainsightonline.com/post/ethiopian-birr-to-kenyan-shilling-and-vice-versa-conversion
---
![](images/b5f565_0ac14fe09ce143e8935c78f427ae207d.webp)

## Introduction

Ethiopia and Kenya neighboring East African countries who shared border, culture, and language. Both countries are members of IGAD and have different bilateral trade and military agreement for mutual interest. Preparing simple application which converts their currencies from one to another will ease the transboundary market in the border towns.

To design and implement applications python is preferred by many developers due to its simplicity plus applicability in almost all disciplines. Some of the applications in which python is used are the following.

1. Web Applications

2. Desktop Graphical User Interface (GUI) Applications

3. Scientific and Numeric Applications

In this article we will try to explain how we can create a simple python application to convert Ethiopian Birr (ETB) to Kenyan Shilling (KS), currencies used in Ethiopia and Kenya respectively.

## Step by Step Explanation of Currency Conversion

## Step One
To start the currency conversion in python the first thing we should do is that set the current conversion rate of two currencies, Ethiopian Birr (ETB) and Kenyan Shilling (KS).

- One Ethiopian Birr = 2.35 Kenyan Shilling as of October 15, 2021

- One Kenyan Shilling = 0.43 Ethiopian Birr

Let us convert the above into python code as follows.

```python
#Declare Todays Exchange Rate of Ethiopian Birr to Kenyan Shillings and Vice Versa
ETB_to_KS = 2.43
KS_to_ETB = 0.43
print(ETB_to_KS)
print(KS_to_ETB)
```

```python
2.43
0.43
```

## Step Two
Set choices for the users whether they need to convert ETB to KS or KS to ETB as follows.

- Option 1 = ETB to KS

- Option 2 = KS to ETB

- Option 3 = Exit Calculator

This will be depicted in python as a comment first and users should enter the amount they wish to convert. Let us see the Python code below.

```python
#Begining Message
print("Ethiopian Birr To Kenyan Shilling Converter!!")
     #1 - Convert from ETB to KS
     #2 - Convert from KS to ETB
     #3 - Exit Calculator
```

Output

```python
Ethiopian Birr To Kenyan Shilling Converter!!
```

After the above beginning message for the calculation we used input() function to allow users enter type of currency as follows. In addition let us enter currency type as 1.

```python
#Set Currency Choice 1, 2, or 3 as defined above for user entry.
CURRENCY_CHOISE = input("Please Chose the Currency Type:")
```

Output after entry of 1 as choice.

```python
Please Chose the Currency Type:1
```

**Note:**

The currency conversion will be coded using python conditions and if statements, commonly known as Ternary Operators, or Conditional Expressions. These expressions supported by python to conduct mathematical calculations using logical operators like greater than, less than, greater than or equal to or equals.

## Step Three
Let us convert Ethiopian Birr to Kenyan Shilling by entering 1000 ETB as input here. In addition to input() we also used type() function here to declare the currency.

```python
#Change Ethiopian Birr to Kenyan Shilling by Entering Amount
if CURRENCY_CHOISE == "1":
    ETB = float(input("Please Enter amount of Birr:"))
    OUTPUT = ETB * ETB_to_KS
    print("The Amount In Kenyan Shilling Is:", OUTPUT)
```

Output of the code after entry of 1000ETB as input for change.

```python
Please Enter amount of Birr:1000
The Amount In Kenyan Shilling Is: 2430.0
```

**Note**:

**Indentation**, whitespace at the beginning of a line, is crucial in python functions like if statements. They are used to tell the python interpreter the group of statements we are writing belongs to a particular block of code.

## Step Four

Let us convert Kenyan Shilling to Ethiopian Birr in similar fashion to the above, rerunning currency choice and entering 2 as input.

```python
#Change Kenyan Shilling to Ethiopian Birr by Entering Amount
if CURRENCY_CHOISE == "2":
    KS = float(input("Please Enter amount of KS:"))
    OUTPUT = KS * KS_to_ETB
    print("The Amount In Ethiopian Birr Is:", OUTPUT)
```

Output after feeding 1000KS for conversion to ETB.

```python
Please Enter amount of KS:1000
The Amount In Ethiopian Birr Is: 430.0
```

## Step Five

Let us combine the above two currency calculators using If, elif, Else conditions and test our code by entering data.

```python
#Declare Todays Exchange Rate of Ethiopian Birr to Kenyan Shillings and Vice Versa
ETB_to_KS = 2.43
KS_to_ETB = 0.43
print("Ethiopian Birr To Kenyan Shilling Converter!!")
     #1 - Convert from ETB to KS
     #2 - Convert from KS to ETB
     #3 - Exit Calculator
#Set Currency Choise 1, 2, or 3 as defined above.
CURRENCY_CHOISE = input("Please Chose the Currency Type:")
#Change currency by Entering Amount
if CURRENCY_CHOISE == "1":
    ETB = float(input("Please Enter amount of Birr:"))
    OUTPUT = ETB * ETB_to_KS
    print("The Amount In Kenyan Shilling Is:", OUTPUT)
elif CURRENCY_CHOISE == "2":
    KS = float(input("Please Enter amoun of Shilling:"))
    OUTPUT = KS * KS_to_ETB
    print("The Amount In Ethiopian Birr:", OUTPUT)
elif CURRENCY_CHOISE == "3":
    exit
else:
    print("Invalid Entry")
```

Output

```python
Ethiopian Birr To Kenyan Shilling Converter!!
Please Chose the Currency Type:1
Please Enter amount of Birr:1000
The Amount In Kenyan Shilling Is: 2430.0
```

Thank you.
