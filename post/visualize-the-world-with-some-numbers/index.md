---
title: "Visualize the World with some Numbers"
author: "Omar Mohamed"
date: 2021-12-06
description: "Data Visualization using Python Seaborn libraryGithub repo: Github repo for Data Visualization project Introduction:Numbers are everywhere around us, each and every pixel in your computer is a..."
categories: ["Visualization"]
image: images/c4edc8_e89d9f741f4e47b2a25cf9d3918c57ac.webp
wix-url: https://www.datainsightonline.com/post/visualize-the-world-with-some-numbers
---
## Data Visualization using Python Seaborn library

![](images/c4edc8_e89d9f741f4e47b2a25cf9d3918c57ac.webp)

#### Github repo: [Github repo for Data Visualization project](https://github.com/omarmohamed2011/DataVisualization_Seaborn_Python/blob/main/DataVisualization_Seaborn.ipynb)

### Introduction:

Numbers are everywhere around us, each and every pixel in your computer is a number, each info about you and me can be represented using a number, numbers can indicate almost everything and every info either when put in a table, shown in a figure, or visualized in graph.. Here in that graph we try to visualize our dataset using Python Seaborn library, simply taking a ' Restaurant tips and bills ' dataset and gain any sort of insights that can be gotten, let's start the adventure now, Shall we !

