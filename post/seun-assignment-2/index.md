---
title: "Seun Assignment 2"
author: "ainatestimony6"
date: 2022-09-17
description: "# Python program to make a simple calculator # taking user input no1 = float(input(\"Enter first number: \")) no2 = float(input(\"Enter second number: \")) # choice operation print(\"Operation: +, -, *..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/seun-assignment-2
---
# Python program to make a simple calculator

# taking user input
no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))

# choice operation
print("Operation: +, -, \*, /")
select = input("Select operations: ")

# check operations and display result
if select == "+":
 print(no1, "+", no2, "=", no1+no2)

elif select == "-":
 print(no1, "-", no2, "=", no1-no2)

elif select == "\*":
 print(no1, "\*", no2, "=", no1\*no2)

elif select == "/":
 print(no1, "/", no2, "=", no1/no2)

else:
 print("Invalid input")
