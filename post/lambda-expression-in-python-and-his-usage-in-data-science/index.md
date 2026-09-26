---
title: "Lambda expression in python and its usage in data science"
author: "TEMFACK DERICK"
date: 2021-10-06
description: "Python, the famous programming language created by Guido van Rossum is a muli-paradigm language. It supports Object Oriented programming, procedural programming, and functional programming.According..."
categories: ["Python"]
image: images/15af94_09ab704b627a430b824c46c32f30a7ee.webp
wix-url: https://www.datainsightonline.com/post/lambda-expression-in-python-and-his-usage-in-data-science
---
![image from https://i1.faceprep.in/](images/15af94_09ab704b627a430b824c46c32f30a7ee.webp)

*image from https://i1.faceprep.in/*

**Python,** the famous programming language created by Guido van Rossum is a muli-paradigm language. It supports **Object Oriented programming, procedural programming,** and **functional programming.**

According to Wikipedia,

> Functional programming is a programming paradigm where programs are constructs by applying and composing functions.

Python follows these principles and the usage of functional programming in this language is by using the keyword **lambda.**

The **lambda** keyword is used to create an anonymous function that accepts any number of the argument. The signature of this function is :

```python
lambda <parameter_list>: <expression_to_evaluate>
```

**Example of lambda function:**

```python
list_name =['atangana','paul','amidou','omar','hasan']

list(map(lambda name : name.capitalize(), list_name))
```

In this example, we apply the lambda function

**lambda name : name.capitalize()** that take each word in **list_name** and capitalize it.

After discovering the lambda function, let's do some manipulation with it using the Malaria dataset in Africa download from Kaggle with [this link](https://www.kaggle.com/lydia70/malaria-in-africa).

After downloading this dataset, let's explore it with some useful pandas functions to know our data.

#### Apply head(), info() and describe() method

```python
import pandas as pd
data = pd.read_csv('DatasetAfricaMalaria.csv')

data.head()
data.info()
data.describe()
```

#### Application of lambda function in Malaria dataset

List of the country in the dataset that the country name starts with "C"

```python
filtering_cond = data['Country Name'].apply(lambda country: country.startswith('C'))
data[filtering_cond]
```

List of the country without malaria cases reported

```python
filtering_cond = data['Malaria cases reported'].apply(lambda nbre_malaria_case: nbre_malaria_case==0)
data[filtering_cond]
```

These two previous examples show you some applications of lambda function in python with a pandas data frame.

You can find the source code of this blog post [here](https://github.com/tderick/lambda-function-in-python).
