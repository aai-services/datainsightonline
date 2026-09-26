---
title: "Basic Calculator Application"
author: "Rubash Mali"
date: 2021-09-20
description: "A simple calculator made using if else condition that performs 5 basic mathematic operation between two numbers( addition, subtraction, multiplication, division and modulus operation). Firstly..."
categories: ["General"]
image: images/0a8409_6710e2b520a949a897e6ef2bbe0c24fb.webp
wix-url: https://www.datainsightonline.com/post/basic-calculator-application-1
---
A simple calculator made using if else condition that performs 5 basic mathematic operation between two numbers( addition, subtraction, multiplication, division and modulus operation).

Firstly calculator function is defined with flag initialized as zero and user input a 7. This flag value allows user to exit while loop and the function itself.

![](images/0a8409_1944c38ad4f143b3ae5f34805d2eed4b.webp)

Then the user is allowed to choose which operation they want to perform which is shown as in the code snippet below. Try catch block is added to ensure that no only integer is entered by the user.

![](images/0a8409_9ef2b3fd1f6e4c84a34b9829b003352c.webp)

![](images/0a8409_855b26be1f7b4d4c9b964bb83ac86394.webp)

If the user input is not in the desired range we exit from the loop and the function as flag is set to 1 . Also if the an non integer is input the user input value will be default 7 which leads to user input being out of range.

![](images/0a8409_4da5a195689e401bab7e625d1e27a30a.webp)

Else the two numbers are to be input by user on which the desired mathematical operation is to be performed . The try catch block is added to ensure floating point numbers are input by user.

![](images/0a8409_d977202bd65b4079b1036932c35b0070.webp)

Finally based on the user input choice desired mathematical operation is performed through if conditions.

![](images/0a8409_1b073e0718a4490ab71587e7251c1040.webp)

In this way a simple calculator application is defined an executed by calling the calculator function.

The entire code is and an output instance are as follow:

![](images/0a8409_5926e019f07b4d97a556253191c2de0a.webp)

![](images/0a8409_7c579d72080c46e0aeff85c867ec2ac1.webp)
