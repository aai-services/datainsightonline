---
title: "10 must-know statistical concepts for data science"
author: "Gilbert Temgoua"
date: 2022-03-14
description: "By Gilbert Temgoua IntroductionData is to data scientist what a raw block of marble is to marble sculptors. Along with sculptors, data scientist need appropriate tools and techniques to draw useful..."
categories: ["Statistics"]
image: images/0fd4ab_3f551fb2a3aa404aafe9bcb6056aa9ea.webp
wix-url: https://www.datainsightonline.com/post/10-must-know-statistical-concepts-for-data-science
---
![](images/0fd4ab_3f551fb2a3aa404aafe9bcb6056aa9ea.webp)

By [Gilbert Temgoua](https://linktrest.io/temgoua)

## Introduction
Data is to data scientist what a raw block of marble is to marble sculptors. Along with sculptors, data scientist need appropriate tools and techniques to draw useful insights from data. Statistics is one of the most powerful toolkit every data scientist should have in their arsenal. Without an adequate level of statistics knowledge, it would be extremely hard if not impossible to interpret, understand and explain the data. Furthermore, machine leaning which helps data scientist to infer and predict the behavior of data highly leans on statistics. It is therefore absolutely necessary to learn statistics and most of its concepts for any aspiring data scientist.

In this article I will try to explain and illustrate with python code 10 statistical concepts every data scientist must know. Before diving into the subject, let's import necessary libraries and modules.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sympy.stats import E
import warnings
warnings.filterwarnings('ignore')
np.random.seed(0)
```

### 1. Population and Sample
Generally speaking, a **population** is the set of people living in a given area at a particular time. However in statistics, A **population** is the entire set of from which we draw data for a statistical study. It can be a set of items, individuals, animals, etc.

Contrarily to a population, a **sample** represents the subset of the population on which the study is being carried out. Moreover, a sample is said to be **representative of the population** if all the unique elements of the population are represented in that sample, otherwise the results obtained from the sample will be wrongly extrapolated to the population. For example let's consider a population of 10000 pieces of clothes including the following items **t-shirt, sleeveless, sweat, pull-over, pants, trousers, dress, jacket, nightdress, underwear** from which we randomly draw a sample of size 1000.

```python
items = ['t-shirt', 'sleeveless', 'sweat', 'pull-over', 'pants',
'trousers', 'dress', 'jacket', 'nightdress', 'underwear']
pop = np.random.choice(items, size=10000, replace=True)
samp = np.random.choice(pop, 1000)

labels, pop_counts = np.unique(pop, return_counts=True)
_, samp_counts = np.unique(samp, return_counts=True)
# Plot
fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize=(10,3))
ax1, ax2 = axs[0], axs[1]
fontdict = {'fontsize':17}
ax1.bar(labels, pop_counts, align='center')
ax1.set_xticklabels(labels, rotation=80)
ax1.set_xlabel('Population', fontdict=fontdict)
ax2.bar(labels, samp_counts, align='center')
ax2.set_xticklabels(labels, rotation=80)
ax2.set_xlabel('Sample', fontdict=fontdict)
plt.show()
```

![](images/0fd4ab_921647c057e94e148474f5832519458a.webp)

We notice that all the items of the population are represented in the sample and the distribution of the sample is not that different from that of the population.

**2. Probability distributions**
In probability theory, a **probability distribution** is a mathematical function that gives the probabilities of different possible outcomes for an experiment. In statistics, it is a mathematical description of a random phenomenon in terms of its sample space and the probabilities of events (subsets of the sample space).
In the example of clothes, the probability of each type of clothes is the number of pieces of this given divided by the total number of clothes (the size of the population). Let's calculate and visualize the probability distribution of our population.

```python
probs = pop_counts/np.sum(pop_counts)
plt.bar(labels, probs)
plt.xticks(rotation=75)
plt.show()
```

![](images/0fd4ab_5cd57d2840a0436faa66853a7f6cdc5c.webp)

We get back the bar chart of the distribution of the population at a different scale (0 - 1). We also notice that every type of clothe has almost the same probability: our population follows a **uniform distribution**. Following the type of random variable (continuous or discrete) there exist several probability distributions (with their PDFs shown on the figure below) among which the **normal distribution** or **bell curve** is the most commonly used.

![](images/0fd4ab_052293b897ee4d3494b3c98577a4a10f.webp)

Where 𝜇 and 𝜎 represent the **mean** and **standard deviation** of the population respectively.

The following figure better illustrates the typical bell shape of the probability density function of a normally distributed random variable with 𝑚𝑒𝑎𝑛=0 and 𝑠𝑡𝑑=1.

```python
def norm(x, mean, std):
    f = np.exp(-0.5 * ((x - mean)/std**2)**2) /(std * (np.sqrt(2*np.pi)))
    return f

