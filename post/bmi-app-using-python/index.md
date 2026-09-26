---
title: "BMI App using python"
author: "Aruna Nuwantha"
date: 2021-10-09
description: "Body Mass Index (BMI) is a commonly used indicator that gives information about how healthy your body is. It is given as a ratio between your weight and height. There is a simple formula to calculate..."
categories: ["Python"]
image: images/92b04d_8cda6d95d0304a9da9255d13defb9e84.webp
wix-url: https://www.datainsightonline.com/post/bmi-app-using-python
---
Body Mass Index (BMI) is a commonly used indicator that gives information about how healthy your body is. It is given as a ratio between your weight and height. There is a simple formula to calculate BMI.

The formula is,

![](images/92b04d_8cda6d95d0304a9da9255d13defb9e84.webp)

According to the below code, firstly I create the function of BMI, which returns the BMI according to the given mass and height parameters. So After the main function, I get the user inputs and check the validation of those inputs, as well as give the proper output.

[#3](https://www.datainsightonline.com/blog/hashtags/3). Body Mass Index calculator

[#find](https://www.datainsightonline.com/blog/hashtags/find) the body mass index -
def BMI(mass, height):
 return mass / (height \*\* 2)

if __name__ == '__main__':
 try:
 [#get](https://www.datainsightonline.com/blog/hashtags/get) the input from users
 mass = float(input("Enter your mass(kg): "))
 height = float(input("Enter your height(m): "))

 print("BMI : {}".format(BMI(mass, height)))

 except:
 print("Error: Please enter the number")

There are some test cases here,

if you are using proper values to your weight and height, it will give the correct answer as BMI.

![](images/92b04d_858e4fa168644ff797faa84daea1d186.webp)

otherwise, if you are not using numbers for your weight, it will give an error.

![](images/92b04d_24eccabb17ef4b1cb16b73a9c793774b.webp)

if you are not using numbers for your height, it will give an errors

![](images/92b04d_1de62ff24b884de9ba12e5070d0c0894.webp)

[Github repo](https://github.com/arunanuwantha97/Datacamp-Assignment/blob/main/bmi.ipynb)
