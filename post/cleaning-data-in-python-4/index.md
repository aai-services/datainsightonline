---
title: "Cleaning Data in Python"
author: "stella tchoutcha"
date: 2022-05-05
description: "Data cleansing strengthens the integrity and relevance of our data by reducing inconsistencies, preventing errors, and enabling better informed and more accurate decisions.import necessary librairies..."
categories: ["Data Cleaning", "Python"]
wix-url: https://www.datainsightonline.com/post/cleaning-data-in-python-4
---
Data cleansing strengthens the integrity and relevance of our data by reducing inconsistencies, preventing errors, and enabling better informed and more accurate decisions.

import necessary librairies and read the dataset using read_csv() function:

```python
import pandas as pd

train = pd.read_csv("C:/Users/STELLA/Documents/dataset/train.csv")
test = pd.read_csv("C:/Users/STELLA/Documents/dataset/test.csv")

#afficher les premières lignes du jeu de données
train.head()
```

The .describe() method

The describe() method is used to provide all essential information about the dataframe, which can be used for data analysis and to derive different mathematical assumptions for further study. The DataFrame describe() function works in the statistical part of the Pandas library.

```python
train.describe()
```

you can see the data information

```python
train.info()
```

**Data wrangling : Process of cleaning and unifying messy and complex data sets**

**-** it reveals more information about your data

- Enables decision - making skills in the organisation

- Helps to gather meaningful and precise data for the business

you can see if your data has missing values:

```python
train.apply(lambda x: sum(x.isnull()),axis=0)
```

you can access the data types of each column in a DataFrame:

```python
train.dtypes
```

**Scaling and Normalization**

Scaling or normalizing: what's the difference?

One of the reasons it's easy to confuse scaling with normalization is that the terms are sometimes used interchangeably, and to make matters even more confusing, they're very similar! In either case, you transform the values of numeric variables so that the transformed data points have specific useful properties. The difference is that:

when scaling you change the range of your data, while

in normalization, you change the shape of the distribution of your data.

example :

```python
for i in [train]:
    i["Gender"] = i['Gender'].map({'Female':0,'Male':1}).astype(np.int)
    i['Married'] = i['Married'].map({'No':0,'Yes':1})
    i['Loan_Satus'] = i['Loan_Status'].map({'N':0,'Y':1})
    i['Education'] = i['Education'].map({'Not Graduate':0,'Graduate':1}).astype(int)
    i['Self_Employed'] = i['Self_Employed'].map({'No':0,'Yes':1}).astype(int)
    i['Credit_History'] = i['Credit_History'].astype(int)
train
```

## so now as we have imputed all the missig values we go on to mapping the categorical variables with the integers

Let's talk a little more in-depth about each of these options.

Scaling

This means that you transform your data to fit a specific scale, like 0-100 or 0-1 For example, you might see prices for certain products in yen and US dollars. A US dollar is worth about 100 yen, but if you don't adjust your prices, methods like SVM or KNN will consider a price difference of 1 yen as big as a difference of 1 US dollar! This clearly does not correspond to our intuitions of the world. With Currency, you can convert between currencies. But what if you look at something like height and weight? It's not entirely clear how many pounds should equal an inch (or how many kilograms should equal a meter).

By scaling your variables, you can help compare different variables on equal footing. To help solidify what scaling looks like, check out [this notebook](https://github.com/Tchoutcha/Data-insight-sandjong/blob/main/Datacleaning.ipynb).

```python
# Using cut() - create category ranges and names
ranges = [0,100000,200000,500000,np.inf]
group_names = ['0-100K','100K-200K', '200k-500k','500K+']
# Create income group column
train['income_group'] = pd.cut(train['Total_incomes'], bins=ranges,labels=group_names)
train[['income_group','Total_incomes']]
```

You could also end up with "unknown" characters. It is often essential to understand the variables of the data set

Inconsistent data entry

```python
# Replace "+" with ""
train["Dependents"] = train["Dependents"].str.replace("+","")
train["Dependents"]
```

**imputing the missing values**

For numerical values a good solution is to fill missing values with the mean , for categorical we can fill them with the mode (the value with the highest frequency)

```python
for i in [train]:
    i['Gender'] = i['Gender'].fillna(train.Gender.dropna().mode()[0])
    i['Married'] = i['Married'].fillna(train.Married.dropna().mode()[0])
    i['Dependents'] = i['Dependents'].fillna(train.Dependents.dropna().mode()[0])
    i['Self_Employed'] = i['Self_Employed'].fillna(train.Self_Employed.dropna().mode()[0])
    i['Credit_History'] = i['Credit_History'].fillna(train.Credit_History.dropna().mode()[0])
train.isna().sum()
```

removing unnecessary columns with drop

```python
train = train.drop(['Loan_ID','Total_incomes','ApplicantIncome','CoapplicantIncome'],axis = 1)
```

## Collapsing data into categories
Create categories out of data: income_group column from income column. Some people might have a low income but strong CoappliantIncome so a good idea is to combine them in a TotalIncome column.

```python
train['Total_incomes'] = train['ApplicantIncome'] + train['CoapplicantIncome']
```

check out [this notebook](https://github.com/Tchoutcha/Data-insight-sandjong/blob/main/Datacleaning.ipynb).
