---
title: "BMI calculator"
author: "bismark boateng"
date: 2021-09-20
description: "Body Mass Index (BMI) is a measurement of a person's weight with respect to his or her height. It is more of an indicator than a direct measurement of a person's total body fat. BMI, more often than..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/bmi-calculator-3
---
Body Mass Index (BMI) is a **measurement of a person's weight with respect to his or her height**. It is more of an indicator than a direct measurement of a person's total body fat. BMI, more often than not, correlates with total body fat. This means that as the BMI score increases, so does a person's total body fat

I started by taking the height and weight of the user

*[#height](https://www.datainsightonline.com/blog/hashtags/height) in float*

height = float(input("Height(m): "))

*[#weight](https://www.datainsightonline.com/blog/hashtags/weight) in float*

weight = float(input("Weight(kg): "))

As seen from the code snippet above, the height is in meters and weight in kilograms

I then calulated the Body Mass Index using the code snippet below

*[#calculating](https://www.datainsightonline.com/blog/hashtags/calculating) the body mass index*

bmi = (weight)/(height\*height)

The bmi is then calculated and printed to the screen to three decimal places to make it more practical

```python
print(f"Body Mass Index is {round(bmi,3)}")
```

The code snippet above prints the resulting output to the screen
