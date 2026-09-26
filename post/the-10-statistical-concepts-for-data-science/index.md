---
title: "The 10 Statistical Concepts for Data Science"
author: "Amr Mohamed Salama"
date: 2022-06-03
description: "IntroductionContent:1. Types of Analytics2. Population and sample3. Central Tendency4. Measure of dispersion(Variability)5. Relationship Between Variables6. Data Reshaping & Transformation 7..."
categories: ["Statistics"]
image: images/83ada7_32303e977e4d44b4a120d884dc2be64f.webp
wix-url: https://www.datainsightonline.com/post/the-10-statistical-concepts-for-data-science
---
Introduction

Content:

*1. Types of Analytics*

*2. Population and sample*

*3. Central Tendency*

*4. Measure of dispersion(Variability)*

*5. Relationship Between Variables*

*6. Data Reshaping & Transformation*

*7. Probability*

*8. Probability Distribution*

*9. Hypothesis Testing and Statistical Significance*

*10. Regression*

**Statistics** is the branch of mathematics that concerns the collection, organization, analysis, interpretation, and presentation of data.

in this article, we are going to discuss some of the most common concepts.

## 1. Types of Analytics
![](images/83ada7_64d1a1f9db7147b6b4c6053b11056848.webp)

### 1.1. Descriptive Analytics

Descriptive analytics is the first step in data analysis. The goal of
 descriptive analytics is to find out *what happened*?

### 1.2. Diagnostic Analytics

With diagnostic analytics, we can go one step deeper and ask the
 question: *Why did this happen?*

### 1.3. Predictive Analytics

Predictive analytics tries to answer the question:

*What is likely* to happen*?* By using what we learned with descriptive
 and diagnostic analytics

### 1.4.Prescriptive Analytics

Now that you have an idea of what is likely to happen, you might
 want to know what the best course of action is. Prescriptive analytics
 tries to answer the question:

*What should be done?* or *what can we do to make ... happen?*

## 2. Population and Sample
![](images/83ada7_025d15af9eab465da5215ec55340d6f4.webp)

### 2.1. Population

is the complete collection of all individuals (scores, people,

measurements, and so on) to be studied. The collection is complete
 in the sense that it includes all of the individuals to be studied.

### 2.2. Sample

is a subcollection of members selected from a population.

![](images/83ada7_12eb9796169c40e3903446eedfb4e220.webp)

### 2.3. Sampling techniques

#### 2.3.1. Probability Sampling

§ Simple Random Sampling

§ Stratified Sampling

§ Cluster Sampling

§ Systematic Cluster Sampling

#### 2.3.2. Non-Probability Sampling

§ Convenience Sampling

§ Purposive Sampling

§ Quota Sampling

§ Snowball/referral sampling

## 3. Measure of Central Tendency
· **Mean**: The average value of the dataset.

· **Median**: The middle value of an ordered dataset.

· **Mode**: The most frequent value in the dataset. If the data have
 multiple values that occurred the most frequently, we have a
 multimodal distribution.

· **Skewness**: A measure of symmetry.

· **Kurtosis**: A measure of whether the data are heavy-tailed or light-
 tailed relative to a normal distribution

![](images/83ada7_d00cc6f77eb046e1874485aa0af72669.webp)

![](images/83ada7_3600a764c08e4949ae0ad66cac346676.webp)

```python
# Filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for Egypt
Eg_consumption = food_consumption[food_consumption['country'] == 'Egypt']
print(Eg_consumption)

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean and median consumption in Belgium
print("The average consumption for Belgium is : {}".format(np.mean(be_consumption.consumption)))
print("The most common consumption for Belguim is : {}".format(np.median(be_consumption.consumption)))

# Calculate mean and median consumption in USA
print("The average consumption for USA is {}:  ".format(np.mean(usa_consumption.consumption)))
print("The most common consumption for USA is : {}".format(np.median(usa_consumption.consumption)))
```

output

```python
The average consumption for Belgium is : 42.132727272727266 The most common consumption for Belguim is : 12.59 The average consumption for USA is 44.650000000000006:   The most common consumption for USA is : 14.58
```

## 4. Measure of dispersion (Variability)
- **Range**: The difference between the highest and lowest value in the
   dataset.
- **Percentiles, Quartiles and Interquartile Range (IQR)**

Ø **Percentiles** — A measure that indicates the value below which
 a given percentage of observations in a group of observations
 falls.

Ø **Quantiles** — Values that divide the number of data points into

four more or less equal parts, or quarters.

Ø **Interquartile Range(IQR)** — A measure of statistical dispersion
 and variability based on dividing a data set into quartiles.

