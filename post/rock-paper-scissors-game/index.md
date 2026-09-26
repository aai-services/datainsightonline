---
title: "Rock-Paper-Scissors Game"
author: "abdelrahman.shaban7000"
date: 2021-09-06
description: "In this blog, we will create a program for a rock, paper, and scissors game that consists of a human player and a computer. So to do that we will divide the program into two functions so let's..."
categories: ["General"]
image: images/33c957_dccb5b9749c14f97bd85d146485bbc87.webp
wix-url: https://www.datainsightonline.com/post/rock-paper-scissors-game
---
In this blog, we will create a program for a rock, paper, and scissors game that consists of a human player and a computer. So to do that we will divide the program into two functions so let's start:

**First function**

```python
def is_win(player,computer):
    ''' This function will return true if the player wins '''
     if (player=='r' and computer =='s') or (player =='s' and computer=='p') or (player =='p' and computer =='r'):
              return True
```

In this function, we specify when should the human player win, and this is done by if statement e.g. if the player selects ' r ' for rock and the computer selects ' s ' for scissors so the human player will win and so on.

**Second function**

```python
import random

def play():
     user=input("Choose one==> 'r' for rock, 'p' for paper, 's' for scissors  ")
     computer=random.choice(['r','p','s'])

     if user==computer:
        print('computer\'s choice ==> ',computer)
        return 'tie'

     if is_win(user,computer):
        print('computer\'s choice ==> ',computer)
        return 'You win!'

     else:
        print('computer\'s choice ==> ',computer)
        return 'You lost'
```

In this function, we will implement when each one of the players the human player or the computer should when so we created two variables one for a human player to select one of the options and another variable for the computer which we used the random module to generate random number through it. then we check for each case as follows: if both the human player and the computer choose the same option then no one will win and if the human player wins and we used the previous function '*is win*' to check for this condition and if neither of these conditions met then the computer player will win.

**Example for the output :**

```python
print(play())

Choose one==>'r' for rock,'p'for paper, 's' for scissors=>  p
 computer's choice ==>  s
You lost
```

link for the GitHub repo [here](https://github.com/Abdelrahman7000/data_insight_rock_paper_scissors)
