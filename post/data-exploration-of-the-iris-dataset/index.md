---
title: "Data exploration of the iris dataset"
author: "Gaurab Awal"
date: 2021-09-15
description: "Get familiar with pandas libraryThe Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica, and Iris..."
categories: ["Projects"]
wix-url: https://www.datainsightonline.com/post/data-exploration-of-the-iris-dataset
---
**Get familiar with pandas library**

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica, and Iris versicolor)

The iris dataset can be explored with the help of the pandas library. We will simply read the minimum value, the maximum value, the mean, and the standard deviation in this project.

We will understand the code step by step.

###### Step 1: Import the pandas library

```python
	import pandas as pd
```

###### Step 2: Read a CSV file of the iris dataset with the help of the pandas library and assigned the data frame into df variable.

```python
	df = pd.read_csv('iris.csv')
```

###### Step 3: For user interaction, we have to input numbers according to the parameter we want to get. The input number is saved to the variable input_value.

###### Input 1 for minimum value

###### Input 2 for maximum value

###### Input 3 for mean calculation

###### Input 4 for standard deviation

```python
	input_value = int(input("Enter number to select: "))
```

Step 4: With respect to the number input then we get value and print it out.

###### For example, if we give 3 as input value then it will print the mean value of each column and give the result as below.

```python
Enter number to select: 3
You have selected mean value.
Mean of sepal length is 5.84,sepal width is 3.06,petal length is 3.76,petal width is 1.2.
```

I have uploaded all of the code in the GitHub [link](https://github.com/awalGaurab/Iris_dataset_exploration) and download an iris dataset from the [iris dataset link](https://gist.github.com/netj/8836201) so that you can get it from Github and try it on your own.
