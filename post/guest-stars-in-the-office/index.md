---
title: "Guest Stars in The Office"
author: "Safia Bashir"
date: 2021-10-16
description: "IntroductionThe Office is a television series that depicts the everyday lives of office employees in the fictional Scranton office of Dunder Mifflin Paper Company. There have been nine seasons of the..."
categories: ["General"]
image: images/cda2bf_92d51eb8c9e449bf9dea53f28d83a13d.webp
wix-url: https://www.datainsightonline.com/post/guest-stars-in-the-office
---
![](images/cda2bf_92d51eb8c9e449bf9dea53f28d83a13d.webp)

## Introduction

The Office is a television series that depicts the everyday lives of office employees in the fictional Scranton office of Dunder Mifflin Paper Company. There have been nine seasons of the show, which aired from March 24, 2005, to May 16, 2013. This notebook investigates the popularity and quality of the Office episodes over time by examining the datasets/office_episodes.csv, which was obtained from Kaggle [here](https://www.kaggle.com/nehaprabhavalkar/the-office-dataset).

In this dataset, you can find information about multiple characteristics of each episode. This includes the following:

- **episode_number:** Canonical episode number.
- **season:** Season in which the episode appeared.
- **episode_title:** Title of the episode.
- **description:** Description of the episode.
- **ratings:** Average IMDB rating.
- **votes:** Number of votes.
- **viewership_mil:** Number of US viewers in millions.
- **duration:** Duration in number of minutes.
- **release_date:** Airdate.
- **guest_stars:** Guest stars in the episode (if any).
- **director:** Director of the episode.
- **writers:** Writers of the episode.
- **has_guests:** True/False column for whether the episode contained guest stars.
- **scaled_ratings:** The ratings scaled from 0 (worst-reviewed) to 1 (best-reviewed).

This project aims to:

1 - Create a scatter plot for the purpose of exploring data and uncovering insights

2 - Find out which stars appeared in the most viewed episode

## libraries and data importing
```python
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]
office_df=pd.read_csv('datasets/office_episodes.csv')
office_df.info()
%matplotlib inline
```

```python
# Load your data and print out a few lines.
# Read the CSV File Using Pandas read_csv function
office_df=pd.read_csv('datasets/office_episodes.csv')

# print the concise summery of the dataset
office_df.info()
```

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 188 entries, 0 to 187
Data columns (total 14 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   episode_number  188 non-null    int64
 1   season          188 non-null    int64
 2   episode_title   188 non-null    object
 3   description     188 non-null    object
 4   ratings         188 non-null    float64
 5   votes           188 non-null    int64
 6   viewership_mil  188 non-null    float64
 7   duration        188 non-null    int64
 8   release_date    188 non-null    object
 9   guest_stars     29 non-null     object
 10  director        188 non-null    object
 11  writers         188 non-null    object
 12  has_guests      188 non-null    bool
 13  scaled_ratings  188 non-null    float64
dtypes: bool(1), float64(3), int64(4), object(6)
memory usage: 19.4+ KB
```

from this dataset, we can observe that 29 guests appeared in 188 episodes.

## Data visualization :

## 1-Simple scatter plot :
Here is a simple scatter plot, where episode number is plotted along the x-axis and viewership, is plotted along the y-axis as follows

```python
fig= plt.figure()
plt.scatter(x=office_df['episode_number'],y=office_df['viewership_mil'])
```

![](images/cda2bf_8b2ec2ad7ed24e24be4151ece32f5218.webp)

This scatter plot indicates that the first few episodes of the show did not have the highest viewership, but popularity picked up as the season progressed and declined later in the season.

This scatter plot is difficult to read. Therefore, we should develop a more sophisticated scatter plot.

## 2-Advanced scatter plot :

We are going to add a color scheme to the previous scatter plot such that each point has a color associated with its rating based on the following:

Ratings < 0.25 are colored "red"

Ratings >= 0.25 and < 0.50 are colored "orange"

Ratings >= 0.50 and < 0.75 are colored "lightgreen"

Ratings >= 0.75 are colored "darkgreen"

This can be accomplished by creating an array of colors to customize the plot

```python
# Initiatlize an  empty list

cols=[]
# Iterate through the DataFrame, and assign colors based on the rating
for ind,row in office_df.iterrows():
    if row['scaled_ratings']<0.25:
        cols.append('red')
    elif row['scaled_ratings']<0.50:
        cols.append('orange')
    elif row['scaled_ratings']< 0.75:
        cols.append("lightgreen")
    else:
        cols.append("darkgreen")
```

```python
fig= plt.figure()
plt.scatter(x=office_df['episode_number'], y= office_df['viewership_mil'],c=cols)
```

![](images/cda2bf_ab309ae807e74da085f6ce62ef40ae86.webp)

Now each point in the scatter plot is colored according to the rating of each episode

As a next step, we can add a sizing system such that episodes with guests have a marker size of 250 and episodes without guests have a marker size of 25. we can do this by using the same technique (by creating an array of sizes to customize the plot )

```python
# Initiatlize an empty list
sizes=[]

for ind,row in office_df.iterrows():
    if row['has_guests']==True:
        sizes.append(250)
    else:
        sizes.append(25)
print(sizes.count(250))
```

```python
fig= plt.figure()

plt.scatter(x=office_df['episode_number'], y= office_df['viewership_mil'],c=cols,s=sizes)
print(sizes.count(250))
```

![](images/cda2bf_a334dc0e188042fb80917226c1593d6b.webp)

If we count the number of points that has a marker size of 250 or used (print(sizes.count(250)) ) we can find that 29 guests appeared in 188 episodes. This is in line with our earlier observations about guest appearances.

This scatter plot will be easier to read by providing labels for both axes and adding a title as follows:

```python
fig= plt.figure()
plt.scatter(x=office_df['episode_number'], y= office_df['viewership_mil'],c=cols,s=sizes)
print(sizes.count(250))
# Create a title
plt.title("Popularity, Quality, and Guest Appearances on the Office")
# Create an x-axis label
plt.xlabel("Episode Number")
# Create a y-axis label
plt.ylabel("Viewership (Millions)")
```

![](images/cda2bf_7e67d62cb6f34176a2a66e20bcc4c41f.webp)

Aside from varying the marker size, we can also change the marker type to star to identify guest appearances. This can be achieved by calling two scatter plots, one with guest appearance data and the other with non-guest appearance data, and changing the marker

```python
# Adding our lists as columns to the DataFrame will make plotting much easier

office_df['colors']=cols
office_df['size']=sizes
# Split data into guest and non_guest DataFrames
non_guest_df=office_df[office_df['has_guests']==False]
guest_df=office_df[office_df['has_guests']==True]
```

```python
fig=plt.figure()
# Create two scatter plots with the episode number on the x axis, and the viewership on the y axis

# Create a normal scatter plot for regular episodes
plt.scatter(x=non_guest_df['episode_number'],
            y=non_guest_df['viewership_mil'],
            c=non_guest_df['colors'],
            s=non_guest_df['size'])
# Create a starred scatterplot for guest star episodes
plt.scatter(x=guest_df['episode_number'],
            y=guest_df['viewership_mil'],
            c=guest_df['colors'],
            s=guest_df['size'],
           marker='*')

# Create a title
plt.title("Popularity, Quality, and Guest Appearances on the Office")
# Create an x-axis label
plt.xlabel("Episode Number")
# Create an y-axis label
plt.ylabel("Viewership (Millions)")
```

![](images/cda2bf_a98837a891de433ea15d1f3131c0fca1.webp)

Finally, let's find out which stars appeared in the most viewed episode

```python
# Get the most popular guest star
print(office_df[office_df['viewership_mil'] > 20]['guest_stars'])
```

77 Cloris Leachman, Jack Black, Jessica Alba
Name: guest_stars, dtype: object

A fun fact is that these stars starred in a fake movie the cast watched.

you can find the source code on [GitHub](https://github.com/safia-bashir/Guest-Stars-in-The-Office)

**References:**

1- Datasets for 'The Office' series were downloaded from Kaggle [**here**](https://www.kaggle.com/nehaprabhavalkar/the-office-dataset)**.**

2- DataCamp's Unguided Project: "Investigating Netflix Movies and Guest Stars in The Office" [**here**](https://projects.datacamp.com/projects/1170)**.**