IQR = Q3−Q1

![](images/83ada7_bd674dabce2f400281066178136277a1.webp)

- **Variance**: The average squared difference of the values from the mean to measure how spread out a set of data is relative to the mean.
- **Standard Deviation**: The standard difference between each data point and the mean and the square root of variance.
- **Standard Error(SE**): An estimate of the standard deviation of the sampling distribution.

```python
# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption.co2_emission, [0, 0.25, 0.5, 0.75, 1]))
```

output

```python
[   0.        5.21     16.53     62.5975 1712.    ]
```

```python
# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Create histogram of co2_emission for food_category 'beef'
plt.hist(food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].mean())
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
plt.hist(food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].mean())
plt.show()
```

output

![](images/83ada7_1c0edf7d386e435fa6924d573f8149ad.webp)

![](images/83ada7_f5a17434840b454e982b003b80283a14.webp)

## 5. Relationship Between Variables
- **Causality**: Relationship between two events where one event is affected by the other.
- **Covariance**: A quantitative measure of the joint variability between two or more variables.
- **Correlation**: Measure the relationship between two variables and ranges from *-1 to 1*, the normalized version of covariance.

![](images/83ada7_63f3dbaa5d8b4587adcd3859fea3bffa.webp)

![](images/83ada7_1ca031cede36436b8e28ee0df69dc21f.webp)

```python
# Scatterplot of food consumption and co2 emission for USA
sns.scatterplot(x='consumption', y='co2_emission', data=usa_consumption)

# Show plot
plt.show()

# Correlation between food consumption and co2 emission for USA
cor = usa_consumption.consumption.corr(usa_consumption.co2_emission)

print(cor)
```

output

![](images/83ada7_7ce36d37f1274b7fbc76830ca5ea8704.webp)

## 6. Probability
**Probability** is the branch of mathematics concerning numerical descriptions of how likely an event is to occur.

- **Complement**: P(A)+P(A’) =1
- **Intersection**: P(A∩B)=P(A)P(B)
- **Union**: P(A∪B)=P(A)+P(B)−P(A∩B)

![](images/83ada7_d5d9f90bf10a4778999cea55ce298a67.webp)

- **Conditional Probability**: P(A|B) is a measure of the probability of one event occurring with some relationship to one or more other events. P(A|B)=P(A∩B)/P(B), when P(B)>0.
- **Independent Events**: Two events are independent if the occurrence of one does not affect the probability of occurrence of the other. P(A∩B)=P(A)P(B) where P(A) != 0 and P(B) != 0 , P(A|B)=P(A), P(B|A)=P(B)
- **Mutually Exclusive Events**: Two events are mutually exclusive if they cannot both occur at the same time. P(A∩B)=0 and P(A∪B)=P(A)+P(B).
- **Bayes’ Theorem** describes the probability of an event based on prior knowledge of conditions that might be related to the event.

![](images/83ada7_34bba0e8f3d647e2ac4ae2dc1fda7d86.webp)

## 7. Probability Distribution
### 7.1. Probability Distribution Functions

- **Probability Mass Function(PMF)**: A function that gives the probability that a *discrete random variable* is exactly equal to some value.
- **Probability Density Function(PDF)**: A function for *continuous data* where the value at any given sample can be interpreted as providing a relative likelihood that the value of the random variable would equal that sample.
- **Cumulative Density Function(CDF)**: A function that gives the probability that a random variable is less than or equal to a certain value.

![](images/83ada7_98e9c1213f91410799a8d59d31b0a6ba.webp)

### 7.2. Continuous Probability Distribution

### *Types of continuous distribution*

- **Uniform Distribution**: Also called a rectangular distribution, is a probability distribution where all outcomes are equally likely.
- **Normal/Gaussian Distribution**: The curve of the distribution is bell-shaped and symmetrical and is related to the **Central Limit Theorem** that the sampling distribution of the sample means approaches a normal distribution as the sample size gets larger.

![](images/83ada7_378e55543f55418495833ea83c36c045.webp)

- **Exponential Distribution**: A probability distribution of the time between the events in a *Poisson* point process.
- **Chi-Square Distribution**: The distribution of the sum of squared standard normal deviates.

![](images/83ada7_db00bfaad48c41339936af064becc6de.webp)

```python
# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'])
plt.show()
```

output

![](images/83ada7_ac138efaee0c4ab3affae80ca0d9faa0.webp)

### 7.3. **Discrete** Probability Distribution

### *Types of d****iscrete*** *distribution*

