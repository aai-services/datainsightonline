---
title: "Roman To Decimal"
author: "Rohit Roy"
date: 2021-09-19
description: "The simple idea is to calculate decimal numbers from roman so for that we have five steps process .The reason we are doing this is to get the idea of list and function to calculate the decimal..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/roman-to-decimal
---
The simple idea is to calculate decimal numbers from roman so for that we have five steps process .The reason we are doing this is to get the idea of list and function to calculate the decimal number.

Step 1. We defined a list of values consisting of roman letters and their significant values.
roman = {
 'I': 1,
 'V': 5,
 'X': 10,
 'L': 50,
 'C': 100,
 'D': 500,
 'M': 1000,

}

Step 2. Then we Calculate the length to know how long the value is as per list defined or is it exceeding it.
for index in range(len(romannumbers) - 1):

Step 3. We checked the first symbol using the index value and followed by the next digit and it’s value.
previous = romannumbers[index]

Step 4. Similarly we keep converting digit by digit checking the previous is always greater than next value.
if previousNumber< nextNumber :
 result -= previousNumber
 else:
 result += previousNumber

Step 5. Hence we calculate the result as in whole and print it.
result+=lastNumber

print(result)

For Example :
MCDXLIX --> 1449

XX-->20

Click on the image to check full code

![](images/22a2e8_13fa70a9383344e09b918ee7d8ef98ac.webp)
