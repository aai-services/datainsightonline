---
title: "Pandas Techniques in Python for Data Manipulation"
author: "Blessing Oluwadaara"
date: 2021-11-04
description: "IntroductionPython is the language of choice for data scientists. It provides a programming language's larger ecosystem as well as the expertise of competent scientific computation packages.Pandas is..."
categories: ["Pandas", "Python"]
image: images/9b2dd8_e18e68f5099b4386bfe24e7bfbcc6693.webp
wix-url: https://www.datainsightonline.com/post/pandas-techniques-in-python-for-data-manipulation
---
## Introduction
Python is the language of choice for data scientists. It provides a programming language's larger ecosystem as well as the expertise of competent scientific computation packages.

Pandas is a Python toolkit for creating simple, high-performance data structures and data analysis tools. The word 'panel data,' which refers to multidimensional data sets used in statistics and econometrics, inspired the name. Pandas was the most beneficial for data science operations among its scientific computation libraries. Wes McKinney came up with the moniker "Pandas" in 2008, which refers to both "Panel Data" and "Python Data Analysis."

This post will show you how to manipulate data in Python in different ways. I've also included some pointers that will help you work more efficiently.

## Why use pandas?
- Pandas makes it possible to evaluate large amounts of data and provide conclusions based on statistical theory.
- Pandas can clean up and produce understandable and useful data collections.
- In data science, relevant data is critical.

## Installation
Simply execute pip install pandas inside the Python environment to install pandas.

```python
C:\Users\Your Name>pip install pandas
```

If this command fails, try Anaconda, Spyder, or another Python distribution that already has Pandas installed.

## Import Pandas
Once Pandas is installed, use the import keyword to include it in your applications:

```python
import pandas
```

Now Pandas is imported and ready to use.

```python
import pandas
mydataset = {  'cars': ["BMW", "Volvo", "Ford"],
              'passings': [3, 7, 2]  }
myvar = pandas.DataFrame(mydataset)
print(myvar)
```

Output:

```python
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
```

Pandas is typically imported using the pd alias.

```python
import pandas as pd
```

Instead of pandas, the Pandas package is now known as pd.

```python
import pandas as pd
mydataset = {'cars': ["BMW", "Volvo", "Ford"],   'passings':                 [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)
```

Output:

```python
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
```

## Pandas Series
What is a Series?

A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.

```python
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
```

output:

```python
0    1
1    7
2    2
dtype: int64
```

## Create Labels
With the index argument, you can name your own labels.

```python
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
```

output:

```python
x    1
y    7
z    2
dtype: int64
```

## Series of Key/Value Objects
When creating a Series, you can also use a key/value object like a dictionary.

```python
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
```

output:

```python
day1    420
day2    380
day3    390
dtype: int64
```

Note that the dictionary's keys serve as labels.

## DataFrames
DataFrames are multi-dimensional tables that Pandas uses to store data.

A DataFrame is the entire table, whereas a Series is a column.

Make a DataFrame by combining two Series.

```python
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
```

output:

```python
 calories  duration
0       420        50
1       380        40
2       390        45
```

## How row is located.
The DataFrame looks like a table with rows and columns, as you can see from the example above.

The loc property is used by Pandas to retrieve one or more specified rows(s)

```python
print(myvar.loc[0])
```

output:

```python
calories    420
duration     50
Name: 0, dtype: int64
```

It's worth noting that this example yields a Pandas Series.

```python
#use a list of indexes:
print(myvar.loc[[0, 1]])
```

Rows 0 and 1 must be returned:

output:

```python
   calories  duration
0       420        50
1       380        40
```

When you use [], you'll get a Pandas DataFrame as the output.

## Indexes with names
You can name your own indexes with the index parameter.

import pandas as pd

```python
data = {"calories": [420, 380, 390], "duration": [50, 40,                 45]}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
```

output:

```python
        calories  duration
day1       420        50
day2       380        40
day3       390        45
```

## Identify Named Indexes
To return the given row, use the named index in the loc property(s).

```python
#refer to the named index:
print(df.loc["day2"])
```

output:

```python
calories    380
duration     40
Name: day2, dtype: int64
```

## Files can loaded into a DataFrame.
Pandas can load your data sets into a DataFrame if they're saved in a file.

## CSV Files Can Be Read
CSV files are a straightforward way to store large data collections (comma separated files).

CSV files include plain text and are a well-known format that everyone, even Pandas, can read.

