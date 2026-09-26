---
title: "Python Concepts for Data Science: List Comprehension"
author: "ayenadykyaw1"
date: 2021-10-03
description: "Python List ComprehensionPython is popular for its simple, elegant and easy-to-write style of writing and it is as simple as writing a plain English. Python list comprehension is a feature that we..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-list-omprehension
---
## Python List Comprehension
Python is popular for its simple, elegant and easy-to-write style of writing and it is as simple as writing a plain English. Python list comprehension is a feature that we can use to create powerful functionality within a single line of code. Before we dive into list comprehension, let's understand list data structure first.

### Python List
Python list is built-in data structure in Python. It is like an array in other programming languages such as Java, C, C++. However unlike arrays, the stored values in the list can be heterogeneous, means that the values do not need to be the same data types. The values are stored in sequential order and they are mutable and changeable. List supports indexing and slicing. An example of list is shown in below:

```python
myList=[1,2,3.4,"Apple",{1:"A"}]
print(type(myList))
```

```python
Output: <class 'list'>
```

In the above example, we can see that list can have different data types.

### Indexing and Slicing
```python
#indexing
print(myList[4])
#slicing
print(myList[1:4])
```

```python
output: {1: 'A'}
        [2, 3.4, 'Apple']
```

Python indexing can be used to access desired list elements(s). Note that list index starts from 0. And for slicing, ' : ' is slicing operator where lower bond is inclusive and upper bond is exclusive. So that index 4 which is a dictionary element is exclusive when we slice myList.

## List Comprehension
After a fresh recap of list, now let's see List Comprehension which is a distinct feature that can create new lists from iterable objects like tuple, strings, arrays, lists, etc. within a single line of code.

### Syntax

> newList = [ expression(element) for element in oldList if condition ]

### Example
```python
#creating an integer list
intList=[1,2,3,4,5,6,7,8,9,10,11,12]
#creating a new list which values are double of intList using list comprehension
newList=[2*i for i in intList]
print(newList)
```

```python
output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
```

In the above example, uses a single line of list comprehension statement to create a new list which values are double of values of intList. We can also use "for loop" instead of list comprehension. Let's see.

```python
#creating the same integer list1
intList1=[1,2,3,4,5,6,7,8,9,10,11,12]
#create an empty list first
newList1=[]
#createing a new list which values are double of intList1 using for loop
for i in intList:
    newList1.append(2*i)

print(newList1)
```

```python
output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
```

Another alternative way is to use map() function. Python map() function is based on functional programming. We need to pass a function and an iterable, and it will create an object.

```python
#creating the same integer list2
intList2=[1,2,3,4,5,6,7,8,9,10,11,12]
#define a funtion to make doubles of the values
def doubleVal(val):
    return 2*val
#creating a new list using list() function and map()function
newList2=list(map(doubleVal,intList2))
print(newList2)
```

```python
output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
```

We physically can see that using List Comprehension is more efficient than using "for loop" and using "map()" function in terms of coding space. Now let's discover about running time.

```python
import timeit

#list comprehension
def list_comprehension(l):
    return [2*i for i in l]

#for loop
def for_loop(l):
    li=[]
    for j in l:
        li.append(2*j)
    return li

#map function
def map_fun(l):
    def double_val(val):
        return 2*val
    lii=list(map(double_val,l))
    return lii

intList=[1,2,3,4,5,6,7,8,9,10,11,12]

# Calculate time takens by list_comprehension()
begin = timeit.default_timer()
list_comprehension(intList)
end = timeit.default_timer()
# Display time taken by list_comprehension()
print('Time taken list_comprehension:',round(end-begin,6))

# Calculate time takens by for_loop()
begin = timeit.default_timer()
for_loop(intList)
end = timeit.default_timer()
# Display time taken by map_fun()
print('Time taken for_loop:',round(end-begin,6))

# Calculate time takens by map_fun()
begin = timeit.default_timer()
map_fun(intList)
end = timeit.default_timer()
# Display time taken by map_fun()
print('Time taken map_function:',round(end-begin,6))
```

```python
output: Time taken list_comprehension: 7.8e-05
        Time taken for_loop: 9.8e-05
        Time taken map_function: 8.1e-05
```

After checking the execution time for each functionality in the above example, literally there is not much difference between the execution times. Using list comprehension generally seems a little bit fast . But we can see that list comprehension is both computationally efficient in terms of space and time . However, this should be analyzed through multiple test cases.

## List Comprehension With Conditionals
We can also use conditional statements to list comprehension. Below are some examples.

```python
studentMarks=[70,32,45,80,50,56,100,25,34,89,98,70]
passMarks=[n for n in studentMarks if n>=50]
print(passMarks)
failMarks=[n for n in studentMarks if n<50]
print(failMarks)
```

```python
output: [70, 80, 50, 56, 100, 89, 98, 70]
        [32, 45, 25, 34]
```

We can use together with range() function as well.

```python
# Take out the even values from 1 to 100 and make it doubles
doubleEven= [i*2 for i in range(1,51) if i%2==0]
print(doubleEven)
```

```python
output: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100]
```

We can also use with if-else conditional statement.

```python
# Make double to even values and triple to odd values from 1 to 50.
doubleEven_tripleOdd=[i*2 if i%2==0 else i*3 for i in range (1,51)]
print(doubleEven_tripleOdd)
```

```python
output: [3, 4, 9, 8, 15, 12, 21, 16, 27, 20, 33, 24, 39, 28, 45, 32, 51, 36, 57, 40, 63, 44, 69, 48, 75, 52, 81, 56, 87, 60, 93, 64, 99, 68, 105, 72, 111, 76, 117, 80, 123, 84, 129, 88, 135, 92, 141, 96, 147, 100]
```

## Nested List Comprehension
We can also implement nested list comprehension like nested loop or nested if. Below is an example.

```python
#creating a list which has three identical even integer lists from 1 to 10
li=[[i for i in range(1,11) if i%2==0] for j in range(3)]
print(li)
```

```python
output: [[2, 4, 6, 8, 10], [2, 4, 6, 8, 10], [2, 4, 6, 8, 10]]
```

The above example is creating a 2-Dimensional Matrix which elements are three identical lists which has even values from 1 to 10.

## List Comprehension with Lambda
Lambda expressions are shorthand representations of python function. We can use list comprehension and lambda expression together to get an efficient combination.

One the above example of creating a new list used map() function. Map function needs a function to pass as an argument so that we need to create a function. Now, let's change the above function using lambda expression instead of defining a function.

```python
#creating the same integer list2
intList3=[1,2,3,4,5,6,7,8,9,10,11,12]

#creating a new list using list() function and map()function and lambda expression
newList3=list(map(lambda val: 2*val,intList2))
print(newList3)
```

```python
output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
```

Then, now let's combine the list comprehension and lambda expression together. The above example again can be changed to a shorter version. Instead of creating an integer list of 1 to 12, we can use list comprehension with range function.

```python
newList4= list(map(lambda val:2*val,[i for i in range(1,13)]))
print(newList4)
```

```python
output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
```

Now, we can see that combining lambda expression and list comprehension can make our code shorter.

## Conclusion
I hope this article can give you to get a little bit clear about list comprehension and know how to use it. List comprehension is computationally efficient and we just need few lines of code to implement it. However, it does not mean that we always start with list comprehension in creating lists. Sometimes, instead of using list comprehension, we might need to use for loop instead. In conclusion, we can use list comprehension when it is appropriate.
