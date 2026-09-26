---
title: "Pandas Techniques for Data Manipulation"
author: "Md Ali Mortaza Sourav"
date: 2022-03-05
description: "Pandas is a powerful python library. Which is mostly used to manipulate and analyze data.Here, we discuss the basic tools that are used to manipulate and analyze data.1. Read datasets with Pandas2..."
categories: ["Pandas"]
image: images/f206ea_3e09fd1405b04a6cae17fc265ea0196f.webp
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-manipulation-3
---
Pandas is a powerful python library. Which is mostly used to manipulate and analyze data.

Here, we discuss the basic tools that are used to manipulate and analyze data.

1. Read datasets with Pandas
2. Apply functions
3. Sorting DataFrames
4. Removing duplicates
5. Cleaning Empty Cells

**Read datasets with Pandas**

An easy way to save large data sets is to use CSV files. CSV files contain plain text and are a well-known format that everyone, including Panda, can read.

![](images/f206ea_3e09fd1405b04a6cae17fc265ea0196f.webp)

**Apply functions**

Apply function in pandas is one of the commonly used functions for manipulating a pandas data frame and creating new variables.

![](images/f206ea_4e4cd1a406e848558da9f4dc43471a5a.webp)

**Sorting DataFrames**

The Pandas sort_values ​​() function arranges a data frame in ascending or descending order of the passed column. This is different from the sorted Python function because it cannot pick a data frame and select a specific column.

![](images/f206ea_b032bc8cc5424a9985d8a95a597fb075.webp)

**Removing duplicates**

We can use Pandas's built-in method drop_duplicates () to drop duplicate rows. By default, this method deletes duplicate rows and provides a new DataFrame. To remove duplicates from the original DataFrame, we can set the argument in place = True.

![](images/f206ea_85360667f7684b44a2a76070a82d6a42.webp)

**Cleaning Empty Cells**

Empty cells can give you an incorrect result when you analyze data. One way to deal with empty cells is to remove the rows that hold the empty cells.

![](images/f206ea_2f4341fdc3ad4789ba5b5d9d7c871b2d.webp)
