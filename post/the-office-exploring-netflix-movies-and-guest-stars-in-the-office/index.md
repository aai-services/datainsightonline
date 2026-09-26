---
title: "The Office: Exploring Netflix Movies and Guest Stars in The Office"
author: "ekow.a.indome"
date: 2021-10-17
description: "The Office! What started as a British mockumentary series about office culture in 2001 has since spawned ten other variants across the world, including an Israeli version (2010-13), a Hindi version..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/the-office-exploring-netflix-movies-and-guest-stars-in-the-office
---
**The Office!** What started as a British mockumentary series about office culture in 2001 has since spawned ten other variants across the world, including an Israeli version (2010-13), a Hindi version (2019-), and even a French Canadian variant (2006-2007). Of all these iterations (including the original), the American series has been the longest-running, spanning 201 episodes over nine seasons.

In this notebook, we will take a look at a dataset of The Office episodes, and try to understand how the popularity and quality of the series varied over time. To do so, we will use the following dataset: datasets/office_episodes.csv, which was downloaded from Kaggle [here](https://www.kaggle.com/nehaprabhavalkar/the-office-dataset).

This dataset contains information on a variety of characteristics of each episode. In detail, these are:

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

1. **Import pandas**

Before we start, we will need a python library used for working with data sets. Here, we use pandas. Pandas has functions for analyzing, cleaning, exploring, and manipulating data. Thus we import pandas as it alias pd.

Also we will need a low level graph plotting library in python that serves as a visualization utility. Here we will use matplotlib and its subset pyplot. Matplotlib is open source and we can use it freely. We thus import pyplot from matplotlib as plt. We are then good to go

```python
# We have to import pandas and matplotlib.pyplot so we can use the dataframe
import pandas as pd import matplotlib.pyplot as plt
```

**2. Reading the Data**

Our data is in a two-dimensional data structure, that is it is aligned in a tabular fashion in rows and columns. We will have to represent and store our data in a tabular, column oriented data in a persistent storage

Thus we read the dataframe in a csv as follows:

```python
# We then have to read in the csv as a DataFrame
office_df = pd.read_csv('datasets/office_episodes.csv', parse_dates=['release_date'])
```

**3. Create an empty lists:**

We then create empty lists so we can organize our data and place them in.

```python
# Create two empty lists, columns and sizes
cols = []
sizes = []
```

**4. Differentiating between the various ratings**

Now with our dataframe, we are going to organize our data by setting the various ratings into colors red, orange, lightgreen and darkgreen.

This is a **color scheme** reflecting the **scaled ratings** of each episode.

```python
# Then iterate through the DataFrame, assigning colors based on the rating
for ind,row in office_df.iterrows():
    if row['scaled_ratings'] < 0.25:
        cols.append('red')
    elif row['scaled_ratings'] < 0.50:
        cols.append('orange')
    elif row['scaled_ratings'] < 0.75:
        cols.append('lightgreen')
    else:
        cols.append('darkgreen')
```

**5. Further differentiation**

Besides using the color, we want to further bring about a separation by giving them sizes. In our for loop, all rows that have guest we give it a size of 250 while those without, a size of 25

```python
# Then we iterate through the DataFrame, assigning a size based on whether it has guests
for ind, row in office_df.iterrows():
    if row['has_guests'] == False:
        sizes.append(25)
    else:
        sizes.append(250)
```

**6. To plot our findings easily, we add our lists as columns to the DataFrame**

```python
office_df['colors'] = cols
office_df['sizes'] = sizes
```

**7. Splitting the data we have into two sub dataFrames**

Now in the cinema, we have guest and participant. Because of this, we have to split data into guest and non guest DataFrames to find out the exact number of those who were invited and those who paid to watch netflix.

```python
non_guest_df = office_df[office_df['has_guests'] == False]
guest_df = office_df[office_df['has_guests'] == True]
```

**8. Test your matplotlib plot**

To test your matplotlib plot, you will need to initalize a matplotlib.pyplotfig object, which you can do using the code fig = plt.figure() . In addition, in order to test it correctly, we have to **make sure to specify our plot (including the type, data, labels, etc) in the same cell as the one we are initializing our figure** (fig)!

```python
# Then set the figure size and plot style
plt.rcParams['figure.figsize'] = [11, 7]
plt.style.use('fivethirtyeight')

# Create the figure
fig = plt.figure()
```

**9. Creating the scatter plot**

We then create two scatter plots with the episode number on the x axis, and the viewership on the y axis. We create a normal scatter plot for regular episodes, assigning our color list as the colors and set marker and size.

```python
plt.scatter(x=non_guest_df.episode_number, y=non_guest_df.viewership_mil, \
            c=non_guest_df['colors'], s=25)
```

Then create a starred scatterplot for guest star episodes, assigning our color list as the colors and set marker and size

```python
plt.scatter(x=guest_df.episode_number, y=guest_df.viewership_mil, \
            c=guest_df['colors'], marker='*', s=250)
```

**10. Labeling our plot**

We'll, finally we get to label our scatterplot. We give it a title, label its x-axis, its y-axis and show our plot

```python
# We create a title
plt.title("Popularity, Quality, and Guest Appearances on the Office", fontsize=28)

# Create an x-axis label
plt.xlabel("Episode Number", fontsize=18)

# Create a y-axis label
plt.ylabel("Viewership (Millions)", fontsize=18)

# Show the plot
plt.show()
```

**11 Who is the most popular guest star?**

To get the most popular guest star, we have to find the star with the viewership_mil greater than 20

```python
print(office_df[office_df['viewership_mil'] > 20]['guest_stars']) top_star = 'Jessica Alba'
```

And who do we have here, Jessica Alba is the most popular guest star.

Well, this is were we end our investigation, Hope you had fun.