We'll be utilizing a CSV file called 'data.csv' in our examples.

Into a DataFrame, load a comma separated file (CSV file):

```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
```

output:

```python
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
```

## Getting information about the data
Information about the data can be extracted using the descride and info function as shown below

```python
df.info()
```

output:

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
```

```python
df.describe()
```

output:

```python
        Duration    Pulse    Maxpulse    Calories
count   169.000000 169.000000 169.000000 164.000000
mean    63.846154  107.461538 134.047337 375.790244
std     42.299949  14.510259  16.4504342 66.379919
min     15.000000  80.000000  100.000000 50.300000
25%     45.000000  100.000000 124.000000 250.925000
50%     60.000000  105.000000 131.000000 318.600000
75%     60.000000  111.000000 141.000000 387.600000
max     300.000000 159.000000 184.000000 1860.400000
```

## **JSON could be read into dataframe**.

JSON is frequently used to store or extract large data collections.

JSON is plain text with an object format that is well-known in the programming community, including Pandas.

We'll use a JSON file called 'data.js' in our examples.

```python
import pandas as pd
df = pd.read_json('data.js')
print(df)
```

output:

```python
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.4
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
```

## Viewing the Information
The head() function is one of the most commonly used methods for gaining a fast overview of the DataFrame.

Starting at the top, the head() function returns the headers and a given number of rows.

```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))
```

output:

```python
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.0
6        60    110       136     374.0
7        45    104       134     253.3
8        30    109       133     195.1
9        60     98       124     269.0
```

The head() function will return the top 5 rows if the number of rows is not given.

There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom.

```python
print(df.tail())
```

output:

```python
     Duration  Pulse  Maxpulse  Calories
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

Information on the Data

The DataFrames object contains a method named info() that provides additional data set information.

```python
print(df.info())
```

output:

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
```

## Manipulating Data
## Adding new column to existing DataFrame in Pandas
```python
# Import pandas package
import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
display(df)
```

output:

```python
	Name	Height	Qualification
0	Jai	5.1		Msc
1	Princi	6.2		MA
2	Gaurav	5.1		Msc
3	Anuj	5.2		Msc
```

**Method [#1](https://www.datainsightonline.com/blog/hashtags/1):** By declaring a new list as a column.

```python
# Declare a list that is to be converted into a column
location = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Using 'Address' as the column name
# and equating it to the list
df['Location '] = location
# Observe the result
df
```

output:

```python
	Name	Height	Qualification	Location
0	Jai	5.1	Msc		Delhi
1	Princi	6.2	MA		Bangalore
2	Gaurav	5.1	Msc		Chennai
3	Anuj	5.2	Msc		Patna
```

**Method [#2](https://www.datainsightonline.com/blog/hashtags/2):** By using DataFrame.insert()

```python
# Using DataFrame.insert() to add a column
df.insert(2, "Age", [21, 23, 24, 21], True)

# Observe the result
df
```

output:

```python
    Name    Height    Age    Qualification    Location
0    Jai      5.1     21        Msc            Delhi
1    Princi   6.2     23        MA            Bangalore
2    Gaurav   5.1     24        Msc            Chennai
3    Anuj     5.2     21        Msc            Patna
```

## Using Pandas to Work with Missing Data
When no information is supplied for one or more components, or for a whole unit, it is known as missing data. In real-life circumstances, missing data is a major issue. In pandas, missing data is sometimes referred to as NA (Not Available) values. Many datasets come in DataFrame with missing data, either because it exists but was not gathered or because it never existed. Assume that different people being questioned opt not to reveal their income, and that other users choose not to give their address, and that as a result, several datasets are missing.

None is a Python singleton object that is frequently used in Python programs to represent absent data.

NaN: A special floating-point value accepted by all systems that employ the standard IEEE floating-point encoding is NaN (an abbreviation for Not a Number).

None and NaN are used interchangeably in Pandas to indicate missing or null data. In Pandas DataFrame, there are numerous handy methods for detecting, deleting, and replacing null values to help with this convention:

isnull()

isnotnull()

isdropna()

isfillna()

isreplace()

isinterpolate()

We'll be utilizing a CSV file in this tutorial.

Searching for missing data, isnull() and notnull() are two functions that may be used to check if something is null ()

We utilize the functions isnull() and notnull() in Pandas DataFrame to check for missing data (). Both functions assist in determining whether or not a value is NaN. These functions may also be used to find null values in a series in Pandas Series.

isnull is used to check for missing values ()

We use the isnull() method to check for null values in a Pandas DataFrame. This function returns a dataframe of Boolean values that are True for NaN values.

```python
# importing pandas as pd
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
```

output:

```python
	First Score	Second Score	ThirdScore
