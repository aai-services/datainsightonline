---
title: "Time Series"
author: "Rana Wahid"
date: 2022-12-14
description: "Everything that happens is related to time. Any action, any change, anything really, will inevitably take place in an interval of time. Therefore, it is essential that we study events about time to..."
categories: ["Time Series"]
wix-url: https://www.datainsightonline.com/post/time-series
---
Everything that happens is related to time. Any action, any change, anything really, will inevitably take

place in an interval of time. Therefore, it is essential that we study events about time to identify the

patterns in which they occur; learn from the past to improve our future. The purpose of this research is to

apply our knowledge of a mathematical term called Time Series, which its sole existence is about data

that is gathered about time. To make use of Time Series data it has to be analyzed, and here comes the

importance of Time Series Analysis. With the patterns extracted from the Analysis, it’s then used in

forecasting, which is one of the many characteristics of the models of Time Series among many more.

Time Series is composed of four variations which are the trend, seasonal, cyclic, and irregular variations.

Each of their contribution to the understanding of the data. The history of the Time Series shows how

much it was needed as the prediction of weather was of great interest to cultured people like Aristotle,

who had developed ideas about the causes and sequences of the weather. Since then, Time Series and its

Analysis has expanded from just being about the weather to being applied in various applications such

as sales, finance, heart rate measurement, stock prices, and much more. Moreover, it has entered countless

fields and to name a few in the computer science fields there is machine learning, cybersecurity, the

internet of things (IoT), and data mining. In this research, more in-depth details are given about each of

these applications and fields regarding the use of Time Series. As great as Time Series is, there are cases

in which its use is not optimal, and sometimes even downright useless, which is mostly decided with the

Stationary and correlation attributes of the data thus needing to convert it to a suitable format. Graphs

play a vital role in visualizing the output of such Analysis, consequently, it takes various shapes and

forms according to the purpose of using it. Lastly, all this big data Analysis is based on theories. Math

equations that describe the relationships that tie all this together.

**Introduction**

Time Series is the study of data observations due to a period, so it is important for a lot of different

fields like machine learning, network, security, data mining, etc. In which we can predict future data after

understanding and analyzing the previous history data over time. On the other hand, data collected

irregularly or only once are not considered Time Series. An all-statistical Analysis of Time Series data is

collected from a real-life thing we are interested in, the data is conditioned so, it can be used to make

predictions of future values.

The simplest example of a Time Series that all of us come across on a day-to-day basis is the change in

the temperature through the day or week or month or year.

Definition of Time Series:

A Time Series is a set of Numerical Measurements of the same entity taken at equally spaced intervals

over time, Time Series data could be collected yearly, monthly, or daily.

The Reason for choosing Time Series:

Time Series Analysis is special as it helps organizations understand the underlying causes of trends or

systemic patterns over time. Using data visualizations, business users can see season trends and dig

deeper into why these trends occur. Companies can also use Time Series Analysis to predict the

likelihood of future events like upcoming trends in fashion and popular music albums.

The goal of using Time Series Data:

Our aim is to use our previously collected data to predict what will occur in the future, in all fields, such

as weather forecasting, or many machine learning application.

**Time Series Analysis:**

Time Series Analysis is a specific way of analyzing a sequence of data points collected over an interval

of time to identify the common patterns displayed by the data.

In Time Series Analysis, analysts record data points at consistent intervals over a set period rather than

just recording the data points intermittently or randomly.

However, this type of Analysis is not merely the act of collecting data over time.

Time Series Analysis typically requires a large number of data points to ensure consistency and

reliability. An extensive data set ensures you have a representative sample size and that Analysis can cut

through noisy data. It also ensures that any trends or patterns discovered are not outliers and can account

for seasonal variance. Additionally, Time Series data can be used for forecasting-predicting future data

based on historical data, there’s always the potential for correlation between variables in these charts

because data points are collected in adjacent periods.

**Types of Time Series Data:**

- Generally, Time Series data is classified into two types:

1. A Stock Series is a measure of certain attributes at a point in time and can be thought of as

“Stock takes”. For example, the monthly labor force survey is a stock measure because it takes

the stock of whether a person was employed in the reference week.

2. A Flow Series are series that are a measure of activity over a given period. For example, surveys

of retail trade activity. Manufacturing is also a flow measure because a certain amount is

produced each day, and then these amounts are summed to give a total value for production for a

