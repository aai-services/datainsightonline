---
title: "Statistical Concepts for Data Science"
author: "tasnim assali"
date: 2022-02-23
description: "In this blog, I'm going to introduce 10 Statistical Concepts for Data Science. all results of implemented code are here in my notebook link.Statistical concepts and tools are very important to the..."
categories: ["Statistics"]
wix-url: https://www.datainsightonline.com/post/statistical-concepts-for-data-science-3
---
In this blog, I'm going to introduce 10 Statistical Concepts for Data Science. all results of implemented code are here in my notebook link.

[Link](https://github.com/tasnimassali/Statistical-Concepts-for-Data-Science)

Statistical concepts and tools are very important to the data science field. It helps us to interpret the data and understand it in a better way in order to identify the better concept and strategy to extract knowledge from information. From this knowledge, we can make an efficient solution such as prediction.

In this blog, I introduce 10 statistical concepts: Population and sample,

Probability distributions, Normal distribution, Measures of central tendency, Measures of dispersion, Binomial Distribution, Bernoulli Distribution, Bernoulli Distribution, T-test,  Measure of Spread, and Z-Test.

1.Population and Sample

It's the most simple statistical concept for data science, I started with importing the data and then take a 200 sample using .sample()

Also there is other type of sample such as: Systematic Sampling, Stratified Sampling, ..etc.

```python
#Population and Sample
import numpy as np
import pandas as pd
  #read the data
df=pd.read_csv("C:/Users/asus/Desktop/Employee_monthly_salary.csv")
df.head()
  #taking 200 units
df.sample(200)
```

2. **Probability distributions**

this is used in order to visualize uniform distribution with the help of a random number generator acting over an interval of numbers (a,b)

```python
#Probability Distributions
%matplotlib inline
# import matplotlib
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})
# import uniform distribution
from scipy.stats import uniform
# random numbers from uniform distribution
n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc = start, scale=width)
ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')
```

**3.Normal distribution**

Also known as Gaussian distribution i implement it by using the norm.rvs() method as showing in the following code:

```python
#Normal distribution
from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(size=10000,loc=0,scale=1)
ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
```

**4.Measures of central tendency**

in this part, it icludes all the functions Python use to calculate the central tendency for a distribution such as : mean(), mode(), median.. etc. As shown in the code bellow:

```python
#Measures of central tendency
import statistics as st
#mean()
nums=[1,2,3,5,7,9]
st.mean(nums)
st.mean([-2,-4,7]) #Negative numbers
#mode()
nums=[1,2,3,5,7,9,7,2,7,6]
st.mode(nums)
st.mode(['A','B','b','B','A','B'])
#median()
st.median(nums)
```

**5.Measures of dispersion**

This statistical concept give us a simple tools to know how the data strays from the typical value. As shown in the code bellow:

```python
#Measures of dispersion
#variance:  variance of the sample
st.variance(nums)
# pvariance:population variance of data
st.pvariance(nums)
#stdev: standard deviation
st.stdev(nums)
```

**6.Binomial Distribution**

by using binom.rvs() method from scipy.stats module method that takes n as number of trials and p as probability of success as shape parameters.

```python
#Binomial Distribution
from scipy.stats import binom
data_binom = binom.rvs(n=10,p=0.8,size=10000)
ax = sns.distplot(data_binom,
                  kde=False,
                  color='blue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')
```

**7.Bernoulli Distribution**

generating a Bernoulli distribution using bernoulli.rvs() method from scipy.stats module that takes p as probability of success as a shape parameter.

```python
#Bernoulli Distribution
from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000,p=0.6)
ax= sns.distplot(data_bern,
                 kde=False,
                 color="skyblue",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')
```

**8.T-test**

T-test is used to tell us if the data strays or differs significantly from the population. That means it gives us the probability of difference between populations as shown in the code below an example of one sample:

And as a result, I get -2.574 which tells how aberrant the sample mean is from the null hypothesis.

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
np.random.seed(6)
population_ages1=stats.poisson.rvs(loc=18,mu=35,size=150000)
population_ages2=stats.poisson.rvs(loc=18,mu=10,size=100000)
population_ages=np.concatenate((population_ages1,population_ages2))
gujarat_ages1=stats.poisson.rvs(loc=18,mu=30,size=30)
gujarat_ages2=stats.poisson.rvs(loc=18,mu=10,size=20)
gujarat_ages=np.concatenate((gujarat_ages1,gujarat_ages2))
population_ages.mean()
gujarat_ages.mean()
stats.ttest_1samp(a=gujarat_ages,popmean=population_ages.mean())
```

9.**Measure of Spread**

identify **how** alike orchanged **the set of observed values are for a particular variable (data item). It** includes the range, quartiles and interquartile range, variance, and standard deviation.

In the following code I made an example of Range.

```python
Range = X(lagest) - X (lowest)
#Measure_of_Spread
#Range
import numpy as np
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5], [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
A

B=A.T
B

a=np.ptp(B, axis=0)
b=np.ptp(B,axis=1)

print("Range in Array A:",a)
print("Range in Array B:",b)
```

And a second example of Quartile:

```python
#Measure_of_Spread
#Quartile

A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5], [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])

B=A.T

a=np.percentile(B,27,axis=0, interpolation='lower')
b=np.percentile(B,25,axis=1, interpolation='lower')
c=np.percentile(B,75,axis=0, interpolation='lower')
d=np.percentile(B,50,axis=0, interpolation='lower')

print(a)

print(b)

print(c)

print(d)
```

**10. Z.Test**

To identify if two population means are different when the variances are known and the sample size is large.

```python
#Z-test
def twoSampZ(X1, X2, mudiff, sd1, sd2, n1, n2):
    from numpy import sqrt, abs, round
    from scipy.stats import norm
    pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
    z = ((X1 - X2) - mudiff)/pooledSE
    pval = 2*(1 - norm.cdf(abs(z)))
    return round(z, 3), round(pval, 4)

z, p = twoSampZ(28, 33, 0, 14.1, 9.5, 75, 50)
print("Z Score:",z)
print("P-Value:",p
```

Finally, after the introduction of 10 statistical concepts that are very helpful in the data sciences fields each one of them offers an ability that improves our understanding of data, especially in cases of a large volume of data. Also, there are a lot of different other statistical concepts that are useful for the field of data sciences each one of them also offers a necessary method to interpret data into mathematical equations and make it easy to visualize data.
