---
title: "Guessing Game"
author: "bismark boateng"
date: 2021-09-20
description: "This is an interactive app where the program accepts input from the user , the app randomly generate a value between the two user's input and the user is made to guess the number the app generated.I..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/guessing-game
---
This is an interactive app where the program accepts input from the user ,

the app randomly generate a value between the two user's input and the user is made to guess the number the app generated.

I started by importing the libraries

*[#importing](https://www.datainsightonline.com/blog/hashtags/importing) libraries*

**import** **random**

*[#taking](https://www.datainsightonline.com/blog/hashtags/taking) user inputs*
lowValue = int(input("LOWEST VALUE: "))
highValue = int(input("HIGHEST VALUE: "))

The code snippet above takes the range in which the guess number will be generated

*[#generating](https://www.datainsightonline.com/blog/hashtags/generating) random between lowValue and highValue* y=random.randint(lowValue,highValue)

print(f"you have 3 chance to get it right!")

This code generate a random number between lowValue and highValue

and tells the user there are only 3 chances

```python
#starting the counter
count = 0
```

The variable count is initialized to count the trials the user will make

```python
#user has only 3 chances to get it right
    while count < 3:
        count += 1

        #allowing the user to guess as an input
        guess = int(input("Guess a number: "))

        #testing if the user guess correct
        if y == guess:
            print(f"Congratulations, you guessed right in {count} try")
            break

        elif  y < guess:
        print("You guessed too high!")

        elif y > guess:
        print("You guessed too small!")

   if count >= 3:
       print(f"The number is {y}")
```

In the while loop, the user is asked to input a number the computer generated ( guess variable)

if it happens to be correct, the program prints out a feedback and exit

the while loop

if the value is too high, the program output that

and if it is too low, the program output that also

if the user is not able to get the number after three attempts, the app prints out the output
