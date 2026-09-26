---
title: "WRITING A SIMPLE ARITHMETIC CALCULATOR PROGRAM WITH PYTHON"
author: "ukaegbu daniel"
date: 2022-06-17
description: "Python is a powerful programming language and there are facts to back that up. Yes of course! Another fact that may interest you is that python is one of the most widely used programming languages..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/writing-a-simple-arithmetic-calculator-program-with-python
---
Python is a powerful programming language and there are facts to back that up. Yes of course! Another fact that may interest you is that python is one of the most widely used programming languages with an amazing community of professionals and learners, it is easy to learn and can be used for virtually every programming task from web development, Artificial intelligence, Automation, data analysis, and even game development. Most of the most popular social media platforms were written using python eg Instagram, pin interest, and Spotify. Python has amazing libraries and modules that make software development exciting. Just to see python in action we are going to write a short program for a simple arithmetic calculator. This is just an illustration as python is and has always been used for writing very complex and sophisticated programs. Building this calculator would require we used basic Python concepts such as variables, functions, conditional statements, strings etc. Below is a code tutorial to help you understand it better.

```python
#Define function
#This functions performs the Addition operation.
def add(x,y):
    return x+y
#this function performs the subtraction operation
def subtract(x,y):
    return x-y
#this function perform multiplication operation
def multiply(x,y):
    return(x*y)
#this function performs the division operation
def divide (x,y):
    return(x/y)
```

```python
#Define variable
num1=float(input('please input a number: '))
num2=float(input('please input a number: '))
#the yes are numbers that represents the different arithematic operation in our calculator
print('please select a simple operation from 1- 4 ')
print('1 Add')
print('2 subtract')
print('3 multiply')
print('4 divide')

Operation=input('please select an operation from the keys above: ')

if Operation in ('1','2','3','4'):
   if Operation=='1':
      print(num2,'+',num2,'=',add(num1,num2))
   if Operation=='2':
      print(num1,'-',num2,'=', subtract(num1,num2))
   if Operation =='3':
      print(num1,'*', num2,'=', multiply(num1,num2))
   if Operation =='4':
      print(num1,'/',num2,'=',divide(num1,num2))
```