x = np.linspace(-4, 4, 1000)
y = [norm(i, 0, 1) for i in x]
plt.plot(x,y)
plt.grid()
plt.show()
```

![](images/0fd4ab_1f6b38ac79e54a5491391dee7ed4b1e4.webp)

We notice that the mean is the most likely value of the sample (p = 0.4) and the probability of the other values are symmetrically distributed around the mean. The next figure gives more details about the normal distribution. Here the percentages represent the portion of data that falls in the given interval. We observe that 99.73% of the data falls within 𝜇−3𝜎 and 𝜇+3𝜎.

![](images/0fd4ab_73441162e0da44b393e5e598d329f877.webp)

## 4. Measures of central tendency
Central tendency designates the central value(s) of a probability distribution. The most commonly used central values are mean, median and mode.

- The **mean** is the average value of the sample. It is used only for quantitative values

![](images/0fd4ab_279c16469fc04b4685b6232c0aad36dc.webp)

- The **median** is the value that divides the sample into two equal parts. In other words, it is the values that appears in the middle of the sample when it is sorted either in ascending or descending order.
- The **mode** is the value with the highest frequency of appearance in the sample.

```python
print(f'mean = {np.mean(pop_counts)}')
print(f'median = {np.median(pop_counts)}')
```

```python
mean = 1000.0
median = 997.0
```

## 5. Measures of dispersion
The measures of central tendency are not enough to describe the summary statistics of a dataset. Measures of dispersion tell us all we need to know about the extent of variability of the data. The three commonly used are **Standard deviation, inter-quartile range** and **range**.

- **Range** is the difference between the largest and the smallest observations of the data. The only advantage of this measure is the ease of evaluation. unfortunately, it is highly sensitive to outliers and does not take into account all the observations of the data. It is much more convenient to provide the largest and the smallest values of a dataset instead of the range.
- **inter-quartile range or IQR for short** is the difference between the 25th and the 75th percentiles of the data, also known as the **first** and **third** percentiles, being the 50% middle observations of the data.
- **Standard deviation (std)** is the most commonly used measure of dispersion. It measures the spread of data about the mean. Mathematically, standard deviation is the square root of sum of squared deviation from the mean divided by the number of observations.

![](images/0fd4ab_36b1427cab544a78a8ea8f1f48800471.webp)

This formulae is a faithful translation of the definition of standard deviation. For calculations, the following simpler formulae is adopted.

![](images/0fd4ab_3293bb1ca20a40f091a8e638d15229a3.webp)

*Note : In practice, the denominator* ***n*** *is replaced by* ***n-1*** *for a better accuracy of the estimation of the standard deviation*.

```python
print(f'std = {np.std(pop_counts):.2f}')
print(f'IQR = {stats.iqr(pop_counts)}')
print(f'range = {np.max(pop_counts) - np.min(pop_counts)}')
```

```python
std = 32.39
IQR = 60.75
range = 86
```

## 6. Expected value of a random variable
The **expected value** of a random variable **X**, noted **E[X]** is the weighted sum of all possible values of this variable. The weights here are the probabilities of these passible values. For discrete random variables, the discrete sum is used and for continuous random variables, the integral is used.

##### *Expected value of a discrete random variable X*
The formulae is given by:

![](images/0fd4ab_e0cdf5ae13764246aa88b4f8df8f6cad.webp)

With:

- 𝑥𝑖 the possible value of the random variable X
- 𝑝(𝑥𝑖) the probability that 𝑋=𝑥𝑖.

##### *Expected value of a continuous random variable X*
Here the probability density function (PDF) 𝑓(𝑥)f(x) is used to evaluate the probability of X being equal to x and the formulae is the following:

![](images/0fd4ab_617f3afc12c7429cb016b664084e20a4.webp)

Let's consider the random variable X defined above. X is a clothe, the expected value of X the sum of different kinds of clothes times their probabilities.

```python
print(f'E = {np.sum(pop_counts*probs):.2f}')
```

```python
E = 1001.05
```

## 7. Linear regression
In statistics, **linear regression** is a linear approach for modelling the relationship between a scalar response and one or more explanatory variables (also known as dependent and independent variables). More specifically, Linear regression refers to the case of a single independent variable, the case of multiple independent variables being known as **Multiple linear regression**. Furthermore, for the sake of better clarification, Multiple linear regression differs from **multivariate linear regression** in that the later refers to the prediction of multiple correlated dependent variables.

#### 7.1. Mathematical formulation

![](images/0fd4ab_a575a6b70b974a0cae7b56abeb792ce8.webp)

be the set of n statistical units, a linear regression model assumes that the relationship between the dependent variable 𝑦 and the p-vector of regressors 𝑥 is **linear** and takes the form:

![](images/0fd4ab_07de2fb116d34cfe9f191c5cc52ba851.webp)

𝜀 is the **disturbance term** or **error variable**.

In matrix notation, the above equation takes the following form:

![](images/0fd4ab_a839672c30c04b98b042ceba04a22a3d.webp)

#### 7.2. Example
We will create a randomly distributed dataset 𝑥x for which we will find the best linear model 𝑦y describing 𝑥x, that is find the values of the **slope** 𝛽1 and the **intercept** 𝛽0β0 such that 𝑦=𝛽0+𝛽1𝑥.

```python
x = np.random.randn(100)
y = 1.5*x + np.random.default_rng().random(100)
res = stats.linregress(x, y)
y_hat = res.intercept + res.slope*x
plt.plot(x, y_hat, label='Data', color='red')
plt.scatter(x, y, label='Best fit')
plt.grid()
plt.legend()
plt.show()
```

![](images/0fd4ab_0ebce6c094cb4a04b0b55c78c5a7bb29.webp)

## 8. Over sampling and under sampling
Some datasets are unbalanced that is the amount of data of one category is highly greater than the other. this is sometimes the case in some classification problems. For example we might have to classify emails either as **spam** or **not spam (or safe)** and the training data contains **90%** of **safe emails** and **10%** of **spams**.

Oversampling means we multiply the minority class such that it has the same count as the majority class. Now we have levelled out our dataset and the distribution of minorities without additional data.

Under-sampling means we select only some data from the majority class, as the same number of the minority classes. Now we have a balance on the probability distribution of the classes.

![](images/0fd4ab_00d565c301c44360bec13e6ec4bf447b.webp)

## 9. Probability
**Probability** is the measure of the likelihood of an event to occur in a Random Experiment. Mathematically, for a random experiment with a discrete outcome, the probability of an event is frequency of this event divided by the total number of events in the experiment.

#### Terminology
- Ω represent the universe, that is the set of all possible outcomes of the experiment. 𝑃(Ω)=1

For illustration purposes, we will consider the random experiment **Rolling a dice** and calculate the probabilities of few possible outcomes. Whatever the outcome, it is an integer that falls between 1 and 6, included.

In this case, Ω={1,2,3,4,5,6}.

Consider the following events:

- A : "Roll a 3"
- B : "Roll an even digit"
- C : "Roll a digit les than or equal to 4"
- D : "Roll an odd digit greater than 2"
- E : "Roll 7"

```python
omega = {1,2,3,4,5,6}
A = {3}
B = {2,4,6}
C = {1,2,3,4}
D = {3,5}
E = {}
print(f'P(A) = {len(A)}/{len(omega)}\nP(B) = {len(B)}/{len(omega)}\n\
P(C) = {len(C)}/{len(omega)}\nP(D) = {len(D)}/{len(omega)}\nP(E) = {len(E)/len(omega)}\n')
```

```python
P(A) = 1/6
P(B) = 3/6
P(C) = 4/6
P(D) = 2/6
P(E) = 0.0
```

## 10. Combinations and Permutations
Combinations and permutations are two slightly different ways to select objects from a set to form a subset. Permutations take into consideration the order of the subset, whereas combinations do not.

#### 10.1. Permutations
A permutation of n elements is any arrangement of those n elements in a definite order. There are n factorial (n!) ways to arrange n elements. Note the bold: order matters! The number of permutations of n things taken r-at-a-time is defined as the number of r-tuples that can be taken from n different elements and is equal to the following equation:

![](images/0fd4ab_c3fd9fe21a2b47ecb64167d56b5b460c.webp)

#### 10.2. Combinations
The number of ways to choose r out of n objects where order doesn’t matter. The number of combinations of n things taken r-at-a-time is defined as the number of subsets with r elements of a set with n elements and is equal to the following equation:

![](images/0fd4ab_d30990638c254709a681b5e9696980f2.webp)

#### 10.3. Examples
- a) Permutation : How many ways (noted X) can first, second and third place be awarded to 10 people?
- b) Combination : In how many different ways (noted Y) a team of 3 people can be formed from a group of 10?

```python
X = np.math.factorial(10)/np.math.factorial(10-3)
Y = np.math.factorial(10)/(np.math.factorial(10-3)*np.math.factorial(3))
print(f"X = {int(X)}\nY = {int(Y)}")
```

```python
X = 720
Y = 120
```

## Conclusion
Data Science is a generic field of knowledge that leverages the power of advanced mathematics to draw useful insights from data. The tenants of mathematics for data science are statistics and probability theory. The concepts presented throughout this post are just few of a large set of concepts and tools statistics provide us with, to help data scientists succeed in our data story telling.

You can find the related notebook [here](https://github.com/tem-ctrl/statitistics_for_data_science).
