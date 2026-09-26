---
title: "Body Mass Index (BMI) calculator"
author: "Lucien Dikla Ngueleo"
date: 2022-05-05
description: "The body mass index (BMI) estimates ideal weight based on height. Its calculation is the weight divided by the square of the height (BMI = weight in kg/height² in m)def bmc(weight,height): ''' bmc..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/body-mass-index-bmi-calculator-7
---
The **body mass index (BMI)** estimates ideal weight based on height. Its calculation is the weight divided by the square of the height (***BMI = weight in kg/height² in m***)

```python
def bmc(weight,height):
  '''
  bmc calcul the body masse index

  Parameters
  ----------
    (weight) person's weight in kg
    (height) person's height in m

  Returns
  ----------
    bmc = weight/height**2
  '''
  return weight/height**2
```

**Example** of using the bmc function

```python
print(bmc(50,1.73))
```

```python
16.70620468441979
```

**Important concepts**

**def** is the keyword to define a function

**return** is a special statement to return the result of the function to the caller

**/ and \*\*** are respectively division and power operators
