---
title: "Time Series Analysis of NAICS: Evolution of Hospital and Construction Industry Through Employment"
author: "Umme Rubaiyat Chowdhury"
date: 2022-01-20
description: "The North American Industry Classification System (NAICS) is an industry classification system developed by the statistical agencies of Canada, Mexico, and the United States. NAICS is designed to..."
categories: ["Time Series", "Projects"]
image: images/981941_2aaf34979f9a4da2b36f831198837b07.webp
wix-url: https://www.datainsightonline.com/post/time-series-analysis-of-naics-evolution-of-hospital-and-construction-industry-through-employment
---
![](images/981941_2aaf34979f9a4da2b36f831198837b07.webp)

The North American Industry Classification System (NAICS) is an industry classification system developed by the statistical agencies of Canada, Mexico, and the United States. NAICS is designed to provide common definitions of the industrial structure of the three countries and a common statistical framework to facilitate the analysis of the three economies.

Time series analysis is a statistical technique that deals with time-series data, or trend analysis. Time series data means that data is in a series of particular time periods or intervals.

The files from the data set are flat files, Excel (.xlsx), and CSV (.csv) files, we will merge and append data from several files to make a Data Output file. Our first task would be to carry out some data wrangling processes before we can make analysis, ask questions, and gain insights.

**Summary of the data set files we will be using:-**

- 15 RTRA (Real-Time Remote Access) CSV files containing employment data by industry at different levels of aggregation, 2-digit NAICS, 3-digit NAICS, and 4-digit NAICS. *We will search through rows with 2, or 3, or 4 digits NAICS and append employment data each month of each year from 1997 - 2018*

**Meaning of columns in the files:**

- SYEAR: Survey Year

- SMTH: Survey Month

- NAICS: Industry name and associated NAICS code in

the bracket

- _EMPLOYMENT_: Employment

- LMO Detailed Industries by NAICS: An excel file for mapping the RTRA data to the desired data row.

**Columns in the file:**

- Column 1 lists all 59 industries that are used frequently

- Column 2 list the industries NAICS definitions

As part of our data wrangling, we would create a dataset of monthly employment series from 1997 to 2018 for the industries.

One of the guiding principles for our data wrangling is to try to create each series from the highest possible level of aggregation in the raw data files, thus, if an LMO Detailed Industry is defined with a 2-digit NAICS only, we would not use a lower level of aggregation (i.e. 3-digit or 4-digit level NAICS files in the RTRA), similarly, if an LMO Detailed Industry is defined with a 3-digit NAICS only, we would not use the 4-digit NAICS files for that industry.

Let's start knowing in details:

![](images/981941_0155735a466441c8b66825460588e101.webp)

![](images/981941_d9dc09ea4d97414e87530b57503f1273.webp)

![](images/981941_05b3845d5d094be1951597ff5d875b42.webp)

![](images/981941_1baf055028b24cea9d83ca93a73f250e.webp)

![](images/981941_c932106e46434c06945705ded5e3b164.webp)

Here after getting the wrap done, We will begin our data wrangling with the two imported files as DataFrames, reviewing the Data Output template, it has columns for SYEAR, SMTH, LMO_Detailed_Industry, and Employment, but for us append employment data successfully, we would need to give each row a unique identifier to be able to select unique rows from the required CSV files, hence we create a column for the NAICS code as NAICS.

![](images/981941_3d13185d3eef4a2ba808e70fac5346af.webp)

![](images/981941_5a0e5a42ca604c04b05001039c732def.webp)

Here we are getting a read over Employment read.

![](images/981941_05c0b6e3890440378d6d9f710db40fff.webp)

![](images/981941_2487cc4781f14b37805e079188d94347.webp)

![](images/981941_8632c1000ff54138a76013f9cc574440.webp)

![](images/981941_fb8e497222b84b89b9171869614e18e2.webp)

Here mainly comparing stage is done based on the 2-Digit-Data vs 3-Digit-Data and 4-Digit-Data. A total clear picture of what are the differences between the three types of comparison. We extract the NAICS and the SYEAR (Year) from the Data Output file so that we can uniquely identify rows from the Data Output file and any particular RTRA file which is being considered in the loop.

![](images/981941_e2e581ea40204985b7271c06a9d9856a.webp)

![](images/981941_7a7a8684536a484b86cbae3df5f7ee01.webp)

![](images/981941_e8ba96afb6cc44d0b4015a3575658afa.webp)

![](images/981941_a3a8a3c6f4d442b683ff3b09b56759fc.webp)

![](images/981941_c790d87b0d3e49afaddbf27cef36e066.webp)

