---
title: "Linear Interpolation using Python"
author: "snpoudelskt"
date: 2022-01-03
description: "Do you have a series of correlated point data (x,y) and need to fit a linear polynomial with these data and plot the generated result? No worries, a few codes in python can do that for you.We will..."
categories: ["Python"]
image: images/7aaf2c_1466e81b70f047e2b2866d52f042d71f.webp
wix-url: https://www.datainsightonline.com/post/linear-interpolation-using-python
---
Do you have a series of correlated point data (x,y) and need to fit a linear polynomial with these data and plot the generated result?
No worries, a few codes in python can do that for you.

We will first generate few data points (x,y) having exponential relationship. Then we will fit a linear polynomial between set of x and y using *interpld* function of *scipy.interpolate* library and finally plot the interpolated linear polynomial among the original correlated point data.

This job can be easily done with following steps of code:

Import Required libraries.

![](images/7aaf2c_1466e81b70f047e2b2866d52f042d71f.webp)

Generate, (x,y) data which are exponentially related to each other.

![](images/7aaf2c_c74562b92b40414aacb9ee02d9e82599.webp)

Interpolate values between (x,y) and return interpolated values (xnew, ynew) using *interp1d*.

![](images/7aaf2c_cbdd93060aef4197b61e26161e8d99de.webp)

Now, Plot the original values (x,y) with interpolated linear polynomial created by (xnew, ynew).

![](images/7aaf2c_c31ebf4521654d2e91054a2b3260710f.webp)

Yay! The codes are completed. Now, run the project and you'll see this beautiful plot which shows original values of (x,y) represented by red dot and interpolated linear polynomial line between them.

![](images/7aaf2c_f9772c4d6d554c15bf9bb977c1cfa5e8.webp)

PS: Above lines of code are performed in Jupyter notebook. The appearance might differ depending on your IDE.
