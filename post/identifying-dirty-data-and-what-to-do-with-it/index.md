---
title: "Identifying dirty data and What to do with it."
author: "Blessing Oludele"
date: 2022-05-01
description: "As an aspiring data scientist like myself, I have come to the painful conclusion that in the real world I would rarely be presented with clean data. You should accept that as the reality so you won't..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/identifying-dirty-data-and-what-to-do-with-it
---
As an aspiring data scientist like myself, I have come to the painful conclusion that in the real world I would rarely be presented with clean data. You should accept that as the reality so you won't end up disappointed and frustrated.

**Dirty data**: A dirty data is any data that is capable of producing misleading insights. It comes in many forms which we would look at briefly.

**Identifying dirty data**;

1. *A column containing more than one information*;
   Every field/column in a data should describe only one characteristic or variable of the record. example; having a single column containing the name and age of a particular person, this are two different variables and it is best they are separated.
2. *Duplicates*:
   A data that has the same information repeated severally is considered dirty and should be cleaned before further modelling is done with that data
3. *Non-uniform data:*
   An example of a data that isn't uniform is a column of temperatures where some of the values are in degrees and some are in Fahrenheit. The inconsistencies of the units affect the quality of any result gotten from that data. Also, data format may not be uniform and this also qualifies as dirty data.
4. *Missing values:*
   A data set with empty fields and several Nan (Not a number) is considered dirty data because those null values will affect any insights gotten from such data.
5. *Incorrect data:*
   Sometimes we can just clearly tell that some values in a data set can simply not be correct. If we have an age column in a survey of teenagers and we see an age of 131, this is most likely a mistake and it is safe to assume this was meant to be 13. Also, there are some temperature values that are simply outrageous and we just know they are wrong, proceeding with such values lead to inaccurate insights derived from them.
6. *Wrong data type:*
   Several times we have a integer data type stored as a string or a float stored as a string, this causes calculations to yield wrong results and hence faulty insights.

**What to do with dirty data:**

Based on the ways we listed above on how to identify dirty data, I'm going to be citing code examples on how to solve them.

1. Separating a column with several information to multiple columns:

2. Removing duplicates:

3.Making data uniform/consistent:

4. Missing Values:

5. incorrect data:

Just like the nonuniform data or missing values, some domain knowledge is necessary in dealing with this. If it is not a large proportion of the data though, it can be dropped without significant impact on the insight to be derived from the data.

6. Wrong data type:

The code snippets provide simple and intuitive examples in dealing with the various instances of dirty data cited above.

Note, however, in real life the fixes won't be this simple but this understanding can still serve as a guide.
