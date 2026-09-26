---
title: "How can I count the number of character occurrence in a sentence"
author: "Gehad Hisham"
date: 2022-01-22
description: "In this blog, I would explain how I create a function to count the number of occurrences of a given character in a given word, phrase, or sentence.And also create a function to count the number of..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/how-can-i-count-the-number-of-character-occurrence-in-a-sentence
---
In this blog, I would explain how I create a function to count the number of occurrences of a given character in a given word, phrase, or sentence.

And also create a function to count the number of occurrences of a given word in a given phrase or a sentence.

**Count the occurrence of a char**

*# A function to count the occurrence of a char in a word or a sentence*
**def** countOccChar(sent, char):
 sent **=** sent.lower() *[#turn](https://www.datainsightonline.com/blog/hashtags/turn) the sentence to lower case*
 char **=** char.lower() *[#turn](https://www.datainsightonline.com/blog/hashtags/turn) the char to lower case*
 count **=** 0 *[#A](https://www.datainsightonline.com/blog/hashtags/A) counter to count the occurrence of the character*
​
 **for** c **in** sent : *[#loop](https://www.datainsightonline.com/blog/hashtags/loop) over the sentence*
 **if** c **==** char: *[#Check](https://www.datainsightonline.com/blog/hashtags/Check) if the char is the same as the iterator*
 count **+=**1 *[#Count](https://www.datainsightonline.com/blog/hashtags/Count) the occurrence*
 **return**(count)

**Count the occurrence of a word**

*# A function to count the occurrence of a word in a sentence*
**def** countOccWord(sent, word):
 sent **=** sent.lower() *[#turn](https://www.datainsightonline.com/blog/hashtags/turn) the sentence to lower case*
 word **=** word.lower() *[#turn](https://www.datainsightonline.com/blog/hashtags/turn) the word to lower case*
 count **=** 0 *[#A](https://www.datainsightonline.com/blog/hashtags/A) counter to count the occurrence of the character*
​  [#Remove](https://www.datainsightonline.com/blog/hashtags/Remove) punctuations from the sentence
 punctuations **=** '''!()-[]{};:'"\,<>./?@#$%^&\*_~'''
 no_punct **=** ""
 s **=** sent.split(" ") *[#Split](https://www.datainsightonline.com/blog/hashtags/Split) the sentence by space*
 **for** char **in** sent: *[#loop](https://www.datainsightonline.com/blog/hashtags/loop) over the sentence*
 **if** char **not in** punctuations: *[#To](https://www.datainsightonline.com/blog/hashtags/To) remove the punctuations*
 no_punct **=** no_punct **+** char
 s **=** no_punct.split(" ")
​
 lensent **=** len(s) *[#get](https://www.datainsightonline.com/blog/hashtags/get) the length of a sentence*
​
 **for** c **in** range(0,lensent) :
 **if** word **==** s[c]:
 count **+=**1 *[#Count](https://www.datainsightonline.com/blog/hashtags/Count) the occurrence of a word*
 **return**(count)
​

Check the code from here: [geehaad](https://github.com/geehaad/Writing-Simple-Apps-with-Python/tree/main/Count%20character%20occurrences%20in%20a%20given%20word%2C%20phrase%20or%20sentence)
