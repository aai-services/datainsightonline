---
title: "Python Concept: Data Visualization with Matplotlib"
author: "ekow.a.indome"
date: 2021-10-06
description: "Data Visualization is an important part of business activities as organizations nowadays to collect a huge amount of data. Sensors all over the world are collecting climate data, user data through..."
categories: ["Visualization", "Python"]
wix-url: https://www.datainsightonline.com/post/python-concept-data-visualization-with-matplotlib
---
Data Visualization is an important part of business activities as organizations nowadays to collect a huge amount of data. Sensors all over the world are collecting climate data, user data through clicks, car data for prediction of steering wheels etc. All of these data collected hold key insights for businesses and visualizations make these insights easy to interpret.

Why are visualizations important?
Visualizations are the easiest way to analyze and absorb information. Visuals help to easily understand the complex problem. They help in identifying patterns, relationships, and outliers in data. It helps in understanding business problems better and quickly. It helps to build a compelling story based on visuals. Insights gathered from the visuals help in building strategies for businesses.

Data visualizations in python can be done via many packages. We’ll be discussing of matplotlib package. It can be used in Python scripts, Jupyter notebook, and web application servers.

**What is Matplotlib?**

Matplotlib is a low level graph plotting library in python that serves as a visualization utility.Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python

**Installation of Matplotlib**

If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.

Install it using this command:

```python
C:\Users\Your Name>pip install matplotlib
```

If this command fails, then use a python distribution that already has Matplotlib installed, like Anaconda, Spyder etc.

**Import Matplotlib:**

Once Matplotlib is installed, import it in your applications by adding the import module statement:

```python
import matplotlib
```

Now Matplotlib is imported and ready to use:

In Data Science, you likely want to see the Big Picture. Where data is abundant in a geographical area, which data is abundant, etc. In other words, you'll like to visualize this data before you make an assumption or state a fact. Well, python's got us covered with that to. With the help of matplotlib, we can plot graphs to help us analyze data very well. Let's begin!

Within the matplotlib, we are going to focus on the pyplot submodule Now, while using pyplot, we may have to use it over and over and over again. This can be tedious and repetitive and may cause a mistake. Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

```python
import matplotlib.pyplot as plt
```

**1. Now let's draw a line in a diagram from position (0,0) to position (6,250):**

```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```

**Plotting x and y points**

The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

**2. Markers: You can use the keyword argument marker to emphasize each point with a specified marker**

```python
Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()
```

**3. Format Strings fmt:**

**You can use also use the shortcut string notation parameter to specify the marker. This parameter is also called fmt, and is written with this syntax:**

```python
marker|line|color
```

```python
Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()
```

**4. Linestyle: You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line**

```python
Use a dotted line, colored red:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted', color = 'r', linewidth = '5.5')
plt.show()
```

**4. Create Labels for a Plot:**

**With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.**

```python
Add labels to the x- and y-axis:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
#You can add a title to it to
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
```

**5. Display Multiple Plots:**

**With the subplots() function you can draw multiple plots in one figure:**

```python
Draw 2 plots:

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
```

**6. Creating Scatter Plots :With Pyplot, you can use the scatter() function to draw a scatter plot. The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:**

```python
A simple scatter plot:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
```

**7. Creating Bars: With Pyplot, you can use the bar() function to draw bar graphs:**

```python
Draw 4 bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
```

**Create Histogram****: In Matplotlib, we use the hist() function to create histograms.**

**The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.**

**The hist() function will read the array and produce a histogram:**

```python
A simple histogram:
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
```

## Conclusion
In summary, we learned how to build data visualization plots. We can now easily build plots for understanding our data intuitively through visualizations.

Hope you had fun learning about matplotlib and pyplot!!!
