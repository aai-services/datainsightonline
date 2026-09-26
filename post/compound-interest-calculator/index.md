---
title: "Compound Interest Calculator"
author: "Amr Mohamed Salama"
date: 2022-01-14
description: "What Is Compound Interest? • Compound interest (or compounding interest) is interest calculated on the initial principal, which also includes all of the accumulated interest from previous periods on..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/compound-interest-calculator
---
[**What Is Compound Interest?**](https://www.investopedia.com/terms/c/compoundinterest.asp#:~:text=PERSONAL%20FINANCE%20%20BANKING-,Compound%20Interest,-By)

- Compound interest (or compounding interest) is interest calculated on the initial principal, which also includes all of the accumulated interest from previous periods on a deposit or loan.
- Compound interest is calculated by multiplying the initial principal amount by one plus the annual interest rate raised to the number of compound periods minus one.
- Interest can be compounded on any given frequency schedule, from continuous to daily to annually.

When calculating compound interest, the number of compounding periods makes a significant difference.

[**How Compound Interest Works**](https://www.investopedia.com/terms/c/compoundinterest.asp#:~:text=PERSONAL%20FINANCE%20%20BANKING-,Compound%20Interest,-By)

Compound interest is calculated by multiplying the initial principal amount by one plus the annual interest rate raised to the number of compound periods minus one. The total initial amount of the loan is then subtracted from the resulting value.

**Compound interest = [P (1 + i)n] – P**

**= P [(1 + i)n – 1]**

Where:

*P = principal*

*i = nominal annual interest rate in percentage terms*

*n = number of compounding periods*

**Importing needed Python packages**

```python
import pandas as pd
import numpy as np
```

**The Calculation Function**

```python
def Compound_Interest_Calculator(p_principle,i_interest_rate,
t_period):
  # Calculates compound interest
  FV = np.round(p_principle * (pow((1 + i_interest_rate / 100),\n
                                   t_period)), decimals=2)
  compound_interest = FV - p_principle
  print("For a Principle of {0} $ \nThe Futur Value is = {1} $\nand The Compound Interest is = {2} $"\n
        .format(p_principle, FV, compound_interest))
```

## The Investment Calculation
```python
investment =Compound_Interest_Calculator(10000, 20, 20)
```

**Output**

```python
For a Principle of 10000 $
The Futur Value is = 383376.0 $
and The Compound Interest is = 373376.0 $
```
