---
title: "Fahrenheit to Celsius, a simple converter"
author: "Sana Omar"
date: 2021-09-22
description: "We start with writing the general theory - the rule of conversion:Celsius = (Fahrenheit- 32) * 5/9image recourse: https://vocal.media/lifehack/how-to-convert-celsius-to-fahrenheit-easyFirst:The..."
categories: ["General"]
image: images/82b983_611b364d752948e9a6f0bee9d2a092b4.webp
wix-url: https://www.datainsightonline.com/post/fahrenheit-to-celsius-a-simple-converter
---
We start with writing the general theory - the rule of conversion:

```python
Celsius = (Fahrenheit- 32) * 5/9
```

![](images/82b983_611b364d752948e9a6f0bee9d2a092b4.webp)

*image recourse: https://vocal.media/lifehack/how-to-convert-celsius-to-fahrenheit-easy*

**First:**

The program accepts the value of the Fahrenheit degree entered by the user and stores it in **feh** variable, as the following:

```python
feh = float(input("Enter your temperature in Fehrenheit: "))
```

A prompt will appear for the user as:

```python
Enter your temperature in Fehrenheit: 1000
```

**Second, the conversion:**

Then, the conversion is calculated using the previous mentioned rule and the result is stored in the variable **celsius**:

```python
celsius = (feh - 32) * 5 / 9
```

Then the result is printed along with the converted Fahrenheit degree:

```python
print("%0.2f degrees in Fehrenheit is %0.2f degrees in Celsius. " %(feh,celsius))
```

The result would be:

```python
1000.00 degrees in Fehrenheit is 537.78 degrees in Celsius.
```

Using the % symbol we linked the place of the variable in the sentence, f symbol is to determine that this value is float, 0.2 is the number of digits after the dot.

Also, we could just convert the celsius variable into String and printed:

```python
print("The temperature in Celesius is :" + str(celsius))
```

It would result in the whole number:

```python
The temperature in Celesius is :537.7777777777778
```

***Thanks for reading.***
