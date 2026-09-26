---
title: "Pandas Techniques For Data Manipulation:"
author: "Ishan Chudali"
date: 2021-11-23
description: "Python is a great language for doing data analysis as it provides large number of data-centric python packages. Pandas is an open-source python library that is used for data manipulation and..."
categories: ["Pandas"]
image: images/4cb298_438a1373839f4c9aa9f1ea7dd8150359.webp
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-manipulation
---
![](images/4cb298_438a1373839f4c9aa9f1ea7dd8150359.webp)

Python is a great language for doing data analysis as it provides large number of data-centric python packages. Pandas is an open-source python library that is used for data manipulation and analysis. It provides many functions and methods to speed up the data analysis process.

Here , we discuss about some of the pandas techniques for data manipulation.

### Importing Dataset and inspecting Dataframe.

In this tutorial , we are basically learning about reading a csv(Comma Separated Values) file into a dataframe and inspect the dataframe, learn about the data types of the columns values .

For this we created a csv file on our local computer named as emp_data.csv which contained the employee information of a company.

**Reading csv file into dataframe:**

First of all ,we import the pandas library.Pandas is usually imported under the 'pd' alias.we use as keyword to create an alias.

```python
import pandas as pd
```

here a dataframe emp_df is created:

```python
emp_df =pd.read_csv("C:\\Users\\DELL\\Desktop\\emp_data.csv")
emp_df.head()
```

![](images/4cb298_bb9fc6b18f6f435da0d675e170aa4bf6.webp)

```python
emp_df.info()
```

![](images/4cb298_e6c01f5c1c724d2f8989ed0cc913fdde.webp)

