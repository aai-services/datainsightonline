---
title: "Simple Apps written in Python"
author: "mohamed bahgat"
date: 2022-09-22
description: "1) This Program is designed to count character occurrences in a given word, phrase or sentence.If the word is empty, then \"The chosen word is empty\" will be printed out, if not, then it will check if..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/simple-apps-written-in-python
---
**1) This Program is designed to count character occurrences in a given word, phrase or sentence.**

If the word is empty, then "The chosen word is empty" will be printed out, if not, then it will check if you have chosen any letter to check its occurrence in the word and print out the final result, and you did not choose any letter the program will show the count the occurrences of the for each letter in the chosen word.

def count_char(word, char = ''):

if word == '':

print('The chosen word is empty')

else:

word = word.lower()

if char == '':

print('since you did not specify and enter any character to be counted, so here is the count of the occurrences of the all characters in your chosen word.')

output = {}

for i in word:

if i in output:

output[i] += 1

else:

output[i] = 1

print(output)

else:

char = char.lower()

count = 0

for i in word:

if i == char:

count += 1

print('The char {} has been found in this word {} {} times.'.format(char, word, count))

count_char('00000')

count_char('koootyy')

count_char('Mohamed Bahgat Salah', 'a')

count_char(''Mohamed Bahgat Salah', 's')

**2) This program is designed to change currency to be in Egyptian Pounds format.**

It checks first if the amount of the money is Zero then the output will be Zero as well, and if it is not Zero then starts to convert it by checking the type of currency in order to calculate the correct percentage between it and the Egyptian Pound, then print out the result.

def to_egy_pound (amount, currency):

currency = currency.upper()

if amount == 0:

return 0

else:

if currency == 'USD':

output = amount \* 21.23

elif currency == 'EUR':

output = amount \* 15.76

elif currency == 'GBP':

output = amount \* 24.30

elif currency == 'KWD':

output = amount \* 64.41

return output

print(to_egy_pound(0, 'USD'), "L.E")

print(to_egy_pound(500, 'USD'), "L.E")

print(to_egy_pound(500, 'EUR'), "L.E")

print(to_egy_pound(500, 'GBP'), "L.E")

print(to_egy_pound(500, 'KWD'), "L.E")
