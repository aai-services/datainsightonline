---
title: "\"Guess the word\" game"
author: "pranita shrestha"
date: 2021-09-17
description: "\"Guess the word\" game is a fun game for anyone who wants to improve their vocabulary. It can also be a great time-pass for anyone who is bored or needs a small break. In this game, one is given a..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/guess-the-word-game
---
"Guess the word" game is a fun game for anyone who wants to improve their vocabulary. It can also be a great time-pass for anyone who is bored or needs a small break. In this game, one is given a word and the person has to keep guessing a letter. Usually, they are give 3 to 5 chances. If they guess the word within the given chance then "Yay" and if not then that's a "Fail". We can easily create the "Guess the word" game in Python.

So, let's start coding!!!!!

**Step 1:**

In the first step, we will need to declare the list of words that can be used for guessing. Here, we have put those words in an array called **words**. We have also initialized a variable called **chance**, which will contain the number of chance the game will provide to the user.

```python
# the list of words to guess
words = ["aeroplane", "bicycle", "doormat", "encyclopedia"]

# number of chances
chance = 3
```

**Step 2:**

In the second step we will create a function called **create_guess_word()**. In this function we will place the code which will randomly select a word to guess from the list of words. We will be using the random package's choice() method for this purpose. The **random.choice()** method requires a list from which it can randomly select an element. The randomly selected word is stored in a variable called **guess_word** and lower() method is also applied to it so that all the letters of the word is in lowercase.

```python
import random

# randomly select a word from the list
def create_guess_word():
    guess_word = random.choice(words)
    guess_word = guess_word.lower()
    return guess_word
```

**Step 3:**

The entire code in the third step will be placed in a function called **guess_game()**. The initial step is to call the **create_guess_word()** function and store the randomly selected word in guess_word variable. We will also initialize a try counter called **try_val** which will count the number of failed tries. A string with the exact number of dashes as the word will be shown to the player so that they will have an idea of how long the word is.

```python
# the guess game
def guess_game():
    # get the guess word
    guess_word = create_guess_word()

    # the try counter
    try_val = 0
    print("Guess the word:\n")
    dash_str = ""
    for i in range(0, len(guess_word)):
        dash_str += "___ "

    # print the same number of dashes as that of the word
    print(dash_str)
```

We will need to initialize an array called **letter_check** which will store the list of letters that the user have inputted throughout the game. The **correct_letter** array will store the list of correct letters inputted by the player. The **unique_guess_letter_len** variable contains the length of unique letters in the guess_word varaible. To obtain the unique letter, we will use the **set()** method.

```python
# the list of letters inputted
letter_check = []

# the list of correct letters
correct_letter = []

# the length of unique letters in a word
unique_guess_letter_len = len(set(guess_word))
```

We will use the **while** loop to ensure that the number of tries (**try_val**) is not more than the given chance and the player hasn't guessed the entire word. As long as **len(correct_letter) < unique_guess_letter_len**, then the word to be guessed is not complete.

The player is then asked to guess a letter and input it which is stored in a variable called letter. The **lower()** method is applied to the letter varaible. The next step is to check whether or not the input letter is in the letter_check array. If the letter hasn't been checked before then the program will proceed with the if loop and if not it will diverted to the else loop where the player will receive a prompt informing the player that the letter has already been inputted.

After ensuring that the letter hasn't been inputted before, the letter will be added to **letter_check** list for future check. Then we will check if the letter exists in the **guess_word** or not. If the letter exists then the **dash_str** will be reinitialized and the letter will be added to the **correct_letter** array. We will loop the letters in the **guess_word** to put the correct letter instead of dashes (___) in the right place. A prompt will also be shown to the player stating that the letter guessed is correct. If the player has guessed the entire word then the program will go to the break block and end the loop.

Similarly, if the letter that has been guessed is wrong and doesn't exist in the word, then a prompt will be given to the player that the letter doesn't exist and the **try_val** counter will be incremented. If all chances has been used the while loop will come to an end. If the user still has some chance, a message to guess the word again will be shown.