This [dataframe.info()](http://dataframe.info) method returns the data type of the dataframe columns.

### Creating pandas datframe from dictionary of list:#

```python
emps = {"Emp_name":["Ishan", "Gaurav", "ram", "Rohit"],
        "role": ["Data_science", "full stack", "front end", "ML and AI"]
        }

ddf = pd.DataFrame(emps)
ddf.head()
```

![](images/4cb298_2e873f2075d648b78550b4e9c8bbe94f.webp)

Here we created a dataframe ddf from dictionary of list using pandas.dataframe().

## Sorting Dataframe:
For sorting the data frame in pandas, function [sort_values()](https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-1/) is used. Pandas sort_values() can sort the data frame in Ascending or Descending order.

For demostrating example we are adding a new column to the existing dataframe.

```python
exp = pd.Series(['6', '8', '4', '3','2','7','8','9'])
emp_df['Experience_in_years'] = pd.to_numeric(exp)
emp_df.head(n=8)
```

Here we converted the object type of datframe column into integer type using pd.to_numeric() function.

#### Sorting in Ascending Order:
```python
emp_dfsorted = emp_df.sort_values(by=["Experience_in_years"],ascending=True)
emp_dfsorted.head(n=8)
```

For sorting the pandas dataframe in ascending order we assign the name of the column to the by parameter . On the basis of that column value sorting is done.We assign True to ascending parameter to sort in ascending order. If we donot assign any value to ascending parameter it is by default sorted in ascending order.

![](images/4cb298_d11eae21435449a4bb839e7e2564161d.webp)

Here we sorted the dataframe in the ascending order of employees experience using **Experience_in_years** column.

#### Sorting in Descending Order:

```python
emp_dfsorted = emp_df.sort_values(by=["Experience_in_years"],ascending=False)
emp_dfsorted.head(n=8)
```

Here we sort the dataframe in descending order by assigning False value to the ascending parameter.

![](images/4cb298_86c3008120034117a49a74e51efa42b8.webp)

#### Sorting by multiple columns:

```python
emp_dfsorted1 = emp_df.sort_values(by=['Emp_id', 'Experience_in_years'],ascending=[True,False])
emp_dfsorted1.head()
```

For sorting the dataframe by multiple columns we pass a list of columns to by parameter and a list of boolean values to ascending parameter.

The first item of the list in ascending parameter assigns to the first column of the list and so on.

![](images/4cb298_7270da56dafb4848a0cc631722b28898.webp)

## Subsetting Dataframe:

Here are some operations by using which we can select a subset of a given dataframe:

### Selecting single column:
For selecting a single column we use square bracket [ ] .If we use single
 square bracket , the output is a pandas series .

```python
emp_exp = emp_df["Experience_in_years"]
print(emp_exp)
print(type(emp_exp))
```

![](images/4cb298_2fe9506401204bfc8793f31d6856dd84.webp)

If we use two square brackets for selecting column , the resukt is a pandas dataframe.

```python
emp_expdf =emp_df[["Experience_in_years"]]
emp_expdf.head()
```

![](images/4cb298_937d30c24daf4c08a2a83a301ace52ef.webp)

```python
print(type(emp_expdf))
```

<class 'pandas.core.frame.DataFrame'>

### Selecting Multiple columns:

For selecting multiple columns we can pass a list of column names inside the square bracket [] .

```python
name_role = emp_df[["Name","Role"]]
name_role.head()
```

![](images/4cb298_fbff14c370fb40038a1e6c3c61348e48.webp)

### Selecting Specific rows from a dataframe:

###### Using Condition to subset rows:

For selecting specific rows ,we can put conditions within the brackets to select specific rows depending on the condition.

```python
Experienced_employee = emp_df[emp_df['Experience_in_years'] > 4]
Experienced_employee.head()
```

![](images/4cb298_c9b4356ea1b747c09a91d5aad9654dbd.webp)

Here we only get the rows having the **Experience_in_years** value greater than 4.

For this we can use plenty of other operators like **<,=,<=, >= ,!=** etc..

###### Using **Square brackets to subset rows:**

We can only select rows using square brackets if we specify a slice, like 1:4. Here we are using the integer indexes of the rows .

```python
print(emp_df[1:4])
```

Here the integer before colon is inclusive and that after the colon is exclusive.

![](images/4cb298_5e683bd1f9c147f08aeb6315619b2778.webp)

### Selecting Both rows and columns:

In above methods , it was not possible to select specific rows and columns combined so the loc and iloc operators are needed. The portion before the comma specifies the rows we would like to choose and the part after the comma specifies the columns we like to choose.

##### Using loc operator:
```python
data_scientist_df = emp_df.loc[emp_df["Role"] == "Data Scientist", "Name"]
data_scientist_df.head()
```

![](images/4cb298_1d76f3e979db477ca10ef4315f3b84bf.webp)

Here we select the rows having **role** value equal to **Data Scientist** and

select the **Name** column.

#### Using iloc operator:
The iloc operator allows us to subset pandas DataFrames based on their position or index.

```python
any_two = emp_df.iloc[[1, 2], [0, 1]]
any_two.head()
```

Here we are selecting the rows having rows index 1 and 2. And the columns having column index 0 and 1.

![](images/4cb298_c22e0c5178c646d39c2a4b6151aa5502.webp)

##### Selecting all rows and only some columns:
```python
all_rows = emp_df.iloc[:, [0, 1]]
all_rows.head()
```

for selecting all rows we pass **colon :** And for selecting specific columns we pass a list of column index.

![](images/4cb298_0539577082b14e4a8d84338ca637238f.webp)

##### subsetting a regular sequence of specific rows and columns:

```python
any_rows = emp_df.iloc[0:4 , 0:2]
any_rows.head()
```

For this we specify the slice to indicate the rows and columns.The end of the slice is exclusive in both the slices.

![](images/4cb298_8c45af9ed9b04c5699788970984bc608.webp)

## Interating over rows of dataframe:

For iterating over rows in dataframe , we make use of the three functions iteritems(), iterrows(), itertuples().

#### Using iterrows():

Iterate over DataFrame rows as (index, Series) pairs.

To iterate over rows of a Pandas DataFrame, we use DataFrame.iterrows() function which returns an iterator yielding index and row data for each row.

In this example we are iterating through dataframe rows using [**Python For Loop**](https://pythonexamples.org/python-for-loop-example/)and **iterrows()** function.

```python
for index, row in emp_df.iterrows():
    print(index,row)
```

![](images/4cb298_7d41899fa607449eb0a369fbd728c875.webp)

#### Using iteritems():

Iterate over (column name, Series) pairs.

This method iterates over (column name, Series) pairs. When this method applied to the DataFrame, it iterates over the DataFrame columns and returns a tuple which consists of column name and the content as a Series.

```python
for key, value in emp_df.iteritems():
    print(key, value)
    print()
```

![](images/4cb298_c910a3c41f6f4a6cbd68e1eec85a13cb.webp)

#### Using itertuples():
Iterate over DataFrame rows as namedtuples.

In order to iterate over rows, we apply a function itertuples() this function return a tuple for each row in the DataFrame. The first tuple element represents row index while other element represents row values.

```python
for t in emp_df.itertuples() :
    print(t)
    print()
```

![](images/4cb298_decc50ea63c644b38b28386f1c246745.webp)

## Dropping Duplicates:

Pandas **drop_duplicates()** method helps in removing duplicates from the data frame.

For demonstrating the examples on drop_duplicates() function we created a dataframe called **games_df ,** that is about the games played by different countries in different years and no of medals won by them.

```python
games_df= pd.read_csv("C:\\Users\\DELL\\Desktop\\games.csv")
games_df.head()
```

![](images/4cb298_57cc3f780abf4bb5b297e8566237bee8.webp)

Now adding a new row that contain entire duplicate values.

```python
games_df.loc[len(games_df.index)] = ['India',2015, 12, 24]
print(games_df)
```

![](images/4cb298_49d1965b1fb14318a4931922d3485e23.webp)

Here first and the last rows are same.

**Removing rows with all duplicate values**

```python
games_df.drop_duplicates()
```

![](images/4cb298_fcf7219033ed40c9982b440482a327b7.webp)

From above result we can see that the rows having all the values same is dropped.Thus, dataframe.drop_duplicates() method is used to drop the rows having entire duplicate values.

**To remove duplicates on specific column we use subset:**

```python
games_df.drop_duplicates(subset=['Country'])
```

![](images/4cb298_8b28448e23bb4161a175fc6eafac8f04.webp)

Here all the rows with repeated country names in the **Country** column are dropped.

This drops the rows having duplicate **Country** column name and **Year** column name.

```python
games_df.drop_duplicates(subset=['Country','Year'])
```

![](images/4cb298_a3e53a7a49674843a955c6aef796b092.webp)

### To remove duplicates and keep first or last occurrences, we use keep.

```python
games_df.drop_duplicates(subset=['Country'], keep='last')
```

It removes duplicates in the **Country** column and kepp the last occurence.

![](images/4cb298_03052b084b8e454e86d0784569f64922.webp)

In above result the last row is kept while the first row is removed.

```python
games_df.drop_duplicates(subset=['Country'], keep='first')
```

![](images/4cb298_5698203c64de414a88b847eca84e6846.webp)

If we assign keep equal to **False.**Both the same rows with same country name are dropped.

```python
games_df.drop_duplicates(subset=['Country'], keep= False)
```

![](images/4cb298_36cb19b1b52d47e8bb67eeebf4ee441e.webp)

### Modifying actual dataframe:

If we assign inplace parameter to **True** the actual dataframe remains changed.

```python
games_df.drop_duplicates(subset=['Country'], keep='first',inplace= True)
games_df
```

![](images/4cb298_bd4aa1c60ae1496c9fcc0ac7e69c301f.webp)

The link to the notebook in the github repo is [here](https://github.com/Techy-Ishan/Pandas-Techniques-for-data-manipulation/blob/master/Pandas%20Techniques%20for%20data%20manipulation.ipynb).
