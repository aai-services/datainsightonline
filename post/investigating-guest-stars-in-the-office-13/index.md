---
title: "Investigating Guest Stars in The Office"
author: "Md Ali Mortaza Sourav"
date: 2022-03-04
description: "DatasetThe name of the dataset is \"The Office Dataset\". This was obtained from the Kaggle website.First import the libraries needed and read the CSV file as we manipulate and analyze the office..."
categories: ["Projects"]
image: images/f206ea_ba46320b920a45ada7569d64a8266f5f.webp
wix-url: https://www.datainsightonline.com/post/investigating-guest-stars-in-the-office-13
---
**Dataset**

The name of the dataset is "The Office Dataset". This was obtained from the Kaggle website.

First import the libraries needed and read the CSV file as we manipulate and analyze the office dataset

![](images/f206ea_ba46320b920a45ada7569d64a8266f5f.webp)

**Output**

![](images/f206ea_f04e47d2a75244a2a3ffa49f9fea3717.webp)

**Data Design**

First, we color each episode based on its rating so we make a list called color, then loop over each episode and check its scaled rating, if it is below 0.25 then we add red to the list, If it is between 0.25 and 0.50, we add orange, if it is between 0.50 and 0.75, we add light green, and finally, dark green for all episodes with a rating above 0.75.

![](images/f206ea_71734b88ca9a4a8a894e7f796f423403.webp)

First few rows of output

![](images/f206ea_92de8ad1e51b452f85e52d0639a0882a.webp)

Then, we calculate the color list as a color parameter in the scatter plot. The output is below.

![](images/f206ea_b779ef666ca042679801e064067bdbe7.webp)

Now we can easily identify the ratings of different episodes. Looking at the graph, there is more work to be done.

Now we will create a scatter plot to visualize the episode:

![](images/f206ea_6a8ec649acf64821b29be8fa90b723c1.webp)

Output

![](images/f206ea_4f48737088db471f8615754c1c4930fe.webp)

In addition to the outlier episode which had a scale of about 9.6 scales and more than 22.5 million views. Most episodes have a rating of 7.5 to 9.0 and 5 to 10 million viewers. It is difficult to say whether any guest presence had a significant impact on quality and popularity.

[Github](https://github.com/AliMourtaza/Investigating-Guest-Stars-in-The-Office/blob/main/Investigating%20Guest%20Stars%20in%20The%20Office.ipynb)
