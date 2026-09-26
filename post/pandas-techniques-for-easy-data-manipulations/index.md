---
title: "Pandas Techniques for Easy Data Manipulation"
author: "Yosef Zeru Seyoum"
date: 2021-11-08
description: "Introductionpandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas is the right..."
categories: ["Pandas"]
wix-url: https://www.datainsightonline.com/post/pandas-techniques-for-easy-data-manipulations
---
## Introduction

[**pandas**](https://pandas.pydata.org/pandas-docs/stable/index.html#module-pandas) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the [Python](https://www.python.org/) programming language. Pandas is the right tool to handle data which is structured in tabular or spreadsheet format. Data stored in pandas in the form of table is called Data Frame, pandas primary data structure with labelled axes (rows and columns).

**1.** **Read DataFrame**

One of the many functionalities which makes pandas usable is that they support integration or transformation of data from one format to another. For example, we can convert from csv, excel, sql, json, parquet and many more to its standard form DataFrame.

read_csv() function helps read a comma-separated values (csv) file into a Pandas DataFrame. All you need to do is mentioned the path of the file you want it to read. It can also read files separated by delimiters other than comma, like | or tab. As displayed above the head () method helps to see the first N rows of the imported data frame by specifying how much rows we need to be displayed. The default display, without specifying N, shows the first five rows only. The syntax is DataFrame.head(N). pandas have a functionality to display N number of the last rows in the data frame based on the need using tail() in a similar fashion to head(). The last 10 rows of TITANIC dataframe looks like this.

```python
#Import Pandas Library
import pandas as pd
#Import titanic data  downloaded from https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv in to pandas dataframe
TITANIC = pd.read_csv("C:/Users/Yosef/OneDrive - cumc.columbia.edu/Desktop/titanic.csv")
#Make sure that it is imported correctly by reviewing the first few raws of the data fram
print(TITANIC.head())
print(TITANIC.shape)
```

**Output**

```python
PassengerId  Survived  Pclass  \
0            1         0       3
1            2         1       1
2            3         1       3
3            4         1       1
4            5         0       3

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1
2                             Heikkinen, Miss. Laina  female  26.0      0
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1
4                           Allen, Mr. William Henry    male  35.0      0

   Parch            Ticket     Fare Cabin Embarked
0      0         A/5 21171   7.2500   NaN        S
1      0          PC 17599  71.2833   C85        C
2      0  STON/O2. 3101282   7.9250   NaN        S
3      0            113803  53.1000  C123        S
4      0            373450   8.0500   NaN        S
(891, 12)
```

The method info() helps us to know more detailed things about our data frame and help us to answer questions like data types, null values, column labels and number of columns and rows in the dataframe. The syntax is similar with head() and tail(). The titanic dataframe looks like the following.

```python
#displaying the last 10 rows of TITANIC Data Frame
print(TITANIC.tail(10))
```

Output:

```python
PassengerId  Survived  Pclass                                      Name  \
881          882         0       3                        Markun, Mr. Johann
882          883         0       3              Dahlberg, Miss. Gerda Ulrika
883          884         0       2             Banfield, Mr. Frederick James
884          885         0       3                    Sutehall, Mr. Henry Jr
885          886         0       3      Rice, Mrs. William (Margaret Norton)
886          887         0       2                     Montvila, Rev. Juozas
887          888         1       1              Graham, Miss. Margaret Edith
888          889         0       3  Johnston, Miss. Catherine Helen "Carrie"
889          890         1       1                     Behr, Mr. Karl Howell
890          891         0       3                       Dooley, Mr. Patrick

        Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
881    male  33.0      0      0            349257   7.8958   NaN        S
882  female  22.0      0      0              7552  10.5167   NaN        S
883    male  28.0      0      0  C.A./SOTON 34068  10.5000   NaN        S
884    male  25.0      0      0   SOTON/OQ 392076   7.0500   NaN        S
885  female  39.0      0      5            382652  29.1250   NaN        Q
886    male  27.0      0      0            211536  13.0000   NaN        S
887  female  19.0      0      0            112053  30.0000   B42        S
888  female   NaN      1      2        W./C. 6607  23.4500   NaN        S
889    male  26.0      0      0            111369  30.0000  C148        C
890    male  32.0      0      0            370376   7.7500   NaN        Q
```

Having such summary let us proceed with explaining additional techniques which will help us to deal with the data in many ways one by one.

**2. PIVOT TABLES**

You may have experience of working on excel pivot tables and pandas have similar function called pivot_table. The syntax is

***pd.pivot_table(data, values=[“”], index=[“”], aggfunc=none, columns=none, margins=False, dropna=True, margins_name)***

- **Data** will denote the dataframe we imported. In our case TITANIC is the data frame.

- **Values** will be the column we planned to aggregate in pivot table. Let us aggregate Age and fare of the Passengers.

-  **Index** mean the column which helps us to group the data. For example, sex and class can be used to group and show pivot tables.

- **aggfunc** helps to aggregate the selected values by different metrics like mean, median and some.

- **margins and margins_name** help to add total for each column.

Example:

```python
#Create pivot table
Age_Sex = pd.pivot_table(TITANIC, values=["Age"], index=["Pclass"], aggfunc='mean')
print(Age_Sex)
```

Output:

```python
Age
Pclass
1       38.233441
2       29.877630
3       25.140620
```

Let us add another column and made the pivot more informative as follows.

```python
#Create pivot table
Age_Sex_1 = pd.pivot_table(TITANIC, values=["Age", "Fare"], index=["Pclass"], aggfunc='mean')
print(Age_Sex_1)
```

Output:

```python
Age       Fare
Pclass
1       38.233441  84.154687
2       29.877630  20.662183
3       25.140620  13.675550
```

**3.** **Merging DataFrames**

When you have data in multiple data frames you may need to merge two or more data frames to get the full image of the data. Pandas has different functionalities to merge these data frames.

We can use the following syntax to merge datafarmes horizontally.

**DataFrame1.****merge****(DataFrame2****,** **how='inner'****,** **on=None****,** **left_on=None****,** **right_on=None****,** **left_index=False****,** **right_index=False****,** **sort=False****,** **suffixes=('_x', '_y')****,** **copy=True****,** **indicator=False****,** **validate=None)**

Based on the data need we may use the arguments as needed. Let us merge Trending youtube videos datasets downloaded from <https://www.kaggle.com/datasnaek/youtube-new>. To do the following one by one.

- Let us import pandas

- Let us import Trending YouTube videos in France and Great Britain as VIDEO_1 and VIDEO_2 respectively.

```python
import pandas as pd
VIDEO_1 = pd.read_csv(r"C:\Users\Yosef\OneDrive - cumc.columbia.edu\Desktop\DATA\FRvideos.csv")
VIDEO_2 = pd.read_csv(r"C:\Users\Yosef\OneDrive - cumc.columbia.edu\Desktop\DATA\GBvideos.csv")
print(VIDEO_1.head())
print(VIDEO_2.head())
print(VIDEO_1.shape)
print(VIDEO_2.shape)
```

Output:

```python
video_id trending_date  \
0  Ro6eob0LrCY      17.14.11
1  Yo84eqYwP98      17.14.11
2  ceqntSXE-10      17.14.11
3  WuTFI5qftCE      17.14.11
4  ee6OFs8TdEg      17.14.11

                                               title        channel_title  \
0           Malika LePen : Femme de Gauche - Trailer  Le Raptor Dissident
1  LA PIRE PARTIE ft Le Rire Jaune, Pierre Croce,...              Le Labo
2  DESSINS ANIMÉS FRANÇAIS VS RUSSES 2 - Daniil...      Daniil le Russe
3                    PAPY GRENIER - METAL GEAR SOLID    Joueur Du Grenier
4  QUI SAUTERA LE PLUS HAUT ? (VÉLO SKATE ROLLER ...    Aurelien Fontenoy

   category_id              publish_time  \
0           24  2017-11-13T17:32:55.000Z
1           24  2017-11-12T15:00:02.000Z
2           23  2017-11-13T17:00:38.000Z
3           20  2017-11-12T17:00:02.000Z
4           17  2017-11-13T16:30:03.000Z

                                                tags   views  likes  dislikes  \
0  Raptor"|"Dissident"|"Expliquez"|"moi"|"cette"|...  212702  29282      1108
1                                             [none]  432721  14053       576
2      cartoon"|"pokémon"|"école"|"ours"|"мультфильм  482153  76203       477
3  Papy grenier"|"Metal Gear Solid"|"PS1"|"Tirage...  925222  85016       550
4  vélo"|"vtt"|"bmx"|"freestyle"|"bike"|"mtb"|"di...  141695   8091        72

   comment_count                                  thumbnail_link  \
0           3817  https://i.ytimg.com/vi/Ro6eob0LrCY/default.jpg
1           1161  https://i.ytimg.com/vi/Yo84eqYwP98/default.jpg
2           9580  https://i.ytimg.com/vi/ceqntSXE-10/default.jpg
3           4303  https://i.ytimg.com/vi/WuTFI5qftCE/default.jpg
4            481  https://i.ytimg.com/vi/ee6OFs8TdEg/default.jpg

   comments_disabled  ratings_disabled  video_error_or_removed  \
0              False             False                   False
1              False             False                   False
2              False             False                   False
3              False             False                   False
4              False             False                   False

                                         description
0  Dimanche.\n18h30.\nSoyez présents pour la vidé...
1  Le jeu de société: https://goo.gl/hhG1Ta\n\nGa...
2  Une nouvelle dose de dessins animés français e...
3  Nouvel ,épisode de Papy Grenier ! Ce mois-ci o...
4  Sauts à plus de 4 mètres de haut dans un tramp...
      video_id trending_date  \
0  Jw1Y-zhQURU      17.14.11
1  3s1rvMFUweQ      17.14.11
2  n1WpP7iowLc      17.14.11
3  PUTEiSjKwJU      17.14.11
4  rHwDegptbI4      17.14.11

                                               title  \
0      John Lewis Christmas Ad 2017 - #MozTheMonster
1          Taylor Swift: …Ready for It? (Live) - SNL
2         Eminem - Walk On Water (Audio) ft. Beyoncé
3  Goals from Salford City vs Class of 92 and Fri...
4  Dashcam captures truck's near miss with child ...

                channel_title  category_id              publish_time  \
0                  John Lewis           26  2017-11-10T07:38:29.000Z
1         Saturday Night Live           24  2017-11-12T06:24:44.000Z
2                  EminemVEVO           10  2017-11-10T17:00:03.000Z
3  Salford City Football Club           17  2017-11-13T02:30:38.000Z
4            Cute Girl Videos           25  2017-11-13T01:45:13.000Z

                                                tags     views   likes  \
0  christmas|"john lewis christmas"|"john lewis"|...   7224515   55681
1  SNL|"Saturday Night Live"|"SNL Season 43"|"Epi...   1053632   25561
2  Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/In...  17158579  787420
3  Salford City FC|"Salford City"|"Salford"|"Clas...     27833     193
4                                             [none]      9815      30

   dislikes  comment_count                                  thumbnail_link  \
0     10247           9479  https://i.ytimg.com/vi/Jw1Y-zhQURU/default.jpg
1      2294           2757  https://i.ytimg.com/vi/3s1rvMFUweQ/default.jpg
2     43420         125882  https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg
3        12             37  https://i.ytimg.com/vi/PUTEiSjKwJU/default.jpg
4         2             30  https://i.ytimg.com/vi/rHwDegptbI4/default.jpg

   comments_disabled  ratings_disabled  video_error_or_removed  \
0              False             False                   False
1              False             False                   False
2              False             False                   False
3              False             False                   False
4              False             False                   False

                                         description
0  Click here to continue the story and make your...
1  Musical guest Taylor Swift performs …Ready for...
2  Eminem's new track Walk on Water ft. Beyoncé i...
3  Salford drew 4-4 against the Class of 92 and F...
4  Dashcam captures truck's near miss with child ...
(40724, 16)
(38916, 16)
```

As you see un the summary VIDEO_1 has 40724 rows and 16 columns whereas VIDEO_2 has 38916 rows and 16 columns. This indicates that youtube videos in the first data frame may be different from videos in the second data frame, even if they contain similar number of columns. Key question here is that how can we merge these two dataframes? Pandas provide different options of merging dataframes.

- Let us merge VIDEO_1 and VIDEO_2 using common video_id column and inner joins as merging option, default option whether specified or not.

- Finally let us see number of rows and columns in the merged data set.

In the data frames used in this note all the columns have similar names. If we need to distinguish which section comes from which datafarme we can add suffixes as indicated in the code.

```python
#Merge the data frames by columns which are common for both
VIDEO_1_2 = VIDEO_1.merge(VIDEO_2, how="inner", on="video_id", suffixes=("_1", "_2"))
print(VIDEO_1_2.head())
print(VIDEO_1_2.shape)
```

Output:

```python
video_id trending_date_1                                     title_1  \
0  n1WpP7iowLc        17.14.11  Eminem - Walk On Water (Audio) ft. Beyoncé
1  n1WpP7iowLc        17.14.11  Eminem - Walk On Water (Audio) ft. Beyoncé
2  n1WpP7iowLc        17.14.11  Eminem - Walk On Water (Audio) ft. Beyoncé
3  n1WpP7iowLc        17.14.11  Eminem - Walk On Water (Audio) ft. Beyoncé
4  n1WpP7iowLc        17.14.11  Eminem - Walk On Water (Audio) ft. Beyoncé

  channel_title_1  category_id_1            publish_time_1  \
0      EminemVEVO             10  2017-11-10T17:00:03.000Z
1      EminemVEVO             10  2017-11-10T17:00:03.000Z
2      EminemVEVO             10  2017-11-10T17:00:03.000Z
3      EminemVEVO             10  2017-11-10T17:00:03.000Z
4      EminemVEVO             10  2017-11-10T17:00:03.000Z

                                              tags_1   views_1  likes_1  \
0  Eminem"|"Walk"|"On"|"Water"|"Aftermath/Shady/I...  17158579   787425
1  Eminem"|"Walk"|"On"|"Water"|"Aftermath/Shady/I...  17158579   787425
2  Eminem"|"Walk"|"On"|"Water"|"Aftermath/Shady/I...  17158579   787425
3  Eminem"|"Walk"|"On"|"Water"|"Aftermath/Shady/I...  17158579   787425
4  Eminem"|"Walk"|"On"|"Water"|"Aftermath/Shady/I...  17158579   787425

   dislikes_1  ...                                             tags_2  \
0       43420  ...  Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/In...
1       43420  ...  Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/In...
2       43420  ...  Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/In...
3       43420  ...  Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/In...
4       43420  ...  Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/In...

    views_2  likes_2  dislikes_2  comment_count_2  \
0  17158579   787420       43420           125882
1  20539417   840642       47715           124236
2  22702386   869304       50018           123227
3  24578152   891283       51977           125444
4  26448434   911883       53873           127481

                                 thumbnail_link_2 comments_disabled_2  \
0  https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg               False
1  https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg               False
2  https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg               False
3  https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg               False
4  https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg               False

  ratings_disabled_2 video_error_or_removed_2  \
0              False                    False
1              False                    False
2              False                    False
3              False                    False
4              False                    False

                                       description_2
0  Eminem's new track Walk on Water ft. Beyoncé i...
1  Eminem's new track Walk on Water ft. Beyoncé i...
2  Eminem's new track Walk on Water ft. Beyoncé i...
3  Eminem's new track Walk on Water ft. Beyoncé i...
4  Eminem's new track Walk on Water ft. Beyoncé i...

[5 rows x 31 columns]
(15838, 31)
```

Outer joins in pandas also known as left outer Join, returns a dataframe containing all the rows of the left dataframe and contain NaN for the columns in the right dataframe. What we need to do is change inner by outer in the merging code and save the data frame. Like the above outer joins, right joins can also be used to merge the dataframes based on our need.

**4.** **Pandas for summary statistics**

Summary statistics summarize and provide information about the data set we are trying to analyze. Pandas provides different functionalities on providing of summary statistics.

**describe ()** function helps to see the summary statistics for the attributes in dataframe. It will show us measures of central tendency and dispersion like mean, median, and percentiles. The syntax looks like the following. **DataFrame.****describe****(),** As example let us describe **YouTube** videos viewed in France. Let us import the data set and describe as follows.

```python
#Import Pandas
import pandas as pd
#Import the data frame
France_Videos = pd.read_csv(r"C:\Users\Yosef\OneDrive - cumc.columbia.edu\Desktop\DATA\FRvideos.csv")
#Generate the Statistical Summary using describe
France_Videos.describe()
```

Output:

```python
category_id     views   likes   dislikes        comment_count
count   40724.000000    4.072400e+04    4.072400e+04    4.072400e+04    4.072400e+04
mean    20.123809       4.199219e+05    1.738886e+04    8.149624e+02    1.832453e+03
std     6.984422        1.772130e+06    8.720509e+04    1.139219e+04    1.404321e+04
min     1.000000        2.230000e+02    0.000000e+00    0.000000e+00    0.000000e+00
25%     17.000000       1.697450e+04    3.380000e+02    1.800000e+01    5.600000e+01
50%     23.000000       7.372100e+04    1.892500e+03    8.300000e+01    2.350000e+02
75%     24.000000       2.708088e+05    7.969500e+03    3.350000e+02    8.410000e+02
max     44.000000       1.009116e+08    4.750254e+06    1.353661e+06    1.040912e+06
```

To calculate mean, median, minimum, and maximum values of views we can use the following code and get the results as seen below.

```python
print(France_Videos["views"].mean())

print(France_Videos["views"].median())

print(France_Videos["views"].min())

print(France_Videos["views"].max())
```

Output:

```python
419921.8506040664
73721.0
223
100911567
```

**5. Missing Values Handling**

Missing values are common in datasets due to different reasons. Whenever we deal or conduct data manipulation we must review and take necessary action on missing values. Pandas provide us different options to deal with missing values in dataframes.

Using You Tube videos trending in Great Britain let us review and manage missing values. We can see which column has non-missing rows using **df.info()** as follows.

```python
#Import Pandas
import pandas as pd
#Import the dataset as UK_VIWS
UK_VIEWS = pd.read_csv(r"C:\Users\Yosef\OneDrive - cumc.columbia.edu\Desktop\DATA\GBvideos.csv")
#Check whether missing value is available or not using .info()
print(UK_VIEWS.info())
```

Output:

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 38916 entries, 0 to 38915
Data columns (total 16 columns):
 #   Column                  Non-Null Count  Dtype
---  ------                  --------------  -----
 0   video_id                38916 non-null  object
 1   trending_date           38916 non-null  object
 2   title                   38916 non-null  object
 3   channel_title           38916 non-null  object
 4   category_id             38916 non-null  int64
 5   publish_time            38916 non-null  object
 6   tags                    38916 non-null  object
 7   views                   38916 non-null  int64
 8   likes                   38916 non-null  int64
 9   dislikes                38916 non-null  int64
 10  comment_count           38916 non-null  int64
 11  thumbnail_link          38916 non-null  object
 12  comments_disabled       38916 non-null  bool
 13  ratings_disabled        38916 non-null  bool
 14  video_error_or_removed  38916 non-null  bool
 15  description             38304 non-null  object
dtypes: bool(3), int64(5), object(8)
memory usage: 4.0+ MB
None
```

According to the output all 15 columns except the last column, description, has no missing values. Python paced missing values as NaN. Let us use **isna().any()** to detect these missing values in the above mentioned dataset. It will show us the status as Boolean (True or False).

```python
#Show Missing Values
UK_VIEWS.isna().any()
```

Output:

```python
video_id                  False
trending_date             False
title                     False
channel_title             False
category_id               False
publish_time              False
tags                      False
views                     False
likes                     False
dislikes                  False
comment_count             False
thumbnail_link            False
comments_disabled         False
ratings_disabled          False
video_error_or_removed    False
description                True
dtype: bool
```

To know the sum of those missing values we can use **isna().sum()** and the code and output looks like the following.

```python
#Count missing values in the dataset
UK_VIEWS.isna().sum()
```

Output:

```python
video_id                    0
trending_date               0
title                       0
channel_title               0
category_id                 0
publish_time                0
tags                        0
views                       0
likes                       0
dislikes                    0
comment_count               0
thumbnail_link              0
comments_disabled           0
ratings_disabled            0
video_error_or_removed      0
description               612
dtype: int64
```

Based on the need we can drop or replace missing values. To drop we can use a function called **dropna()**  and to replace we can use **fillna().**  Let us try both one by one using UK_VIEWS dataset.

```python
#Drop Missing Values from UK_VIEWS and Save as UK_VIEWS_1
UK_VIEWS_1 = UK_VIEWS.dropna()
#Check wheter missing values were dropped or not
UK_VIEWS_1.isna().sum()
```

Output:

```python
video_id                  0
trending_date             0
title                     0
channel_title             0
category_id               0
publish_time              0
tags                      0
views                     0
likes                     0
dislikes                  0
comment_count             0
thumbnail_link            0
comments_disabled         0
ratings_disabled          0
video_error_or_removed    0
description               0
dtype: int64
```

Replacing of null values using fillna().

```python
#Replace Missing Values with "Not Described" and save as UK_VIEWS_2
UK_VIEWS_2 = UK_VIEWS.fillna("Not Described")
#Check wheter missing values were replaced or not
UK_VIEWS_2.isna().sum()
```

Output:

```python
video_id                  0
trending_date             0
title                     0
channel_title             0
category_id               0
publish_time              0
tags                      0
views                     0
likes                     0
dislikes                  0
comment_count             0
thumbnail_link            0
comments_disabled         0
ratings_disabled          0
video_error_or_removed    0
description               0
dtype: int64
​
```

**References**

www. datacamp.com

<https://www.datainsightonline.com/>

Acknowledgement to data insights online data scientist program. https://www.datainsightonline.com/data-scientist-program
