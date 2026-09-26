---
title: "Pandas techniques - part 4 - Tidy Data"
author: "Thiha Naung"
date: 2021-10-07
description: "Happy families are all alike; every unhappy family is unhappy in its own way. ( Leo Tolstoy )Tidy datasets are all alike but every messy dataset is messy in its own way. ( Hadley Wickham )You can..."
categories: ["Pandas"]
image: images/1d64a7_4bff069766504b04bdb95296ffe538e9.webp
wix-url: https://www.datainsightonline.com/post/pandas-techniques-part-4-tidy-data
---
> Happy families are all alike; every unhappy family is unhappy in its own way. ( Leo Tolstoy )

> Tidy datasets are all alike but every messy dataset is messy in its own way. ( Hadley Wickham )

You can read about tidy data from the [Journal of Statistical Software](https://www.jstatsoft.org/article/view/v059i10) written by Hadley Wickham which described data cleaning, data tidying, relational databases and he coined the term '**tidy data**' and he explained when tidy data should be used and how to implement that type of data.

In general, a dataset is called tidy data if

1. Each variable forms a column.
2. Each observation forms a row.
3. Each type of observational unit forms a table.

The five most common problems with messy datasets are

1. Column headers are values, not variable names.
2. Multiple variables are stored in one column.
3. Variables are stored in both rows and columns.
4. Multiple types of observational units are stored in the same table.
5. A single observational unit is stored in multiple tables.

In that article, he used R language, and here I want to implement them by using Python. The Pandas techniques I want to focus on in this post are **melt** and **pivot**. ( not **pivot-table** )

### First dataset

This dataset will look like this.

![](images/1d64a7_4bff069766504b04bdb95296ffe538e9.webp)

It does not follow the rule of tidy data as the column headers should be the values. In Pandas, we can use the melt method for this kind of operation. First, see it in action.

The tidy data set looks like this.

![](images/1d64a7_fc757aa435eb46d2aed4f7ee31f27969.webp)

The melt method received

- **data frame**

- **id_vars** - column/s to use as identifier variables (means columns that you want to pivot)

- **value_vars** - column/s to unpivot ( columns that you want to become rows variables, in this case, I used as raw.columns[1:] means all columns without the first column from the data frame.)

- **var_name** - Name to use for the variable column

- **value_name** - Name to use for the value column

### Second Dataset

![](images/1d64a7_8d2aba4888fb4f459e0f57c35720c740.webp)

This dataset is about TB patients. The column names that contain 'm' are male patients and 'f' are female patients and the following numbers after 'm' and 'f' represent the age range. The values inside the table are case numbers. Let's clean the dataset.

![](images/1d64a7_0b586ba7c4e84c6bbb655765f680b6d6.webp)

The melt method is used and the 'column' contains both sex and age range, and this column needs to separate into 2 columns; 'sex' and 'age'. The cases column should be an integer type.

```python
array(['014', '1524', '2534', '3544', '4554', '5564', '65'], dtype=object)
```

The age column contains 7 unique values and I want to use the format with '-', for example '0-14','15-24'. So, I used the if-else loop to create that type of column. Then select the columns that are wanted.

![](images/1d64a7_f94c63df5a724eea97b8fe60a8bad933.webp)

### Third Dataset

![](images/1d64a7_2ab580b8d1d14b5f8df8995501064265.webp)

It is a weather dataset. There is a column for each possible day in the month. I used the melt method to gather the day column.

The first line from the code above is I want to use the data frame omitted from the first column and melt it into 'id', 'year', 'month', 'element', 'day', and 'temp' columns and then removed the missing values.

![](images/1d64a7_3ea8ea1f9e4a4a6c8a5dbc3ee36e7c85.webp)

For the day column, the first alphabet 'd' is removed. To be clear, year, month, and day columns are combined into the date column. From above code, the **zfill** method with 2 will fill with values with zero if the number from month or day has only one digit as I want to create the date format of 'YYYY/mm/dd'. Then changes into a date data type.

To that stage, the data frame looks like this.

![](images/1d64a7_a66f31fa9266408ebe91022e0ff0e700.webp)

I want to spread the values of the element columns into two columns; tmax and tmin. Here comes the **pivot** method.

- **index** - column to use to make new frame's index

- **columns** - column to use to make new frame's columns

- **values** - column/s to use for populating new frame's values.

The final result looks as following.

![](images/1d64a7_b52ccc8f27a143ff87fd9872da2993b9.webp)

Compared with the original raw data frame, there is a lot of improvement.

I think you will get the idea about tidy data and how to gather and separate the data. Thanks a lot for your time.

Here are my previous Pandas techniques articles:

- [read_csv](https://www.datainsightonline.com/post/pandas-techniques-part-1-read_csv)

- [groupby](https://www.datainsightonline.com/post/pandas-techniques-part-2-groupby)

- [merging dataframes](https://www.datainsightonline.com/post/pandas-techniques-part-3-merging-data-frames)
