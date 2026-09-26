---
title: "Guess the number of oranges in a box game"
author: "mrbenjaminowusu"
date: 2021-09-19
description: "This game guesses the number of oranges in a closed box. There is a secret number that when guessed correctly, you win the game. This is a pure game by chance.I started by setting a secret number to..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/guess-the-number-of-oranges-in-a-box-game
---
This game guesses the number of oranges in a closed box. There is a secret number that when guessed correctly, you win the game. This is a pure game by chance.

I started by setting a secret number to the variable "orange_num" i.e. 13. The number times the game can be played to the variable "guess_count" i.e. 0.The limit at which the user can guess to the variable "guess_limit i.e 3.

```python
orange_num= 13
guess_count=0
guess_limit= 3
```

Using the while loop, so far as the guess_count is less than the guess_limit, the input function is called to allow the user to choose any number. Then the integer function is called on the number guessed by the user to return the numeric integer equivalent from the input function. Then the guest count is increased by one

```python
while guess_count < guess_limit:
    guess=int(input("Guess number: "))
    guess_count=guess_count+1
```

An if statement is called inside the while loop. if the guess number is the same as the orange_num. The print statement "YOU WON" returned. Then the break statement is called to break out of the loop.

```python
        if guess == orange_num:
                print("YOU WON")
                break
```

An else statement is called on the while loop if all the user fails to guess the orange_num. "SORRY, GAME OVER" is printed out.

```python
else:
    print("SORRY, GAME OVER")
```

An example of the user winning the guess game on the third try is below

```python
Guess number: 1
Guess number: 5
Guess number: 13
YOU WON
```
