---
title: "Real Time Currency Converter with Python"
author: "Gilbert Temgoua"
date: 2021-08-31
description: "Build hands-on skills in the programming language of the futureThe development of the exchanges between individuals and societies led to the invention of more than 160 standard currencies, as..."
categories: ["Python"]
image: images/0fd4ab_6248b97a1e9e4b619e3b2be0c4376c92.webp
wix-url: https://www.datainsightonline.com/post/real-time-currency-converter-with-python
---
### Build hands-on skills in the programming language of the future

![](images/0fd4ab_6248b97a1e9e4b619e3b2be0c4376c92.webp)

The development of the exchanges between individuals and societies led to the invention of more than 160 standard currencies, as mentioned by the [ISO 4217 standard](https://currencysystem.com/codes/) and each currency is associated with a three-letter code. Not only, These currencies do not have the same value but also the exchange rates fluctuate regularly, hence the need of real time conversion to establish the equivalence between two different currencies.

In this project, we create a function **convert** with four input arguments:

- The amount in source currency: amount
- The three-letter code of the input currency:
- The code of the target currency;
- The user's API key if exists

The function yields the equivalent amount in the target currency.
Refer to [ExchangeRate-API Documentation](https://www.exchangerate-api.com/docs/overview) for more information about the **API Key**.

### Import necessary packages

```python
import requests, json
import socket  # To test internet availability
```

To make sure the program runs even offline, the exchange rates with respect to **US Dollar**(our base currency) are stored in **old_rate** and the date of the last update is stored in **old_date**. If we run the program offline, the last conversion rates will be used and the corresponding date will be printed. On the other hand, when connected to internet, the program uses the real time rate and updates the old one.

### Check internet availability

```python
def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

# Test the function
is_connected()
```

```python
True
```

### Get the conversion rates with respect to the base currency

Make sure to be connected to internet the first time you run the code, this way, **old-rate** and **old_date** will be initialized.

```python
base_curr = 'USD'
api_key = None
old_rate = {}

if api_key == None:
    url = 'https://open.er-api.com/v6/latest/'+ base_curr
else:
    url = 'https://v6.exchangerate-api.com/v6/'+ api_key + '/latest/'+ base_curr

if is_connected():
    result = requests.get(url, timeout=10).json()
    rate_usd = result['rates']
    old_date = result['time_last_update_utc'][:-6] + ' UTC'
else:
    print("Can't connect to internet... \nUsing old rate from {}".format(old_date))
    rate_usd = old_rate
```

We might want to set a different base currency. In this case we'll just have to replace 'USD' by the code of the currency we want as base. **Make sure to get the exchange rate with respect to this currency in case you might want to run the program offline,** to assign it to **old_rate** at a given **old_date**.

### Define the main function

Once the exchange rates are downloaded, the conversion between two currencies different from the base currency is performed through the following formulae:

**output_amount = input_amount x rate_output_curr_to_usd / rate_input_curr_to_usd**

```python
def convert(amount, from_curr = 'USD', to_curr = 'USD', api_key=None):

    output_amount = (amount / rate_usd[from_curr]) *
    rate_usd[to_curr]

    return output_amount
```

### Testing our function

```python
# Online
api = 'Your API' # If there's one
convert(100, 'USD', 'XAF', api)
```

```python
55618.340000000004
```

```python
# Offline
convert(100, 'USD', 'XAF', api)
```

```python
Can't connect to internet...
Using old rate from Mon, 30 Aug 2021 00:02:31 UTC
55638.0
```

Find the repository [here](https://github.com/tem-ctrl/real_time_currency_converter)
