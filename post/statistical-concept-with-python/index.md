---
title: "Statistical Concept with Python"
author: "Abu Bin Fahd"
date: 2022-02-22
description: "# Import necessary libries import pandas as pd import numpy as np import matplotlib.pyplot as plt from scipy.stats import norm import seaborn as sns01. Population and SampleA population is an entire..."
categories: ["Statistics", "Python"]
wix-url: https://www.datainsightonline.com/post/statistical-concept-with-python
---
```python
# Import necessary libries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
```

## 01. Population and Sample
A population is an entire group that you want to draw conclusions about. A sample is a specific group that you will collect data from. The size of the sample is always less than the total size of the population. In research, a population doesn't always refer to people.

## **02. Normal Distribution** Normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. In graph form, the normal distribution will appear as a bell curve.

### Plotting normal distributions
A certain restaurant chain has been collecting data about customer spending. The data shows that the spending is approximately normally distributed, with a mean of 3.15 dollars and a standard deviation of 1.50 dollars per customer.

```python
# Create the sample using norm.rvs()
sample = norm.rvs(loc=3.15, scale=1.5, size=10000, random_state=13)

# Plot the sample
sns.histplot(sample)
plt.show()
```

## 03. Measures of central tendency
- Mean
- Median
- Mode

**Mean**

The mean, or average, is calculated by adding up the scores and dividing the total by the number of scores. Consider the following number set: 3, 4, 6, 6, 8, 9, 11. The mean is calculated in the following manner:
3 + 4 + 6 + 6 + 8 + 9 + 11 = 47
47 / 7 = 6.7
The mean (average) of the number set is 6.7.

**Median**

The median is the middle score of a distribution. To calculate the median.

- Arrange your numbers in numerical order.
- Count how many numbers you have.
- If you have an odd number, divide by 2 and round up to get the position of the median number.
- If you have an even number, divide by 2. Go to the number in that position and average it with the number in the next - -- higher position to get the median. Consider this set of numbers: 5, 7, 9, 9, 11. Since you have an odd number of scores, the median would be 9. You have five numbers, so you divide 5 by 2 to get 2.5, and round up to 3. The number in the third position is the median.

**Mode**

Since the mode is the most frequently occurring score in a distribution, simply select the most common score as your mode. Consider the following number distribution of 2, 3, 6, 3, 7, 5, 1, 2, 3, 9.
The mode of these numbers would be 3 since three is the most frequently occurring number. In cases where you have a very large number of scores, creating a frequency distribution can be helpful in determining the mode.

```python
import pandas as pd
A = [65,68,70,72,76,76,76,82,85,88]
A = pd.DataFrame(A)
a_mean = A.mean()
a_median = A.median()
a_mode = A.mode()
print(a_mean)
print(a_median)
print(a_mode)
```

## 04. Central Limit Theorem
This sampling distribution more closely resembles the normal distribution. This phenomenon is known as the Central Limit Theorem or CLT, Which states that a sampling distribution will approach a normal distribution as the number of trials increases.

```python
die = pd.Series([1, 2, 3, 4, 5, 6])
# Roll 5 times
samp_5 = die.sample(5, replace=True)
print(samp_5)

# Rolling the dice 5 times 10 times
```

```python
sample_means = []
for i in range(10):
    samp_5 = die.sample(5, replace=True)
    sample_means.append(np.mean(samp_5))
print(sample_means)
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()
```

```python
# 100 sample means
sample_means = []
for i in range(100):
    sample_means.append(np.mean(die.sample(5, replace=True)))
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()
```

```python
# 1000 sample means
sample_means = []
for i in range(1000):
    sample_means.append(np.mean(die.sample(5, replace=True)))

# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()
```

## 05. Bayes' rule
Bayes' theorem, named after 18th-century British mathematician Thomas Bayes, is a mathematical formula for determining conditional probability. Conditional probability is the likelihood of an outcome occurring, based on a previous outcome occurring.

**Factories and parts**
A certain electronic part is manufactured by three different vendors named V1, V2, and V3.
Half of the parts are produced by V1, 25% by V2, and the rest by V3. The probability of a part being damaged given that it was produced by V1 is 1%, while it's 2% for V2 and 3% for V3.
If a part taken at random is damaged, answer the following questions.

```python
# What is the probability that the part was manufactured by V1?
# Individual probabilities & conditional probabilities
P_V1 = 0.5
P_V2 = 0.25
P_V3 = 0.25
P_D_g_V1 = 0.01
P_D_g_V2 = 0.02
P_D_g_V3 = 0.03

# Probability of Damaged
P_Damaged = (P_V1 * P_D_g_V1) + (P_V2 * P_D_g_V2) + (P_V3 * P_D_g_V3)

# Bayes' rule for P(V1|D)
P_V1_g_D = (P_V1 * P_D_g_V1) / P_Damaged

print(P_V1_g_D)
```

```python
# What is the probability that it was manufactured by V2?
# Individual probabilities & conditional probabilities
P_V1 = 0.5
P_V2 = 0.25
P_V3 = 0.25
P_D_g_V1 = 0.01
P_D_g_V2 = 0.02
P_D_g_V3 = 0.03

# Probability of Damaged
P_Damaged = (P_V1 * P_D_g_V1) + (P_V2 * P_D_g_V2) + (P_V3 * P_D_g_V3)

# Bayes' rule for P(V2|D)
P_V2_g_D = (P_V2 * P_D_g_V2) / P_Damaged

print(P_V2_g_D)
```

## 06. Binomial Distribution
**binom.pmf()** calculates the probability of having exactly k heads out of n coin flips.
**binom.cdf()** calculates the probability of having k heads or less out of n coin flips.
**binom.sf()** calculates the probability of having more than k heads out of n coin flips.

