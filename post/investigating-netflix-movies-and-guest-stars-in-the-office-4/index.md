---
title: "Investigating Netflix Movies and Guest Stars in The Office"
author: "Arpan Sapkota"
date: 2021-10-27
description: "First of all pandas and matplotlib was imported as pd and plt respectivelyimport pandas as pd import matplotlib.pyplot as pltHere office episodes dataset was read as dataframe office_df =..."
categories: ["Projects"]
image: images/a8b2bc_e35724d3ea264a09899263ae76f0d169.webp
wix-url: https://www.datainsightonline.com/post/investigating-netflix-movies-and-guest-stars-in-the-office-4
---
![](images/a8b2bc_e35724d3ea264a09899263ae76f0d169.webp)

First of all pandas and matplotlib was imported as pd and plt respectively

```python
import pandas as pd
import matplotlib.pyplot as plt
```

Here office episodes dataset was read as dataframe

```python
office_df = pd.read_csv('datasets/office_episodes.csv', parse_dates=['release_date'])
```

Based on the ratings colors was appended with the help of for loop as shown below:

```python
for ind, row in office_df.iterrows():
    if row['scaled_ratings'] < 0.25:
        cols.append('red')
    elif row['scaled_ratings'] < 0.50:
        cols.append('orange')
    elif row['scaled_ratings'] < 0.75:
        cols.append('lightgreen')
    else:
        cols.append('darkgreen')
```

If the office dataframe row has guest then size 250 was appened and if it has no guest then size was kept 25 as shown in the loop below:

```python
for ind, row in office_df.iterrows():
    if row['has_guests'] == False:
        sizes.append(25)
    else:
        sizes.append(250)
```

Data were divided according to the having guest and not having guest,

```python
non_guest_df = office_df[office_df['has_guests'] == False]
guest_df = office_df[office_df['has_guests'] == True]
```

Finally, at the end the most popular guest star was printed

```python
print(office_df[office_df['viewership_mil'] > 20]['guest_stars'])
top_star = 'Jessica Alba'
```

Popularity, Quality and Guest Appearances in office were resulted.

Viewership were plotted vertically and viewership were plotted horizontally on a plot. Viewership was displayed in Millions count. Data were falling between 7.5 to 10 Millions. Episode number from 0 to 175 having views not more than 10 Millions.
