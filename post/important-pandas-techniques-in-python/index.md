---
title: "Important Pandas Techniques in Python"
author: "Mariam Ahmed"
date: 2022-05-20
description: "Apply a function to apply a function along an axis of the DataFrame we use:pandas.DataFrame.applyDataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)Objects passed to the..."
categories: ["Pandas", "Python"]
image: images/47a959_e075eb342a5140f99640c92dfd5b43a9.webp
wix-url: https://www.datainsightonline.com/post/important-pandas-techniques-in-python
---
![](images/47a959_e075eb342a5140f99640c92dfd5b43a9.webp)

### Apply a function
to apply a function along an axis of the DataFrame we use:

pandas.DataFrame.apply

```python
DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)
```

Objects passed to the function are Series objects whose index is either the DataFrame’s index (axis=0) or the DataFrame’s columns (axis=1). By default (result_type=None), the final return type is inferred from the return type of the applied function. Otherwise, it depends on the result_type argument.

**Parametersfunc**function

Function to apply to each column or row.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Axis along which the function is applied:

- 0 or ‘index’: apply function to each column.
- 1 or ‘columns’: apply function to each row.

**raw**bool, default False

Determines if row or column is passed as a Series or ndarray object:

- False : passes each row or column as a Series to the function.
- True : the passed function will receive ndarray objects instead. If you are just applying a NumPy reduction function this will achieve much better performance.

**result_type**{‘expand’, ‘reduce’, ‘broadcast’, None}, default None

These only act when axis=1 (columns):

- ‘expand’ : list-like results will be turned into columns.
- ‘reduce’ : returns a Series if possible rather than expanding list-like results. This is the opposite of ‘expand’.
- ‘broadcast’ : results will be broadcast to the original shape of the DataFrame, the original index and columns will be retained.

The default behaviour (None) depends on the return value of the applied function: list-like results will be returned as a Series of those. However if the apply function returns a Series these are expanded to columns.

**args**tuple

Positional arguments to pass to func in addition to the array/series.

**\*\*kwargs**

Additional keyword arguments to pass as keywords arguments to func.

**Returns**Series or DataFrame

Result of applying func along the given axis of the DataFrame.

### Filling missing values using Pandas

pandas.DataFrame.fillna

```python
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
```

Fill NA/NaN values using the specified method.

**Parameters : value :** scalar, dict, Series, or DataFrame

Value to use to fill holes (e.g. 0), alternately a dict/Series/DataFrame of values specifying which value to use for each index (for a Series) or column (for a DataFrame). Values not in the dict/Series/DataFrame will not be filled. This value cannot be a list.

**method :** {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None

Method to use for filling holes in reindexed Series pad / ffill: propagate last valid observation forward to next valid backfill / bfill: use next valid observation to fill gap.

**axis :** {0 or ‘index’, 1 or ‘columns’}

Axis along which to fill missing values.

**inplace :** bool, default False

If True, fill in-place. Note: this will modify any other views on this object (e.g., a no-copy slice for a column in a DataFrame).

**limit :** int, default None

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None.

**downcast :** dict, default is None

A dict of item->dtype of what to downcast if possible, or the string ‘infer’ which will try to downcast to an appropriate equal type (e.g. float64 to int64 if possible).

**Returns :** DataFrame or None

Object with missing values filled or None if inplace=True.

**Useful Examples:**

**>>>**

```python
>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
...                    [3, 4, np.nan, 6],
...                    [np.nan, np.nan, np.nan, np.nan],
...                    [np.nan, 3, np.nan, 8]],
...                   columns=list("ABCD"))
>>> df
    A    B   C    D
 0  NaN  2.0 NaN  0.0
 1  3.0  4.0 NaN  6.0
 2  NaN  NaN NaN  NaN
 3  NaN  3.0 NaN  8.0
```

Replace all NaN elements with 0s:

```python
>>> df.fillna(0)
    A    B    C    D
 0  0.0  2.0  0.0  0.0
 1  3.0  4.0  0.0  6.0
 2  0.0  0.0  0.0  0.0
 3  0.0  3.0  0.0  8.0
```

We can also propagate non-null values forward or backward:

```python
>>> df.fillna(method="ffill")
    A    B   C    D
 0  NaN  2.0 NaN  0.0
 1  3.0  4.0 NaN  6.0
 2  3.0  4.0 NaN  1.0
 3  3.0  3.0 NaN  8.0
```

That's it, I hope this article was worth reading and helped you acquire new knowledge no matter how small.

Feel free to check up on the [notebook](https://github.com/MariamAlsaedy/Data-Insight-Scholarship-Article-4/blob/main/Pandas.ipynb). You can find the results of code samples in this post.