0	False		False		True
1	False		False		False
2	True		False		False
3	False           True            False
```

```python
CODE 2
# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating bool series True for NaN values
bool_series = pd.isnull(data["Gender"])

# filtering data
# displaying data only with Gender = NaN
data[bool_series]
```

notnull() is used to check for missing values

We utilize the notnull() method to check for null values in a Pandas Dataframe. This function returns a dataframe of Boolean values that are False for NaN values.

```python
# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe using dictionary
df = pd.DataFrame(dict)

# using notnull() function
df.notnull()
```

output:

```python
    FirstScore    SecondScore    ThirdScore
0    True            True            False
1    True            True            True
2    False            True            True
3    True            False            True
```

```python
# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating bool series True for NaN values
bool_series = pd.notnull(data["Gender"])

# filtering data
# displayind data only with Gender = Not NaN
data[bool_series]
```

output:

```python
    FirstName  Gender    StartDate    LastLoginTime  Salary  Bonus %  \
0      Douglas    Male   8/6/1993        12:42 PM   97308    6.945
1       Thomas    Male  3/31/1996         6:53 AM   61933    4.170
2        Maria  Female  4/23/1993        11:17 AM  130590   11.858
3        Jerry    Male   3/4/2005         1:00 PM  138705    9.340
4        Larry    Male  1/24/1998         4:47 PM  101004    1.389
..         ...     ...        ...             ...     ...      ...
994     George    Male  6/21/2013         5:47 PM   98874    4.479
996    Phillip    Male  1/31/1984         6:30 AM   42392   19.675
997    Russell    Male  5/20/2013        12:39 PM   96914    1.421
998      Larry    Male  4/20/2013         4:45 PM   60500   11.985
999     Albert    Male  5/15/2012         6:24 PM  129949   10.169

    Senior Management                  Team
0                True             Marketing
1                True                   NaN
2               False               Finance
3                True               Finance
4                True       Client Services
..                ...                   ...
994              True             Marketing
996             False               Finance
997             False               Product
998             False  Business Development
999              True                 Sales

[855 rows x 8 columns]
```

Using fillna(), replace(), and interpolate() to fill in missing values

We employ the fillna(), replace(), and interpolate() functions to fill null values in datasets. These functions substitute NaN values with their own values. All of these functions aid in the filling of null values in DataFrame datasets. The Interpolate() method is used to fill NA values in a dataframe, but instead of hard-coding the value, it employs various interpolation techniques to do it.

```python
# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)

# filling a missing value with
# previous ones
df.fillna(method ='pad')
```

output:

```python
    First Score	    Second Score    Third Score
0	100.0	        30.0	        NaN
1	90.0	        45.0	        40.0
2	90.0	        56.0	        80.0
3	95.0	        56.0	        98.0
```

```python
# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# will replace  Nan value in dataframe with value -99
data.replace(to_replace = np.nan, value = -99)
```

output:

```python
First Name	Gender	Start Date	Last Login Time	Salary	Bonus %	Senior Management	Team
0	Douglas	Male	8/6/1993	12:42 PM	97308	6.945	True	Marketing
1	Thomas	Male	3/31/1996	6:53 AM	61933	4.170	True	-99
2	Maria	Female	4/23/1993	11:17 AM	130590	11.858	False	Finance
3	Jerry	Male	3/4/2005	1:00 PM	138705	9.340	True	Finance
4	Larry	Male	1/24/1998	4:47 PM	101004	1.389	True	Client Services
...	...	...	...	...	...	...	...	...
995	Henry	-99	11/23/2014	6:09 AM	132483	16.655	False	Distribution
996	Phillip	Male	1/31/1984	6:30 AM	42392	19.675	False	Finance
997	Russell	Male	5/20/2013	12:39 PM	96914	1.421	False	Product
998	Larry	Male	4/20/2013	4:45 PM	60500	11.985	False	Business Development
999	Albert	Male	5/15/2012	6:24 PM	129949	10.169	True	Sales
```

Using dropna() to remove missing values

We utilized the dropna() method to remove null values from a dataframe. This function removes rows/columns of datasets containing null values in a variety of ways.

```python
# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)
df
```

output:

```python
    First Score	Second Score	Third Score	Fourth Score
