---
title: "5 must known techniques in pandas"
author: "Rawda Rumaieh"
date: 2021-11-21
description: "In this article I used a dataset on kagglehttps://www.kaggle.com/tgdivy/poetry-foundation-poems 1. Sorting DataFramewhat is a data frame?A DataFrame is a data structure with labelled axes for both..."
categories: ["Pandas"]
image: images/d96e14_8a710edc896145b084e9620d848d8f62.webp
wix-url: https://www.datainsightonline.com/post/5-must-known-techniques-in-pandas
---
![](images/d96e14_8a710edc896145b084e9620d848d8f62.webp)

In this article I used a dataset on kaggle

<https://www.kaggle.com/tgdivy/poetry-foundation-poems>

### 1. Sorting DataFrame

what is a data frame?

A DataFrame is a data structure with labelled axes for both rows and columns. You can sort a DataFrame by row or column value as well as by row or column index.

## Sorting by Values

1st: lets sort by values in a DataFrame along either axis (columns or rows)

```python
df.sort_values("Poet")
```

*1. Sorting by a Column in Ascending Order*

To use .sort_values(), you pass a single argument to the method containing the name of the column you want to sort by

```python
df.sort_values("Poet")
```

*2. Changing the Sort Order to Descending Order*

Another parameter of .sort_values() is ascending. By default .sort_values() has ascending set to True. If you want the DataFrame sorted in **descending order**, then you can pass False to this parameter:

```python
df.sort_values(by="Poet",ascending=False)
```

*3.Choosing a Sorting Algorithm*

It’s good to note that pandas allows you to choose different **sorting algorithms** to use with both .sort_values() and .sort_index(). The available algorithms are quicksort, mergesort, and heapsort.

You can do that with the kind parameter in .sort_values() or .sort_index(), like this

```python
df.sort_values(by="Poet",ascending=False,kind="mergesort")
```

**Note:** In pandas, kind is ignored when you sort on more than one column or label.

*4.Sorting on Multiple Columns*

In data analysis, it’s common to want to sort your data based on the values of multiple columns.To sort by two keys, you can pass a list of column names to by:

```python
df.sort_values(by=["Poem", "Poet"])
```

*5.Sorting Multiple Columns with different Order*

Up to this point, We've sorted only in ascending order on multiple columns. In the next example, W'll sort in descending order based on the Poet,Poem and Title columns.

```python
df.sort_values(by=["Poet", "Poem", "Title"],ascending=[True, True, False])
```

## Sorting Indexes
Before sorting on the index, it’s a good idea to know what an index represents. A DataFrame has an **.index** property, which by default is a numerical representation of its rows’ locations. You can think of the index as the row numbers. It helps in quick row lookup and identification.

Start by creating a new sorted DataFrame using .sort_values():

```python
assigned_index_df = df.set_index(["Poet", "Poem"])
```

*1. Sorting by Index*

Using this method, you replace the default integer-based row index with two axis labels. This is considered a [MultiIndex](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.html#pandas.MultiIndex) or a **hierarchical index**. Your DataFrame is now indexed by more than one key, which you can sort on with .sort_index():

```python
assigned_index_df.sort_index()
```

*2. Sorting by Index in Descending Order*

You can also use the column labels of a DataFrame as the sorting key for .sort_index(). Setting axis to 1 sorts the columns of your DataFrame based on the column labels:

```python
df.sort_index(axis=1)
```

*3. Sorting the columns in descending order*

```python
df.sort_index(axis=1, ascending=False)
```

### 2. Apply Function
The apply() function is used to apply a function along an axis of the DataFrame.

Objects passed to the function are Series objects whose index is either the DataFrame’s index (axis=0) or the DataFrame’s columns (axis=1)

If you want to iterate over each row in the data frame you probably guessed it right!! use (lambda)

if we want to apply the function to the rows rather than the columns then we should use (axis=1)

Let's assume that we want to add a text after the poet name.

The text is (he was talented)

we can make it into two steps:

1- function to add the name:

```python
def add_r(x):
    return(x+' He was' +' Tallented')
```

2- applying the lambda function

```python
df.apply(lambda row: add_r(row['Poet']),axis=1)
```

the result is:

```python
0      Michelle Menting He was Tallented
1         Lucia Cherciu He was Tallented
2            Ted Kooser He was Tallented
3       Grace Cavalieri He was Tallented
4          Connie Wanek He was Tallented
                     ...
13        Jody Gladding He was Tallented
14    William Jay Smith He was Tallented
15    William Jay Smith He was Tallented
0     Hailey Leithauser He was Tallented
1        Wendy Videlock He was Tallented
Length: 13854, dtype: object
```

we can also apply a numpy function in the apply function.

i used a numerical dataframe that i created to sqaure root the demands

```python
df1['demand'].apply(np.sqrt)

0     17.029386
1     16.124515
2     16.970563
3     17.320508
4     17.606817
5     17.406895
6     18.138357
7     18.439089
8     17.776389
9     18.165902
10    17.549929
11    17.606817
Name: demand, dtype: float64
```

### 3. Pandas Cut

Pandas cut() function is used to separate the array elements into different bins . The cut function is mainly used to perform statistical analysis on scalar data.

let's create a new column containing the range of demands:

```python
df1['bins'] = pd.cut(x=df1['demand'], bins=[250, 290, 330, 370])
```

We can check the frequency of each bin:

```python
print(df1['bins'].unique())
```

```python
[(250, 290], (290, 330], (330, 370]]
Categories (3, interval[int64]): [(250, 290] < (290, 330] < (330, 370]]
```

### 4. Pandas Query

Talking about one of my absolute favourites is Pandas Query

there are many methods that enable you to retrieve subsets [based on row and column labels](https://www.sharpsightlabs.com/blog/pandas-loc/) or [by integer index of the rows and columns](https://www.sharpsightlabs.com/blog/pandas-iloc/). however those tools can be a little cumbersome syntactically.

In many ways, the Pandas .query method solves those problems.

Query enables you to “query” a DataFrame and retrieve subsets based on logical conditions.

Moreover, the syntax is a little more streamlined than Pandas bracket notation.

For example if i want to find the months where the demand exceeded 300

```python
df1.query('demand > 300').month
```

and the result is:

```python
4      5
5      6
6      7
7      8
8      9
9     10
10    11
11    12
Name: month, dtype: int64
```

### 5. Pandas Where !?

searching for something a vast dataframe? Where is your savoir.

Pandas **where()** method is used to check a data frame for one or more condition and return the result accordingly. By default, The rows not satisfying the condition are filled with NaN value.

It is surprisingly easy to use and the method is very versatile.

```python
filter = df1["demand"]==300
df1.where(filter, inplace = True)
# display
df1
```

you can also make as many filters as you want and add the filters this way:

```python
df1.where(filter1 & filter2, inplace = True)
```

inplace= True means that the change will be applied on the original dataframe.

This is all for this Article. Hope it can enlighten your way :)
