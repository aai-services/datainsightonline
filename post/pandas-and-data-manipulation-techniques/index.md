---
title: "Pandas and Data manipulation techniques"
author: "imene.maallem"
date: 2021-11-22
description: "Pandas presents an open-source python library that can perform data manipulation to data analysis easily, using different techniques and data analysis tools. Pandas is an open-source library that is..."
categories: ["Pandas"]
image: images/a8e214_9ad6482808ce4f2c997e491b75b53450.webp
wix-url: https://www.datainsightonline.com/post/pandas-and-data-manipulation-techniques
---
![](images/a8e214_9ad6482808ce4f2c997e491b75b53450.webp)

Pandas presents an open-source python library that can perform data manipulation to data analysis easily, using different techniques and data analysis tools. Pandas is an open-source library that is used from & is very powerful, flexible & easy to use tool.In this article, we will introduce some fundamental features of Pandas and how they can be applied.

1.**Boolean Indexing** :

Boolean Indexing is one of panda's techniques that can be used when filtering values of a column based on conditions from another set of columns .Boolean indexing can be helpful in selecting the data from the DataFrames using a boolean vector. Noting thar there should be a DataFrame with a boolean index in order to use the boolean indexing. First , we create a dictionary of data . Then, we need to convert it into a DataFrame object with a boolean index as a vector . After that, we access the data using boolean indexing.

Here are some example below in order to get the idea.

**# boolean indexing in pandas (example 1)**

```python
import pandas as pd
# data
data = {
   'Name': ['Asia', 'Sarah', 'Maya'],
   'Age': [15, 20, 17]
}
# we create  DataFrame with boolean index vector
data_frame = pd.DataFrame(data, index = [True, False, True])
print(data_frame)
```

**# boolean indexing in pandas ( example 2) :**

```python
import pandas as pd
df = pd.DataFrame({
    'Name': ["Corina","Molly","Tenia","Sarah","Holly"],
    'Age':  [13,39,25,30,28],
    'Score': [356, 320, 301, 358,380],
})
print("Initial DataFrame:")
print(df,"\n")
df['Age-Range'] = pd.cut(x=df['Age'], bins=[20,30,40,50])
print("DataFrame with Age-Range:")
print(df)
```

**# Boolean indexing in Pandas(example 3) :**

```python
import pandas as pd
# data
data = {
  'Name': ['Mary', 'Stephany', 'Polly'],
  'Age': [19, 20, 19]
}
# We create a DataFrame with boolean index vector
data_frame = pd.DataFrame(data, index = [True, False, True])
print(data_frame)
```

when running the above program, we will get the following: .

```python
          Name   Age
```

```python
True    Mary   19
```

```python
False Stephany  20
```

```python
True    Polly   19
```

**2. Second Technique : imputing missing values**

Missing Data can occur when no information is provided for one or more items or for a whole unit. In data science ,missing Data can also refer to as NA(Not Available) values in pandas. In DataFrame sometimes many datasets simply arrive with missing data, either because it exists and was not collected or it never existed In Pandas missing data is represented by two value:

· None: None is often used for missing data in Python code.

· NaN : NaN (an acronym for Not a Numbe

In Pandas, treat None and NaN are treated as essentially interchangeable for indicating missing or null values. There are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame :

· [isnull()](https://www.geeksforgeeks.org/python-pandas-isnull-and-notnull/)/ [notnull()](https://www.geeksforgeeks.org/python-pandas-isnull-and-notnull/)/ [dropna()](https://www.geeksforgeeks.org/python-pandas-dataframe-dropna/)/ [fillna()](https://www.geeksforgeeks.org/python-pandas-dataframe-fillna-to-replace-null-values-in-dataframe/)/ [replace()](https://www.geeksforgeeks.org/python-pandas-dataframe-replace/) / [interpolate()](https://www.geeksforgeeks.org/python-pandas-dataframe-interpolate/). Let us take 2 examples : **isnull() and f()**

### a. Checking for missing values using isnull()
In order to check missing values in Pandas DataFrame, we use a function isnull() .This function helps in checking whether a value is NaN or not. It can also be used in Pandas Series in order to find null values in a series.In order to check null values in Pandas DataFrame, we use isnull() function to return dataframe of Boolean values

which are True for NaN values. Let us see the example below :

**# Checking for missing values using isnull() :**

[#importing](https://www.datainsightonline.com/blog/hashtags/importing) pandas as pd

import pandas as pd

# importing numpy as np

import numpy as np

# dictionary of lists

dict = {'First Score':[100, 90, np.nan, 95],

'Second Score': [30, 45, 56, np.nan],

'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe from list

df = pd.DataFrame(dict)

# using isnull() function

df.isnull()

### Checking missing values using fillna() :
In order to fill null values in a datasets, we use fillna(), function which

replace NaN values with some value of their own. This function helps

in filling a null values in datasets of a DataFrame. Let's take this example

Filling null values with a single value :

# importing pandas as pd

import pandas as pd

# importing numpy as np

import numpy as np

# dictionary of lists

dict = {'First Score':[100, 85, np.nan, 93],

'Second Score': [20, 50, 58, np.nan],

'Third Score':[np.nan, 30, 80, 88]}

# creating a dataframe from dictionary :

df = pd.DataFrame(dict)

# filling amissing value with previous ones

df.fillna(method ='pad')

**3. 3rd technique : Pandas cut() function :**

Pandas cut() function is utilized to isolate exhibit components into independent receptacles. The cut() function works just on one-dimensional array like articles. The cut() function in Pandas is useful when there are large amounts of data which has to be organized in a statistical format.

This method is called labelling the values using Pandas cut() function. Use cut once you have to be compelled to section and type information values into bins. This operate is additionally helpful for going from an eternal variable to a categorical variable. As an example,cut may convert ages to teams getting on supports binning into associate degree equal variety of bins, or a pre-specified array of bins. The syntax of Pandas cut() is given as it follows :

**Pandas.cut(x, duplicates=’raise’, include_lowest = false, precision = 3, retbins = false, labels = none, right = true, bins).**

Given below shows how cut() function works in Pandas using some examples :

#### Example 1 : Utilizing Pandas Cut() function to segment the numbers into bins :
```python
import numpy as np
import pandas as pd
df_num1 = pd.DataFrame({'num': np.random.randint(1, 30, 20)})
print(df_num1)
df_num1['num_bins'] = pd.cut(x=df_num1['num'], bins=[1, 5, 10, 15, 30])
print(df_num1)
print(df_num1['num_bins'].unique())
```

#### **Example 2 :** Utilizing Pandas cut() function to label the bins.

```python
import numpy as np
import pandas as pd
df_num1 = pd.DataFrame({'number': np.random.randint(1, 50, 30)})
print(df_num1)
df_num1['numbers_labels'] = pd.cut(x=df_num1['number'], bins=[1, 25, 50], labels=['Lows', 'Highs'],     right=False)
print(df_num1)
print(df_num1['numbers_labels'].unique())
```
