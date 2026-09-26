---
title: "--- North American Industry Classification System (NAICS)"
author: "Sakayo Toadoum Sari"
date: 2022-01-28
description: "The North American Industry Classification System (NAICS) is an industry classification system developed by the statistical agencies of Canada, Mexico and the United States. NAICS is designed to..."
categories: ["Machine Learning", "Time Series"]
wix-url: https://www.datainsightonline.com/post/north-american-industry-classification-system-naics
---
The North American Industry Classification System (NAICS) is an industry classification system developed by the statistical agencies of Canada, Mexico and the United States. NAICS is designed to provide common definitions of the industrial structure of the three countries and a common statistical framework to facilitate the analysis of the three economies. The NAICS structure is hierarchical with a six-digit code numbering system adopted, of which the first five digits are used to describe the NAICS levels that will be used by the three countries (i.e. Canada, Mexico and the United States) to produce comparable data. The first two digits designate the sector, the third digit designates the subsector, the fourth digit designates the industry group and the fifth digit designates the industry. The sixth digit is used to designate national industries. A zero as the sixth digit indicates that there is no further national detail.

#### Description of the File used for the analysis

As said earlier, the hierarchical structure of the NAICS defines industries at different levels of aggregation with highest aggregate been a 2-digit NAICS industry (e.g., 23 — Construction) which is then composed of some 3-digit NAICS industries (236 — Construction of buildings, 237 — Heavy and civil engineering construction, and a few more 3-digit NAICS industries). Similarly, a 3-digit NAICS industry (e.g., 236 — Construction of buildings), is composed of 4-digit NAICS industries (2361 — Residential building construction and 2362 — Non-residential building construction). The above example is top-down approach while down-top approach will be the smaller industries with 4-digit NAICS making up a 3-digit NAICS industry which in turn make a 2-digit NAICS industry.

For more information can be found at <https://www.statcan.gc.ca/eng/subjects/standard/naics/2017/index> on the files and datasets used in the analysis.

#### Description of the Datasets Used

