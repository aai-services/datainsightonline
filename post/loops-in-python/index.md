---
title: "Loops in Python"
author: "Isuru Lakshan"
date: 2021-10-11
description: "Today we are going to talk about the most crucial concept in any programming language in this world. If we do something in a loop It also means that we do something over and over again. Some may..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/loops-in-python
---
Today we are going to talk about the most crucial concept in any programming language in this world. If we do something in a loop It also means that we do something over and over again. Some may think why someone would do things in a loop. Nobody likes it, right?? But most of the things we do in day to day life is repetitive tasks in a loop. We get up every morning, brush teeth, get dressed, get breakfast, go to work so much repetitive things.

yeah, I understand you, that is boring.

That's why we create computers in the first place. since we do not like it. we give those tasks to someone else. That is human nature right?? The computers like to do these repetitive tasks and they are also very fast making them the ideal ones for this line of work.

Since we understand the importance of loops, let's move on to understand how looping is done in the programming world. More specifically here we talk about Loops in python language.

In python, there are mainly two types of loops we use, they can be identified as,

1. For Loops
2. While loops

Usage of these loops mainly depends on the situation and the common practice and the experience of the programmer.

The important point to note here is we can interchange these loops. which means we can change for loops to while loops or while loops to for loops if we want. But based on the scene using one type of loop may be easy compared to other types of loop.

**FOR LOOPS**

FOR loops are by my experience the most used loop, when I considered specifically python language. That is because python for loops have nice implementations which we can use on varies situations. It is easy to use and more understandable compared to while loops.

1. **for loop to iterate over a finite number of times**

for i in range(10):
 print(i)

above code snippet will execute the print command 10 times.

2. **for loop to Iterate over items of an array.**

cars = ["ford", "lamborghini", "toyota"]
for x in cars:
 print(x)

above code snippet will iterate over the array and print each element.

3. **for loop to loop over characters of a string**

for x in "datasciene":
 print(x)

above code snippet will print each character one by one.

**WHILE LOOPS**

While loops iterate over a loop over and over again until a particular condition is met.

i = 1
while i < 10:
 print(i)
 i += 1

The above code snippet will execute the loop over and over again until the ' i ' variable is less than 10.

**FORCE STOP A LOOP FROM EXECUTING**

There may be situations that we want to stop a loop from moving forward these times we can use ' break ' keyword to do that. When the loop gets to the break keyword it stops and jumps to the end of the loop and start executing from there.

Example:

i = 1
while i < 10:
 print(i)
 if i == 5:
 break
 i += 1

Above code snippet, the loop will break when ' i ' hits 5 rather than going up to 10.

**SKIP SOME CODE SNIPPET FROM EXECUTING IN A LOOP**

As well as stopping a loop there is another important functionality that we want to use when we work with loops. That is skip from executing. we use the ' continue ' keyword to state this in the code. What this keyword does is stop at this point and start from the beginning without breaking it. This is the difference between continue and break. break just breaks the loop and continue just continue the loop as the name implies in both keywords. so it's easy to remember and use. both keywords stop the execution of the next instructions which is thereafter the keyword.

Example:

i = 0
while i < 10:
 i += 1
 if i == 6:
 continue
 print(i)

The above code snippet will print 1 to 10 except number 6. Why?? it skips print command when ' i ' hits to 6. but not stopped the loop like in the previous case.

I hope this article will help you. Thank you for reading.
