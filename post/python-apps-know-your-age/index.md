---
title: "Python apps: know your age"
author: "Imene Maallem"
date: 2021-10-21
description: "These days, developers are highly likely to be working on a mobile or web application.Python is a rather universal programming language that is appropriate for solving a wide range of tasks. Python..."
categories: ["Python"]
image: images/e0a26d_c9db1e52606c41828c85112c99375720.webp
wix-url: https://www.datainsightonline.com/post/python-apps-know-your-age
---
![](images/e0a26d_c9db1e52606c41828c85112c99375720.webp)

These days, developers are highly likely to be working on a mobile or web application.Python is a rather universal programming language that is appropriate for solving a wide range of tasks. Python is often used as a support language for software developers,Python doesn't have built-in mobile development capabilities. for build control and management, testing, and in many other ways

# know you age !

[#This](https://www.datainsightonline.com/blog/hashtags/This) code was created to determine the users' age by entering the birth year and prior to whether the person have celebrated his birthday or not :

We are going to use first the input function which allows the user to choose a digit from 2 to 10 and write it :

```python
num=input("enter a digit from 2 to 10:")
```

Then we generate the same function in order to ask from the user
 whether he has celebrated his birthday or not :

```python
birth=input("Have you already celebrated your birthday ?:")
```

if he says yes, we do use if statement and do some excplicit calculations :

if birth=="yes":

a= (int(num)\*2+5)\*50+1771

We then generate same i=function inorder to enter his year of birth :

```python
  year=input("enter the year of birth:")
  fin= a- int(year)
  fina= str(fin)
  final=int(fina[1]+ fina[2])
```

Finally, we print the final age

```python
  print("your age is" , final)
```

In case the user has not already celebrated his birthday , we use elif statement and perform some calculations

```python
elif birth== "no":
   a= (int(num)*2+5)*50+1771
   year=input("enter the year of birth:")
   fin= a- int(year)
   fina= str(fin)
   final=int(fina[1]+ fina[2])
   print("your age is" , final)
```

Let's try the code together :

```python
num=input("enter a digit from 2 to 10:")
birth=input("Have you already celebrated your birthday ?:")
if birth=="yes":
  a= (int(num)*2+5)*50+1771
  year=input("enter the year of birth:")
  fin= a- int(year)
  fina= str(fin)
  final=int(fina[1]+ fina[2])
  print("your age is" , final)
elif birth== "no":
   a= (int(num)*2+5)*50+1771
   year=input("enter the year of birth:")
   fin= a- int(year)
   fina= str(fin)
   final=int(fina[1]+ fina[2])
   print("your age is" , final)
```
