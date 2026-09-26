---
title: "Python Concept for Data Science: Decision Making Statements"
author: "mairajsaleem92"
date: 2021-10-06
description: "Introduction:In your programming journey, decision making will be with you from the beginning to the end. At every stage, you need to make certain decisions based on a condition. Therefore, we will..."
categories: ["Python"]
image: images/b581a2_6220f8e5fa4a4075931e46a94fb037e8.webp
wix-url: https://www.datainsightonline.com/post/python-concept-for-data-science-decision-making-statements
---
![](images/b581a2_6220f8e5fa4a4075931e46a94fb037e8.webp)

**Introduction:**

In your programming journey, decision making will be with you from the beginning to the end. At every stage, you need to make certain decisions based on a condition. Therefore, we will be discussing Python decision making statements and learn to use if statements, if-else statements, if-elif ladder and Nested statements in Python.

**The idea of decision-making statements in Python:**

There comes a point in your life where you need to decide what steps should be taken and based on that you decide your next decisions.

In programming, we often have a similar situation where we need to decide which block of code should be executed based on a condition.

Let’s take a simple example.

Suppose you are writing a program for providing remarks to students for their performance in the exam. So, at every step, we need to make decisions like:

- If the student has marked more than 90%, then the student is excellent in his studies.
- If the student has marked between 70% to 90%, then the student is good in his studies.
- If the student has marked between 50% to 70%, then the student is average in his studies.
- If the student has marked less than 50%, then the student is poor in his studies.

Decisions like these are required everywhere in programming and they decide the direction of the flow of program execution.

**Python has the following decision-making statements:**

- If statements
- If-else statements
- If-elif ladder
- Nested statements
- Single statement condition

Let's discuss all statements one by one.

**If statement:**

An if statement in python takes an condition with it. If the condition amounts to True, then the block of statements under it is executed.

If it amounts to False, then the block is skipped and control transfers to the statements after the block. But remember to indent the statements in a block equally. Also, use a colon (:) after the condition.

**The general syntax of the if statement is shown below:**

if (condition):

# If the condition is True, Statement occurs in the output

If Statement 1

If Statement 2

If Statement 3

.

.

If Statement n

Let's learn through example,

```python
# if statement
# Compare the age of two people, who's younger than other
Sam_age = 35
Albert_age = 41

# if age of Sam is less than Albert then Sam is younger
if (Sam_age < Albert_age):
    print("Sam is younger than Albert")
```

Output shows that:

Sam is younger than Albert

When if condition is not True so we need an else statement to print the output. Now learn the if-else statement.

**If-else statement:**

The if-else statement checks the condition and executes the if block when the condition is True otherwise it will execute the else block of code. The else block should be right after if block and it is executed when the condition is False.

**The general syntax is:**

If (expression):

If Statement

else:

Else Statement

Example of if-else statement is given below:

```python
# if-else statement
potatoes_per_kg = 64
mangoes_per_kg = 85

if (potatoes_per_kg > mangoes_per_kg):
   print("Potatoes is costly than Mangoes")
else:
   print("Potatoes is cheaper than Mangoes")
```

In our example, Potatoes is less in amount as compare to Mangoes so the output should be:

Potatoes is cheaper than Mangoes

One point to be noted is that, only one else statement is followed by an if statement. If you use two else statements after an if statement, then you get the error. Let's check with example, how the error occurred,

```python
if (10 < 7):
    print("10 is smaller than 7")
else:
    print("10 is greater than 7")
else:
   print("condition closed")
```

Output show an error like this:

```python
 File "<ipython-input-8-3299bac54d8a>", line 5
    else:
       ^
 SyntaxError: invalid syntax
```

To apply multiple conditions, we use elif condition between if and else expression. Let's explain in detail, how the if-elif work.

**If-elif ladder:**

Python allows the elif keyword as a replacement to the multiple else statement. When we have more than one condition to check, we can use it. With elif ladder, we can make complex decision-making statements.

The elif statement helps you to check multiple expressions and it executes the code as soon as one of the conditions evaluates to True.

**The general syntax of the if-elif ladder is given by:**

If (condition 1):

Statement 1

elif (condition 2):

Statement 2

elif (condition 3):

Statement 3

.

.

else:

Else statement

If condition 1 isn’t True, condition 2 is checked. If it isn’t true, condition 3 is checked so on till the last elif condition after the failure of all elif statement else statement shows in the output.

Example 1:

```python
# BMI checker by using if, elif and else statement
bmi = 32.4

# Condition is true in the third or last elif statement
if (bmi < 18.5):
    print('person is underweight')
elif (bmi < 25):
    print('person is normal')
elif (bmi < 30):
    print('person is overweight')
elif (bmi < 35):
    print('person is obese')
else:
    print('person is extremely obese')
```

As you know, the output should be:

person is obese

Example 2

```python
# In this example, we check if all elif statement fails, the output should be from else statement
temperature = 75

if (temperature < 0):
    print("it's cold outside.")
elif (temperature < 30):
   print("temperature is stable, weather is pleasant.")
elif (temperature < 50):
    print("it's hot,avoid to go outside.")
else:
    print("it's very hot, don't go outside. It will burn your skin.")
```

The output is:

it's very hot, don't go outside. It will burn your skin.

**Nested if statement:**

Nested if statements are an if statement inside another if statement. Python allows us to stack any number of if statements inside the block of another if statement. They are useful when we need to make a series of decisions.

**The general syntax is :**

if (condition):

if(condition):

Statement of nested if

else:

Statement of nested if-else

Statement of outer if

Statement outside if block

Let's learn with example:

```python
# Nested if statement
number = float(input("Enter a number: "))

if (number >= 0):
    if (number == 0):
       print("Number is zero")
    else:
       print("Number is positive")
else:
    print("Number is negative")
```

Above code first check number is greater than or equal to zero, if yes then it enters the inside if condition if the number is equal to zero then it prints "Number is zero" else "Number is positive" or if the first check is false so the output is "Number is negative". We enter the number -15, so output is:

Number is negative

**Single statement condition**

If you only need to write a single statement under if, you can write it in the same line using a single statement. It is similar to the if statement although its complete code consists of one line only.

**The general syntax is**:

if (condition): If Statement 1 ; If Statement 2; .... If Statement n

Let's learn the syntax with example,

```python
# If single statement
# complete code in one line
if (35 > 21): print("35 is greater than 21"); print("Yes, you are correct.")
```

In the above example, the condition and statement are both described in one line and the output is :

35 is greater than 21

Yes, you are correct.

**Conclusion:**

In this blog, we learned how a computer program can make decisions using any condition. We learned how to use decision-making statements like if, if-else, nested if and if-elif ladder and single statement. We have discussed all these statements with syntax and examples for better understanding. I Hope, this post will helpful for you. Kindly check my Git Hub repository https://github.com/MuhammadMairajSaleem92/Python-Concept-for-Data-Science/blob/main/Decision%20Making.ipynb
