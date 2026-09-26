---
title: "Data Cleaning In Python"
author: "Sakayo Toadoum Sari"
date: 2021-12-08
description: "Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many..."
categories: ["Data Cleaning", "Python"]
wix-url: https://www.datainsightonline.com/post/data-cleaning-in-python
---
Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many opportunities for data to be duplicated or mislabeled. If data is incorrect, outcomes and algorithms are unreliable, even though they may look correct ([Click here](https://www.tableau.com/learn/articles/what-is-data-cleaning#:~:text=Data%20cleaning%20is%20the%20process,incomplete%20data%20within%20a%20dataset.&text=If%20data%20is%20incorrect%2C%20outcomes,though%20they%20may%20look%20correct.))

Data scientists spend a large amount of their time cleaning datasets and getting them down to a form with which they can work. A lot of data scientists argue that the initial steps of obtaining and cleaning data constitute 80% of the job.

#### Common Issues With Data are:

- Reading the file
- Inconsistent Column Names
- Missing Data
- Different Data Types
- Duplicate rows
- etc

#### Loading or Reading the File

- Encoding Error
- Inconsistent rows

```python
# importing packages
import pandas as pd
import numpy as np
```

```python
# Issue 1
df = pd.read_csv("unclean_data.csv")
```

```python
---------------------------------------------------------------------------

UnicodeDecodeError                        Traceback (most recent call last)

<ipython-input-3-0b7adce25293> in <module>
      1 # Issue 1
----> 2 df = pd.read_csv("unclean_data.csv")

~\anaconda3\lib\site-packages\pandas\util\_decorators.py in wrapper(*args, **kwargs)
    309                     stacklevel=stacklevel,
    310                 )
--> 311             return func(*args, **kwargs)
    312
    313         return wrapper

~\anaconda3\lib\site-packages\pandas\io\parsers\readers.py in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, error_bad_lines, warn_bad_lines, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)
    584     kwds.update(kwds_defaults)
    585
--> 586     return _read(filepath_or_buffer, kwds)
    587
    588

~\anaconda3\lib\site-packages\pandas\io\parsers\readers.py in _read(filepath_or_buffer, kwds)
    480
    481     # Create the parser.
--> 482     parser = TextFileReader(filepath_or_buffer, **kwds)
    483
    484     if chunksize or iterator:

~\anaconda3\lib\site-packages\pandas\io\parsers\readers.py in __init__(self, f, engine, **kwds)
    809             self.options["has_index_names"] = kwds["has_index_names"]
    810
--> 811         self._engine = self._make_engine(self.engine)
    812
    813     def close(self):

~\anaconda3\lib\site-packages\pandas\io\parsers\readers.py in _make_engine(self, engine)
   1038             )
   1039         # error: Too many arguments for "ParserBase"
-> 1040         return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
   1041
   1042     def _failover_to_python(self):

~\anaconda3\lib\site-packages\pandas\io\parsers\c_parser_wrapper.py in __init__(self, src, **kwds)
     67         kwds["dtype"] = ensure_dtype_objs(kwds.get("dtype", None))
     68         try:
---> 69             self._reader = parsers.TextReader(self.handles.handle, **kwds)
     70         except Exception:
     71             self.handles.close()

~\anaconda3\lib\site-packages\pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader.__cinit__()

~\anaconda3\lib\site-packages\pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader._get_header()

~\anaconda3\lib\site-packages\pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader._tokenize_rows()

~\anaconda3\lib\site-packages\pandas\_libs\parsers.pyx in pandas._libs.parsers.raise_parser_error()

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 275: invalid start byte
```

We are getting this error because Python tries to convert a byte-array (bytes which it assumes to be a utf-8-encoded string) to a Unicode string (str). This process of course is decoding according to utf-8 rules. When it tries this, it encounters a byte sequence that is not allowed in utf-8-encoded strings (namely this 0xff at position 0).

As a solution we can use the following code it will strip out (ignore) the characters and return the string without them. We only use this if our need is to strip them not convert them.

```python
# Solution 1
# Use Text Editor and Save it as Utf-8,ISO-8859-1,latin1
df = pd.read_csv("unclean_data1.csv",encoding='utf8')
```

```python
#print out the head of the dataframe
df.head()
```

#### Inconsistent Column Names

- Change Cases
- Rename them

```python
df.columns
```

```python
Index(['movie_title', 'num_critic_for_reviews', 'duration',
       'DIRECTOR_facebook_likes', 'actor_3_facebook_likes',
       'ACTOR_1_facebook_likes', 'gross', 'num_voted_users',
       'Cast_Total_facebook_likes', 'facenumber_in_poster',
       'num_user_for_reviews', 'budget', 'title_year',
       'ACTOR_2_facebook_likes', 'imdb_score', 'title_year.1'],
      dtype='object')
```

According to these columns’ names, it appears that they are inconsistent (a mix of upper and lower). When can convert all the columns names to upper:

```python
df.columns=df.columns.str.upper()
```

```python
df.columns
```

```python
Index(['MOVIE_TITLE', 'NUM_CRITIC_FOR_REVIEWS', 'DURATION',
       'DIRECTOR_FACEBOOK_LIKES', 'ACTOR_3_FACEBOOK_LIKES',
       'ACTOR_1_FACEBOOK_LIKES', 'GROSS', 'NUM_VOTED_USERS',
       'CAST_TOTAL_FACEBOOK_LIKES', 'FACENUMBER_IN_POSTER',
       'NUM_USER_FOR_REVIEWS', 'BUDGET', 'TITLE_YEAR',
       'ACTOR_2_FACEBOOK_LIKES', 'IMDB_SCORE', 'TITLE_YEAR.1'],
      dtype='object')
```

#### Renaming Columns

We can also decide to rename a column using the following line of code:

```python
df.rename(columns = {'DURATION':'TIME'})
```

#### Missing Data

In statistics, missing data, or missing values, occur when no data value is stored for the variable in an observation. Missing data are a common occurrence and can have a significant effect on the conclusions that can be drawn from the data.

Missing data can occur because of nonresponse: no information is provided for one or more items or a whole unit (“subject”). Some items are more likely to generate a non response than others: for example items about private subjects such as income ([Wikipedia](https://en.wikipedia.org/wiki/Missing_data)).

There are many techniques that can be used to deal with missing data/values.

- Add a default value for missing data or use mean to fill it
- Delete the row/column with missing data
- Interpolate the rows
- Replace

#### To check for missing data

#### False means no missing data

- df.isnull().sum() int
- df.isnull().any() bool

```python
df.isnull().head()
```

```python
df.isnull().any()
```

```python
MOVIE_TITLE                  False
NUM_CRITIC_FOR_REVIEWS       False
DURATION                      True
DIRECTOR_FACEBOOK_LIKES       True
ACTOR_3_FACEBOOK_LIKES       False
ACTOR_1_FACEBOOK_LIKES       False
GROSS                        False
NUM_VOTED_USERS               True
CAST_TOTAL_FACEBOOK_LIKES     True
FACENUMBER_IN_POSTER          True
NUM_USER_FOR_REVIEWS         False
BUDGET                       False
TITLE_YEAR                   False
ACTOR_2_FACEBOOK_LIKES        True
IMDB_SCORE                   False
TITLE_YEAR.1                  True
dtype: bool
```

This output shows all columns that contain missing values (True)

```python
# Columns with NAN using Integer
df.isnull().sum()
```

```python
MOVIE_TITLE                  0
NUM_CRITIC_FOR_REVIEWS       0
DURATION                     3
DIRECTOR_FACEBOOK_LIKES      2
ACTOR_3_FACEBOOK_LIKES       0
ACTOR_1_FACEBOOK_LIKES       0
GROSS                        0
NUM_VOTED_USERS              1
CAST_TOTAL_FACEBOOK_LIKES    2
FACENUMBER_IN_POSTER         5
NUM_USER_FOR_REVIEWS         0
BUDGET                       0
TITLE_YEAR                   0
ACTOR_2_FACEBOOK_LIKES       1
IMDB_SCORE                   0
TITLE_YEAR.1                 7
dtype: int64
```

```python
# Total Number of Missing NA
df.isnull().sum().sum()
```

```python
21
```

#### Adding A Default Value or Filling the Missing Data

We can fill in missing data using a default value.

```python
df.head()
```

We can fill all the NAN with zero (0).

```python
df_with_0 = df.fillna(0)
df_with_0.head()
```

We can also fill it using the mean().

```python
# Fill it with the mean
df['DURATION'].mean()
```

```python
150.72727272727272
```

```python
df_with_mean = df.DURATION.fillna(df['DURATION'].mean())
```

```python
df_with_mean
```

```python
0     178.000000
1     150.727273
2     148.000000
3     150.727273
4     132.000000
5     156.000000
6     150.727273
7     141.000000
8     141.000000
9     153.000000
10    183.000000
11    169.000000
12    106.000000
13    151.000000
Name: DURATION, dtype: float64
```

#### Droping NA

```python
## Droping NA
df.head()
```

```python
df.shape
```

```python
(14, 16)
```

```python
df_drop = df.dropna()
```

```python
df_drop.shape
```

```python
(4, 16)
```

Our shape have changed to 4 by 16 instead of 14 by 16 because we have dropped missing values.

```python
df_drop.head()
```

[Click here for full code and Data](https://github.com/Toadoum/Data-Insight-Certification-Data-Science-program-/tree/main/Cleaning%20Data)
