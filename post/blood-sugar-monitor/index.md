---
title: "Blood sugar monitor"
author: "Wilson Waha"
date: 2022-05-06
description: "Glucose shows your blood sugar level. It is important to know your blood sugar level to prevent possible complications. There are several levels of blood sugar: hypoglycemia, normal blood sugar..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/blood-sugar-monitor
---
Glucose shows your blood sugar level. It is important to know your blood sugar level to prevent possible complications. There are several levels of blood sugar: hypoglycemia, normal blood sugar, moderate hyperglycemia and Diabetes. We wrote a program that asks the user for their blood sugar level and returns the class to which they belong.

```python
def blood_sugar():
    """
    Blood sugar monitor

     Args:


     Returns:
    str: Health status based on blood sugar


    """

    blood_s = float(input("Enter your blood sugar : "))
    threshold = 0.7
    if(blood_s<threshold):
        print("Your are in Hypoglycemia")
    elif(threshold<=blood_s and blood_s<=1):
        print("Your blood sugar level is right")
    elif(blood_s>=1 and blood_s<=1.25):
        print("Moderate Hyperglycemia")
    else:
        print("Diabetes")
```

Illustration

```python
in: blood_sugar()
```

```python
out: Enter your blood sugar : 1.03
     Moderate Hyperglycemia
```

```python
in : blood_sugar()
```

```python
out: Enter your blood sugar : 0.9
     Your blood sugar level is right
```
