---
title: "Rock Paper and Scissor"
author: "Sabin Panta"
date: 2022-05-10
description: "From an early age, we have been playing Rock Paper, and scissors with our friends mostly either in a duel or to make a group in a football match. Sometimes, a losing one has to be a keeper(Sadly, I..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/rock-paper-and-scissor
---
From an early age, we have been playing Rock Paper, and scissors with our friends mostly either in a duel or to make a group in a football match. Sometimes, a losing one has to be a keeper(Sadly, I lost most of the time).

import random
game=['R','P','S']
computer_action=random.choice(game)
print(computer_action)
user_action=input("Rock Paper Scissor(R/P/S):").upper()
if user_action == computer_action:
 print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "R":
 if computer_action == "S":
 print("Rock smashes scissors! You win!")
 else:
 print("Paper covers rock! You lose.")
elif user_action == "P":
 if computer_action == "R":
 print("Paper covers rock! You win!")
 else:
 print("Scissors cuts paper! You lose.")
elif user_action == "S":
 if computer_action == "P":
 print("Scissors cuts paper! You win!")
 else:
 print("Rock smashes scissors! You lose.")

The code is as simple as it looks. First, we have to import random modules in Python which allow us to choose randomly from our given choice(here it's either Paper, Rock, or Scissor as defined by the list "game"). The input function allows users to enter the value. ".upper()" changes the string value in upper case given the value is in lower case to allow for the later conditional procedure. The loops are quite easy to figure out. If the user enters Paper, there is only one way he could win and one way he could lose as shown in the conditional statement. Thus the coding task is solved. Congratulation on creating your first game.