The file containing the datasets used in this time series analysis is obtained from [https://wixlabs-file-sharing.appspot.com.](https://wixlabs-file-sharing.appspot.com) The zipped files consist of 15 CSV files beginning with Real Time Remote Access (RTRA). These files contain employment data by industry at different level of aggregation; 2-digit NAICS, 3-digit NAICS, and 4-digit NAICS. The source of the data is from Real Time Remote Access (RTRA) data from the Labour Force Survey (LFS) by Statistics Canada. Below is the description of the column names as used in each dataset (CSV file):

1. SYEAR: Survey Year
2. SMTH: Survey Month
3. NAICS: Industry name and associated NAICS code in the bracket
4. *EMPLOYMENT*: Number of Employment offered in the industry aggregate

Each level of aggregation (i.e.2-digit NAICS, 3-digit NAICS, and 4-digit NAICS) has survey data from 1997 to 2020 segregated into 1997–1999, 2000–2005, 2006–2010, 2011–2015 and 2016–2020 with 2020 data yet not available during the time of this analysis.

#### IMPORT DATASET

As mentioned earlier, as the data are survey data, they are separated into several year bands for each level of aggregation. Therefore, the data from each level of aggregation are imported and concatenated into a single data frame for exploratory data analysis (EDA).

```python
#import the necessary packages
#import pandas for data manipulation and wrangling using its DataFrame
import pandas as pd
#import numpy for mathematical data modeling
import numpy as np
#import glob for filename pattern matching
from glob import glob
#import matplotlib for data visualization
import matplotlib.pyplot as plt
#import seaborn for data visualization
import seaborn as sns
%matplotlib inline

#Set the style of the Seaborn Diagrams
sns.set(style="darkgrid")

#Enarge the size of graphs in the Notebook
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size
```

```python
# Save all the files into their respective variable
# Save all files with 2 NAICS code to a varaible
filename_2NAICS = glob("RTRA_Employ_2NAICS_*.csv")
# Read 2 NAICS code files into varaible
list_2NAICS = [pd.read_csv(file,dtype={"SYEAR":str,"SMTH":str}) for file in filename_2NAICS]

# Save all files with 3 NAICS code to a varaible
filename_3NAICS = glob("RTRA_Employ_3NAICS_*.csv")
# Read 3 NAICS code files into varaible
list_3NAICS = [pd.read_csv(file,dtype={"SYEAR":str,"SMTH":str}) for file in filename_3NAICS]

# Save all files with 4 NAICS code to a varaible
filename_4NAICS = glob("RTRA_Employ_4NAICS_*.csv")
# Read 4 NAICS code files into varaible
list_4NAICS = [pd.read_csv(file,dtype={"SYEAR":str,"SMTH":str}) for file in filename_4NAICS]
```

First, each aggregate level data is saved to a file using the glob package which allows for filename pattern matching using various wildcards. It came handy in this case with less code for readability and understanding. Then list comprehension is used to read each CSV file into a list of dataframes for each aggregate level because we have many data as RTRA_Employ_3NAICS following with a code. The datatypes of the “SYEAR” and “SMTH” columns are converted to object (i.e. string)

For convenience, code maintenance and reusability, a function is used to concatenate the list of dataframes into a single dataframe for the EDA.

DEFINITIONS OF FUNCTIONS TO USE

```python
def combine_dataframes(list_of_DataFrames):
    """Convert list of DataFrames into a single DataFrame, and add the month
        ending day and a date columns. Set the added date column as the index
        and sort.
    Args:
        list of DataFrames to be converted.

    Return:
        A single sorted DataFrame with month end day column and a DATE index added
    """
    #Concatenate the list of DataFrames into a single DataFrame
    converted_df = pd.concat(list_of_DataFrames,ignore_index=True)
    #Dictionary with the month as the key and last day of the month as value
    days = {"1":"31","2":"28","3":"31","4":"30","5":"31","6":"30","7":"31","8":"31"\
            ,"9":"30","10":"31","11":"30","12":"31"}
    day = []
    #Iterating through the Dataframe and appending DAY and DATE columns to it, taking
    #into acoount the last of the month especially leap years
    for i in range(len(converted_df)):
        #Save the month column to a variable
        month = converted_df.loc[i,"SMTH"]
        #Save the year column to a variable
        year = converted_df.loc[i,"SYEAR"]
        #If the current year is a leap year and the month is February ("2")
        if (year =="2000" or year =="2004" or year =="2008" or year =="2012"\
            or year =="2016" or year =="2020") and month is "2":
            #Assign the value '29' to the _day variable for leap year of the month February
            _day = "29"
        else:
            #Assign the value '28' to the _day variable for non-leap year of the month February
            _day = days[month]
        #Append the variable '_day' to the list variable day
        day.append(_day)
    #The list variable is broadcast to the DAY column created for the DataFrame
    converted_df["DAY"] = day
    #New column is added to the DataFrame which consists of the last day of the month, month and year
    converted_df["DATE"] = converted_df.DAY + "-" + converted_df.SMTH + "-" + converted_df.SYEAR
    #The 'DATE' column is converted to datetime object for time series analysis
    converted_df["DATE"] = pd.to_datetime(converted_df["DATE"])
    #The 'DATE' column is set as the index of the DataFrame for convienence
    converted_df=converted_df.set_index('DATE')
    #Sort the index in ascending order to start from 1997 to 2019
    converted_df = converted_df.sort_index()
    #converted_sorted_df = converted_df.sort_values(by='DATE').reset_index(drop=True)
    return converted_df

def split_NAICS(dataframe):
    """ Convert the NAICS column of the DataFrame into two columns: NAICS name and NAICS code
    Args:
        DataFrame to have its 'NAICS' columns split.

    Return:
        DataFrame with 'NAICS' column dropped and two new columns added (i.e. 'NAICS_code' and 'NAICS_name')
        obtained from splitting the code from the NAICS names
    """
    #Split on '[' and save to a new column 'splitted_NAICS'
    dataframe['splitted_NAICS'] = dataframe.NAICS.str.split('[')
    #Save the first element in the list to a variable as the 'NAICS_name' and add it as a new column
    dataframe['NAICS_name'] = dataframe['splitted_NAICS'].str.get(0)
    #Strip off the ']' from the second element of the list and save to a column in the DataFrame as 'NAICS_code'
    dataframe['NAICS_code'] = dataframe['splitted_NAICS'].str.get(1).str.strip(']')
    #Drop the 'splitted_NAICS' column created and the NAICS column along
    dataframe.drop(['splitted_NAICS','NAICS'],axis=1,inplace=True)
    return dataframe
```

```python
<>:26: SyntaxWarning: "is" with a literal. Did you mean "=="?
<>:26: SyntaxWarning: "is" with a literal. Did you mean "=="?
<ipython-input-3-2c6a8bffc177>:26: SyntaxWarning: "is" with a literal. Did you mean "=="?
  or year =="2016" or year =="2020") and month is "2":
```

```python
"""The function definitions are used to achieve what they were defined for"""
#Read all dataframes of each NAICS code into a single DataFrame
naics_2_code_employ_data = combine_dataframes(list_2NAICS)
naics_3_code_employ_data = combine_dataframes(list_3NAICS)
naics_4_code_employ_data = combine_dataframes(list_4NAICS)

#Split the NAICS column of the combined DataFrame into NAICS name and their respective codes.
naics_2_code_employ_data = split_NAICS(naics_2_code_employ_data)
naics_3_code_employ_data = split_NAICS(naics_3_code_employ_data)
#Display the a few rows of each aggregate level
display(naics_2_code_employ_data.head(3),naics_3_code_employ_data.head(3),naics_4_code_employ_data.head(3))
```

#### EDA

The ‘NAICS’ column in the “naics_4_employ_data” is inconsistent with the column names of the other dataframes, therefore it will be renamed for consistency.

```python
#Change the 'NAICS' column of the 4NAICS to NAICS_code for consistency
naics_4_code_employ_data = naics_4_code_employ_data.rename(columns={"NAICS":"NAICS_code"})
print(naics_4_code_employ_data.columns)
```

```python
Index(['SYEAR', 'SMTH', 'NAICS_code', '_EMPLOYMENT_', 'DAY'], dtype='object')
```

```python
#Check for missing values in the 2-digit NAICS data
naics_2_code_employ_data.isna().sum()
```

```python
SYEAR           0
SMTH            0
_EMPLOYMENT_    0
DAY             0
NAICS_name      0
NAICS_code      0
dtype: int64
```

```python
#Check for missing values in the 4-digit NAICS data
naics_4_code_employ_data.isna().sum()
```

```python
SYEAR           0
SMTH            0
NAICS_code      0
_EMPLOYMENT_    0
DAY             0
dtype: int64
```

```python
#Check for missing values in the 3-digit NAICS data
naics_3_code_employ_data.isna().sum()
```

```python
SYEAR             0
SMTH              0
_EMPLOYMENT_      0
DAY               0
NAICS_name        0
NAICS_code      552
dtype: int64
```

The output of naics_3_code_employ_data showed 552 entries with NaN (i.e. missing values) for the NAICS_code column but naics_2_code_employ_data and naics_4_code_employ_data are without missing values. Therefore, further analysis on the data would reveal the course of the missing value.

```python
#Check which NAICS is having null or missing values for NAICS_code
naics_3_code_employ_data[naics_3_code_employ_data.NAICS_code.isnull()].head()
```

It is evident that “Securities, commodity contracts, and other fin” and “Other” NAICS do not have associated NAICS codes. Therefore, there is the need to resolve them. From the booklet, North American Industry Classification System (NAICS) Canada 2017 Version 1.0 (pdf) which can be obtained at [https://www.statcan.gc.ca/eng/subjects/standard/naics/2017/index,](https://www.statcan.gc.ca/eng/subjects/standard/naics/2017/index) specify the 3-digit NAICS of “Securities, commodity contracts, and other financial investment and related acti” as 523, however there is no specify 3-digit NAICS for “Other”.

The NAICS_code for the entries of “Other” would be assigned the value of 999 since there is no NAICS_name with such code.

```python
#Fill the missing NAICS_code for "Securities, commodity contracts, and other financial investment and related acti"
naics_3_code_employ_data.loc[naics_3_code_employ_data.NAICS_name == "Securities, commodity contracts, and other financial investment and related acti", "NAICS_code"] = 523
#FIll the missing NAICS_code for "Other"
naics_3_code_employ_data.loc[naics_3_code_employ_data.NAICS_name == "Other", "NAICS_code"] = 999
#Check for missing values in the 3-digit NAICS data
naics_3_code_employ_data.isna().sum()
```

```python
SYEAR           0
SMTH            0
_EMPLOYMENT_    0
DAY             0
NAICS_name      0
NAICS_code      0
dtype: int64
```

```python
#Save the number of unique industries in each aggregate level
unique_industries_2NAICS = naics_2_code_employ_data.NAICS_name.nunique()
print("The 2-digit NAICS industry has {} unique industries".format(unique_industries_2NAICS))
unique_industries_3NAICS = naics_3_code_employ_data.NAICS_name.nunique()
print("The 3-digit NAICS industry has {} unique industries".format(unique_industries_3NAICS))
unique_industries_4NAICS = naics_4_code_employ_data.NAICS_code.nunique()
print("The 4-digit NAICS industry has {} unique industries".format(unique_industries_4NAICS))
```

```python
The 2-digit NAICS industry has 20 unique industries
The 3-digit NAICS industry has 103 unique industries
The 4-digit NAICS industry has 314 unique industries
```

```python
#Aggregate the _EMPLOYMENT_ column through summation and grouping by the SYEAR, SMTH, NAICS_name
#and NAICS_code for 2-digit NAICS industries
naics2_by_year = naics_2_code_employ_data.groupby(['SYEAR','SMTH','NAICS_name','NAICS_code']).\
_EMPLOYMENT_.sum().reset_index()
#Display the first five rows
naics2_by_year.head()
```

```python
#Aggregate the _EMPLOYMENT_ column through summation and grouping by the SYEAR, SMTH, NAICS_name
#and NAICS_code for 3-digit NAICS industries
naics3_by_year = naics_3_code_employ_data.groupby(['SYEAR','SMTH','NAICS_name','NAICS_code']).\
_EMPLOYMENT_.sum().reset_index()
#Display the first five rows
saving_naics_3 = naics3_by_year.sort_values(by=["SMTH","SYEAR"],ascending=True)
#saving_naics_3.drop("NAICS_code",inplace=True,axis=1)
saving_naics_3.to_excel("naics3_by_year.xlsx",index=False)
```

```python
#List of months and years to display along the x-axis
months=["January","February","March","April","May","June","July","August",\
        "September","October","November","December"]
years=["1997","1998","1999","2000","2001","2002","2003","2004",\
        "2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
```

DEFINITIONS OF THE SECOND SET OF FUNCTIONS USED

Purposely for datetime or time series selection, whether on monthly, specific months of a particular year, yearly or specific years.

```python
def naics_data_specific_years(data,start_year,end_year):
    """Select data for specified years
    Arg:    start_month - the year to start from
            end_month - the year to end
            data   - DataFrame to use
    Return: Data of the specified years
    """
    year = [i for i in years if i >= start_year and i<= end_year]
    dataframe = data.loc[start_year:end_year].resample("A").sum().reset_index()
    return dataframe
```

```python
def naics_data_specific_months_year(data,start_month,end_month):
    """Select data from any month to another month of a specific year
    Arg:    start_month - the month to start from
            end_month - the month to end
            data   - DataFrame to use
    Return: Data of the specified months of the year
    """
    month_dict = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August",\
        "09":"September","10":"October","11":"November","12":"December"}
    monthFrom = start_month[-2:]
    monthTo = end_month[-2:]
    year = start_month[:-3]
    mth = [value for key,value in month_dict.items() if key >=monthFrom and key <=monthTo]
    dataframe = data.loc[start_month:end_month].resample("M").sum()
    return dataframe
```

```python
#Aggregate the sum of  _EMPLOYMENT_ column for 1997 monthly
display(naics_data_specific_months_year(naics_3_code_employ_data,"1997-01","1997-12"))
#Aggregate the sum of  _EMPLOYMENT_ column for yearly from 2010 to 2019
naics_data_specific_years(naics_3_code_employ_data,"2010","2019")
```

FUNCTION DEFINITION FOR PLOTTING

Function Definition for Plotting Scatterplot and Bar Chart for specific months of a particular year, specific years within the entire period and compare the trend between specific months of two different years

```python
def plot_naics_per_month_plot(data,start_month,end_month):
    """Plot a Seaborn scatterplot from any month to another month of a specific year
    Arg:    start_month - the month to start from
            end_month - the month to end
            data   - DataFrame to use
    Return: Seaborn scatterplot
    """
    month_dict = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August",\
        "09":"September","10":"October","11":"November","12":"December"}
    monthFrom = start_month[-2:]
    monthTo = end_month[-2:]
    year = start_month[:-3]
    mth = [value for key,value in month_dict.items() if key >=monthFrom and key <=monthTo]
    sns.lineplot(x=mth,y="_EMPLOYMENT_", data=data)
    plt.title("Total number of employment from {} to {} of {}".format(mth[0],mth[-1],year))
    plt.ylabel("Total number of employment")
    plt.xlabel("Months")
    plt.xticks(range(len(mth)),mth,rotation=60)
    plt.show()
```

```python
def plot_naics_per_month_barplot(data,start_month,end_month):
    """Plot a Seaborn scatterplot
    Arg:    year to plot its monthly employment
            data   - DataFrame to use
    Return: Seaborn scatterplot
    """
    month_dict = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August",\
        "09":"September","10":"October","11":"November","12":"December"}
    monthFrom = start_month[-2:]
    monthTo = end_month[-2:]
    year = start_month[:-3]
    mth = [value for key,value in month_dict.items() if key >=monthFrom and key <=monthTo]
    g = sns.barplot(x=mth,y="_EMPLOYMENT_", data=data)
    for index, row in data.iterrows():
        g.text(row.name,row._EMPLOYMENT_, row._EMPLOYMENT_, color='black', ha="center",rotation=90)
    plt.title("Total number of employment from {} to {} of {}".format(mth[0],mth[-1],year))
    plt.ylabel("Total number of employment")
    plt.xlabel("Months")
    plt.xticks(range(len(mth)),mth,rotation=60)
    plt.show()
```

```python
def compare_monthly_employ(data1,start_month,end_month,data2,start2_month,end2_month):
    """Create a lineplot for comparing employments between months for two different years
    Arg:    start_month - the month to start from
            end_month - the month to end
            data   - DataFrame to use
    Return: Seaborn scatterplot
    """
    month_dict = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August",\
        "09":"September","10":"October","11":"November","12":"December"}
    monthFrom = start_month[-2:]
    monthTo = end_month[-2:]
    year1 = start_month[:-3]
    year2 = start2_month[:-3]
    mth = [value for key,value in month_dict.items() if key >=monthFrom and key <=monthTo]
    sns.lineplot(x=mth,y="_EMPLOYMENT_", data=data1,label=year1)
    sns.lineplot(x=mth,y="_EMPLOYMENT_", data=data2,label=year2)
    plt.title("Total number of employment from {} to {} between {} and {}".format(mth[0],mth[-1],year1,year2))
    plt.ylabel("Total number of employment")
    plt.xlabel("Months")
    plt.xticks(range(len(mth)),mth,rotation=60)
    plt.legend()
    plt.show()
```

```python
def compare_yearly_employ(data1,start_year,end_year,data2,start_2nd_year,end_2nd_year):
    """Create a lineplot for comparing employments for two different years
    Arg:    start_year - the start year of the first data
            end_year - the end year of the first data
            data1   - the first dataset
            start_2nd_year - the start year of the second data which must be the same as the start-year of the first data
            end_2nd_year - the end year of the second data which must be the same as the end-year of the first data
            data2   - the second dataset
    Return: Seaborn scatterplot
    """
    year = [i for i in years if i >= start_year and i<= end_year]
    sns.lineplot(x=year,y="_EMPLOYMENT_", data=data1,label="Construction industry")
    sns.lineplot(x=year,y="_EMPLOYMENT_", data=data2,label="All other industries")
    plt.title("Total number of employment from {} to {}".format(start_year,end_year))
    plt.ylabel("Total number of employment")
    plt.xlabel("Months")
    plt.xticks(range(len(year)),year,rotation=60)
    plt.legend()
    plt.show()
```

```python
def plot_naics_per_year_plot(data,from_year,to_year):
    """Plot a Seaborn scatterplot
    Arg:    from_year - starting year
            to_year - ending year
            data   - DataFrame to use
    Return: Seaborn scatterplot
    """
    year = [i for i in years if i >= from_year and i<= to_year]
    sns.lineplot(x=year,y="_EMPLOYMENT_", data=data)
    plt.title("Total number of employment per year from {} to {}".format(from_year,to_year))
    plt.ylabel("Total number of employment")
    plt.xlabel("Year")
    plt.xticks(range(len(year)),year,rotation=60)
    plt.show()
```

```python
def plot_naics_per_year_barplot(data,from_year,to_year):
    """Plot a Seaborn scatterplot
    Arg:    from_year - starting year
            to_year - ending year
            data   - DataFrame to use
    Return: Seaborn scatterplot
    """
    year = [i for i in years if i >= from_year and i<= to_year]
    g = sns.barplot(x=year,y="_EMPLOYMENT_", data=data)
    for index, row in data.iterrows():
        g.text(row.name,row._EMPLOYMENT_, row._EMPLOYMENT_, color='black', ha="center",rotation=90)
    plt.title("Total number of employment per year from {} to {}".format(from_year,to_year))
    plt.ylabel("Total number of employment")
    plt.xlabel("Year")
    plt.xticks(range(len(year)),year,rotation=90)
    plt.show()
```

#### QUESTIONS DRIVING THE TIME SERIES ANALYSIS

The following questions would drive the time series analysis of the data.

1. How employment in Construction evolved overtime?
2. How employment in Construction evolved over time, compared to the total employment across all industries?
3. How the total employment evolve overtime?
4. What is the peak month (s) for employment overtime?
5. What is the 2-digit NAICS industry employing most people?

#### 1. HOW EMPLOYMENT IN CONSTRUCTION EVOLVED OVERTIME?

```python
def industry_by_code_select(data,code):
    """Select data from the specified data using the provided code
    Arg:    code - NAICS code to use
            data   - DataFrame to use
    Return: Data of the specified code
    """
    dataframe = data[data.NAICS_code==code]
    return dataframe
```

Few rows of the construction industry’s employment is shown below.

```python
construction_industry_ = industry_by_code_select(naics_2_code_employ_data,"23")
display(construction_industry_.head(5))
display(construction_industry_.shape)
```

The shape of the construction industry employment data is *276* rows with *6* columns, which will make it difficult to observe the any trend in employment overtime. Therefore the data will be resampled yearly to observe it trend over the *23* years range.

```python
construction_industry = naics_data_specific_years(construction_industry_,"1997","2019")
plot_naics_per_year_barplot(construction_industry,"1997","2019")
plot_naics_per_year_plot(construction_industry,"1997","2019")
```

Employment in the construction industry started off on a high note (i.e., in *1997*), but declined over the next four years (i.e., from \*1998 to *2001*) and experienced a *fifty-four thousand two hundred and fifty (54,250)* increase in employment over the *2001* figure. Employment figures in the industry continued to increase steadily until they rose sharply between 2004 and 2008. Thereafter, the industry began to experience a decline in employment from *2009* to *2011* and a slight increase from *2012* to *2013*, followed by a decline again in *2014* and *2015*. The second strong increase in industry employment occurs from *2016* to *2018* reaching the *maximum industry value in 2018* with total employment of *two million eight hundred and sixty thousand seven hundred and fifty (or 2,860,750)*. However, a decline in employment in the construction industry was observed in *2019*. It is important to note that the early years (*1997–2003*) have the lowest employment in the sector, with the sector employing more people in the periods *2005* and *2008*.

Overall, employment in the construction industry has been volatile with some fluctuations here and there that are not available from the data available in this analysis.

#### 2. How employment in Construction evolved over time, compared to the total employment across all industries?

To find the trend of all other industry as compared to the Construction industry, the data of these industries must first be extracted from the dataset. Below is the first few rows of all other industries excluding the construction industry

```python
without_const_industry = naics_2_code_employ_data[naics_2_code_employ_data.NAICS_code!="23"]
display(without_const_industry.head(10))
without_const_industry.shape
```

As expected, the data is **5196** rows with **6** columns, which will make it difficult to compare the construction employment with non-construction industry employment (i.e. all other industries). Therefore, the data will be resampled yearly to do the comparison over the *23* years range.

```python
non_construct = naics_data_specific_years(without_const_industry,"1997","2019")
fig,(ax,ax1) = plt.subplots(2,sharex=True,figsize=(8,6))
plt.subplots_adjust(top = 0.89, bottom=0.01, hspace=0.2, wspace=0.2)
fig.suptitle("Comparison between the Construction and Non-construction industry, 1997 to 2019")
ax.scatter(x=years,y=construction_industry._EMPLOYMENT_)
ax.set_title("Construction industry employment")
ax.set_ylabel("Total employment")
#plt.xticks(range(len(years)),years,rotation=90)
ax1.scatter(x=years,y=non_construct._EMPLOYMENT_)
ax1.set_title("Non-construction industry employment")
ax1.set_ylabel("Total employment")
ax1.set_xlabel("Year")
plt.xticks(range(len(years)),years,rotation=90)
plt.show()
```

While employment in the construction industry began to decline, employment in non-construction industries began to increase steadily from *1997* to *2000*, then declined in *2001*, before continuing to increase, but this time more steadily (from *2002* to *2008*). Over the same period (from *2002* to *2008*), however, the construction industry grew strongly each year to its third highest employment rate over a *23* year period (behind *2017* and *2018*). Although both sectors experienced a decline in employment in 2009, the non-construction sector recovered in subsequent years from *2010* to *2012*, but with a slight decline in *2013* (i.e., *32,500* less than employment in *2012*). However, the decline in construction employment continued through *2011* and appreciated in *2012* and *2013*, with *69,750* more than *2012* employment in *2013*. From *2014* to *2018*, employment figures in non-construction industries again increased significantly over the period, peaking in employment in *2018* with a total of *27 million sixty-two thousand two hundred and fifty (27,062,250*). While the value of employment in the non-construction industry continued to increase from 2014 to 2018, employment in the construction industry instead experienced a decline in 2014 and 2015, followed by a continuous and significant increase until 2018, the year of peak employment in the construction industry (i.e. *two million eight hundred and sixty thousand seven hundred and fifty, 2,860,750*). Both sectors experienced a sharp decline in the value of employment in 2019, with the non-construction sector having a higher rate of decline than construction.

The non-construction industries appear to outperform the construction industry in terms of employment opportunities offered over a *23* year period (i.e. *1997–2019*). In addition, the cause of the spike in employment over the years *2016* to *2018* in both sectors and in other sectors is not known, so further research and data analysis is needed to uncover the cause(s) of these spikes.

```python
without_const_industry_month_2016 = naics_data_specific_months_year(without_const_industry,"2016-01","2016-12")
without_const_industry_month_2017 = naics_data_specific_months_year(without_const_industry,"2017-01","2017-12")
without_const_industry_month_2018 = naics_data_specific_months_year(without_const_industry,"2018-01","2018-12")
const_industry_month_2016 = naics_data_specific_months_year(construction_industry_,"2016-01","2016-12")
const_industry_month_2017 = naics_data_specific_months_year(construction_industry_,"2017-01","2017-12")
const_industry_month_2018 = naics_data_specific_months_year(construction_industry_,"2018-01","2018-12")
fig,((ax,ax1),(ax2,ax3),(ax4,ax5)) = plt.subplots(3,2,figsize=(10,8))
plt.subplots_adjust(top = 0.89, bottom=0.01, hspace=0.85, wspace=0.4)
fig.suptitle("Comparison between the Construction and Non-construction industry per month, 2016 to 2018")
ax.scatter(x=months,y=const_industry_month_2016["_EMPLOYMENT_"])
ax.set_title("Monthly Construction industry's employment, 2016")
ax.set_ylabel("Total employment")
ax1.scatter(x=months,y=without_const_industry_month_2016["_EMPLOYMENT_"])
ax1.set_title("Monthly Non-construction industry's employment, 2016")
ax1.set_ylabel("Total employment")
ax2.scatter(x=months,y=const_industry_month_2017["_EMPLOYMENT_"])
ax2.set_title("Monthly Construction industry's employment, 2017")
ax2.set_ylabel("Total employment")
ax3.scatter(x=months,y=without_const_industry_month_2017["_EMPLOYMENT_"])
ax3.set_title("Monthly Non-construction industry's employment, 2017")
ax3.set_ylabel("Total employment")
ax4.scatter(x=months,y=const_industry_month_2018["_EMPLOYMENT_"])
ax4.set_title("Monthly Construction industry's employment, 2018")
ax4.set_ylabel("Total employment")
ax5.scatter(x=months,y=without_const_industry_month_2018["_EMPLOYMENT_"])
ax5.set_title("Monthly Non-construction industry's employment, 2018")
ax5.set_ylabel("Total employment")
plt.xlabel("Months")
for ax in fig.axes:
    ax.set_xticklabels(months,rotation=90)
plt.show()
```

```python
<ipython-input-51-a4f5d1c513a5>:30: UserWarning: FixedFormatter should only be used together with FixedLocator
  ax.set_xticklabels(months,rotation=90)
```

#### 3. How the total employment evolve overtime?

In this anlaysis, we want to find out how the total accumulated employment from all sectors evolve over time in respect to *23* year range. As usual we have to aggregate the data for total employment for each year from *1997* to *2019*. A few rows of the data is shown below.

```python
total_employ_97_19 = naics_data_specific_years(naics_2_code_employ_data,"1997","2019")
display(total_employ_97_19.head())
total_employ_97_19.shape

plot_naics_per_year_barplot(total_employ_97_19,"1997","2019")
plot_naics_per_year_plot(total_employ_97_19,"1997","2019")
```

From the outset, total employment fell in 1998, with *six thousand two hundred and fifty (26,250)* fewer jobs than in 1997. It then began to rise sharply from *2001* to *2008*, but there was a slight decline in 2001 (i.e. *118,000 fewer jobs than in 2000*) when the numbers began to rise from *1999*. After *2008*, *2009* saw a decline of *five hundred and ninety-nine thousand two hundred and fifty, 599,250* jobs from the *2008* figure, followed by a steady increase in total employment until *2015* and a sharp increase from *2015* to *2018*. However, the 2019 employment figure has dropped to a value of 23 million 57 thousand five hundred, 23,057,500\*, which is consistent with the data we have analysed, so again the reason for the drop is not readily available for this analysis. The consistency is not just with the 2019 figures, 2018 was also the year with the highest number of jobs in terms of the data analysed.

#### 4. What is the peak month (s) for employment overtime?

In this analysis, we would approach it in two ways. First, we will determine the peak month when the data is aggregated on monthly basis for each year and secondly, the peak month when the aggregation is done monthly for the whole period (i.e. 1997–2019).

```python
#Find the total employment for each month within each year (i.e. Jan 1997, Feb 1997 ...)
month_employ = naics_2_code_employ_data.loc["1997-01":"2019-12"].resample("M").sum()
#Sorted the data in decsending order and display the first 10 rows
month_employ_sorted = month_employ.sort_values(by="_EMPLOYMENT_",ascending=False)
display(month_employ_sorted.head(10),month_employ_sorted.tail(10))
```
