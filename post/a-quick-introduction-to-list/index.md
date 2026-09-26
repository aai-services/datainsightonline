---
title: "A Quick Introduction to Lists in Python"
author: "Rubash Mali"
date: 2021-10-04
description: "Lists in python are mutable ordered sequence datatype. They are heterogenous i.e. each item in the list doesn't need to be of the same type. In this blog we will discuss about list and some of..."
categories: ["Python"]
image: images/0a8409_e90e40458e11417c9972834626e1766f.webp
wix-url: https://www.datainsightonline.com/post/a-quick-introduction-to-list
---
Lists in python are mutable ordered sequence datatype. They are heterogenous i.e. each item in the list doesn't need to be of the same type.

In this blog we will discuss about list and some of popular concepts and functionalities associated with lists.

**1. Creating a list :-** We can create a list using square brackets ' [] ' and separating elements using commas ' , '. An example can be seen below:

```python
list_example=["Mac", "Windows", "Linux"]
print(list_example)
print(type(list_example))
#Output
['Mac', 'Windows', 'Linux']
<class 'list'>
```

Similarly an empty list can also be initialized without any element.

```python
empty_list=[] #empty list
```

**2.Diffrent types of list :-** A list can be of any datatype.

```python
list1=["apple", "mango", "orange"] # list of strings
list2=[1,2,3]                   # list of integers
list3=[True, False, False]        # Boolean List
```

As mentioned earlier a list can contain items having more than one data type. Below is an example:

```python
mix_list=["apple",2,False]
```

**3.Accessing Items of a list:-** As list is an ordered sequence so its items can be accessed by calling the list name followed by square brackets. Inside the squared bracket we mention the position of the item.

Python is zero indexed i.e. first element in a sequence is at position zero.

Also the last item is at index -1 regardless of the list's length.

```python
list1=["apple","mango","orange","grape","banana"]
print(list1[0])
print(list1[1])
print(list1[-1])
#Output
apple
mango
banana
```

For accessing more than one element of the list we can slice the list by mentioning the start index followed by ' : ' and end index(exclusive) inside the square brackets.

```python
# Slicing
# Start index : End index (Exclusive)
list1=["apple","mango","orange","grape","banana"]
print(list1[1:3])
#Output
['mango', 'orange']
```

**4 Changing List Items:-**Since lists are mutable so we can change the items of a list. This can be done using assignment operator ' = ' followed by the changed item.

```python
my_list=["HP","Dell","MSI","Lenovo"]
print(my_list)
my_list[0]="Acer"
print(my_list)
#Output
['HP', 'Dell', 'MSI', 'Lenovo']
['Acer', 'Dell', 'MSI', 'Lenovo']
```

We can also modify more than one item in the list by using the concept of slicing and assignment operator. Slicing allows us to select the sub list that is to be modified.

```python
my_list=["HP","Dell","MSI","Lenovo"]
my_list[0:2]=["Asus","Acer"]
print(my_list)
#Output
['Asus', 'Acer', 'MSI', 'Lenovo']
```

**5.Adding new item to the list:-** One can easily add new item to the list using the append function. Append function takes the item that is to be added to the list as a parameter. The new item is added at the end of the list.

```python
my_list=["HP","Dell","MSI","Lenovo"]
my_list.append("Acer")
print(my_list)
#Output
['HP', 'Dell', 'MSI', 'Lenovo', 'Acer']
```

We can also concatenate an entire list to other using the extend function as shown in the example below :

```python
list1=["HP","Dell","MSI"]
list2=["Lenovo","Acer"]
print(list1.extend(list2))
#Output
['HP', 'Dell', 'MSI', 'Lenovo', 'Acer']
```

**6.Removing Item From a List:-** We can use the pop method to remove item based on their index.

```python
my_list=["HP","Dell","MSI","Lenovo"]
my_list.pop(1)
print(my_list)
#Output
['HP', 'MSI', 'Lenovo']
```

We can also use the remove method to remove item from a list . In the remove method we mention the item itself that is to be removed.

```python
my_list=["HP","Dell","MSI","Lenovo"]
my_list.remove("MSI")
print(my_list)
#Output
['HP', 'Dell', 'Lenovo']
```

**7.Looping through the List:-**We can easily loop through the items of a list using the For loop. The For loop runs for each item in the list.

```python
my_list=["HP","Dell","MSI","Lenovo"]
for item in my_list:
    print(item)
#Output
HP
Dell
MSI
Lenovo
```

Another variation for looping through a list is using the range and len function along with For loop. This allows more flexibility and access to index of the list.

```python
my_list=["HP","Dell","MSI","Lenovo"]
for i in range(0,len(my_list)):
    print("List Item at Index "+ str(i)+" is "+my_list[i])
#Output
List Item at Index 0 is HP
List Item at Index 1 is Dell
List Item at Index 2 is MSI
List Item at Index 3 is Lenovo
```

You can find the GitHub repo of this code through this [link](https://github.com/rubash9849/data_inisghts/blob/main/List.ipynb)