given reporting period.

The main difference between a stock and a flow series is that a flow series can contain effects related to

the calendar (Trading Day Effects). Both types of series can still be seasonally adjusted using the same

seasonal adjustment process.

- In addition to the above classification, Time Series data could also be classified

into three types:

1. Univariate:

A univariate Time Series consists of sequential measurements of a single variable over time.

Consider a Time Series dataset that contains measurements of a person named mike, who has

certain features (variables), such as gender, high, weight, and pulse. If we collect

measurements of one of these variables, say mike’s weight, over time, we have a univariate

Time Series. Using these values of mike’s weight, we can build a model to predict hit the

future weight

2. Multivariate (Bivariate):

A multivariate Time Series is multiple related variables over time. For example, mike’s

height and weight and we know that there is a relationship between the two variables (weight

and height). In that case, we have a bivariate Time Series. And using these values of mike’s

weight and height, we can build a prediction model to determine his future weight or height.

3. Multiple (Pooled Data):

It contains measurements of multiple entities that are independent. Now, let’s build upon the

univariate example, by including measurements about mike’s neighbor’s, and Kate’s weight.

Suppose we know that the measurements of these individuals are independent of each other.

In that case, we can say that the dataset contains multiple univariate Time Series, and

predicting the weight of an individual would depend on his or her previous weight alone.

**Time Series in Computer Science Fields:**

##### 1. Machine learning (ML):

The predictive models based on machine learning found wide implementations in time series

projects required by various businesses for facilitating the predictive distribution of time and

resources.

###### Its methods:

1.1 Recurrent neural network (RNN): RNNs are neural networks with memory that can be

used for predicting time-dependent targets. Recurrent neural networks can memorize the

preciously captured state of the input to decide for the future time step. Recently, lots of

variations have been introduced to adapt recurrent networks to a variety of domains.

1.2 Long short-term memory (LSTM):

special RNN cells were developed to find

the solution to the issue with gradients by

presenting several gates to help the model

decide on what information to mark as

significant and what information to

ignore. GRU is another type of gated

recurrent network.

##### 2. Cyber security and network: computer attacks

interrupt day-to-day services and cause data

losses and network interruption. Time series

analyses are popular machine-learning methods

that help to quantitatively detect anomalies or

outliers in data, by either data fitting or

forecasting. Time series analysis helps thwart

compromises and keep information loss to a

minimum.

The following graph shows the attacks mitigated

on a routed platform.

##### 3. Internet of things (IoT): IOT prediction can

play a key role to enable companies to plan and

operate more efficiently.

IoT-based temperature prediction is already

being used successfully by manufacturers in

collecting weather data via a sensor board to

store and analyze the same data for next-day

predictions.

### Modeling

##### 1. Model Characteristics:

Each model can make any of these characteristics.

1.1 Classifications: identifies and assigns categories to the data.

1.2 Curve fitting: plots the data along a curve to studying the relationships of variables within the

Data.

1.3 Descriptive analysis: identifies patterns in time series data, like trends, cycles, or seasonal

variations.

1.4 Explanative analysis: attempts to understand the data and the relationships within it. As well

as cause and effect.

1.5 Exploratory analysis: highlights the main characteristics of the time series data, usually in a

visual format.

1.6 Forecasting: predicts future data, this type is based on historical trends. use historical data as

a model for future data, predicting scenarios that could happen along future plot points.

Time series forecasting is the process of analyzing time series data using statistics and

modeling to make predictions and inform strategic decision-making. It’s not always an exact

prediction.

Organizations analyze data over consistent intervals. They can also use time series

forecasting to predict the likelihood of future events. Time series forecasting is part of

predictive analysis. It can show likely changes in the data, like seasonality or cyclic

behavior, which provides a better understanding of data variables and helps forecast better.

1.7 Intervention analysis: studies how an event can change the data.

1.8 Segmentation: splits the data into segments to show the underlying properties of the source

information

Note that you should clean your data, we would be able

to identify outliers in the data. perhaps instead of

looking at actual sales, it would make more sense to

plot the percentage difference between observations.

this is a technique that can help smooth out very noisy

data. In this case, by plotting the percentage difference

in sales from month to month we smoothed out much of

the data – except for the enormous spike in March 2017.

This is not necessarily a bad thing. however, without

performing these analytic steps we may have been

unaware that such a spike existed.