You can see full dataset from this repo; [Dataset repo](https://github.com/mwaskom/seaborn-data/blob/master/tips.csv)

### The Tips Dataset Description:

The *Tips* dataset is available in the seaborn data belonging to Michael Waskom - the creator of the Seaborn python data visualisation package. It is one of the example datasets built into the **seaborn** package and is used in the documentation of the seaborn package and can be easily loaded using the seaborn load_dataset command. The tips csv file is also available at the Rdatasets website which is a large collection of datasets originally distributed alongside the statistical software environment R and some of its add-on packages for teaching and statistical software development purposes maintained by [Vincent Arel-Bundock](http://arelbundock.com/).

Let's start coding and visualizing using the data;

Let's import firstly mat plot library and Sea born;

```python
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```

The seaborn library provide us with the dataset so we can load it directly like;

```python
# load dataset of tips given in resteraunts / caffes
df = sns.load_dataset('tips')
```

Here is the data of the tip given and info about the charge and the person receiving the service;

```python
df.head(10)
```

![](images/c4edc8_1b796b35e8dc48f089f3ff7ef3a90109.webp)

Let's plot the total bills distribution and see it;

```python
## Let's plot firstly the total bills:
sns.set_style()
sns.distplot(df['total_bill'], color ='black', bins = 25)
```

![](images/c4edc8_b102dec9147c4b2a8c22623b83e9ccf2.webp)

Seeing the distribution of the total bills in the caffe we can see that most people - so is the average bill - is between 10 and 25 pounds and rarely to see people paying more than 40 pounds or less than 5, which seems almost never.

Let's do plot for the tips given:

```python
sns.set_style()
sns.distplot(df['tip'], color ='black', bins = 25)
```

![](images/c4edc8_e27f1d7841614205b84bd48488081080.webp)

Seeing the distribution of the tips given in the caffe we can see that most people - so is the average tip - is between 2 and 4 pounds and rarely to see people paying more than 8 pounds or giving no tips at all, that also seems like never.

Now, let's check for the distribution of tips for males and females and try to create some insights:

Here we create a sub data frame for sex is male, and another for females and plot the tip for each in order to compare between them

```python
df_male = df[df['sex']=='Male']
df_female = df[df['sex']=='Female']

sns.set_style()
sns.distplot(df_male['tip'], color ='gray', bins = 25) # bins can be 25, 30 or even 40 don't mind it..
sns.distplot(df_female['tip'], color ='red', bins = 25)
```

![](images/c4edc8_57cb00146de34a3a85bac7ee13028338.webp)

Seeing the distribution of the 'Males' vs 'Females' tips given in the Caffe we can see that most people - so is the average tip- knowing that red color represents females and gray color represents males, and we can notice that above average tips are more likely to be given by females than males in this restaurant / Caffe BUT not yet to be confirmed with this graph as the difference is not much big.

Let's then compare between smokers and non smokers in the tips given;

```python
df_smoker = df[df['smoker']=='Yes']
df_nonsmok= df[df['smoker']=='No']

sns.set_style()
sns.distplot(df_smoker['tip'], color ='gray', bins = 25)
sns.distplot(df_nonsmok['tip'], color ='red', bins = 25)
```

![](images/c4edc8_e700e1d8c4e04878a3cb9d6e029a32f1.webp)

Seeing the distribution of the 'Smokers' vs 'Non Smokers' tips given in the Caffe we can see that most people - so is the average tip - knowing that red color represents Non Smokers and gray color represents Smokers, and we can notice that above average tips are more likely to be given by Non Smokers than Smokers in this caffe as their density of above average is more than the latter.

Let's try also to compare the daytime of the arrival of the recipient with their total bills and their tips respectively; daytime here are Dinner and Lunch.

```python
df_dinner= df[df['time']=='Dinner']
df_lunch = df[df['time']=='Lunch']

sns.set_style()
sns.distplot(df_dinner['total_bill'], color ='blue', bins = 25)
sns.distplot(df_lunch['total_bill'], color ='red', bins = 25)
```

![](images/c4edc8_a4c99e08b7034c34b9c5124209649539.webp)

Seeing this distribution we can deduce that the above average total bills are more likely to be bigger in dinner time which is indicated in blue, however the less than average total bills are more likely to be bigger in lunch time which is indicated in red here.

Though, let's try also to compare the time of the arrival of the recipient with their total bills and their tips respectively;

```python
df_dinner= df[df['time']=='Dinner']
df_lunch = df[df['time']=='Lunch']

sns.set_style()
sns.distplot(df_dinner['tip'], color ='blue', bins = 25)
sns.distplot(df_lunch['tip'], color ='red', bins = 25)
```

![](images/c4edc8_b5b9cf6d8b93414f8cc1c29b032aa227.webp)

Seeing this distribution we can not deduce any strong preferences above or under average in tips in different day times.

Getting more insights ,now we should try to plot the total bills vs the tip in the regression plot

```python
sns.set_style('whitegrid')
sns.lmplot(x ='total_bill', y ='tip', data = df)
```

![](images/c4edc8_ddaffd22509947fca93186533454ef0d.webp)

Here it's easy to notice how the two variables are correlated and a high bill will mostly mean a good tip

We should not forget to visualize males and females separately;

```python
sns.set_style('whitegrid')
sns.lmplot(x ='total_bill', y ='tip', data = df,
           hue ='sex', markers =['o', 'v'])
```

![](images/c4edc8_62fe2950e83d4e74b380118893b9787a.webp)

We can add to our insights from this reg-plot that in high total bills - more than 40, males are more likely to give higher tips more than females.

Let's not forget to visualize lunch and dinner time as well;

```python
sns.set_style('whitegrid')
sns.lmplot(x ='total_bill', y ='tip', data = df,
           hue ='time', markers =['o', 'v'])
```

![](images/c4edc8_c0fc79dd752545fa92b8b741bb9564e8.webp)

That assures that in most cases lunch time visitors give more tips than dinner timers.

Now we combine those plots together;

```python
## Combining both things
sns.lmplot(x ='total_bill', y ='tip', data = df, col ='sex',
           row ='time', hue ='smoker', aspect = 0.6,
           size = 4, palette ='coolwarm')
```

![](images/c4edc8_d2e14547f59844119f757bba9f2f5edd.webp)

Let's not forget to visualize smokers and non-smokers separately;

```python
sns.set_style('whitegrid')
sns.lmplot(x ='total_bill', y ='tip', data = df,
           hue ='smoker', markers =['o', 'v'])
```

![](images/c4edc8_bfd97bde17a14d388f0b7d846c16e56a.webp)

That assures that in most cases non-smokers give more tips than smokers.

Now let's finally multi plot for different sizes;

```python
sns.pairplot(df, hue ='size')
plt.show()
```

![](images/c4edc8_9485971b0356471aa2003c93340f41bb.webp)

### Final Thought:

Well that's where the article ends but the visualization doesn't end, you can check the github code link above and see more details and getting to understand more about the data, good luck and happy visualizing, thanks for reading my article and hopeful that it might help you in your way to visualize your data, have a nice day.