- **Bernoulli Distribution**: The distribution of a random variable that takes a single trial and only 2 possible outcomes, namely 1(success) with probability p, and 0(failure) with probability (1-p).
- **Binomial Distribution**: The distribution of the number of successes in a sequence of *n* independent experiments, each with only 2 possible outcomes, namely 1(success) with probability p, and 0(failure) with probability (1-p).
- **Poisson Distribution**: The distribution that expresses the probability of a given number of events k occurring in a fixed interval of time if these events occur with a known constant average rate λ and independently of the time.

![](images/83ada7_6c15ea2ef80f41659d0b1079fdec8f29.webp)

## 8. Data Reshaping & Transformation

**Data Transformation**

is the application of a deterministic mathematical
 function to each point in a data set—that is, each data
 point zi is replaced with the transformed value yi = f(zi),
 where f is a function. Transforms are usually applied so
 that the data appear to more closely meet the
 assumptions of a statistical inference procedure that is to
 be applied or to improve the interpretability or
 the appearance of graphs.

TYPES OF TRANSFORMATION

8.1. Logarithmic Transformation

8.2. Cube Root Transformation

8.3. Square Root Transformation

8.4. Square Transformation

![](images/83ada7_5be39875b6de4a1ea9bf19601cb84a4f.webp)

## 9. Hypothesis Testing and Statistical Significance
***Null and Alternative Hypothesis***

**Null Hypothesis**:

A general statement that there is no relationship
 between two measured phenomena or no association among groups.

**Alternative Hypothesis**:

Be contrary to the null hypothesis.

In statistical hypothesis testing, a

- **type I error** is the rejection of a true null hypothesis, while a
- **type II error** is the non-rejection of a false null hypothesis.

![](images/83ada7_ce2b2a09193a46f2b321631257bd5d7b.webp)

**Interpretation**

**P-value**:

The probability of the test statistic is at least as extreme as the one
 observed given that the null hypothesis is true. When p-value > α, we

fail to reject the null hypothesis, while p-value ≤ α, we reject the null
 hypothesis and we can conclude that we have a significant result.

**Critical Value**:

A point on the scale of the test statistic beyond which we reject the null
 hypothesis, and, is derived from the level of significance α of the test.
 It depends upon a test statistic, which is specific to the type of test,
 and the significance level, α, which defines the sensitivity of the test.

**Significance Level and Rejection Region**: The rejection region is
 actually depended on the significance level. The significance level is
 denoted by *α* and is the probability of rejecting the null hypothesis if it
 is true.

**Z-Test**

A *Z*-test is any statistical test for which the distribution of the test
 statistic under the null hypothesis can be approximated by a normal
 distribution and tests the mean of a distribution in which we already
 know the population variance. Therefore, many statistical tests can be
 conveniently performed as approximate *Z*-tests if the *sample size is*

*large* or the *population variance is known*.

![](images/83ada7_d72b1a76c5fd49d4ae4d161ed9ed89a0.webp)

**T-Test**

A T-test is a statistical test if the *population variance is unknown* and
 the *sample size is not large* (n < 30).

**Paired sample** means that we collect data twice from the same group,
 person, item, or thing.

**An Independent sample**

implies that the two samples must have come from two completely
 different populations.

**ANOVA(Analysis of Variance)**

ANOVA is the way to find out if experiment results are significant.

**One-way ANOVA**

compares two means from two independent groups using only one
 independent variable.

**Two-way ANOVA**

is the extension of one-way ANOVA using two independent variables
 to calculate the main effect and interaction effect.

**Chi-Square Test**

- **Chi-Square** Test checks whether or not a model follows approximately normality when we have s discrete set of data points.
- **Goodness of Fit Test** determines if a sample matches the population fit of one categorical variable to a distribution.
- **Chi-Square Test for Independence** compares two sets of data to see if there is a relationship.

![](images/83ada7_7b056214ddf34378aaf1657ae1546dac.webp)

## 10. Regression
**Linear Regression**

is a linear approach to modeling the relationship between a ***dependent variable*** (the variable being measured in a scientific experiment ) and one ***independent variable***(the variable that is controlled in a scientific experiment to test the effects on the dependent variable).

![](images/83ada7_dc9c668cc24c469ba66bb4666ca9a7a6.webp)

**Multiple Linear Regression**

is a linear approach to modeling the relationship between a dependent variable and two or more independent variables.

![](images/83ada7_d61c9cc74eee4cf3b88672185784ce0c.webp)

**Steps for Running the Linear Regression**

1. Define the problem

2. Build the dataset

3. Train the model

4. Evaluate the model

5. Use the model
