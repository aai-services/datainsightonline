---
title: "A Simple Cards Draw Game using Python"
author: "Hamza kchok"
date: 2021-09-19
description: "In this post, I'll present to you the mini card drawing game in which the user can draw from 1 up to 5 cards and see if he won against the computer.The winner is decided by the sum of drawn card..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/a-simple-cards-draw-game
---
In this post, I'll present to you the mini card drawing game in which the user can draw from 1 up to 5 cards and see if he won against the computer.

The winner is decided by the sum of drawn card values which range from 1 to 13.

For starters, we make sure to explain the rules to the user (and to you the reader ;) )

```python
print('''Hello\n
Welcome to this simple card draw game, How lucky are you feeling today?
The minimum draw value is 1 and the maximum draw value is 15
You will have a maximum of 5 a draws but you can choose to reveal cards whenever you want if you feel like you have a higher count that the computer\n
The computer will always have to draw the same number of cards as you! so don't worry it won't have more cards!
Best of luck!''')
```

First, we make sure to initialize some variables that will need:

- The list of user cards
- The list of computer cards
- The maximum number of draws
- Initialize the current draw to zero as the game still hasn't begun.

```python
user_cards = list()
computer_cards = list()
draws = 5
current_draw = 0
```

After the explanation part and variables' initialization, the first draw will happen and the user will have the choice to continue drawing till he draws a maximum of 5 cards if he sees fit. At each draw, we make sure the draw is uniform and as fair as possible for both players. For that, we use the "randint" function in the random package of "numpy".

```python
import numpy as np
while current_draw < draws and cont == True:
    u_d = np.random.randint(1,13)
    c_d = np.random.randint(1,13)

    user_cards.append(u_d)
    computer_cards.append(c_d)

    print('You drew a {}'.format(u_d))
    print('your current deck is {}'.format(user_cards))
    if current_draw == 4:
        print('That was the final draw, let\'s see if you\'ll win or not ;) ')
        break
    c = input('Do you want to continue drawing? [y]/n\t')
    if c == 'n':
        break
    current_draw+=1
```

Finally, after counting the sum of both players' cards, we tell the user who won this mini-game!

To calculate the sum of cards we simply use the "sum" function predefined in python.

```python
c_cs = sum(computer_cards) #computer cards sum
u_cs = sum(user_cards) #user cards sum
if c_cs > u_cs:
    print('Oh oh, that\'s unlucky! the computer won with a score of {} (computer) against {} (you)'.format(c_cs,u_cs))
elif u_cs > c_cs:
    print('Congratz!!! You won with a score of {}(you) against {} (computer)'.format(u_cs,c_cs))
else:
    print('This is pretty rare but this was a draw with a both having a sum of'.format(u_cs))
```

I hope this was worth your reading time!

The link to the code is [here](https://github.com/zqngetsu96/DataInsight_Assignments_and_projects/blob/main/Assignment%201/Card%20Draw%20Game.ipynbhttps://github.com/zqngetsu96/DataInsight_Assignments_and_projects/blob/main/Assignment%201/Card%20Draw%20Game.ipynb).
