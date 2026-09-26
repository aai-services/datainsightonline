---
title: "Basic Data Visualization using Seaborn"
author: "Rubash Mali"
date: 2021-12-09
description: "In this blog we will apply some basic statistical univariate and bivariate techniques to visualize and gain insights on the iris dataset.1.About DatasetThe Iris flower data set or Fisher's Iris data..."
categories: ["Visualization"]
image: images/0a8409_e495461dc6194769afbe505eb0168ba7.webp
wix-url: https://www.datainsightonline.com/post/basic-data-visualization-using-seaborn
---
In this blog we will apply some basic statistical univariate and bivariate techniques to visualize and gain insights on the iris dataset.

### 1.About Dataset

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper .The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

### 2.Loading the Dataset

We import the necessary libraries and read the data in csv format as follow:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import numpy as np
iris_data = pd.read_csv("iris.csv")
iris_data.head()
```

![](images/0a8409_009057047abe4aa39363f68c92fc3cbd.webp)

```python
print(iris_data.shape)
# Output
(150, 5)
```

### 3.Univariate Analysis

By univariate analysis we simply mean using one among the above four features for further insights.

### 3.1Histogram

It is an approximate representation of the distribution of numerical data. The data is grouped into continuous number ranges and each range corresponds to a vertical bar.

Here we draw the histogram plot using seaborn's distplot function we select specific species and their petal length using the loc function as show in the code snippet below:

```python
sns.distplot( iris_data.loc[iris_data['species'] == 'setosa']['petal_length'] , color="skyblue", label="setosa")
sns.distplot( iris_data.loc[iris_data['species'] == 'versicolor']['petal_length'] , color="orange", label="versicolor")
sns.distplot( iris_data.loc[iris_data['species'] == 'virginica']['petal_length'] , color="green", label="virginica")
plt.legend()
plt.title('Histogram of various types of iris flower based on petal length')
```

![](images/0a8409_0393fa553f8c44d9b6c232119d3dd921.webp)

Similarly we the plot histogram of other features ( petal width ,sepal width sepal length) using distplot function. The plots are as follow

![](images/0a8409_b9d5344061f7481fa35d2a8f12754bdd.webp)

![](images/0a8409_511a3b21b2834cd9ad0d05976fd2c94d.webp)

![](images/0a8409_6d0521b59d97425cb8473972c197aca6.webp)

Here from the above figures we can observe that setosa can be easily separated from other iris flowers using petal length and petal width features. As for virginica and versicolor both show certain overlap across all features.

Due to this we will only be performing further univariate analysis on features petal length and petal width.

### 3.2 Box plot

A boxplot is a standardized way of displaying the dat aset based on a five-number summary: the minimum, the maximum, the sample median, and the first and third quartiles.

Here we use seaborn's built in boxplot function to draw the box plot based on selected features (petal length and petal width) based on their species as follows:

```python
sns.boxplot(x='species',y='petal_length', data=iris_data)
plt.show()
```

![](images/0a8409_57b573304f374c539acf1773527aa0f5.webp)

```python
sns.boxplot(x='species',y='petal_width', data=iris_data)
plt.show()
```

![](images/0a8409_b678919cbc5141bd9e4ff1517268298a.webp)

Here the length of boxes show the petal length and sepal length variation for each type of iris flower.

### 3.3 Violin Plot

A violin plot is a method of plotting numeric data. It is similar to a box plot, with the addition of a rotated kernel density plot on each side.

Here we use seaborn's built in violin plot function to draw the violin plot based on selected features (petal length and petal width) based on their species a follows:

```python
sns.violinplot(x="species", y="petal_length", data=iris_data)
plt.show()
```

![](images/0a8409_ec163408cdcc4b8c9e352fcca87129b8.webp)

```python
sns.violinplot(x="species", y="petal_width", data=iris_data)
plt.show()
```

![](images/0a8409_0d098efe3c8e42c6b5fb8a1ffa8452fd.webp)

Here similar to boxplot ,length of boxes show the petal length and sepal length variation for each type of iris flower while the width represents their distribution.

### 4 Bivariate Analysis:

As the name suggests here we consider two features and their combined impact and insights.

4.1 Scatter plot

In a scatter plot one feature is represented by the standard x-axis while other feature is represented using the standard y-axis.

We plot the scatter plot with sepal length as x-axis and sepal width as y-axis very straightforward using seaborn scatterplot method

![](images/0a8409_aafa01a2254e49a38087404718cb1fa1.webp)

Here we can observe the setosa flower is easily linearly separable while versicolor and virginica have some overlap.

### 4.2 Pair Plot

Rather than drawing scatter plot for each possible attribute combination we can directly use the seaborn's pair plot method. In this method all possible scatter plot combination are included along with diagonal element being the distribution plot for each distinct feature.

The code snippet and output for pair plot are as follow:

![](images/0a8409_24d9df4601174da9a4e0378bd45be51e.webp)

5 Conclusion

Hence we visualized the iris data using various univariate and bivariate technique's using seaborn library. We can conclude that even a simple if else condition based model can provide considerable amount of accuracy. The link to git-hub code is [here](https://github.com/rubash9849/data_inisghts/blob/main/Iris.ipynb)
