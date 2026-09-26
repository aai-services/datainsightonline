---
title: "Simple interest calculator"
author: "jackson_gargar"
date: 2022-01-22
description: "This is a simple program that will teach you how to quickly find simple interest in python \"\"\" Author: Jackson I. Gargar Date: 1/12/2022 Assignment: Task: Simple interest calculator. Simple interest..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/simple-interest-calculator-1
---
This is a simple program that will teach you how to quickly find simple interest in python

""" Author: Jackson I. Gargar
Date: 1/12/2022
Assignment:
Task: Simple interest calculator.
Simple interest is calculating the amount of interest that is been charged on a sum
at a given rate and for a given period of time. You can use a computer program to calculate
the simple interest and below is an example of simple codes that will teach you how to calculate the Simple interest
that is been charged on a sum at a given rate and for a given period of time
Formular: Simple Intrest = P × R × T
Simple Interest is calculated using the following formula: SI = P × R × T,
where P = Principal, R = Rate of Interest, and T = Time period.
and the rate is given in percentage (r%) is written as r/100
To find the sample interest, you will need to use a data type called float.
"""
# request the user to import the principal
P = float(input('Enter the principal amount: '))

# request the user to import the rate
R = float(input('Enter the total number of rate: '))

# request the user to import the number of years
T = float(input('Enter the time in years: '))

# formula to calculate the interest
S_interest = (P \* R \* T)/100

# this below create a space
print()

# Print the Principal
print('The principal amounts:', P )

# Print the Rate
print('The rate is:', R)

# Print the Time
print('The total number of years:', T)

# Print the total Interest
print('The Total interest is:', S_interest)
