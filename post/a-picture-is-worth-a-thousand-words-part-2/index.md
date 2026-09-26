---
title: "“A picture is worth a thousand words” part 2"
author: "Sana Omar"
date: 2022-03-02
description: "Part2: An example for visualization using seaborn hereWe are going to simplify the example from Data visualization in Python using Seaborn - LogRocket Blog by exploring a pre-built in dataset of..."
categories: ["General"]
image: images/82b983_878576ad1aee423ba976d858a9504c32.webp
wix-url: https://www.datainsightonline.com/post/a-picture-is-worth-a-thousand-words-part-2
---
***Part2: An example for visualization using seaborn here***

***We are going to simplify the example from*** [Data visualization in Python using Seaborn - LogRocket Blog](https://blog.logrocket.com/data-visualization-python-seaborn/) by exploring a pre-built in dataset of diamonds using seaborn package:

1. Histogram and KDE

2. Barplt and Countplot

3. Scatter plots

4. Pair plots

```python
diamonds = sns.load_dataset("diamonds")
diamonds.columns
Index(['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y',        'z'],       dtype='object')
diamonds.describe()
```

![](images/82b983_878576ad1aee423ba976d858a9504c32.webp)

## Histograms plots:
```python
sns.histplot(diamonds["carat"])
```

![](images/82b983_2eda132af5e44c389a7d16a7976cb64e.webp)

This is just a histogram to draw the counts of diamonds according to carat variable, Histogram divide into random number of equal-sized bins, here we can say that most diamonds weighs less than 1, we can do the same for other variables:

we can first work on sample from diamonds dataset because it has 53940 set of data -

```python
diamonds.shape : (53940, 10)
sample = diamonds.sample(3000)
sns.histplot(x=diamonds["price"])
```

![](images/82b983_625072c1a7a647ccade13038afc564e3.webp)

### Kernel Density estimate plot:

We use KDE to find the distribution of the probability as an estimation, KDE seems to give smoother figures.

```python
sns.kdeplot(sample["price"])
```

![](images/82b983_b0e199f668e34e40b3fde1627c098b13.webp)

### Count plots:
```python
sns.countplot(sample["cut"])
```

![](images/82b983_16030631e41c406dba802f06b5e15af8.webp)

It seems that most of our cuts are ideal, count plot gives us what the name indicates : the count.

### Scatter plots -Bivariate analysis:

It gives us the relationship between two variables.

```python
sns.scatterplot(x=sample["carat"], y=sample["price"])
```

Each dot is a diamond, it seems heavier diamonds are more expensive.

![](images/82b983_3ddc9bb68c504502b8561d504108f6cc.webp)

### Boxplots -Bivariate analysis:

Theses can gives us side by side characteristic of a variable.

```python
sns.boxplot(x=sample["color"], y=sample["price"])
```

Hereby, we see the distribution of each color, this plot is useful for categorical data, it is basically a percentile divided into minimum, maximum, and outliers which are the black dots.

![](images/82b983_1615e98cce4c475abbb9be40014afa48.webp)

### Bair plots: Multivariable analysis:

```python
sns.pairplot(sample[["price", "carat", "table", "depth"]])
```

![](images/82b983_86ea6988b2924abe9cabbb67bc1bcba8.webp)

In pair plots it creates 4\*4 variations of plots because we have 4 variables. It is useful and concise to make us take a glimpse of what variables that have a clear relationship between each other, we might be able to draw some correlation primarily.

If we want to know exactly the percentage of correlation between them we could use the correlation coefficient, correlation maps which have a range between -1 to 1.

```python
correlation_matrix = diamonds.corr()
correlation_matrix
```

![](images/82b983_3f6fc28ee44a43e79d27dacf924a31be.webp)

```python
correlation_matrix.shape
(7, 7)
```

We can draw a heatmap with annotation of colors and numbers that represents the variation in correlation range.

```python
sns.heatmap(correlation_matrix, square=True, annot=True, linewidths=3)
```

![](images/82b983_0022da70fafd4909bd2fc3cda4a6acbb.webp)

Another trick to make scatterplot a multivariate plot is to use more variables:

```python
sns.scatterplot(sample["carat"], sample["price"], hue=sample["cut"])
```

![](images/82b983_9e4b10b6fa3b419eb6db375eef7fea8d.webp)

More can be explored in details by exploring all variables in details.

Thank you for reading up to this point, if you like it follow me on twitter @sanaomaro.
