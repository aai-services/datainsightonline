---
title: "How to perform Regression Analysis in R using lm()"
author: "mathiastamakloe23"
date: 2021-11-29
description: "Let’s start by looking at basic definitions, examples, explanations, Assumptions, types of regression Analysis before taking you through the steps in R.What is regression analysis?Regression analysis..."
categories: ["Machine Learning", "Projects"]
image: images/70d499_6e2362212c0b496e92f7393e5fa4b827.webp
wix-url: https://www.datainsightonline.com/post/how-to-perform-regression-analysis-in-r-using-lm
---
Let’s start by looking at basic definitions, examples, explanations, Assumptions, types of regression Analysis before taking you through the steps in R.

What is regression analysis?

Regression analysis is the linear relationship that exist between independent variables and dependent variables. The independent variables can be referred to as Explanatory variables and the dependent variables as Response variable.

Before we continue, let’s understand a Variable. A Variable is any factor that is liable to change. For example; In most cases, “x” variable is used to denote the explanatory variable while “y” variable is used to denote the response variable as well.

Explanatory variables are factors that one suspect to have an impact on the response/dependent variables and the Response variables are the main factors that we are trying to predict or Understand. For example; Predicting Crop yields based on the amount of rainfall. In this example the dependent/explanatory variable is yield and the independent/response variable is the measure of precipitation.

For the purpose of the topic in discussion, let’s quickly state the basic assumptions of any regression model which include Homogeneity of Variance (Homoscedasticity), Independence of Observations and normality assumption.

There are three different types of regression model namely; simple linear regression, multiple linear regression and polynomial linear regression model.

For the purpose of this blog, we will look at simple linear regression and how to perform it using R.

Simple linear regression is a linear regression model with a single explanatory variable. It can be represented below;

![](images/70d499_6e2362212c0b496e92f7393e5fa4b827.webp)

Now; let’s look at a practical example in R using “leap” data set loaded from library.

The “leap” data set has the following: mpg ~ cylinders + horsepower + weight + acceleration +year+name .

Step 1: load “leap” from library and fit a regression model.using lm() as indicated below

![](images/70d499_998a9994918048a4b1a13c8bb2baf502.webp)

The output becomes;

![](images/70d499_a6f7094a638740f6bfbdd9a61136927d.webp)

![](images/70d499_52d0aa2fe892414f900aae706468746a.webp)

![](images/70d499_14b3384667674a22bdb76379be4e9d7f.webp)

Step 2; we would like to balance the model,fitness and its complexity. Code below

![](images/70d499_b3996472163a49ba91f6653ea177d98e.webp)

And the out becomes;

![](images/70d499_d19b5c1bafca4c1792da07098b1e1ea6.webp)

![](images/70d499_b6b4aa2ee56343e89e814c189401ae59.webp)

![](images/70d499_6050e5fe9238412a9b567090f4bbcb50.webp)

Quite easy right?

The above codes and output should guide you to perform a simple linear regression in R.

Please leave your Comments, Questions and suggestions. Thanks!

Reference: google.com, ISLR 4 pdf
