---
title: "Pandas to Read a CSV file"
author: "bismark boateng"
date: 2021-10-07
description: "Pandas were initially developed by Wes McKinney in 2008 while he was working at AQR Capital Management. He convinced the AQR to allow him to open source the Pandas. Another AQR employee, Chang She..."
categories: ["Pandas"]
wix-url: https://www.datainsightonline.com/post/pandas-to-read-a-csv-file
---
Pandas were initially developed by Wes McKinney in 2008 while he was working at AQR Capital Management. He convinced the AQR to allow him to open source the Pandas. Another AQR employee, Chang She, joined as the second major contributor to the library in 2012. Over time many versions of pandas have been released. The latest version of the pandas is 1.3.3

Pandas helps a data scientist to read csv file and also manipulate the csv files be read to get more insight from the data set being give

to read a csv file using pandas , the pandas package has to be installed

using pip since it does not common with default python installation.

```python
pip install pandas
```

The command above is used to install pandas using the command prompt, meanwhile users of anaconda don't have to worry about this as it comes preinstalled

To use the pandas package, we need to import the package

```python
import pandas as pd
```

In the above code, the pandas package is imported under the alias pd

```python
pd.read_csv("path_to_file")
```

The code above is used to read the csv file using pandas method .read_csv()

Note; you need to specifiy the path of the csv file correctly into the method .