0	100.0	30.0	            52	            NaN
1	90.0	NaN	             40	            NaN
2	NaN	45.0	             80	            NaN
3	95.0	56.0	            98	            65.0
```

```python
#Dropping rows with at least 1 null value
# using dropna() function
df.dropna()
```

output:

```python
    First Score	Second Score	Third Score	Fourth Score
3	95.0	    56.0	     98	             65.0
```

```python
#Dropping columns with at least 1 null value.
# using dropna() function
df.dropna(axis = 1)
```

output:

```python
	Third Score
0	52
1	40
2	80
3	98
```

```python
# dictionary of lists
dict = {'First Score':[100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, np.nan, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)

df
```

output:

```python
    FirstScore    SecondScore	ThirdScore    FourthScore
0	100.0	    30.0	    52.0	NaN
1	NaN	    NaN	            NaN	        NaN
2	NaN	    45.0	    80.0	NaN
3	95.0	    56.0	    98.0	65.0
```

```python
#Dropping rows if all values in that row are missing
# using dropna() function
df.dropna(how = 'all')
```

```python
    First Score	Second Score	Third Score	Fourth Score
0	100.0	    30.0	    52.0	NaN
2	NaN	    45.0	    80.0	NaN
3	95.0	    56.0	    98.0	65.0
```

```python
Dropping Rows with at least 1 null value in CSV file
# making data frame from csv file
data = pd.read_csv("employees.csv")

# making new data frame with dropped NA values
new_data = data.dropna(axis = 0, how ='any')

new_data
```

output:

```python
    First Name	Gender	Start Date    Last Login Time        Salary	Bonus %	Senior Management	Team
0	Douglas	Male	8/6/1993	12:42 PM	97308	6.945	True	Marketing
2	Maria	Female	4/23/1993	11:17 AM	130590	11.858	False	Finance
3	Jerry	Male	3/4/2005	1:00 PM	138705	9.340	True	Finance
4	Larry	Male	1/24/1998	4:47 PM	101004	1.389	True	Client Services
5	Dennis	Male	4/18/1987	1:35 AM	115163	10.125	False	Legal
...	...	...	...	...	...	...	...	...
994	George	Male	6/21/2013	5:47 PM	98874	4.479	True	Marketing
996	Phillip	Male	1/31/1984	6:30 AM	42392	19.675	False	Finance
997	Russell	Male	5/20/2013	12:39 PM	96914	1.421	False	Product
998	Larry	Male	4/20/2013	4:45 PM	60500	11.985	False	Business Development
999	Albert	Male	5/15/2012	6:24 PM	129949	10.169	True	Sales
764 rows × 8 columns
```

you can also count the unique value in a particular column

```python
new_data.Team.value_counts()
```

output:

```python
Business Development    88
Client Services         85
Product                 83
Finance                 80
Engineering             79
Human Resources         76
Marketing               74
Sales                   72
Legal                   67
Distribution            60
Name: Team, dtype: int64
```

you can also change column name as shown below:

```python
new_data = data.rename(columns = {'Team':'Department'})
new_data.head()
```

output:

```python
   FirstName  Gender  StartDate  LastLoginTime  Salary Bonus%    SeniorManagement    Department
0    Douglas    Male    8/6/1993    12:42PM    97308    6.945    True    Marketing
1    Thomas    Male    3/31/1996    6:53AM    61933    4.170    True    NaN
2    Maria    Female    4/23/1993    11:17AM    130590 11.858    False    Finance
3    Jerry    Male    3/4/2005    1:00PM    138705    9.340    True    Finance
4    Larry    Male    1/24/1998    4:47PM    101004    1.389    True    Client Services
```

I’ll be using a company data provided by an [Intrinio developer sandbox](https://product.intrinio.com/developer-sandbox).

```python
import pandas as pd
import numpy as np
import urllib.request
url='https://raw.githubusercontent.com/leosmigel/analyzingalpha/master/2019-09-30-data-manipulation-with-python/companies.csv'
with urllib.request.urlopen(url) as f:
companies = pd.read_csv(f, index_col='id')
companies.head()
```

output:

```python
    name    cik	sector    industry_category    industry_group	        employees
id
1    Apple Inc	320193	Consumer Goods	Consumer Durables	Electronic Equipment	132000
2	American Express Co	4962	Financial	Financial Services	Credit Services	59000
3	Boeing Co	12927	Industrial Goods	Aerospace/Defense	Aerospace/Defense Products & Services	153027
4	Caterpillar Inc	18230	Industrial Goods	Manufacturing	Farm & Construction Machinery	104000
5	Cisco Systems Inc	858877	Technology	Computer Hardware	Networking & Communication Devices	74200
```

## groupby()
In data analysis, the "groupby()" function is highly important since it helps us to see the underlying correlations between distinct variables. Then, using the "agg()" method, we can apply Aggregations to the groups and feed it different aggregation operations such as mean, size, sum, std, and so on.

###### Aggregation
Aggregation takes the values and transforms them into a value of a smaller dimension. A function that accepts a series and returns a single scalar value is an example. A grouping column, an aggregate column, and a function column are all present in every GroupBy aggregation, either implicitly or explicitly. The following are some common aggregating functions:

|  |  |
| --- | --- |
| **FUNCTION** | **DESCRIPTION** |
| mean() | Compute mean of groups |
| sum() | Compute sum of group values |
| size() | Compute group sizes |
| count() | Compute count of group |
| std() | Standard deviation of groups |
| var() | Compute variance of groups |
| sem() | Standard error of the mean of groups |
| describe() | Generates descriptive statistics |
| first() | Compute first of group values |
| last() | Compute last of group values |
| nth() | Take nth value, or a subset if n is a list |
| min() | Compute min of group values |
| max() | Compute max of group values |

Lets consider an example of calculating the total number of enterprises in each industry.

```python
sector_group = companies.groupby(by='sector')
print(sector_group.size())
sector_group.size().sum()
```

output:

```python
sector
Basic Materials     2
Consumer Goods      4
Financial           5
Healthcare          4
Industrial Goods    5
Services            3
Technology          5
dtype: int64
28
```

We may also divide the data into groups based on numerous columns. The aggregate function was automatically called on the workers column because it is the sole number-type column.

```python
companies.groupby(['sector', 'industry_group'])['employees'].sum()
```

output:

```python
sector            industry_group
Basic Materials   Major Integrated Oil & Gas                   119600
Consumer Goods    Beverages - Soft Drinks                       62600
                  Electronic Equipment                         132000
                  Personal Products                             92000
                  Textile - Apparel Footwear & Accessories      73100
Financial         Credit Services                               76000
                  Investment Brokerage - National               36600
                  Money Center Banks                           256105
                  Property & Casualty Insurance                 30400
Healthcare        Drug Manufacturers - Major                   296500
                  Health Care Plans                            300000
Industrial Goods  Aerospace/Defense Products & Services        393027
                  Diversified Machinery                        376516
                  Farm & Construction Machinery                104000
Services          Discount, Variety Stores                    2200000
                  Home Improvement Stores                      413000
                  Restaurants                                  210000
Technology        Business Software & Services                 131000
                  Information Technology Services              350600
                  Networking & Communication Devices            74200
                  Semiconductor - Broad Line                   107400
                  Telecom Services - Domestic                  144500
Name: employees, dtype: int64
```

## Transformation
The altered data is returned in the same size as the provided data. To alter data, you may use a variety of methods and functions, as demonstrated below.

|  |  |
| --- | --- |
| **METHOD / FUNCTION** | **DESCRIPTION** |
| Series.map | Substitute each value for another |
| Series.apply | Invoke a function elementwise on a series |
| DataFrame.applymap | Apply a function elementwise to a dataframe |
| DataFrame.apply | Invoke a function on each column or row |
| Series.transform | Invoke a function returning series of transformed values |
| DataFrame.transform | Invoke a function returning dataframe of transformed values |
| pandas.melt | Reshape a dataframe. Useful for graphing, vectorized operations, and tidying data. |
| pandas.pivot | Reshape a dataframe. Essentially an unmelt operation |

We supply a specified function find percent and return the converted series in the example below.

```python
def find_percent(column):
  return column / float(column.sum())
companies.groupby('sector').agg({'employees': 'sum'}).transform(find_percent)
```

output:

```python
	employees
sector
Basic Materials	0.020003
Consumer Goods	0.060159
Financial	0.066749
Healthcare	0.099763
Industrial Goods	0.146098
Services	0.472141
Technology	0.135086
```

We can pass numerous functions, including lambda functions, just like we can with agg.

```python
companies.groupby('sector').agg({'employees':'sum'}).transform([lambda x: x / x.sum()])
```

output:

```python
	employees
<lambda>
sector
Basic Materials	0.020003
Consumer Goods	0.060159
Financial	0.066749
Healthcare	0.099763
Industrial Goods	0.146098
Services	0.472141
Technology	0.135086
```

While we can't send multiple functions to apply as we can with transform, we can use apply to access other columns that transform can't. Again, it's essential to be aware of what's available and to choose the greatest tool for the work at hand.

```python
companies.groupby('sector').apply(lambda x: x['employees'] * 2)
```

ouput:

```python
sector            id
Basic Materials   6       97200
                  28     142000
Consumer Goods    1      264000
                  14     125200
                  19     146200
                  21     184000
Financial         2      118000
                  25      34000
                  8       73200
                  13     512210
                  22      60800
Healthcare        12     270200
                  17     138000
                  20     184800
                  23     600000
Industrial Goods  3      306054
                  4      208000
                  7      566000
                  24     480000
                  16     187032
Services          9      826000
                  15     420000
                  27    4400000
Technology        5      148400
                  10     701200
                  11     214800
                  18     262000
                  26     289000
Name: employees, dtype: int64
```

## Filtration
The data returned by the filter is a subset of the original data. It operates in a similar way as boolean indexing, only it works on individual groups rather than individual rows. For the whole group, Filter must return a True or False response. The services industry is the only one with more than one million workers.

```python
companies.groupby('sector').filter(
    lambda x: x['employees'].sum() > 1000000
    )[['name', 'employees']]
```

output:

```python
         name	      employees
id
9	Home Depot Inc	413000
15	McDonald's Corp	210000
27	Walmart Inc	2200000
```

## Pivot Tables
Using pandas.pivot table, we may generate the same data in a different format.

```python
companies.pivot_table(columns='sector', values='employees', aggfunc='sum')
```

output:

```python
sector	Basic Materials	Consumer Goods	Financial	Healthcare	Industrial Goods	Services	Technology
employees	119600	359700	399105	596500	873543	2823000	807700
```

**Joining Data**

By using join, merge, and concat, we may swiftly join two dataframes. All join/merge behavior is based on the merging function. The settings for Join are slightly different, and it is given as a convenience technique.

|  |  |
| --- | --- |
| **METHOD / FUNCTION** | **DESCRIPTION** |
| pandas.DataFrame.join | Join dataframe on on index, or key column |
| pandas.DataFrame.merge | Merge dataframe using database-style joins |
| pandas.concat | Concatenate dataframes along a particular axis |

```python
import pandas as pd
import numpy as np
import urllib.request
url= 'https://raw.githubusercontent.com/leosmigel/analyzingalpha/master/2019-09-30-data-manipulation-with-python/securities.csv'
with urllib.request.urlopen(url) as f:
  securities = pd.read_csv(f, index_col='id')
securities.head()
```

output:

```python
	ticker	currency	figi
id
1	AAPL	USD	BBG000B9Y5X2
2	AXP	USD	BBG000BCR153
3	BA	USD	BBG000BCSV38
4	CAT	USD	BBG000BF0LJ6
5	CSCO	USD	BBG000C3JBN9
```

```python
securities_companies = companies.join(securities)
securities_companies.head()
```

output:

```python
name	cik	sector	industry_category	industry_group	employees	ticker	currency	figi
id
1	Apple Inc	320193	Consumer Goods	Consumer Durables	Electronic Equipment	132000	AAPL	USD	BBG000B9Y5X2
2	American Express Co	4962	Financial	Financial Services	Credit Services	59000	AXP	USD	BBG000BCR153
3	Boeing Co	12927	Industrial Goods	Aerospace/Defense	Aerospace/Defense Products & Services	153027	BA	USD	BBG000BCSV38
4	Caterpillar Inc	18230	Industrial Goods	Manufacturing	Farm & Construction Machinery	104000	CAT	USD	BBG000BF0LJ6
5	Cisco Systems Inc	858877	Technology	Computer Hardware	Networking & Communication Devices	74200	CSCO	USD	BBG000C3JBN9
```

## Conclusion
Pandas is an open source library for analyzing data in Python. It reads data from a CSV or SQL database and generates a data frame, which is an object containing rows and columns. In this post, we discussed different Pandas functions that might make our lives easier while undertaking data exploration and feature engineering. In addition, we built several generic methods that may be utilized to achieve similar goals on various datasets.
