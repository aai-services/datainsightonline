---
title: "Data Analysis Time Series Analysis of NAICS"
author: "Arpan Sapkota"
date: 2022-01-20
description: "Hello there, new analyst, the department has a job opening for you. It's time to put your newfound abilities and experiences to the test.\"What's your job?\" you might wonder. Simply simply, a data..."
categories: ["Time Series", "Projects"]
wix-url: https://www.datainsightonline.com/post/data-analysis-time-series-analysis-of-naics
---
Hello there, new analyst, the department has a job opening for you. It's time to put your newfound abilities and experiences to the test.

"What's your job?" you might wonder. Simply simply, a data analyst collects, cleans, and analyzes data sets in order to assist in issue solving. (Come on, newbie, you have to show that you can keep up.)

So, the department has just gotten the data you'll be working with. The NAICS code is used to label employment data from various industries (North American Industries Classification System). The system's goal is to provide definitions for common industries in Canada, Mexico, and the United States.

The NAICS ID system is structured in a hierarchical manner:

Sector: 2 digits ID

Subsector: 3 digits ID

Industry Group: 4 digits ID

LMO NAICS Detailed Industries: An excel file that maps RTRA data to the necessary data. This file's first column contains a list of 59 commonly used industries. The NAICS definitions are listed in the second column. This file contains the industries we'll be looking at in our analysis.

We're working with 15 CSV files that start with RTRA. From 1997 through 2019, these files provide employment data by industry at various levels of aggregation, which are polled every month. We will, however, end at 2018 due to the assignment requirement.

The goal is to use data from the North American Industry Classification System to complete the task (NAICS).

The North American Industry Classification System (NAICS) was developed by Canada's, Mexico's, and the United States' statistical agencies. NAICS is intended to give similar definitions of the three countries' industrial structure as well as a common statistics framework to ease trade.

The three economies are analyzed.

The data is divided into 15 CSV files, the first of which begins with RTRA. These files offer information on employment by industry at three levels of aggregation: 2-digit NAICS, 3-digit NAICS, and 4-digit NAICS.

The following are the definitions of the columns:

(i) SYEAR: Survey Year

(ii) SMTH: Survey Month

(iii) NAICS: Industry name and associated NAICS code in the bracket

(iv) _EMPLOYMENT_: Employment

There is also an excel file that serves as an NAICS dictionary, which we will use to approve the employment figures.

Job requirements include the following:

1- Fill out the Data Output Template, which is an excel file with an empty employment column. Fill in the blank column with the data you gathered throughout your analysis.

2- Python programs should be used for all stages that generate the necessary data, including merging or appending data.

I began by importing data and inspecting it.

import pandas as pd file1 = pd.read_csv('RTRA_Employ_2NAICS_00_05.csv', parse_dates=([['SYEAR','SMTH']])) file2 = pd.read_csv('RTRA_Employ_2NAICS_06_10.csv', parse_dates=([['SYEAR','SMTH']]))

The remainder of the files are the same. Then group files of the same type together.

two_digit = pd.concat([file1, file2, file3, file4, file5])

Cleaning of data

Take a look at the data to see if there are any missing values:

Extract the NAICS from the industry name:(keep only the number

```python
three_digit['NAICS'] = three_digit.NAICS.str.extract('(\d+)')
```

When we look at the data again, we'll note that there are now missing NAICS, which we'll have to remove.

Extract the following information from the lmo file, which is the NAICS dictionary:

lmo = pd.read_excel('\LMO_Detailed_Industries_by_NAICS.xlsx') lmo['NAICS']= lmo['NAICS'].replace(regex='&', value=',').astype('str') lmo.head()

We now have a dictionary that will translate NAICS to names as they appear in the output file.

We check for NaN values again after merging each dictionary with its kind of file.

It's important to note that we must deal with each level of digits independently. Because this is the highest level, missing data from 2digit, for example, will be dropped instantly. However, for the 3d data, convert the NAICS of the missing names to 2d first, then discard the rest.

Converting a three-digit number to a two-digit number:

```python
full_three_digit.loc[full_three_digit['Name'].isna(), 'NAICS'] = full_three_digit['NAICS'].apply(lambda x: str(x)[:-1])
```

The final step is to find the sum of Employment :

```python
full_three_digit_updated.groupby(['SYEAR_SMTH', 'Name'])['_EMPLOYMENT_'].sum()
```

Now we can visualize the sums per industry.

```python
plt.figure(figsize=(7,17))
```

```python
sns.barplot(x='Employments', y='Industry', data = total_df)
```

That's all there is to it, guys! View the notebook via this Github [link](https://github.com/arpansapkota/Data-Insight---Time-Series-Analysis-of-NAICS) to see more outputs (I try to avoid posting as many outputs as possible to keep the text readable).

I hope you found this essay interesting and that you learned something new from it!
