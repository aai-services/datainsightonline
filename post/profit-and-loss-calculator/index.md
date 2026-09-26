---
title: "Profit and Loss Calculator"
author: "ekow.a.indome"
date: 2021-09-22
description: "As business firm, you would always want to know how well you are performing and if you are making more than expected or less than what you invest in your business. This calculator is a simple..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/profit-and-loss-calculator
---
As business firm, you would always want to know how well you are performing and if you are making more than expected or less than what you invest in your business. This calculator is a simple calculator that calculates either profit or loss based on monthly sales.
Here is how it works:

The program first takes the enterprise's name. Then a selling price in the form of monetary value(i.e. .00) is entered, followed by the cost price of the product.

```python
print("A program to analyze profit and loss")
name = input("Enter the name of the enterprise: ")
selling_price = float(input("Enter the selling price: "))
cost_price = float(input("Enter the cost price: "))
```

All now that it's left is for the program to use decision statements to find our if you are making profit or making losses. This helps reduce excess calculations .

```python
if (selling_price > cost_price):
    profit = selling_price - cost_price
    profit_percent = (profit / cost_price) * 100
    txt = "You had a profit of {:.2f} at a profit percent of {:.2f}"
    print(txt.format(profit, profit_percent))
else:
    loss = cost_price - selling_price
    loss_percent = (loss / cost_price) * 100
    text = "You had a loss of {:.2f} at a loss percent of {:.2f}"
    print(text.format(loss, loss_percent))
```
