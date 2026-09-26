---
title: "Simple Interest Calculator"
author: "Blessing Oluwadaara"
date: 2021-10-15
description: "Simple interest is interest calculated on the principal portion of a loan or the original contribution to a savings account. Simple interest does not compound, meaning that an account holder will..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/simple-interest-calculator
---
Simple interest is interest calculated on the principal portion of a loan or the original contribution to a savings account. Simple interest does not compound, meaning that an account holder will only gain interest on the principal, and a borrower will never have to pay interest on interest already accrued.

The formula for calculating simple interest is: amount \* Interest Rate \* Term of the loan.

amount = input('Enter the amount you want to save or borrow: ')

rate = 10

term =input('Enter how long you wan to save or borrow for: ')

interest = (float(amount)\*rate\*float(term))/100

interest

print('Your interest is '+ str(interest))
