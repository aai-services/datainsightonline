---
title: "Clean The Data, Open The Door !"
author: "Rawda Rumaieh"
date: 2021-12-08
description: "Since A lot will stick to dirty hands, Cleaning your data is a foundational step. It is the door opener.I can never guarantee that you will come up with incredible analysis if you cleaned your data..."
categories: ["Data Cleaning"]
image: images/d96e14_cba7ce3bb14146af984b61b1fb5f2b91.webp
wix-url: https://www.datainsightonline.com/post/clean-the-data-open-the-door
---
![](images/d96e14_cba7ce3bb14146af984b61b1fb5f2b91.webp)

Since A lot will stick to dirty hands, Cleaning your data is a foundational step. It is the door opener.I can never guarantee that you will come up with incredible analysis if you cleaned your data, but surely can guarantee that you will never be able to have a (fair) analysis if you didn't.

So let's jump to steps we must follow to clean the data and get fruitful insights from it.

For this articles I will be demonstrating the methods on a data-set taken from kaggle.

https://www.kaggle.com/PromptCloudHQ/us-jobs-on-monstercom

## Viewing the data

After reading the dataframe and saving it to df variable, I called the method:

```python
df.info()
```

This is the result

```python
 0   country          22000 non-null  object
 1   country_code     22000 non-null  object
 2   date_added       122 non-null    object
 3   has_expired      22000 non-null  object
 4   job_board        22000 non-null  object
 5   job_description  22000 non-null  object
 6   job_title        22000 non-null  object
 7   job_type         20372 non-null  object
 8   location         22000 non-null  object
 9   organization     15133 non-null  object
 10  page_url         22000 non-null  object
 11  salary           3446 non-null   object
 12  sector           16806 non-null  object
 13  uniq_id          22000 non-null  object
```

There are many columns with missing values.

Then I used the .describe() to some statistics and I found some unwanted columns.

For example, **has_expired** contains only **No. We** are also analysing USA only data so no need to have **country and country code.** We will also gain nothing from **job_board** since it contains only the same URL of the company.

Also, there are some columns which are not required for analysis such as **uniq_id and page_url.**

1) Pandas provides an easy way of removing columns or rows from a DataFrame with the **drop()** function.

```python
df=df.drop(['country','country_code','job_board','has_expired','page_url','uniq_id'], axis=1)
```

```python
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   date_added       122 non-null    object
 1   job_description  22000 non-null  object
 2   job_title        22000 non-null  object
 3   job_type         20372 non-null  object
 4   location         22000 non-null  object
 5   organization     15133 non-null  object
 6   salary           3446 non-null   object
 7   sector           16806 non-null  object
```

## Fixing the Data of some columns

Tthe job_type column contained some redundant data.

```python
df.job_type.value_counts()
```

```python
Full Time                                        6757
Full Time Employee                               6617
Full Time, Employee                              3360
Full Time Temporary/Contract/Project             1062
Full Time, Temporary/Contract/Project             533
Full Time , Employee                              406
Part Time Employee                                382
Part Time                                         329
Part Time, Employee                               196
```

To fix them:

```python
df['job_type'][df['job_type']=='Full Time Employee']='Full Time'
df['job_type'][df['job_type']=='Full Time , Employee']='Full Time'
df['job_type'][df['job_type']=='Full Time, Employee']='Full Time'
df['job_type'][df['job_type']=='Full Time, Temporary/Contract/Project']='Full Time'
df['job_type'][df['job_type']=='Full Time Temporary/Contract/Project']='Full Time'
df['job_type'][df['job_type']=='Part Time Employee']='Part Time'
df['job_type'][df['job_type']=='Part Time, Employee']='Part Time'
```

```python
Full Time                                        18735
Part Time                                          911
```

Let's check the completeness of this dataset.

```python
df.isnull().sum()
```

```python
date_added         21878
job_description        0
job_title              0
job_type            1628
location               0
organization        6867
salary             18554
sector              5194
dtype: int64
```

The Salary column is one of the most important in the dataset yet it contains to many null values !

We Have to Fix this... We will be digging more in this column

```python
df.salary.value_counts()
```

```python
40,000.00 - 100,000.00 $ /year        50
Commensurate with Experience          38
50,000.00 - 60,000.00 $ /year         32
75,000.00 - 85,000.00 $ /year         27
40,000.00 - 50,000.00 $ /year         26
                                      ..
57,000.00 - 60,000.00 $ /year          1
$24.00+ /year                          1
13.90 - 15.29 $ /hour                  1
Expected earnings $50k+                1
Send Salary History / Requirements     1
```

We can notice that we are having a range per year and a range per hour, the way it is represented is not so easy to handle due to commas and dollar sign..

We can construct a function and apply this function on a certain column.. this is a very handy technique in cleaning the data and working with it !

first define a function that first changes the Null values with NaN

and strip the '/hour' and the dollar sign, then splitting the maximum and minimum values so we can easier work with these values.

```python
def range_perHour_salary(x):
    if pd.isnull(x):
        return np.nan
    elif ' /hour' in val:
        i=x.split('/hour')[0].replace('$',' ').strip()
        if '-' in i:
            min=i.split('-')[0]
            max=i.split('-')[1]
```

Then we assign this function to our dataset by using

```python
df=df.assign(salary_perHour_Range=df['salary'].apply(range_perHour_salary))
```

the assign function takes the new column name, the column where i will apply the function on and the function name. to check the result we can use:

```python
df.salary_perHour_Range.value_counts()
```

```python
(20.00 ,  25.00)    22
(14.00 ,  14.00)    18
(12.00 ,  14.00)    18
(14.00 ,  16.00)    18
(12.00 ,  13.00)    17
                    ..
(14.50 ,  16.00)     1
(11.00 ,  13.50)     1
(13.00 ,  14.50)     1
(15.60 ,  15.60)     1
(52.00 ,  57.00)     1
```

In this particular dataset I couldn't drop the rows containing Null Vals since they are contributing with a big part in this dataset

The method for it is

```python
dropna()
```

Also the columns in my dataset were named in a good way so I didn't change them. However it may by crucial in some cases

we can then use

```python
df.rename(columns=new_names, inplace=True)
```

where new_names is a dictionary consisting of old name as a key and new name as a value

```python
new_names =  {'old': 'new'}
```

Each dataset can have different problems .. however practising is the key so you can know exactly the problems and the way to tackle them