```python
# repeat until try_val counter is less than 3 (i.e. the user has failed to guess the word) and
 # the length of correct letter is as same as  unique_guess_letter_len (i.e. the user has guessed the word)
while(try_val < chance and len(correct_letter) < unique_guess_letter_len):
        print("\nGuess a letter and input it:")
        letter = input().lower()
        # check if the input letter is not in the letter_check array
        if letter not in letter_check:
            letter_check.append(letter)

            # if the letter is in the guess_word
            if letter in guess_word:
                dash_str = ""
                print("\nThe letter {} is in the word.\n".format(letter))
                correct_letter.append(letter)
                for i in guess_word:
                    # add the letter instead of the dash (___)
                    if i in correct_letter:
                        dash_str += i
                    else:
                        dash_str += " ___ "

                # to check if the player has guessed the entire word
                if len(correct_letter) == unique_guess_letter_len:
                    break
            else:
                # if the guessed letter is not correct
                print("\nThe letter \033[1m {} \033[0m is not in the word.\n".format(letter))
                try_val += 1
                print("\nYou have {} chances left.\n".format(chance - try_val))

                # if the try_val counter reaches the same value as chance, chance is over
                if try_val == chance:
                    break
        else:
            # if the user has already tried the letter before
            print("\nYou have already tried the letter \033[1m {} \033[0m before.".format(letter))

        print("Guess the word again:\n")
        print(dash_str)
```

If the player successfully guesses the word then show them the "Congratulations" message along with the given word and if they have failed to guess the word then show the "Failed" message. Also, ask them if they want to play the game again. If yes, call the **guess_game**() function again and if not, just continue with the code.

```python
# if the player successfully guesses the word
if len(correct_letter) == unique_guess_letter_len:
	print("Congratulations!! You have successfully guessed the word \033[1m {} \033[0m.".format(guess_word))
        print("Do you want to play again Y/N ?")
    # if the player fails to guess the word
else:
        print("Oh no!! You were not able to guess the word. Do you want to play again Y/N ?")

try_again = input().lower()
if try_again == "y":
	guess_game()
```

Here, is the snippet of the entire code.

```python
# Guess the word

# the list of words to guess
words = ["aeroplane", "bicycle", "doormat", "encyclopedia"]

# number of chances
chance = 3

import random

# randomly select a word from the list
def create_guess_word():
    guess_word = random.choice(words)
    guess_word = guess_word.lower()
    return guess_word

# the guess game
def guess_game():
    # get the guess word
    guess_word = create_guess_word()
    # the number of try check counter
    try_val = 0
    print("Guess the word:\n")
    dash_str = ""
    for i in range(0, len(guess_word)):
        dash_str += "___ "

    # print the same number of dashes as that of the word
    print(dash_str)

    # the list of letters inputted
    letter_check = []

    # the list of correct letters
    correct_letter = []

    # the length of unique letters in a word
    unique_guess_letter_len = len(set(guess_word))

    # repeat until try_val counter is less than 3 (i.e. the user has failed to guess the word) and
    # the length of correct letter is as same as  unique_guess_letter_len (i.e. the user has guessed the word)

    while(try_val < chance and len(correct_letter) < unique_guess_letter_len):
        print("\nGuess a letter and input it:")
        letter = input().lower()
        # check if the input letter is not in the letter_check array
        if letter not in letter_check:
            letter_check.append(letter)

            # if the letter is in the guess_word
            if letter in guess_word:
                dash_str = ""
                print("\nThe letter {} is in the word.\n".format(letter))
                correct_letter.append(letter)
                for i in guess_word:
                    # add the letter instead of the dash (___)
                    if i in correct_letter:
                        dash_str += i
                    else:
                        dash_str += " ___ "

                # to check if the player has guessed the entire word
                if len(correct_letter) == unique_guess_letter_len:
                    break
            else:
                # if the guessed letter is not correct
                print("\nThe letter \033[1m {} \033[0m is not in the word.\n".format(letter))
                try_val += 1
                print("\nYou have {} chances left.\n".format(chance - try_val))

                # if the try_val counter reaches the same value as chance, chance is over
                if try_val == chance:
                    break
        else:
            # if the user has already tried the letter before
            print("\nYou have already tried the letter \033[1m {} \033[0m before.".format(letter))

        print("Guess the word again:\n")
        print(dash_str)

    # if the player successfully guesses the word
    if len(correct_letter) == unique_guess_letter_len:
        print("Congratulations!! You have successfully guessed the word \033[1m {} \033[0m.".format(guess_word))
        print("Do you want to play again Y/N ?")
    # if the player fails to guess the word
    else:
        print("Oh no!! You were not able to guess the word. Do you want to play again Y/N ?")

    try_again = input().lower()
    if try_again == "y":
        guess_game()

guess_game()
```
