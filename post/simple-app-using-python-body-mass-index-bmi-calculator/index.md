---
title: "Simple App using python: Body Mass Index (BMI) calculator"
author: "arijbentej"
date: 2021-08-30
description: "Body mass index (BMI) is a measure of body fat using height and weight that applies to both adult men and women.This post is about a simple application using python that calculates the BMI using a..."
categories: ["Python"]
image: images/c10f9f_2db2b7985e9246e098a05f34367b1ca4.webp
wix-url: https://www.datainsightonline.com/post/simple-app-using-python-body-mass-index-bmi-calculator
---
![](images/c10f9f_2db2b7985e9246e098a05f34367b1ca4.webp)

Body mass index (BMI) is a measure of body fat using height and weight that applies to both adult men and women.

This post is about a simple application using python that calculates the BMI using a height and a weight values given by the user and it also returns the user's weight category he/she falls in based on the calculated value.

### 1. BMI formula

BMI is weight in kilograms divided by height in meters squared.

**BMI = weight (in kg) / height (in m²)**

In our python application, we defined a function called BMI that takes the weight and the height as arguments and returns the BMI value as shown below:

![](images/c10f9f_9a25d2d626fa43759149b202cd49c320.webp)

### 2. Testing the BMI function

The code below shows the use of the BMI function and the classification in the weight category based on the returned value:

![](images/c10f9f_842dd7f09e8645a28fdbe06d23ec9d5a.webp)

The values of height and weight are given by the user. Then, the BMI function is called and the returned value is displayed. Finally, the weight category of the user will be displayed based on the calculated BMI range.

This is an example of a test performed using the code above:

![](images/c10f9f_336720ead8424fe5bb8c86e2a3671c25.webp)

You can find the link to the github repo [here](https://github.com/arijbt/Data-Insight2021/blob/main/Assignments/1).
