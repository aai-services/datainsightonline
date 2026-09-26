---
title: "A Brief Overview of NUMPY"
author: "Roshan Gyawali"
date: 2021-10-06
description: "NumPy is a Python package, which stands for 'Numerical Python', and used for working with arrays. It also has different functions and mostly used for mathematical and logical operation on arrays..."
categories: ["Python"]
image: images/d42fcb_42159d47f6f14d61902705490cefe583.webp
wix-url: https://www.datainsightonline.com/post/a-brief-overview-numpy
---
![](images/d42fcb_42159d47f6f14d61902705490cefe583.webp)

NumPy is a Python package, which stands for 'Numerical Python', and used for working with arrays. It also has different functions and mostly used for mathematical and logical operation on arrays, fourier transforms and routines for shape manipulation, operations related to linear algebra and many more.

Let's dive deep into the numpy array and talk about different opertions that can be carried out using it.

##### Loading numpy

```python
import numpy as np
```

First we need to import numpy package in order to use it, and standard alias used is np.

##### Initializing NumPy array

Any dimensional array can be initialized according to our desire; here in this blog we mostly talk about 1-, 2-d and 3-d array, but it can be initialized as 4-d, 5-d and so on.

###### Single dimentional array

```python
numpy_array = np.array([1,2,3])
print(numpy_array)
type(numpy_array)
```

###### Output: [ 1, 2, 3]

###### numpy.ndarray

###### Two dimentional array: float values

We can also initialize two dimentional array, holding float value as well.

```python
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
```

###### Output: [ [9. 8. 7.] [6. 5. 4.] ]

##### Dimension of numpy array

```python
numpy_array.ndim
```

###### Output: 1

###### It determines numpy_array variable holds single dimensional array.

```python
b.ndim
```

###### Output: 2

###### It means b hold 2 dimentional array.

##### Shape of the numpy array

We can check the shape of the desired numpy array.

```python
numpy_array.shape
```

###### Output: ( 3, )

```python
b.shape
```

###### Output: ( 2, 3)

##### Accessing/Changing specific elements, rows, columns, etc

Now let's discuss about accessing, updating the specific elements, row, columns.

```python
single_d = np.array([1,2,3,4,5])
print(single_d)
```

###### Output: [1 2 3 4 5]

If we wish to access fifth element of the single_d array, we have to pass the index value to single_d. As the index of array starts from 0, to pass index value 4 to access the 5th value.

```python
print(single_d[4])
```

###### Output: 5

Further, let's print the elements from 2nd index value to the end.

```python
print(single_d[2:])
```

###### Output: [3 4 5]

Sometimes we need to change the value of the given numpy array. Let's change the last value as 50.

```python
single_d[-1]=50;
print(single_d)
```

###### Output: [ 1 2 3 4 50]

Now, let's access, mutate, and slice the elements in two dimentional array.

```python
two_d = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(two_d)
```

###### Output: [ [ 1 2 3 4 5 6 7 ] [ 8 9 10 11 12 13 14 ] ]

Now let's write code in order to get the value 13 from the two_d array.

```python
two_d[1, 5]
```

###### Output: 13

We can also get a specific row as well as column from the given two dimensional numpy array.

At first let's retrieve first row from the two_d array.

```python
two_d[0, :]
```

###### Output: array ( [ 1, 2, 3, 4, 5, 6, 7 ] )

Now it's turn to retrieve specific column, let us say third column.

```python
two_d[:, 2]
```

###### Output: array([ 3, 10])

There are many ways of initializing different types of array. Let's look through it for a minute.

```python
np.zeros(5)
```

###### Output: array([0., 0., 0., 0., 0.])

###### Initializing an array of single dimension with 5 zeroes.

```python
np.zeros((2,3))
```

###### Output: array ([[0., 0., 0.], [0., 0., 0.]])

###### Initializing an array with two rows and three columns with zeroes.

```python
np.ones((4,5))
```

###### Output: array ([[1., 1., 1., 1., 1.], [1., 1., 1., 1., 1.], [1., 1., 1., 1., 1.], [1., 1., 1., 1., 1.]])

###### Initialize an array with four rows and five columns with 1 at all places.

What if we wish to initialize an array with any other values.

```python
np.full((2,2),99)
```

###### Output: array ([[ 99, 99 ], [ 99, 99 ]])

###### Initialize an array of two by two size with value 99.

Sometimes we need to initialize array with random numbers. So, what to do in such situation. We can implement with random variable generator.

```python
np.random.rand(4,2)
```

###### Output: array([[0.63020206, 0.04093202], [0.77430849, 0.6007599 ], [0.95535216, 0.08625923], [0.90716061, 0.47418161]])

we also can create a random integers and implement in desired sized array.

```python
np.random.randint(7, size=(3,3))
```

###### Output: array([[0, 4, 1], [2, 3, 0], [2, 0, 0]])

Also sometimes we need to generated random number within the limits.

```python
np.random.randint(1,20, size=(3,3))
```

###### Output: array([[14, 2, 11], [19, 17, 7], [13, 10, 12]])

Now let us perform element wise operations on the numpy array.

```python
simple_array= np.array([1,2,3,4])
simple_array + 2
```

###### Output: array([3, 4, 5, 6])

###### 2 is added to every elements and returned to same array.

```python
simple_array * 3
```

###### Output: array([ 3, 6, 9, 12])

###### 3 multiplied with every elements of simple_array and returned.

There are many cool stuff that can be done with the numpy array. If you wish to see more, you can visit to the GitHub [link](https://github.com/gyawali9/numpy_overview_python).
