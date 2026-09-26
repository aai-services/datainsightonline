---
title: "Pandas Techniques for Data Manipulation in Python"
author: "Ahmed Shebl"
date: 2022-02-18
description: "1. Apply Function:This function takes a function as an input and applies this function to an entire DataFrame or every single value of the pandas series. The apply() function can be used with default..."
categories: ["Pandas", "Python"]
image: images/1af961_afcd3d9c37f948b484521bffc6b85f48.webp
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-data-manipulation-in-python-4
---
**1. Apply Function:**

This function takes a function as an input and applies this function to an entire DataFrame or every single value of the pandas series. The **apply()** function can be used with default or user-defined functions. When we work with DataFrame, we must specify an axis we want the function to act on(columns: 0, rows: 1).

Let’s see an example:

1. **import** **pandas** **as** **pd**
2. df = pd.read_csv('summer2016.csv')
3. df.head(2)

![](images/1af961_afcd3d9c37f948b484521bffc6b85f48.webp)

Let's say we want to create a new column which is transforming the Height by meter (= Height / 100) of each player

we can use apply() with lambda function

1. df['Height_Square'] = df['Height'].apply(**lambda** h: h/100)
3. df.head(2)

![](images/1af961_f618eac8d1b74007857f409128b73100.webp)

Now, let's try to calculate PMI(= Weight / Height\*\*2), then create a new column "PMI"

We use the second argument "axis = 1" to make calculations for each row

1. df['PMI'] = df.apply(**lambda** row: row['Weight'] / row['Height_Square']\*\*2, axis = 1)
3. df.head(2)

![](images/1af961_d9f52186704042cf9ffd58ef51d32b22.webp)

We can create another column "PMI_Status" and fill it with the status related to this PMI value. We can define a function and use it with apply()

1. **def** pmi_range(row):
2. status = ""
3. **if** row['PMI'] < 18.5:
4. status = 'Thin'
5. **elif** row['PMI'] > 25:
6. status = 'Obese'
7. **else**:
8. status = 'Normal'
10. **return** status
12. df['PMI_Status'] = df.apply(pmi_range, axis=1)
14. df.head(2)

![](images/1af961_00ca40b5976849bcab0424298d09d9b8.webp)

Also, we can use the built-in function from the NumPy module, to calculate the mean of two columns("Weight" and "Height").

like this

1. **import** **numpy** **as** **np**
2. df[['Weight', 'Height']].apply(np.mean, axis=0)

![](images/1af961_427fd102cd2043a397b97ce60824d9c1.webp)

Note: We can use map() when dealing with one column (Series) in the data frame (map() is used to substitute each value in a Series with another), but when dealing with more than one column we use apply() (apply() is used to apply a function along an axis of the DataFrame or on values of Series. )

**2. Boolean Indexing****:**

Its main task is to use the actual values of the data in the DataFrame to select subsets of data based on the actual values of the data in the DataFrame and not on their row/column labels or integer locations.. In boolean indexing, we use a boolean vector to filter the data. We can filter the data in the boolean indexing in different ways, which are as follows:

1. **import** **pandas** **as** **pd**
2. df = pd.read_csv('summer2016.csv')
3. df.head(2)

![](images/1af961_40824b6d8e54490c946750ae69101160.webp)

We can select rows and columns of a data frame using boolean arrays.

1. mask = df['Age'] > 50
2. print(mask)

![](images/1af961_a7937846521f4547aed2950cc17e4d3f.webp)

1. df[mask]

![](images/1af961_e2d263cc527e4812a40aebe33cea3cd8.webp)

We also can make a boolean index first

1. df.index = mask
3. df.head(2)

![](images/1af961_e71903d9faab48bb8dac41e798135c69.webp)

then, we can access dataframe using .loc[] function

1. df.loc[**True**]

![](images/1af961_35446d6b11a745b2aa2c018ffea6ee17.webp)

**3. Cut function****:**

Pandas cut() function is used to segregate array elements into separate bins.
The cut() function works only on one-dimensional array-like objects.
The cut() function is useful when we have a large number of scalar data and we want to perform some statistical analysis on it.

1. **import** **pandas** **as** **pd**
2. df = pd.read_csv('summer2016.csv')
3. df.head(2)

![](images/1af961_11c83b52cf6e45379e5049968793bcf2.webp)

1. df['Age_bins'] = pd.cut(x=df['Age'], bins = [10, 20, 30, 40, 50, 60])
3. df.head(10)

![](images/1af961_1c6a0a48c65747909deda8091d0c7488.webp)

We can also add labels to these bins

1. df['Age_bins'] = pd.cut(x=df['Age'], bins = [10, 20, 30, 40, 50, 60],
2. labels=['ten to twenty', 'twenty to thirty', 'thirty to forty', 'forty to fifty', 'fifty to sixty'])
4. df.head()

![](images/1af961_b2ef81e05d3e45bf9a2cd430151d14c9.webp)

**4. query() method****:**

It's is one of the methods pandas provide to filter (subsetting) a data frame.

1. **import** **pandas** **as** **pd**
2. df = pd.read_csv('summer2016.csv')
3. df.head(2)

![](images/1af961_4a519fdd940d4007af11c6daf420ee6f.webp)

1. df.query('Age > 55')

![](images/1af961_f6a165ec38c44f6198d09847bf5c553e.webp)

We can use multi conditions

1. df.query('Age > 50 and Height > 175')

![](images/1af961_0b771dd0df114e47832d981043d06280.webp)

### 5. Removing VAriables from a data frame****:
1. **import** **pandas** **as** **pd**
2. df = pd.read_csv('summer2016.csv')
3. df.head(2)

![](images/1af961_e85546f1eb924232b2ca22795e9fbf3f.webp)

We can remove a column, like this:

1. df.drop('NOC', axis=1)

![](images/1af961_b31e99003e2c4346bd77bf067449f0b0.webp)

We also can remove multiple columns, by putting a list in the .drop() method, containing all the columns we want to remove. like this:

1. df.drop(['NOC', 'Team'], axis=1)

![](images/1af961_f9887b4a4060440a9808011abc066c8e.webp)

If we want to make the change permanent, we add the inplace argument:

1. df.drop('Name', axis=1, inplace=**True**)
3. df

![](images/1af961_850b9caa663a47b299a15fef6002cf2c.webp)
