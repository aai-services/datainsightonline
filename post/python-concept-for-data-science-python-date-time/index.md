---
title: "Python concept for Data Science: Python Date & Time"
author: "Eman Mahmoud"
date: 2021-10-06
description: "Date & Time is an important form of structured data in many different fields, such as finance, and economics. We will use the date class of the datetime module.date.today() method to get the current..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concept-for-data-science-python-date-time
---
**Date & Time is an important form of structured data in many different fields, such as finance, and economics.**

**We will use the date class of the datetime module.**

### date.today()** **method to get the current local date.
```python
from datetime import date
today = date.today()
print("Today's date:", today)
```

Today's date: 2021-10-06

### use the** **strftime()** **method to create a string representing date in different formats.
```python
from datetime import date
today = date.today()
# dd/mm/YY
D1 = today.strftime("%d/%m/%Y")
print("D1 =", D1)
# Textual month, day and year
D2 = today.strftime("%B %d, %Y")
print("D2 =", D2)
# mm/dd/y
D3 = today.strftime("%m/%d/%y")
print("D3 =", D3)
# Month abbreviation, day and year
D4 = today.strftime("%b-%d-%Y")
print("D4 =", D4)
```

D1 = 06/10/2021

D2 = October 06, 2021

D3 = 10/06/21

D4 = Oct-06-2021

### Get the current date and time
### use** **datetime.now()** **method
```python
from datetime import datetime
now = datetime.now()
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
```

now = 2021-10-06 02:06:11.523039

date and time = 06/10/2021 02:06:11

### Python** **timedelta** **class is used for calculating differences in dates and also can be used for date manipulations in Python
```python
from datetime import datetime, timedelta
ini_time_for_now = datetime.now()
# 'datetime.date' can converted to steing use str print("initial_date",str(ini_time_for_now))
future_date_after_2yrs = ini_time_for_now
+ timedelta(days=730)
print('future_date_after_2yrs:', str(future_date_after_2yrs))
```

initial_date 2021-10-06 02:06:11.678496

future_date_after_2yrs: 2023-10-06 02:06:11.678496

[code link in github](https://github.com/eman888991/Data-Insight/blob/main/Python_Date%26Time.ipynb)
