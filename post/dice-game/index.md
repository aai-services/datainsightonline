---
title: "Dice Game Simulation with Python"
author: "Kala Maya Sanyasi"
date: 2021-09-17
description: "This is a simple python code for rolling a six sided dice. The program simulates two players and declares the winner to the player who gets the highest number while rolling the dice.For this program..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/dice-game
---
This is a simple python code for rolling a six sided dice. The program simulates two players and declares the winner to the player who gets the highest number while rolling the dice.

For this program I have used random module to generate a random number. To evaluate the winner I have used if, elif, else statement.

Below is the full program code for the Dice Game.

```python
#importing random module to generate random number
import random
#Get random number between 1 and 6 for each players
player1_score = random.randint(1,6)
player2_score = random.randint(1,6)
#display the result
print('Player 1 scored : ' + str(player1_score))
print('player 2 scored : ' + str(player2_score))
#winner declaration
if player1_score > player2_score :
    print('Player 1 won')
elif player1_score < player1_score :
    print('Player 2 won')
else:
print('It is a draw')
```

Here is the explanation of each part of the code.

First we import random module to generate the random number. The randint() method takes two integer values separated by a comma. The randint(1,6) will generate any random number between 1 and 6 including 1 and 6. Two different random numbers are assigned to the variable player1_score and player2_score.

```python
#importing random module to generate random number
import random
#Get random number between 1 and 6 for each players
player1_score = random.randint(1,6)
player2_score = random.randint(1,6)
```

The next part of the code is used to display what random numbers each player has got.

```python
#display the result
print('Player 1 scored : ' + str(player1_score))
print('player 2 scored : ' + str(player2_score))
```

The last part of the code is for the declaration of the winner which is done by using if, elif and else statement. The code checks which player has got the highest number and declares that player as the winner, if both the players has the same number it says it is a draw.

```python
#winner declaration
if player1_score > player2_score :
    print('Player 1 won')
elif player1_score < player1_score :
    print('Player 2 won')
else:
    print('It is a draw')
```
