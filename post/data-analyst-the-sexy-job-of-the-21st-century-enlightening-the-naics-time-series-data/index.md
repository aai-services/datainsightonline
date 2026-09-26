---
title: "Data analyst, the sexy job of the 21st century enlightening the NAICS time series data."
author: "Espoir Gaglo"
date: 2020-09-08
description: "A. Data AnalystThe rise of social networks, e-commerce and the Internet of Things has meant that companies in all industries now possess immense amounts of data. This data can be related to their..."
categories: ["Time Series"]
image: images/9b2dd8_1c8b26e946254def9d3a1dca68d47b54.webp
wix-url: https://www.datainsightonline.com/post/data-analyst-the-sexy-job-of-the-21st-century-enlightening-the-naics-time-series-data
---
**A. Data Analyst**

![](images/a27d24_4a21b997cf3d448db21be2582f2708d2.webp)

The rise of social networks, e-commerce and the Internet of Things has meant that companies in all industries now possess immense amounts of data. This data can be related to their customers, their products, their own performance, or even the market as a whole and the competition.

By analyzing this raw data, it is possible to extract very useful information to support decision making and gain competitive advantage. However, data analysis requires expertise and skills. This is where the Data analyst's job can help. It is in charge of processing the data available to the company in order to extract information from it to stimulate the company's growth and guide its strategy.

This information can then be used to decide which products to develop, or to define a marketing strategy. Thus, it is at the heart of the company. He is the one who must define the strategy to adopt and the direction to take. His role is to give meaning to the data, to transform it into usable information.

**B. NAICS**

![](images/a27d24_68d4d014d73043898fc9fd218b8f3f10.webp)

The **North American Industry Classification System (NAICS)** is an industry classification system developed by the statistical agencies of Canada, Mexico and the United States. It is used by business and government to classify business establishments according to type of economic activity or industry.

A NAICS code can have up to 6 digits. The breakdown:

- The **1st and 2nd numbers** = economic sector
- The **3rd number** = sub-sector
- The **4th number** = industry group
- The **5th number** = industry
- The **6th number** = national industry (a zero indicates no national industry is needed)

**C. Analysis**

Before analyzing these data, activities will be carried out to structure, clean up, extend, validate and publish the results in a suitable format. The whole of these processes is **data wrangling**. Questions related to this task are:

- Which most companies hired the most in Canada?
- How employment in Construction evolved overtime? In which month the recruitment are most important?
- How employment in Construction evolved over time, compared to the total employment across all industries?
- How food manufacturing companies have evolved in recruitment over time ? In which month the recruitment are most important?
- How employment in Repair, personal and non-profit services evolved over time? At what month are volunteers most needed?

1. **Preparation of the data set**

We worked with the glob package which allows to assemble the different csv files according to their classification (2, 3, 4 digits). This method avoids us to write a lot of code. The main activities before EDA consisted in converting some columns into strings for extractions, character replacements, concatenations and data joins.

![](images/a27d24_44b55bda0ab14df1a97b22669b46a56f.webp)

a- Preprocessing of the five 2-digit NAICS datasets

![](images/a27d24_e82baa094bdb4394aa8693487a6cdf65.webp)

![](images/a27d24_53bc2c32ffff4cfa9792115a41f07582.webp)

b- Preprocessing of the five 3-digit NAICS datasets

![](images/a27d24_8f31b666578948379e6f2a25cd3f0359.webp)

c- Preprocessing of the five 4-digit NAICS datasets

![](images/a27d24_ea825ea17ea14489acfcaf871195115b.webp)

d- Join all dataset in one

![](images/a27d24_7579868c0b1b4eeabab00a3d741d5213.webp)

e- Extraction Industries code in LMO_Detailed_Industries_by_NAICS file

![](images/a27d24_affef16f2573437cbe8a74983b7047b5.webp)

```python
##Conversion my list type in integer
list_of_code = [int(i) for i in new_list]
print(list_of_code)
```

2. Exploratory Data analysis

![](images/a27d24_6485c4460fde406fbfc5cc5336867e11.webp)

**Q1: Which 3 companies hired the most in Canada?**

![](images/a27d24_9ec3806e94764545bb722b51021a59bb.webp)

![](images/a27d24_946054628a9b449d9f162827d8563be0.webp)

- The top 2 companies that hire the most in Canada are: construction companies (23) with 86032500, then non-profit services with 47391750

**Q2: How employment in Construction evolved overtime? In which month the recruitment are most important?**

![](images/a27d24_af7f4458a24e4189a50400c46d8363d3.webp)

![](images/a27d24_531d4fe469ca44d88da32d766a42a193.webp)

![](images/a27d24_27f22b94bff64c259354f0506ce4075a.webp)

![](images/a27d24_d5403aa997b746c583a9974b7f4793bd.webp)

- Employment in construction has fluctuated with a significant downturn in 2000 probably due to the economic crisis. The increase in employment gradually rebounded until 2018, its highest point. From the same year, there was a clear decrease and it is not going to stop with the health crisis of 2020.
- Recruitment in the construction industry is highest for almost 4 months (highest in August). However, the variation is not very significant for the other months, even though December is still the smallest.

**Q3: How employment in Construction evolved over time, compared to the total employment across all industries?**

![](images/a27d24_28f559d54b1d445495fffc0eee2dc16b.webp)

![](images/a27d24_45ba474b964f49a5ae4f5c42627424f7.webp)

- Generally it is the construction industry that hires the most part of all the companies included in the study, this hiring rate varies on average between 40% and 60%. This result demonstrates the influence of this industry in the Canadian economy.

**Q4: What is the evolution of employment in food manufacturing during the year?**

![](images/a27d24_6c50f2efce1c415b85d74a09cc9db9b2.webp)

![](images/a27d24_8cbd2360ffc249cca76d2a660eb36006.webp)

![](images/a27d24_a64fb81198e0495cab514b03cb4d586b.webp)

- Employment in food manufacturing is generally very low and is higher in December than in January.

**Q5: How employment in Repair, personal and non-profit services evolved over time? At what month are volunteers most needed ?**

![](images/a27d24_57f199b359f8449cae9ebb52b11a13e0.webp)

![](images/a27d24_1de5714cbbc446cb8c368021a9e67acf.webp)

- Employment in not-for-profit organizations tends significantly over time. At its lowest level in 2007, it increased in the next few years with some fluctuations, peaking in 2019. Average over the months, the difference is not too significant even if October remains the least important period in terms of employment in this sector.

**D. Conclusion**
The previous analyses show that the sector that hires the most is the construction sector. Even if during the year 2000, jobs fell dramatically, probably due to the crisis, a gradual recovery is noted in the following years with 2018 as the year that recorded more hiring. This sector represents a major source of employment compared to other sectors.

**References**

https://www.bls.gov/bls/naics.htm
 https://www.edureka.co/blog/data-analyst-vs-data-engineer-vs-data-scientist/
