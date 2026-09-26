---
title: "How to write a program that generates passwords?"
author: "Bah Alain Sei"
date: 2021-09-14
description: "As part of the Data Science training program, we were asked to choose a project to be carried out followed by a project of their choice. My choice of work fell on the project concerning password..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/how-to-write-a-program-that-generates-passwords
---
```python
As part of the Data Science training program, we were asked to choose a project to be carried out followed by a project of their choice. My choice of work fell on the project concerning password generation.
```

import string

import random

lettres=string.ascii_letters

chiffres= string.digits

ponc= string.punctuation

while True:

try:

ulettres= eval (input("Lettres (True ou False): "))

uchiffres= eval (input("Chiffres (True ou False): "))

uponc = eval(input("Ponctuation (True ou False): "))

L=int(input("Longueur du mot de passe: "))

char = ""

char += Lettres if ulettres else ""

char += chiffres if uchiffres else ""

char += ponc if uponc else ""

passe ="".join(random.choices(char, k=l))

print(passe)

except:

print("veillez suivre les instructions")

try:

if eval(input("Quitter (True ou False): ")):

break

except:

print("Veuillez suivre les instructions")