This cell is our most complex code block with a long computation time based on the repetitive and conditional computation we have to do to be able to get unique employment data for each row from over the 15 RTRA CSV files for each month of each year for each industry. Printing the head() of the Data Output file shows that the Employment has been appended with unique values, their authenticity can be confirmed manually. Gives us clear vision about the LMO_Detailed_industry.

![](images/981941_e89445ba28614703985c3a81b19085fb.webp)

![](images/981941_828074264db243fab003784c02cd61d5.webp)

![](images/981941_520ee62f789040059bb6759d8b2d7696.webp)

![](images/981941_441f42ecf3084682a23917cada200c8e.webp)

![](images/981941_376f303efb8a42adaa71609645bcbf15.webp)

![](images/981941_3870d29ed54246139c81730a2b50092a.webp)

![](images/981941_f9419d03a0f04eee8abda1741a8b3d74.webp)

**We have been able to successfully wrangle and append the employment data unique for every row in the Data Output file. Now we can progress to make some data analysis, ask questions, create visualizations****,** **and gain some insights****,** **and derive some new knowledge from the dataset.**

On the following cell the data section is determining possible outcomes from 1997-2018. Which gives us statistics of the number to drop and the employment numbers left. Which is very efficient in our data science journey to learn about the following subject.

![](images/981941_7c50bf4b31554dfb881e1faf512abf21.webp)

![](images/981941_7b0d9645092b4208874244713336b615.webp)

![](images/981941_63a4c2c8e9d64082a8f2b176b7051cc2.webp)

![](images/981941_00d4e0290fcc49b7979553113b88ed09.webp)

![](images/981941_efde20db98b54648b877b48395213067.webp)

![](images/981941_e6cb6eb5cc664308a1ddcf579a6fe858.webp)

**The construction industry has a significant employment rate, compared to the total employment rate of the other industries, as they experience growth in the number of employees, the construction industry also experiences significant employments as well, and in the case where the total growth rate of the other companies, remain the same, the construction industry experienced a significant increase in employment, see the year 2003 and 2004.**

We can agree that the construction industry is a significant industry among other industries in North America.

![](images/981941_f1b011c9739f46a9b1876f6f19e7a860.webp)

![](images/981941_32ed3f28769f41489ee77739880abb0d.webp)

![](images/981941_7591604af77c42a59b42dab93ac160e2.webp)

Gives us a read about the date time index. Then we are going to compile different types of employment rate in different systems.

![](images/981941_bdefc149b9404b8e8e75cee09ec550c5.webp)

![](images/981941_fa0350c880db4c5290bb8565512c4f09.webp)

![](images/981941_90ff14f07844492fb18ff689f9639731.webp)

![](images/981941_056d01631e084c20a19444e398e47943.webp)

![](images/981941_0ea947fe361e4983afa37988558365b0.webp)

![](images/981941_c688c71d882c472d83eb2d65586486de.webp)

![](images/981941_3636726bc12d44fd87d2c329572db4ca.webp)

![](images/981941_b2ab14f6fecf4157b124bd07986a8945.webp)

![](images/981941_eaa617fb6cc74df3b8b2a377ef876c23.webp)

![](images/981941_70f0fd4b47f24265989838eee80ac633.webp)

How employment in Construction evolved over time and how this compares to the total employment across all industries?

For complete analysis, we have to analyse

- trend - upward, horizontal/stationary, downward
- seasonality - repeating trends
- cyclical - trends with no set repetition

![](images/981941_3e569e0d4a7041eda3036677495b2933.webp)

![](images/981941_298c017b56c749b5999179cc98408740.webp)

## Analysis for construction

![](images/981941_55fcc0d5640541a9b12ad5bce1450ad4.webp)

![](images/981941_89d176aadfa7429eb2a3fa8830327e05.webp)

![](images/981941_3dfcc8d47e9445289fca96e9f70f7daa.webp)

We can see the upward trend and annual seasonality for construction.

### Comparing Total Employment and Construction
As the original data scales do not match and I will be using differencing scales.

![](images/981941_6703ea4bef0048a29b86699958ba5259.webp)

After scaling, compared to total industries, the construction industry evolved abruptly started since 2004. There may be an association between total employment and construction but it is difficult to tell there is association between total employment and construction by looking at the graph and so, I will use Granger Causality test to determine.

### Granger Causality Test
- if one time series is useful in forecasting another
- used to see if there is an indication of causality, but there could always be some outside factor unaccounted for

![](images/981941_fd558ce3af9e445882761504b6a0aa06.webp)

