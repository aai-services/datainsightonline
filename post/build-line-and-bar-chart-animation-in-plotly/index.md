---
title: "Build Line and Bar Chart Animation in Plotly"
author: "Ajibola Salami"
date: 2021-10-13
description: "In this article you will learn how to use Plotly to build beautiful line and bar chart animation with few lines of code. You will also learn the difference between the high-level Plotly Express and..."
categories: ["Visualization"]
image: images/bf66ac_d5ebcb1b264449aca03d02f0878cf4df.webp
wix-url: https://www.datainsightonline.com/post/build-line-and-bar-chart-animation-in-plotly
---
If you use Python for making visualizations, you obviously are open to several open-source options. If you do more interactive visualizations, that should amount to an unnoticeable reduction in the available options. But go a step further into animation and you won’t only be left with fewer options but may also need to be a bit more selective.

Yes, while one of the many Python animation tools out there is likely to serve your purpose, some of them have grown in popularity that they just can't stop badging in on you. And one of such tools is none other than Plotly.

A Python visualization library, it usually come to the fore when there is a mention of building high level production-ready visualizations.

In the last article, we explored the option of [making animation with Matplotlib](https://www.datainsightonline.com/post/a-simple-guide-for-making-aminated-visualizations-in-matplotlib) where we built an animated line plot and bar chart with an intuitive approach. Same idea will be explored here too but with Plotly.

## Data
The data for this article is the same as the one used in the Matplotlib example, a [Kaggle](https://www.kaggle.com/aishu200023/stackindex) data about the count of questions asked monthly about different Data Science, tools, and libraries on StackOverflow, from which a subset of four Python libraries were explored. Below is the first five rows of the data

## Plotly Visualization Modules
Graphing in Plotly is basically done in either Plotly Express or Plotly Graph Objects:

- **Plotly Express**: A high-level interface for making quick plots. Does a lot of heavy-lifting from the backend like automatic chart-type selection, layout configuration, figure labelling, etc so that not much is left for the user to do to make beautiful visualizations.
- **Plotly Graph Objects**: A low-level interface for building plots from scratch that allows for a lot of flexibility and control. Plots graphs using its Figure class through three key attributes namely **data**, **layout**, and **frame.**

## Plotly Line Chart Animation
Just like in the Matplotlib example, we will start by building a static version of the line plot first. However, unlike the Matplotlib case, we will not be building the animation on top of the static plot as [Plotly does not expressly support building line plot animation](https://plotly.com/python/animations/#current-animation-limitations-and-caveats). So the animation will be built separately.

As stated earlier, Plotly Express can help build us quick visualizations with little or or no extra effort. Below is the one-liner that generates a simple static line plot:

As you must have guessed, the animated version of the plot will be made using the Graph Object module as shown in the code below:

And below is the generated animation:

## Code Explanation
1. The Graph Objects Figure as stated earlier has three key properties: **data**, **layout** and **frame**. The data is a list of traces. A trace is simply a container for both the data to be plotted and the specifications of the plot. In our case, the data in the columns numpy, pandas, scipy and scikit-learn and the line chart specified make up our traces.
2. Since the traces are similar, we created a For Loop to append each of them in our empty data attribute from line **3** to line **8**.
3. Then in line **11** to **24** the layout is defined. Layout is where the whole non-data part of our figure is built. Name it, dimension, margin, title, axes labels, font, color, etc. It is a dictionary of key/value properties.
4. Then the frame comes in from **26** to **40**. This is where the traces of the data attribute are made to enter the figure in sequence. Almost similar to the data attribute in structure, except that the data is iterated over per index. Meanwhile, the button that controls the animation is defined in the layout section.
5. Finally the three key properties are entered into the figure to create the animation object between line **43** to **46**.

## Plotly Bar Chart Animation
Plotly Express supports bar charts and so we do not need to go through the granular method of Graph Objects. However, we would need a little bit of manipulation for our data to fit in with the Plotly Express default state before plotting the graph as shown below:

Basically, the index is reset so as to allow for the rearrangement of the data with Pandas DataFrame melt method. Then the month is string-formatted to be used for counting on the animation slider.

With this, you should have an idea of how to build animation in Plotly, in addition to understanding the different modules that can be used achieve your results.

Thank you for reading. And kindly share your thoughts about the article.
