---
title: "Time Series Analysis of NAICS"
author: "Md Ali Mortaza Sourav"
date: 2022-03-06
description: "IntroductionThe North American industrial classification system is so unique in its industrial classification that it is built into a single conceptual framework. Economic units with similar..."
categories: ["Time Series", "Projects"]
image: images/f206ea_e988585cf6ed4ff3907b9dbd05f72b0b.webp
wix-url: https://www.datainsightonline.com/post/time-series-analysis-of-naics-6
---
**Introduction**

The North American industrial classification system is so unique in its industrial classification that it is built into a single conceptual framework. Economic units with similar manufacturing processes are categorized in the same industry and the lines drawn between the industries distinguish between usable production processes. This supply-based, or production-based, economic concept was adopted for NAICS because an industrial classification system is a framework for collecting and publishing data of inputs and outputs for statistical use that requires inputs and outputs to be used together and classified consistently. Examples of such services include productivity measurement, individual labor costs, and intensity of production capital, estimating employment-output relationships, creating input-output tables, and other uses that indicate production relationship analysis.

**Raw data**

15 CSV files beginning with RTRA. These files contain information on collective employment at different levels of the industry; 2-digit NAICS, 3-digit NAICS, and 4-digit NAICS. Columns mean as follows:

(1) SYEAR: Survey Year

(2) SMTH: Survey Month

(3) NAICS: Industry name and associated NAICS code in the bracket (iv) (4)_EMPLOYMENT_: Employment

Library Import:

![](images/f206ea_e988585cf6ed4ff3907b9dbd05f72b0b.webp)

Read File:

![](images/f206ea_a3ec8d062e134a3cb9c6cb7e1e4febf3.webp)

Clean File:

![](images/f206ea_f7f40d2c11994792b0b581234998b1d2.webp)

Get the data of 2digit NAICS industries:

![](images/f206ea_4193f56e2b6b4692a59baa34a40a9942.webp)

Time series employment in Construction IndustryTime series employment in Construction Industry:

![](images/f206ea_3d8121f6f722467080980ce6ef61e1c8.webp)

Comparing employment in Construction

![](images/f206ea_66a844720ae843d5a8dfbb38eabe866d.webp)

Time Series Employment in Food services and drinking places Sector:

Subsector Contribution:

![](images/f206ea_7660b268ee044e3eba9bc5c1647e5ded.webp)

Contribution of Employment by Food services and drinking places Sector:

![](images/f206ea_2c9a691d2c2d4979813baf37b37c3ea7.webp)

Time series Employment Analysis of Repair, personal and non-profit services Sector:

![](images/f206ea_d3e640851d4440a3b233fc1b01c7671f.webp)

Subsector Contribution towards Employment of Repair, personal and non-profit services:

![](images/f206ea_dbd0a814cdf748cd8926b707ed5f65fb.webp)

**Conclusion**

The top three largest employment contributing sectors contribute about 20 to 25% of the total employment. The construction sector is the largest contributor with over 11% contribution.
