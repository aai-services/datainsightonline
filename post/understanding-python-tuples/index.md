---
title: "Understanding Python Tuples"
author: "Rashidat Sikiru"
date: 2021-10-06
description: "Tuples are a core data structure in Python. They let you store an ordered sequence of items. For example, a tuple may be used to store a list of employee names. You could use a tuple to store a list..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/understanding-python-tuples
---
Tuples are a core data structure in Python. They let you store an ordered sequence of items. For example, a tuple may be used to store a list of employee names. You could use a tuple to store a list of ice cream flavors stocked at an ice cream shop. A tuple is a comma-separated sequence of items. This sequence is surrounded by parenthesis (). Let’s create a tuple:

```python
this_tuple = ('Chocolate', 'Vanilla', 'Mint', 'Strawberry', 'Choc-Chip')
```

The code above returns:

```python
('Chocolate', 'Vanilla', 'Mint', 'Strawberry', 'Choc-Chip')
```

#### Features of Tuple
1. Tuples are used to store multiple items in a single variable.

2. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

3. A tuple is a collection which is ordered and unchangeable.

4. Tuples are written with round bracket.

**Tuple Items:**

Individual values in a tuple are called items. The following are features of tuple items.

1. **Tuple items are ordered:**When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

2. **Unchangeable:**  meaning that we cannot change, add or remove items after the tuple has been created.

3. **Indexing:** Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

4. **Allow duplicate values:** Since tuples are indexed, they can have items with the same value.

For example:

```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```

Then output is:

```python
('apple', 'banana', 'cherry', 'apple', 'cherry')
```

#### Tuple Length:

To determine how many items a tuple has, use the len() function.

Example:

```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```

Output:

```python
3
```

#### Create Tuple With One Item:

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

Example:

One item tuple, remember the comma:

```python
thistuple = ("apple",)
print(type(thistuple))
```

This returns a item as as tuple:

```python
<class 'tuple'>
```

When there is no comma at end of single tuple item, python returns a string.

```python
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
```

Output:

```python
 <class 'str'>
```

#### Tuple Items - Data Types

Tuple items can be of any data type: String, int and boolean data types:

For example:

```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```

#### The tuple() Constructor

It is also possible to use the tuple() constructor to make a tuple

Example:

Using the tuple() method to make a tuple:

```python
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

Output:

```python
('apple', 'banana', 'cherry')
```

#### Accessing Tuple Items
You can access tuple items by referring to the index number, inside square brackets:

Example:

Print the second item in the tuple:

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
```

Output:

```python
banana
```

**Note:** The first item has index 0.

#### Negative Indexing

Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.

Example: Print the last item of the tuple:

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
```

Output:

```python
cherry
```

#### Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new tuple with the specified items.

Example:

Return the third, fourth, and fifth item

```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
```

Output:

```python
('cherry', 'orange', 'kiwi')
```

**Note:** The search will start at index 2 (included) and end at index 5 (not included). Remember that the first item has index 0.

**By leaving out the start value, the range will start at the first item**:

Example

This example returns the items from the beginning to, but NOT included, "kiwi":

```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
```

Output:

```python
('apple', 'banana', 'cherry', 'orange')
```

**By leaving out the end value, the range will go on to the end of the list:**

Example:

This example returns the items from "cherry" and to the end:

```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
```

Output:

```python
('cherry', 'orange', 'kiwi', 'melon', 'mango')
```

#### Range of Negative Indexes

Specify negative indexes if you want to start the search from the end of the tuple.

Example:

This example returns the items from index -4 (included) to index -1 (excluded)

```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
```

Output:

```python
('orange', 'kiwi', 'melon')
```

#### Updating Tuples

Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. But there are some workarounds.

**a.Change Tuple Values**

Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called. But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Convert the tuple into a list to be able to change it:

```python
x = ("apple", "banana", "cherry")
y = list(x) #convert a tuple to a list
```

The code returns:

```python
['apple', 'banana', 'cherry']
```

Replace banana with kiwi using index

```python
y[1] = "kiwi" #replace banana with kiwi
```

ouput :

```python
['apple', 'kiwi', 'cherry']
```

convert the list back to a tuple using the tuple constructor

```python
x = tuple(y)
print(x)
```

Output:

```python
('apple', 'kiwi', 'cherry')
```

**b. Add Items**

Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

**i. Convert into a list**: Just like the workaround forchanginga tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

Example:

Convert the tuple into a list, add "orange", and convert it back into a tuple:

```python
thistuple = ("apple", "banana", "cherry")
 y = list(thistuple)
 y.append("orange")
 thistuple = tuple(y)
 print(thistuple)
```

Output:

```python
('apple', 'banana', 'cherry', 'orange')
```

**ii. Add tuple to a tuple**. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

Example:

Create a new tuple with the value "orange", and add that tuple:

```python
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
```

Output:

```python
('apple', 'banana', 'cherry', 'orange')
```

**Note:** When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

#### c. Remove Items

Tuples are unchangeable, so you cannot remove items from it.

i. You can use the same workaround as we used for changing and adding tuple items.

Example:

Convert the tuple into a list, remove "apple", and convert it back into a tuple:

```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
```

Output:

```python
('banana', 'cherry')
```

ii. You can delete the tuple completely:

Example:

The del keyword can delete the tuple completely:

```python
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists.
```

#### Unpacking a Tuple

When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

**Example**

Packing a tuple:

```python
fruits = ("apple", "banana", "cherry")
```

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

Example

Unpacking a tuple:

```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
```

Output:

```python
apple
banana
cherry
```

**Note:** The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

#### Joining Tuples

**Join Two Tuples:**

To join two or more tuples you can use the + operator:

Examples:

Join two tuples:

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
```

Output:

```python
('a', 'b', 'c', 1, 2, 3)
```

**Multiply Tuples**

If you want to multiply the content of a tuple a given number of times, you can use the \* operator:

**Example**

Multiply the fruits tuple by 2:

```python
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
```

Output:

```python
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

#### Conclusion

The tuple data type is an immutable, ordered data type that allows you to store data in Python. Tuples are somewhat faster to use than list in Python because they cannot be changed. As such, they’re useful if you need to store data that will not change.

**Reference:**

[W3School](https://www.w3schools.com/python/python_tuples.asp)
