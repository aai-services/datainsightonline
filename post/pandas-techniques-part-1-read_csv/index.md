---
title: "Pandas techniques - part 1 - read_csv( )"
author: "Thiha Naung"
date: 2021-10-06
description: "For a data scientist, the first step is to import data to the workplace. In python, most of us use the `read_csv` method for importing tabular data. I have written the `read_csv( )` method a thousand..."
categories: ["Pandas"]
wix-url: https://www.datainsightonline.com/post/pandas-techniques-part-1-read_csv
---
For a data scientist, the first step is to import data to the workplace. In python, most of us use the `read_csv` method for importing tabular data. I have written the `**read_csv**( )` method a thousand times but I only passed the `**file path`** parameter and did not aware of other parameters. There are many parameters you can pass. Here is [full documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html?highlight=read_csv#pandas.read_csv). The followings are the most useful parameters for this method, I think.

The data are created by the nano editor and the cat command shows the text (CSV) file. For example,

```python
cat datasets/example.csv
```

```python
a,b,c,d,e
1,2,3,4,hello
5,6,7,8,python
9,10,11,12,pandas
```

It is the actual text file that can be seen in the terminal or in the text editor. I only used the parameter for the file path.

```python
pd.read_csv('datasets/example.csv')
```

```python
   a   b   c   d       e
0  1   2   3   4   hello
1  5   6   7   8  python
2  9  10  11  12  pandas
```

Pandas imports the first line as header as default. If we want to import selected columns, we can pass the `**usecols**` parameter.

```python
pd.read_csv('datasets/example.csv', usecols=['a','b','e'])
```

```python
   a   b       e
0  1   2   hello
1  5   6  python
2  9  10  pandas
```

We can arrange the order of columns by adding a list of column orders.

```python
 pd.read_csv('datasets/example.csv', usecols=['a','b','e'])[['e','b','a']]
```

```python
        e   b  a
0   hello   2  1
1  python   6  5
2  pandas  10  9
```

If we do not want to use the first row as a header, we can use the `**header**` parameter sets to `**None**`.

```python
pd.read_csv('datasets/example.csv', header=None)
```

```python
   0   1   2   3       4
0  a   b   c   d       e
1  1   2   3   4   hello
2  5   6   7   8  python
3  9  10  11  12  pandas
```

If we import the data with no header, the column names will be set to numbers. If we want to specify the column names, we can use the `**names**` parameter.

```python
pd.read_csv('datasets/example.csv', header=None,
            names=['col1','col2','col3','col4','col5'])
```

```python
  col1 col2 col3 col4    col5
0    a    b    c    d       e
1    1    2    3    4   hello
2    5    6    7    8  python
3    9   10   11   12  pandas
```

We can set the index column with the `**index_col**` parameter.

```python
pd.read_csv('datasets/example.csv', header=None,
          names=['col1','col2','col3','col4','col5'],
          index_col = 'col5')
```

```python
       col1 col2 col3 col4
col5
e         a    b    c    d
hello     1    2    3    4
python    5    6    7    8
pandas    9   10   11   12
```

We can want to form a hierarchical index from multiple columns, pass a list of column numbers or names.

```python
cat datasets/2-example.csv
```

```python
key1,key2,value1,value2
one,a,1,2
one,a,3,4
one,b,5,6
one,b,7,8
two,a,1,2
two,a,3,4
two,b,5,6
two,b,7,8
```

```python
pd.read_csv('datasets/2-example.csv', index_col=['key1','key2'])
```

```python
           value1  value2
key1 key2
one  a          1       2
     a          3       4
     b          5       6
     b          7       8
two  a          1       2
     a          3       4
     b          5       6
     b          7       8
```

In some cases, the table might not have a fixed delimiter, using spaces, tabs, or other patterns to separate values. In that case, you can use a regular expression as a delimiter.

```python
cat datasets/3-example.csv
```

```python
	AAA	BBB	CCC
aaa	123	234	345
bbb	124	454	545
ccc	454	785	975
```

Here I use `tab` to separate values.

```python
pd.read_csv('datasets/3-example.csv', sep='\t')
```

```python
  Unnamed: 0  AAA  BBB  CCC
0        aaa  123  234  345
1        bbb  124  454  545
2        ccc  454  785  975
```

Sometimes, the data contains additional comment lines; for example,

```python
cat datasets/4-example.csv
```

```python
# this is an example how skip rows
# for pd.read_csv() method.
a,b,c,d,e
# this is also interrupted line
1,2,3,4,hello
5,6,7,8,python
2,4,6,8,pandas
```

You can skip the first, second, and fourth rows of that file with `**skiprows**`.

```python
pd.read_csv('datasets/4-example.csv', skiprows=[0,1,3])
```

```python
   a  b  c  d       e
0  1  2  3  4   hello
1  5  6  7  8  python
2  2  4  6  8  pandas
```

Or you can also use the `comment` parameter passing to a specific comment.

```python
pd.read_csv('datasets/4-example.csv', comment='#')
```

Output is the same. Handling missing values are important and missing values may present with an empty string or be marked by some sentinel values. By default, '#N/A', '-1.#IND', '#QNAN', '-NaN','-nan','NA', 'NaN', 'n/a','null', etc values are interpreted as NaN by default. For example,

```python
cat datasets/5-example.csv
```

```python
A,B,C,D,E
one,1,2,3,NA
two,4,5,NULL,6
three,-1.#IND,5,6,7
```

NA, NULL, -1.#IND values will be interpreted as NaN value.

```python
pd.read_csv('datasets/5-example.csv')
```

```python
       A    B  C    D    E
0    one  1.0  2  3.0  NaN
1    two  4.0  5  NaN  6.0
2  three  NaN  5  6.0  7.0
```

You can set other values to consider as missing values bypassing the **na_values** parameter, which can take either a list or set of strings.

```python
pd.read_csv('datasets/5-example.csv', na_values = ['one','6.0'])
```

The values 'one' and '6.0' will be considered as missing values and the output looks like this.

```python
       A    B  C    D    E
0    NaN  1.0  2  3.0  NaN
1    two  4.0  5  NaN  NaN
2  three  NaN  5  NaN  7.0
```

You can also specify the values according to columns.

```python
pd.read_csv('datasets/5-example.csv', na_values={'A': ['one','three'],'C':[5]})
```

Then, the value of 'one' and 'three' from column 'A' and value '5' from column 'C' will be considered as missing values.

```python
     A    B    C    D    E
0  NaN  1.0  2.0  3.0  NaN
1  two  4.0  NaN  NaN  6.0
2  NaN  NaN  NaN  6.0  7.0
```

When processing very large files or do not know which arguments/columns to use, you can read only a small piece of data or iterate through smaller chunks of the file. Here I create random data set that contains 2500 rows and 4 columns.

```python
arr = np.random.randn(10000).reshape(2500,4)
np.savetxt('datasets/6-example.csv',arr,delimiter=',')
```

```python
pd.read_csv('datasets/6-example.csv', nrows=5, header=None)
```

With the `**nrows`** parameter with the value, 5 will import only 5 rows of the data.

```python
          0         1         2         3
0  0.671909 -0.700201 -1.961235 -0.295577
1  1.278847 -0.275689 -0.282427 -0.086346
2 -0.232476 -1.221327 -0.687825 -0.107018
3  0.421533  1.217264  0.040075 -1.483822
4  1.158106 -0.894026 -0.058134 -0.075550
```

Or you can use the `**chunksize**` parameter to specify as the number of rows.

```python
chunk = pd.read_csv('datasets/6-example.csv',
        header=None, chunksize=5)
chunk
```

```python
<pandas.io.parsers.TextFileReader at 0x7f8d2e0605e0>
```

The TextParser object is returned and you can iterate over the parts of the file according to the chunk size. For example, `next(chunk)` will give you the first chunk with 5 rows as above. It is an iterator and you can also iterate through loops.

There are many parameters left for the **read_csv** method**.**

Here is thesummary of the above methods.

|  |  |
| --- | --- |
| ​Argument | Description |
| path | String indicating file system location, URL, or file-like object |
| sep or delimiter | Character sequence of regular expression to use to split fields in each row |
| header | Row number to use as column names. Default to 0 (first row), None if there is no header row |
| index_col | Column numbers or names to use as the row index in the result. Can be a single name/number or a list for a hierarchical index |
| names | List of column names for result, combine with header=None |
| skiprows | Number of rows at beginning of file to ignore or list of row numbers (starting from 0) to skip |
| na_values | Sequence of values to replace with NA |
| comment | Characters to split comments off the end of lines |
| nrows | Number of rows to read from beginning of file |
| chunksize | For iteration, size of file chunks |
