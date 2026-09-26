---
title: "A Quick Introduction to Numpy"
author: "Rubash Mali"
date: 2021-10-04
description: "Numpy stands for Numbers in python and is a powerful library for processing multi-dimensional arrays. Numpy is popular for its unmatchable speed and flexibility. In this blog we will observe some..."
categories: ["Python"]
image: images/0a8409_6150e7b2406d4f2aa2cd2d41d7f3ecfa.webp
wix-url: https://www.datainsightonline.com/post/a-quick-introduction-to-numpy
---
Numpy stands for Numbers in python and is a powerful library for processing multi-dimensional arrays. Numpy is popular for its unmatchable speed and flexibility. In this blog we will observe some common functionalities and techniques regarding Numpy.

**1.Creating a Numpy array :-** Numpy package is imported usually with an alias name np. After that we use the array function to create the desired nd array.

```python
import numpy as np
a = np.array([0, 1, 2, 3, 4, 5])
print(type(a))
#Output
<class 'numpy.ndarray'>
```

Same can be done for multidimensional array also we can check the dimensionality using the ndim function.

```python
arr_0d = np.array(42)
arr_1d=np.array([1,2,3])
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print(arr_0d.ndim)
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
#Output
0
1
2
3
```

While shape attribute returns a tuple with each index having the number of corresponding elements.

```python
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d.shape)
#Output
(2, 4)
```

Another popular way to create a numpy array is using arange function. Inside the arange function we can simply mention the end value (n) which gives us values from 0 to n-1

```python
a = np.arange(5) # 0.... n-1
a
#Output
array([0, 1, 2, 3, 4])
```

Arange function also provides us more flexibilty ,we can define the start point endpoint (exclusive) and the increment / decrement.

```python
b = np.arange(2, 30, 4) #start, end (exclusive), step
b
#Output
array([ 2,  6, 10, 14, 18, 22, 26])
```

**2.Speed comparison:-** As mentioned earlier in data science one has to deal with huge data and numpy is preferred to list. It is due to its unmatched speed. Below code snippet shows speed of creating a list and the same numpy array of 10000 numbers and finding their cube.

```python
L = range(10000)
%timeit [i**3 for i in L]
#Output
2.96 ms ± 237 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

```python
a = np.arange(10000)
%timeit a**3
#Output
15.9 µs ± 600 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

The timeit function is used to find the time taken to . We can clearly see numpy is much faster than list.

**3.Numpy array with different data types:-** Numpy supports more than numbers ,it supports boolean , string and complex data type etc...

```python
d= np.array([1+2j, 2+4j])   #Complex datatype
b = np.array([True, False, True, False])  #Boolean datatype
s = np.array(['Ram', 'Robert', 'Rahim']) #String datatype
print(d.dtype)
print(b.dtype)
print(s.dtype)
#Output
complex128
bool
<U6
```

**4.Indexing and Slicing:-** Similar to list we can select a particular element of a numpy array by mentioning the numpy array name followed by sqaure brackets. Inside the square bracket index position of the desired element is mentioned.

```python
arr_1d=np.array([1,2,3])
print(arr_1d[1])
#Output
2
```

For a 2D numpy array first square brackets denotes the row position and second square brackets denotes the column position.

```python
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d[1][1])
#Output
6
```

For selecting more than one element we use slicing technqiue it is similar to indexing ,however inside the square brackets we mention the starting index position followed by ' : ' and the exclusive end index position.

```python
arr_1d=np.array([1,2,3,4])
print(arr_1d[0:2])
#Output
[1,2]
```

**5.Elementwise Operation in numpy:-**Numpy allows us to operate on each element. Some popular element wise operations are:

**5.1 Arithmetic Operations With Scalars:-** We can simply perform arithmetic operation of each element in a numpy array with a scalar value. This is direct forward and we simply mention the numpy array, arithmetic operator and the scalar value.

```python
arr_1d=np.array([1,2,3,4])
print(arr_1d+4)
print(arr_1d**3)
#Output
[5 6 7 8]
[ 1  8 27 64]
```

**5.2 Matrix Multiplication:-** Numpy allows us to perform matrix multiplication of two numpy arrays by simply using the ' \* ' operator . The only perquisites is that numpy arrays should shapes should satisfy matrix multiplication condition. Below is an example of the same.

```python
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
print(a*b) # Matrix Multiplication
#Output
[[ 7 16 27]
 [40 55 72]]
```

**5.3 Element-wise comparison:-** We can compare each element with a desired condition. This is done in a straight forward manner by using comparison operators ( ==, <=, >=, !=). The result is a boolean array showing the mentioned condition is true or false for numpy array element particular index position.

```python
a = np.array([1, 2, 3])
b = np.array([9, 6, 3])
print(a == b)
#Outputarray
([False, False,  True])
```

Here both the numpy arrays a and b have value 3 at third index position so the array returns True at that position and False at other positions.

**5.4 Element-wise Logical Operations:-** We can perform logical operations such as and, or, not on each element of numpy arrays by calling np.logical_logical_operation function. This also returns an array of boolean values based on element wise logical operation.

```python
a = np.array([True, True, False, False])
b = np.array([True, False, True, False])
print(np.logical_and(a, b))
#Output
[ True False False False]
```

Additionally numpy considers 0 as logical False and any other number as True. This allows us to perform element wise logical operation on numeric numpy arrays. An example is as follow:

```python
a= np.array([1, 5, -2, 0])
b = np.array([1, 0, 1, 0])
print(np.logical_and(a, b))
#Output
[ True False  True False]
```

**5.5 Element-wise Transcendental operations:-** Numpy supports element wise transcendental operation such as sine, cosine, exponential and logarithmic. We can perform this operations by simply calling np.transcendental_function_name and the numpy array inside the bracket. An example is as follow:

```python
s
a = np.array([1, 2, 3])
print(np.cos(a))
print(np.exp(a))
#Output
[ 0.54030231 -0.41614684 -0.9899925 ]
[ 2.71828183  7.3890561  20.08553692]
```

You can find the GitHub repo of this code through this [link](https://github.com/rubash9849/data_inisghts/blob/main/numpy.ipynb)