Consider a survey about employment that contains the question "Are you employed?" It is known that 65% of respondents will answer "yes." Eight survey responses have been collected.

from scipy.stats import binom

```python
# Calculate the probability of getting exactly 5 yes responses
prob_five_yes = binom.pmf(k=5, n=8, p=0.65)
print(prob_five_yes)

# Calculate the probability of getting 3 or less no responses
prob_three_or_less_no = 1-binom.cdf(k=3, n=8, p=.65)
print(prob_three_or_less_no)

# Calculate the probability of getting more than 3 yes responses
prob_more_than_three_yes = binom.sf(k=3, n=8, p=0.65)
print(prob_more_than_three_yes)
```

## 07. Calculation probabilities of two events
```python
from scipy.stats import binom
from scipy.stats import find_repeats
```

The sample_of_two_coin_flips has 1,000 experiments, each consisting of two fair coin flips. For each experiment, we record the number of heads out of the two coin flips 0, 1, or 2.

```python
sample_of_two_coin_flips = binom.rvs(n=2, p=0.5, size=1000, random_state=1)
```

```python
# We can found how many time each outcome repeats using the function find_repeats

# From the provided samples in sample_of_two_coin_flips, get the probability of having 2 heads out of the 1,000 trials.
# Count how many times you got 2 heads from the sample data
count_2_heads = find_repeats(sample_of_two_coin_flips).counts[2]

# Divide the number of heads by the total number of draws
prob_2_heads = count_2_heads / 1000

# Display the result
print(prob_2_heads)
```

### Joint probabilities
```python
# Calculate the probability that the engine and gear box both work.
# Individual probabilities
P_Eng_works = 0.99
P_GearB_works = 0.995

# Joint probability calculation
P_both_works = P_Eng_works*P_GearB_works

print(P_both_works)
```

```python
# Calculate the probability that one fails -- either engine or gear box -- but not both.
# Individual probabilities
P_Eng_fails = 0.01
P_Eng_works = 0.99
P_GearB_fails = 0.005
P_GearB_works = 0.995

# Joint probability calculation
P_only_GearB_fails = P_GearB_fails * P_Eng_works
P_only_Eng_fails = P_Eng_fails * P_GearB_works

# Calculate result
P_one_fails = P_only_GearB_fails + P_only_Eng_fails

print(P_one_fails)
```

## 08. Conditional Probability
Conditional probability is defined as the likelihood of an event or outcome occurring, based on the occurrence of a previous event or outcome. Conditional probability is calculated by multiplying the probability of the preceding event by the updated probability of the succeeding, or conditional, event.

**A certain airline offers flights departing to New York on Tuesdays and Fridays, but sometimes the flights are delayed:**

```python
# What is the probability of a flight being on time?

# Needed quantities
On_time = 241
Total_departures = 276

# Probability calculation
P_On_time = On_time / Total_departures

print(P_On_time)
```

```python
# Every departure is on time with probability P_On_time. What is the probability of a flight being delayed?

# Needed quantities
P_On_time = 241 / 276

# Probability calculation
P_Delayed = 1 - P_On_time

print(P_Delayed)
```

```python
# Given that it's Tuesday, what is the probability of a flight being delayed (P(Delayed|Tuesday))?

# Needed quantities
Delayed_on_Tuesday = 24
On_Tuesday = 138

# Probability calculation
P_Delayed_g_Tuesday = Delayed_on_Tuesday / On_Tuesday

print(P_Delayed_g_Tuesday)
```

## 09. Total probability law
The total probability law allows you to calculate probabilities under some conditions.
The total probability law state that the probability of an event in a non-overlapping partitioned space is the sum of the probabilities of such an event in each partition.

1. Suppose that two manufacturers, A and B, supply the engines for Formula 1 racing cars, with the following characteristics:

- 99% of the engines from factory A last more than 5,000 km.
- Factory B manufactures engines that last more than 5,000 km with 95% probability.
- 70% of the engines are from manufacturer A, and the rest are produced by manufacturer B.

```python
# What is the chance that an engine will last more than 5,000 km?
# Needed probabilities
P_A = 0.7
P_last5000_g_A = 0.99
P_B = 0.3
P_last5000_g_B = 0.95

# Total probability calculation
P_last_5000 = P_A * P_last5000_g_A + P_B * P_last5000_g_B

print(P_last_5000)
```

## 10. Poisson Distribution
In statistics, a Poisson distribution is a probability distribution that is used to show how many times an event is likely to occur over a specified period. Poisson distributions are often used to understand independent events that occur at a constant rate within a given interval of time.

**Tracking lead responses**
Your company uses sales software to keep track of new sales leads. It organizes them into a queue so that anyone can follow up on one when they have a bit of free time. Since the number of lead responses is a countable outcome over a period of time, this scenario corresponds to a Poisson distribution. On average, Amir responds to 4 leads each day.

```python
# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_5 = poisson.pmf(5, 4)

print(prob_5)
```

```python
# Amir's coworker responds to an average of 5.5 leads per day. What is the probability that she answers 5 leads in a day?
# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_coworker = poisson.pmf(5, 5.5)

print(prob_coworker)
```

```python
# What's the probability that Amir responds to 2 or fewer leads in a day?
# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2, 4)

print(prob_2_or_less)
```

```python
# What's the probability that Amir responds to more than 10 leads in a day?
# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of > 10 responses
prob_over_10 = 1 - poisson.cdf(10, 4)

print(prob_over_10)
```

For more check out my repository: [GitHub](https://github.com/abubinfahd/Data-Insight/blob/main/Assignments/Statistical%20Concept/Statistical%20Concept%20with%20Python.ipynb)
