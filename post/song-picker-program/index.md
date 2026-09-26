---
title: "Song Picker Program using Python"
author: "Teresa Rady"
date: 2021-09-20
description: "This simple python program aims at taking the users' preference of genre then recommending a random song to listen to from this genre.print('what genre do you prefer ?') user_pick =..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/song-picker-program
---
This simple python program aims at taking the users' preference of genre then recommending a random song to listen to from this genre.

```python
print('what genre do you prefer ?')
user_pick = input().casefold()
```

This part prints a question to the user and receives the answer in the form of string. The casefold here ignores the entry of capital or small letters in the input.

In the next lines of code we define the songs under each genre as a list.

```python
blues = ['I Cant Quit You Baby – Otis Rush.' ,
"I'd Rather Go Blind – Etta James." ,
'Crossroad Blues – Robert Johnson.' ,
'Pride and Joy – Stevie Ray Vaughan.',
"I'm Tore Down – Freddy King. " ,
"Born Under A Bad Sign – Albert King." ,
'Sunshine of Your Love – Cream.' ,
'Hoochie Coochie Man – Muddy Waters.' ]
```

```python
jazz = ["All The Things You Are." ,
"Georgia On My Mind.",
"Body and Soul.",
"Fly Me to the Moon." ,
"Night and Day."]
```

```python
rock = ["Skullcrusher",
"Spirit of the Beehive",
"For Your Health",
"Thirdface",
"Iceage",
"Wolf Alice"]
```

```python
country = ["I Walk the Line" ,
"Jolene" ,
"Friends in Low Places",
"Choices" ,
"Concrete Angel" ,
"Kiss an Angel Good Morning" ,
"Where Were You",
"Live Like You Were Dying" ]
```

```python
dance = ["We Are Family" ,
"The Hustle",
"I Will Survive" ,
"Thank You"]
```

```python
genre = ["blues", "jazz" , "rock" , "country" , "dance"]
```

In the next section we import random method and use a for loop to match the user's input with the song outcome. The random.choice chooses a random song from the genre list chosen by the user.

If the user chose a genre that is not listed the function prints "pick another genre".

```python
import random
i = user_pick
```

```python
for i in genre :
    if user_pick == "blues":
        blues_song = random.choice(blues)
        print(blues_song)
        break
    elif user_pick == "jazz" :
        jazz_song = random.choice(jazz)
        print(jazz_song)
        break
    elif user_pick == "rock" :
        rock_song = random.choice(rock)
        print(rock_song)
        break
    elif user_pick == "country":
        country_song = random.choice(country)
        print(country_song)
        break
    elif user_pick == "dance" :
        dance_song = random.choice(dance)
        print(dance_song)
        break
    else:
        print("pick another genre")
        break
```
