---
title: "Python List"
author: "Aizaz Khan"
date: 2021-10-06
description: "A list is a container which holds comma-separated values (items or elements) between square brackets where items or elements need not all have the same type.In general, we can define a list as an..."
categories: ["Python"]
image: images/e12b50_b7e17aebb9f84d35af23648fbc3eb2f9.webp
wix-url: https://www.datainsightonline.com/post/python-list
---
A list is a container which holds comma-separated values (items or elements) between square brackets where items or elements need not all have the same type.

In general, we can define a list as an object that contains multiple data items (elements). The contents of a list can be changed during program execution. The size of a list can also change during execution, as elements are added or removed from it.

![](images/e12b50_b7e17aebb9f84d35af23648fbc3eb2f9.webp)

**Examples of lists:**

- numbers = [10, 20, 30, 40, 50]
- names = ["Sara", "David", "Warner", "Sandy"]
- student_info = ["Sara", 1, "Chemistry"]

## Create a Python list
**Following list contains all string:**

![](images/e12b50_52ed9758fc044c5c9c6102b0de8fc6de.webp)

**Following list contains a string, an integer and a float values:**

![](images/e12b50_a82ecc71ad8f4983a1c437b13817701d.webp)

![](images/e12b50_0c644af4d4d44728ae7cf9ae90b4a12c.webp)

**use + operator to create a new list that is a concatenation of two lists and use \* operator to repeat a list. See the following statement**s.

![](images/e12b50_818060d2050d4213ac1c3d72ca1a0c9b.webp)

## List indices:
List indices work the same way as string indices, list indices start at 0. If an index has a positive value it counts from the beginning and similarly it counts backward if the index has a negative value. As positive integers are used to index from the left end and negative integers are used to index from the right end, so every item of a list gives two alternatives indices. Let create a list called color_list with four items.
color_list=["RED", "Blue", "Green", "Black"]

ItemREDBlueGreenBlackIndex (from left) 0 1 2 3Index (from right)-4-3-2-1

If you give any index value which is out of range then interpreter creates an error message. See the following statements.

![](images/e12b50_90dd56b076c0466f93d3b6210f266b1f.webp)

**Add an item to the end of the list:**

![](images/e12b50_1d41df92e2ba41659ad0241b24d87ff2.webp)

![](images/e12b50_625bff40812f4aefb6d91626744ce611.webp)

## Insert an item at a given position:
![](images/e12b50_cc7a53371efd4ed4a9187f3a615f224f.webp)

![](images/e12b50_fa321c4ff0dc42b0aef44318c40336bf.webp)

## Modify an element by using the index of the element:

![](images/e12b50_d8fef3b22789446d96678ae42f514aec.webp)

![](images/e12b50_d98858aacfc84a6b946765e4a9e43ba1.webp)

## Remove an item from the list:

![](images/e12b50_0c0eb66c86ae4fcfb4d7fdd3b5f14f94.webp)

![](images/e12b50_e736aef832c344b9a1d62ccccd74dc0c.webp)

## Remove all items from the list:

![](images/e12b50_0370f514810f4b22b28b364c08cc788e.webp)

![](images/e12b50_b962323b05c6465b933788049a713896.webp)

## Remove the item at the given position in the list, return it

![](images/e12b50_60b7f9ced489404ea5de3e02c7f5a8d4.webp)

## Slicing list:
This refers to the items of a list starting at index startIndex and stopping just before index endIndex. The default values for list are 0 (startIndex) and the end (endIndex) of the list. If you omit both indices, the slice makes a copy of the original list.

![](images/e12b50_5a067cf6a7734dba8e9a6d634771de91.webp)

![](images/e12b50_6d7a7b9e874e4bd8bda6bcd17f92ea10.webp)

## Sort the items of the list in place:
![](images/e12b50_f2c81e1b191048b2be703414d766347e.webp)

![](images/e12b50_584e3a1cdc224a8dbe4690fcbb7eb5bf.webp)
