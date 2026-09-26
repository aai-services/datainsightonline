---
title: "Statistical Concepts for Data Science"
author: "Vanessa Arhin"
date: 2022-02-25
description: "What is Statistics?Statistics is the science of collecting, analyzing, interpreting, and manipulating data in order to draw conclusions from the data. In this article, we will talk about a few..."
categories: ["Statistics"]
wix-url: https://www.datainsightonline.com/post/statistical-concepts-for-data-science-6
---
**What is Statistics?**

Statistics is the science of collecting, analyzing, interpreting, and manipulating data in order to draw conclusions from the data. In this article, we will talk about a few statistical concepts that are useful in the data science field.

**1. Population and Sample**

The study of statistics revolves around data. There are two types of
data sets that are being used, that is population and sample.

Population is the total set of observations that can be drawn from data. For example, the population of cats in NYC is the total number of cats in NYC. Population is used in statistical approaches to observe trends and patterns in a data set.

Sample is a subset of a population, containing one or more observations. This implies that more than one sample can be derived from a population. They are cost-effective and much easier to collect as compared to population. Samples are used to make inferences about a population.

**2. Continuous and Discrete Variables.**

Continuous and discrete variables are types of quantitative variables. Continuous variables can be described as a ratio variable while discrete variables can be described as integer variables.

Continuous Variables refer to a variable that assumes an infinite number of different values. They are measurable. Examples of continuous variables are the age of a person, the height of a person, weight of a person.

Discrete Variables refers to a variable whose value is obtained by counting. Therefore, they are countable. Examples of number of children in a family, number of females in a class, number of tins in a basket, etc.

**3. Measures of Central Tendency**

A measure of central tendency is an important aspect of quantitative data. It is an estimate of a value that describes a dataset by identifying the central position. Mean, median and mode are the three main types of central tendency.

Mean (also known as the average) is the sum of all values in a data set divided by the total number of values in a data set. It is the relevant measure of central tendency because it includes information on every single member in a data set. Finding mean in python can be done in different ways.

```python
#method 1
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mean = sum(values) / len(values)
mean
#method 2
import statistics
mean = statistics.mean([1, 2, 3, 4, 5, 6, 7, 8, 9])
mean
#method 2
import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
np.mean(a)
```

Median is the middle value of an ordered or sorted data set. It is very important to make sure that your dataset is arranged in an increasing order. The median gives you an idea of where the central value is located within the data set. In cases where the middle value is two, the sum is taken and divided by two to give you the median.

```python
import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
np.median(a)

import statistics
median = statistics.median([1, 2, 3, 4, 5, 6, 7, 8, 9])
median
```

Mode is the most occurring value(s) in a data set. There can be more than one mode in a data set. Mode is most useful when dealing with categorical data.

```python
import statistics
mode = statistics.multimode([1, 2, 2, 3, 4, 5, 8, 6, 8, 9])
mode
```

**4. Standard Deviation**

Standard Deviation is the measure of how values are spread out in a data set. It shows you how much of your data is around the mean. It is a useful measure for normal distributions. Standard deviation can also be used for comparisons between data sets. Note, standard deviation can be derive from variance by taking the square root.

```python
import statistics
std = statistics.stdev([1, 2, 2, 3, 4, 5, 8, 6, 7, 8, 9])
std
```

**5. Variance**

Variance is the measure of the dispersion of values in a data set from the mean. It is calculated by taking the average of the squared differences from the mean. The variance shows you how each value in a data set is related to another.

```python
import statistics
var = statistics.variance([1, 2, 2, 3, 4, 5, 8, 6, 7, 8, 9])
var
```

**6. Normal Distribution**

Normal Distribution(also known as the Gaussian Distribution) refers to a probability distribution that is symmetrical around the mean. It is the most important and commonly used probability distribution. It has a bell-shaped curve, giving you a clear look at the mean. The normal distribution has two parameters, **mean** and **standard deviation.** The shape of the curve is based on the parameters. It is important to note that the area under the curve of a normal distribution is 1 and the probability can never be 0. Also, the mean, median and mode have the same value. A normal distribution follows the empirical rule, that is, 68% of observations are within one standard deviation, 95% of observations are within two standard deviations and 99.7% of observations are within three standard deviations of the mean value. It is easy to work with, making it very important in the statistical field.

```python
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()
```

**7. Central Limit Theorem (CLT)**

The central limit theorem is one of the most important properties of normal distribution. Central limit theorem in statistics, states that the sample mean distribution of a random variable will assume a normal distribution if the sample size is large enough. The application of this theorem implies that mean of the sample is the same as the mean of the population, the same thing applies to the standard deviation.

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def apply_CLT(sample_data,sample_size,total_samples):
  sample_mean = []
  for a in range(total_samples):
    sample = np.random.choice(sample_data, size = sample_size)
    mean = np.mean(sample)
    sample_mean.append(mean)

  return sample_mean

sample_data = np.random.normal(size=100

sns.distplot( apply_CLT(sample_data,30,1000) )
```

**8. Poisson Distribution**

Poisson Distribution is a probability distribution that is used to measure the probability of certain events happening in a specified period of time. It is used to determine the likely maximum or minimum number of times an event will occur with a given time. Hence, poison distribution can be a great tool to improve efficiency.

```python
from scipy.stats import poisson

poisson.rvs(mu=3, size=10)
array([2, 2, 2, 0, 7, 2, 1, 2, 5, 5])

pmf = poisson.pmf(k=5, mu=3)

cdf = poisson.cdf(k=4, mu=7)

cdf_greater =  1-poisson.cdf(k=20, mu=15)
```

**9. P-Value**

P-value is the probability of obtaining a value that is at least as extreme as what was observed, under the assumption that the null hypothesis is accurate. P-value can be used as an alternative to or in addition to preselected confidence levels for hypothesis testing. It is calculated using the deviations between an observed value and chosen reference value.

```python
from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))

stats.ttest_1samp(rvs,5.0)
```

**10. Skewness**

Skewness is the measure of how much the probability distribution of a random variable deviates from the normal distribution. A graph is said to be **positively skewed** if it has a thicker right tail and mode < median < mean. **Negative skew** is observed when the distribution has a thicker left tail and mode > median > mean.

```python
from scipy.stats import skew
x =[53, 78, 64, 98, 97, 61, 67, 65, 83, 65]

skew(x, bias = False)
```