![](images/981941_fb1b65c4a1934e5b887536875df233eb.webp)

![](images/981941_c07403859c954ae8ba7fbcbf3e91ea97.webp)

![](images/981941_906869739b91474ea2bbec9530ecd8d5.webp)

```python
Granger Causality
number of lags (no zero) 12
ssr based F test:         F=2.6760  , p=0.0022  , df_denom=236, df_num=12
ssr based chi2 test:   chi2=35.5135 , p=0.0004  , df=12
likelihood ratio test: chi2=33.2964 , p=0.0009  , df=12
parameter F test:         F=2.6760  , p=0.0022  , df_denom=236, df_num=12
{1: ({'lrtest': (0.17336608572122714, 0.6771374245916899, 1),
   'params_ftest': (0.17150861164675918, 0.6791045424472555, 269.0, 1.0),
   'ssr_chi2test': (0.17342134709297358, 0.6770888775149655, 1),
   'ssr_ftest': (0.1715086116470952, 0.6791045424469386, 269.0, 1)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306697d10>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306588b50>,
   array([[0., 1., 0.]])]),
 2: ({'lrtest': (7.562693436618247, 0.022791976375589294, 2),
   'params_ftest': (3.7638541286150544, 0.02443887507683075, 266.0, 2.0),
   'ssr_chi2test': (7.669206532741953, 0.02160991014780283, 2),
   'ssr_ftest': (3.763854128615055, 0.02443887507683075, 266.0, 2)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f93065a57d0>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f93065a5450>,
   array([[0., 0., 1., 0., 0.],
          [0., 0., 0., 1., 0.]])]),
3: ({'lrtest': (8.163572525411382, 0.04274939180198536, 3),
   'params_ftest': (2.69112005618511, 0.04669907993550864, 263.0, 3.0),
   'ssr_chi2test': (8.288240477223688, 0.04041552509554141, 3),
   'ssr_ftest': (2.691120056184975, 0.04669907993551605, 263.0, 3)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930662e150>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306526d50>,
   array([[0., 0., 0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 1., 0.]])]),
 4: ({'lrtest': (8.381838885848993, 0.0785508883643849, 4),
   'params_ftest': (2.0572359256669586, 0.0868460116782913, 260.0, 4.0),
   'ssr_chi2test': (8.513791753914544, 0.0744702798134845, 4),
   'ssr_ftest': (2.0572359256670834, 0.08684601167827534, 260.0, 4)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f93066564d0>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f93065a5d50>,
   array([[0., 0., 0., 0., 1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 1., 0.]])]),
 5: ({'lrtest': (10.24047807566376, 0.06870119349676021, 5),
   'params_ftest': (2.0020380810382594, 0.0787915087071051, 257.0, 5.0),
   'ssr_chi2test': (10.438642134597494, 0.06371878441543284, 5),
   'ssr_ftest': (2.0020380810384744, 0.07879150870707374, 257.0, 5)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306594590>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f93065941d0>,
   array([[0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]])]),
6: ({'lrtest': (16.44937324836883, 0.011534828134779884, 6),
   'params_ftest': (2.690092900923142, 0.015038909647987594, 254.0, 6.0),
   'ssr_chi2test': (16.966648926293786, 0.009406599121754428, 6),
   'ssr_ftest': (2.6900929009229846, 0.015038909647992866, 254.0, 6)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306530810>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306530290>,
   array([[0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]])]),
 7: ({'lrtest': (25.97134620761517, 0.0005096405970445466, 7),
   'params_ftest': (3.6775833414679298, 0.0008408571495103865, 251.0, 7.0),
   'ssr_chi2test': (27.281514668577717, 0.0002965460328249264, 7),
   'ssr_ftest': (3.6775833414677805, 0.0008408571495107047, 251.0, 7)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306530b50>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f9306530c50>,
   array([[0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]])]),
 8: ({'lrtest': (19.710196159119278, 0.011489882919618534, 8),
   'params_ftest': (2.3936346740439483, 0.01674696195062338, 248.0, 8.0),
   'ssr_chi2test': (20.461715761989492, 0.008723474745102029, 8),
   'ssr_ftest': (2.393634674044054, 0.016746961950618942, 248.0, 8)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930651ffd0>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930651f7d0>,
   array([[0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.,
           0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.,
           0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,
           0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,
           0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
           0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
           0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,
           0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,
           0.]])]),
 9: ({'lrtest': (19.357534382642825, 0.022318769457664086, 9),
   'params_ftest': (2.071042805987614, 0.03272155407924133, 245.0, 9.0),
   'ssr_chi2test': (20.08488860011002, 0.017395692320118946, 9),
   'ssr_ftest': (2.0710428059877755, 0.03272155407922628, 245.0, 9)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653a090>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653a1d0>,
   array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 1., 0.]])]),
 10: ({'lrtest': (22.51179941539158, 0.012699353370307937, 10),
   'params_ftest': (2.162665632246804, 0.02072817440093774, 242.0, 10.0),
   'ssr_chi2test': (23.503349639704933, 0.009033617110407883, 10),
   'ssr_ftest': (2.1626656322466133, 0.02072817440094969, 242.0, 10)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653a850>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653a990>,
   array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,
           0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
           0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
           0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,
           0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,
           0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 1., 0.]])]),
 11: ({'lrtest': (26.51501030850568, 0.005436314755165043, 11),
   'params_ftest': (2.313965337871958, 0.010299604214227997, 239.0, 11.0),
   'ssr_chi2test': (27.903130141199423, 0.0033497808744396068, 11),
   'ssr_ftest': (2.313965337871847, 0.010299604214231968, 239.0, 11)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653d0d0>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653d210>,
   array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
           0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,
           0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,
           0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           1., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 1., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 1., 0.]])]),
 12: ({'lrtest': (33.29640643123594, 0.0008700750914753203, 12),
   'params_ftest': (2.675987483666006, 0.002161697394656369, 236.0, 12.0),
   'ssr_chi2test': (35.513528808653305, 0.00038775264793192984, 12),
   'ssr_ftest': (2.6759874836660855, 0.0021616973946557046, 236.0, 12)},
  [<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653d990>,
   <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f930653dad0>,
   array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,
           0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,
           0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           1., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 1., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 1., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 1., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 1., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 1., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0., 0., 0., 0., 1., 0.]])])}

We can see p-value of less than 0.05 starting from lag 2 and above except 4,5 and so, there is a relationship between total employment and it means if there is an increasing employment in construction, in next 2 months or above, there will be increasing total employment. But keep in mind, there is always some external factors unaccounted for.
```

