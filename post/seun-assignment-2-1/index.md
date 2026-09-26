---
title: "Seun Assignment 2"
author: "ainatestimony6"
date: 2022-09-17
description: "print(\"Invalid input\") program create simple calculator using functions def add(x, y): return x + y def subtract(x, y): return x - y def multiply(x, y): return x * y def divide(x, y): return x / y..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/seun-assignment-2-1
---
print("Invalid input") program create simple calculator using functions
def add(x, y):
 return x + y
def subtract(x, y):
 return x - y
def multiply(x, y):
 return x \* y
def divide(x, y):
 return x / y

[#User](https://www.datainsightonline.com/blog/hashtags/User) input

no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4):")

if choice == '1':
 print(no1,"+",no2,"=", add(no1,no2))

elif choice == '2':
 print(no1,"-",no2,"=", subtract(no1,no2))

elif choice == '3':
 print(no1,"\*",no2,"=", multiply(no1,no2))

elif choice == '4':
 print(no1,"/",no2,"=", divide(no1,no2))
else:
 print("Invalid input")

Explanations :
This example also ask user input and choice which is arithmetic operator but in-stand of calculating output directly it will pass both number to function based on choice and function will return answer. In this method you need to define function for every operation you want to perform.
