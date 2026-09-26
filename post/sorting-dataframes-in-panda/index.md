---
title: "Sorting DataFrames in Panda"
author: "Arpan Sapkota"
date: 2021-11-22
description: "We can use df.sort_values in order to sort Pandas DataFrame.In this short tutorial, We see 3 examples of sorting:1. A column in an ascending order2. A column in a descending order3. By multiple..."
categories: ["Pandas"]
image: images/a8b2bc_6ef0ed3fe76445d4bfc165fcb3137d5e.webp
wix-url: https://www.datainsightonline.com/post/sorting-dataframes-in-panda
---
![](images/a8b2bc_6ef0ed3fe76445d4bfc165fcb3137d5e.webp)

We can use df.sort_values in order to sort Pandas DataFrame.

In this short tutorial, We see 3 examples of sorting:

1. A column in an *ascending* order
2. A column in a *descending* order
3. By multiple columns

Lets start with the dataframe;

```python
import pandas as pd
data = {
'Brand': ['HH','TT','FF','AA'],
'Price': [22000,25000,27000,35000],
'Year': [2015,2013,2018,2018]
}
df = pd.DataFrame(data, columns=['Brand','Price','Year'])
print (df)
```

1. Sort Pandas DataFrame in an ascending order

Let’s say that we want to sort the DataFrame, such that the Brand will be displayed in an ascending order. In that case, we need to add the following syntax to the code:

```python
df.sort_values(by=['Brand'], inplace=True)
```

Note that unless specified, the values will be sorted in an ascending order by default.

Sorted Dataframe in ascending order look like this:

```python
print (df)
```

```python
  Brand  Price  Year
3    AA  35000  2018
2    FF  27000  2018
0    HH  22000  2015
1    TT  25000  2013
```

When we run the code, we notice that the Brand will indeed get sorted in an ascending order, where ‘AA’ would be the first record, while ‘TT’ would be the last:

2. Sort Pandas DataFrame in a descending order

Alternatively, we can sort the Brand column in a descending order. To do that, simply add the condition of ascending=False in the following manner:

sort Brand in a descending order

```python
df.sort_values(by=['Brand'], inplace=True, ascending=False)
```

Sorted Dataframe in descending order look like this:

```python
print (df)
```

```python
  Brand  Price  Year
1    TT  25000  2013
0    HH  22000  2015
2    FF  27000  2018
3    AA  35000  2018
```

We now notice that ‘TT’ would be the first record, while ‘AA’ would be the last (as we would expect to get when applying a descending order for our sample):

3. Sort by multiple columns

In this case, we may use the following template to sort by multiple columns:

```python
df.sort_values(by=['First Column','Second Column',...], inplace=True)
```

Suppose that we want to sort by both the ‘Year’ and the ‘Price.’ Since we have two records where the Year is 2018 (i.e., for the ‘FF’ and the ‘AA’ brands), then sorting by a second column – the ‘Price’ column – would be useful:

```python
# sort by multiple columns: Year and Pricedf.sort_values(by=['Year','Price'], inplace=True)

print (df)
 Brand  Price  Year
1    TT  25000  2013
0    HH  22000  2015
2    FF  27000  2018
3    AA  35000  2018
```

Notice that all the records are now sorted by both the year and the price in an ascending order, so ‘FF’ would appear before ‘AA’:

Also note that the ‘Year’ column takes the priority when performing the sorting, as it was placed in the df.sort_values before the ‘Price’ column.