### Autocorrelation and Partial Autocorrelation plots

![](images/981941_3a77c7b10dd94f588ede3a921a35d799.webp)

![](images/981941_4533c5728fa546d98b5ba042edba4285.webp)

Theoratically, if autocorrelation plot show positive autocorrelation at first lag, then it suggests to use AR terms in relation to the lag. If autocorrelation plot shows negative autocorrelation at first lag, it suggests to use MA terms. But it is difficult to decide whether to use AR, MA, ARIMA or SARIMA by looking at autocorrelation and partical autocorrelation plots as I am a beginner. So, here, I am searching the best model by grid search by using pmdarima library.

### Train-Test-Split

![](images/981941_d0e0888661654c7185cee2c45894c7ec.webp)

![](images/981941_d7d7592cfb7048c0b8e777fb1e2c0ca0.webp)

![](images/981941_3f4c78574f2c4927b6a9b6a23e1bc413.webp)

![](images/981941_ec8fdfebeffa4b0f89bde87034f2c539.webp)

Warnings:

[1] Covariance matrix calculated using the outer product of gradients (complex-step).

[2] Covariance matrix is singular or near-singular, with condition number 9.04e+31. Standard errors may be unstable.

### Model evaluation

![](images/981941_6af3f4ef58c348258b9733e545472dce.webp)

![](images/981941_124636735407487ca0be2bf67fb6b21e.webp)

![](images/981941_5cdfe2bd062c45dab32785e2155f246d.webp)

![](images/981941_376ed8e87891409290e9abeab4125522.webp)

Actually, these steps should be done for time series analysis but there are next 59 variables left to do. So, I will left the analysis steps and will only forecast.

![](images/981941_562b05e39c57417cb62ab3293aae3383.webp)

![](images/981941_d342e662ef62422db3f257e90f13955d.webp)

![](images/981941_add349ae7c9d4db2ab9d9b360b348659.webp)

![](images/981941_6b8c15bdcb064285845e5472e2edbb02.webp)

**Conclusion:** We can clearly draw insights and derive some knowledge about the Construction industry and the Hospitals. We can see that the construction industry is an industry in which the government of the North American countries in the NAICS can consider investing in through ways of education and infrastructure, to make available more jobs, while not neglecting the Hospitals. The construction industry can become a major source of GDP for these countries, considering the employment rate, it shows there are a huge market and demand for construction workers in North America.

**Data Source:**

1. Labour Force Survey (LFS) by the Statistics of Canada.
