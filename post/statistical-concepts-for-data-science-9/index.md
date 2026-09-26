---
title: "Statistical Concepts for Data Science"
author: "Md Ali Mortaza Sourav"
date: 2022-03-06
description: "In data science, statistics is at the heart of sophisticated machine learning algorithms, capturing data patterns and turning them into action. Data scientists use statistics to collect, review..."
categories: ["Statistics"]
wix-url: https://www.datainsightonline.com/post/statistical-concepts-for-data-science-9
---
In data science, statistics is at the heart of sophisticated machine learning algorithms, capturing data patterns and turning them into action. Data scientists use statistics to collect, review, analyze and draw data, as well as apply mathematical models measured in appropriate variables.

Programmers, researchers, business executives, and more use data science. However, what they all have in common is the basis of statistics. Thus, understanding the statistical programming language in data science is just as important.

The following part discusses the basic statistical concept.

**Data**

IIn computing, data is information that is translated into a form that is efficient for movement or processing. Compared to today's computer and transmission media, data is converted to binary digital form. The use of data as a singular subject or plural subject is acceptable. Raw refers to describing data in its most unorganized digital format.

**Population and Sample**

In statistics, the population is the complete set of items from which you draw data for statistical studies. It can be a group of individuals, a set of items, and so on. This creates a data pool for a study. Generally, population refers to people living in a particular area at a particular time. But statistically, population refers to the study data of your interest.

A sample represents the interest group of the population, which you will use to present the data. The sample is a neutral subset of the population that best presents the entire data.

**Mean**

The average of a data set is obtained by adding all the numbers in the data set and then dividing by the number of values ​​in the set. Medium is the middle value when a data set is ordered from minimum to maximum. Mode refers to the number that most frequently occurs in a data set.

```python
import numpy as np
data = [5,7,9,2,7,6,4,6,2,8,9,3,4,4,6,]
mean = np.mean(data)
print(mean)
```

**Measures of central tendency**

The central tendency is a descriptive summary of a dataset through a single value that reflects the center of the data distribution. The variability of a dataset, as well as the central trend, is a branch of descriptive statistics.

The central tendency is one of the most subtle concepts of statistics. Although it does not provide information about the individual values ​​of the dataset, it does provide a comprehensive summary of the entire dataset.

**Median**

The median defines the middle value in the sorted list of values. In order to determine the average value of a sequence of numbers, the numbers must first be sorted or sorted from the lowest to the highest or from the highest to the lowest. The median can be used to determine an approximate average or mean, but do not confuse it with the actual average.

```python
import numpy as np
data = [5,7,9,2,7,6,4,6,2,8,9,3,4,4,6,]
median = np.median(data)
print(median)
```

**Mode**

A mode is defined as a value that has a higher frequency in a given set of values.

```python
import numpy as np
from scipy import stats
data = [5,7,9,2,7,6,4,6,2,8,9,3,4,4,6,]
mode = stats.mode(data)
print(mode[0])
```

**Measures of dispersion**

In [statistics](https://en.wikipedia.org/wiki/Statistics), dispersion is the extent to which a [distribution](https://en.wikipedia.org/wiki/Probability_distribution) is stretched or squeezed. Examples of measures of statistical dispersion are the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation), correlation, [variance](https://en.wikipedia.org/wiki/Variance), covariance, and [interquartile range](https://en.wikipedia.org/wiki/Interquartile_range). When the variance is small, the data in the set is clustered.

**Variance**

The term variance refers to the statistical measure of the spread of numbers in a data set. More precisely, variation measures how far each number in the set is from the average and thus from every other number in the set. Variations are often represented by these symbols: σ2.

```python
import numpy as np
variance = np.var(data)
print(variance)
```

**Probability distributions**

A probability distribution is a statistical function that describes all possible values ​​and probabilities that a random variable can take within a certain range. This range is bound to be between the minimum and maximum possible values, but the exact value of where the potential value will be plotted depends on many factors.

**Normal distribution**

The general distribution, also known as the Gaussian distribution, is a probability distribution that is symmetrical about the mean, which shows that the data near the average occurs more frequently than the data away from the average. In the form of graphs, the normal distribution will appear as a bell curve.

**Covariance and Correlation**

Covariance is a statistical tool used to determine the relationship between the movements of two random variables. When two stocks move together, they are seen as positive companions; When they move in the opposite direction, the covariance is negative.

```python
import numpy as np
covariance = np.cov(data)
print(covariance)
```

Mutual relations, in the finance and investment industries, is a statistic that measures how the two securities are related to each other. Correlation is used in advanced portfolio management, the correlation is calculated as a coefficient, which has a value that must be read between -1.0 and +1.0.

```python
import numpy as np
height =[14,13.7,14.5,15.5,13.3,12,13,14.5]
weight =[60,55,65,75,50,48,52,69]
cor = np.corrcoef(height,weight)
print(cor[0,1])
```
