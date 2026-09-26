---
title: "Importing cleaning and Visualizing data using python"
author: "Umme Rubaiyat Chowdhury"
date: 2021-12-09
description: "In this instructional exercise, we’ll utilize Python’s Pandas and NumPy libraries to clean data. In the primary portion I will clarify cleaning information in python: • Dropping unnecessary columns..."
categories: ["Visualization", "Data Cleaning", "Python"]
wix-url: https://www.datainsightonline.com/post/importing-cleaning-and-visualizing-data-in-python-2
---
In this instructional exercise, we’ll utilize Python’s Pandas and NumPy libraries to clean data.

In the primary portion I will clarify cleaning information in python:

- Dropping unnecessary columns in a DataFrame
- Changing the index of a DataFrame
- Using .str methods to clean columns
- Using the DataFrame.apply() function to clean the column,
- Cleaning entire dataset using dataset.applymap (),
- Renaming columns to a more recognizable set of labels and Skipping unnecessary rows in a CSV file

Within the second portion, I will clarify how visualizing information in python Let’s begin with the primary portion and import the desired modules.

***1. Importing and cleaning data***

in this part, we will use three data sets

- BL-Flickr-Images-Book.csv – a data set that contains information about books
- university_towns.txt – A data set that contain some names of college
- olympics.csv – a data set summarizing the participation of all countries in summer

**Dropping unnecessary columns in a DataSet**

We start by importing the libraries (pandas and NumPy)

```python
# Import Libraries
import numpy as np
import pandas as pd
```

First, let’s create a data frame (name book) out of the CSV file ‘BL-Flickr-Images-Book.csv’.

```python
book = pd.read_csv('BL-Flickr-Images-Book.csv')
book.head()
```

Using the head() method, we inspect the first five entries.

Some of the columns provide information that might be beneficial to the library but are not descriptive of the books themselves, as can be seen.

Then we can use the drop() function to eliminate these columns:

```python
#Dropping Columns in a DataFrame
to_drop = ['Edition Statement','Corporate Author','Corporate Contributors','Former owner','Engraver','Contributors','Issuance type','Shelfmarks']
book.drop(to_drop, inplace=True, axis=1)

book.head()
```

We now can observe that the undesired columns have been eliminated when we inspect the DataSet again:

**Changing the Index of a DataSet**

We may expect that when a librarian looks for a record in the dataset we used in our example, he or she will be able to input the unique identification (values in the Identifier column) for a book:

```python
book['Identifier'].is_unique
```

Let's use set index to replace the existing index with this column:

```python
book = book.set_index('Identifier')
book.head()
```

With loc[], we can quickly access each record.

Despite its unassuming name, loc[] allows us to do label-based indexing, that is, naming a row or record regardless of its position:

```python
book.loc[206]
```

**Using .str methods to clean columns**

We may use Pandas' str methods and NumPy's np.where function to tidy up the Publication Location field.

Because this column contains string objects, we'll utilize these two routines to tidy up the publication location.

The column's contents are as follows:

```python
book['Place of Publication'].head(10)
```

We can see that the publication location for several lines contains superfluous information.

We can observe that this is only the case for some lines where the place of publishing is "London" or "Oxford" if we look at more values.

```python
book.loc[4157862]
```

```python
book.loc[4159587]
```

Both of these novels were published in the same location, however one contains hyphens in the place name while the other does not.

We can use str.contains() to generate a boolean mask to clean up this column in a single scan.

Then they're combined with np.where:

## Using DataSet.apply() for clean the column
```python
unwanted_characters = ['[', ',', '-']

def clean_dates(item):
    dop= str(item.loc['Date of Publication'])if dop == 'nan' or dop[0] == '[':return np.NaNfor character in unwanted_characters:if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]return dop

book['Date of Publication'] = book.apply(clean_dates, axis = 1)
book.head()
```

**Cleaning entire dataset using dataset.applymap ()**

In rare cases, the.applymap() method can be used to apply a custom function to each cell or element of a DataFrame.

We'll make a DataSet out of the file "university towns.txt" as follows:

```python
university_towns = []with open('university_towns.txt', 'r') as file:
    items = file.readlines()
    states = list(filter(lambda x: '[edit]' in x, items))for index, state in enumerate(states):
        start = items.index(state) + 1if index == 49: #since 50 states
            end = len(items)else:
            end = items.index(states[index + 1])

        pairs = map(lambda x: [state, x], items[start:end])
        university_towns.extend(pairs)

towns_df = pd.DataFrame(university_towns, columns = ['State', 'RegionName'])
towns_df.head()
```

the applymap() function is called on our object. Now the DataFrame is much cleaner. This method took each element of the DataFrame, passed it to the function and the original value was replaced with the returned value.

**Renaming columns and skipping rows**

Often, the datasets we'll be dealing with will include difficult-to-understand column names or unnecessary information in the initial and/or last rows, such as dataset definitions or footnotes.

We'd like to rename the columns and skip some rows in this situation so that we can get the information we need with accurate and understandable labeling.

Let's have a look at the first five rows of the "olympics.csv" data collection to see how this is done:

```python
olympics_df = pd.read_csv('olympics.csv')
olympics_df.head()
```

The columns are the string form of integers indexed at 0. The row that should have been our header (i.e. the one to use to define the column names) is at olympics_df.iloc[0]. This happened because our CSV file starts with 0, 1, 2, ..., 15.

Therefore, we need to do two things:

1. Ignore a row and set the header as the first row (0 indexed)
2. Rename the columns

We can skip rows and set the header when reading the CSV file bypassing some parameters to the read_csv() function.

This function takes a lot of optional parameters, but in this case, we only need one (header) to delete the 0th row:

```python
olympics_df = pd.read_csv('olympics.csv', skiprows = 1, header = 0)
olympics_df.head()
```

All extraneous rows have been eliminated, and the relevant row has been set as the header.

Take note of how Pandas renamed the column that contains country names from NaN to No name: 0.

We'll utilize the DataFrame's rename() method to change the columns, which allows you to rename an axis based on a mapping (in this case, a dict).

To begin, create a dictionary that links the present column names (as keys) to the more useful ones (the dictionary values):

Our object is passed to the rename() function, and in place is set to True, indicating that our modifications should be done directly to the object.

```python
new_names =  {'Unnamed: 0': 'Country','? Summer': 'Summer Olympics','01 !': 'Gold','02 !': 'Silver','03 !': 'Bronze','? Winter': 'Winter Olympics','01 !.1': 'Gold.1','02 !.1': 'Silver.1','03 !.1': 'Bronze.1','? Games': '# Games','01 !.2': 'Gold.2','02 !.2': 'Silver.2','03 !.2': 'Bronze.2'}

olympics_df.rename(columns = new_names, inplace = True)
olympics_df.head()
```

***2. Importing and visualizing data in python***

In this part, we will use iris.csv dataset

let's start with importing libraries and data

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)
iris = pd.read_csv("Iris.csv")
iris.head()
```

The first way to plot things is to use the .plot extension of Pandas data frames

We'll use it to create a scatterplot of the Iris features.

```python
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
```

We can also use the Seaborn library to make a similar plot

*A seaborn* jointplot shows bivariate scatterplots and univariate histograms on the same figure

```python
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)
```

One piece of information missing from the above graphs is the species of each plant.

Here we will use Seaborn's FacetGrid to color the scatterplot by species

```python
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
   .add_legend()
```

We can examine an individual feature in Seaborn through a boxplot

```python
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
```
