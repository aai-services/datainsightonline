---
title: "Password generator from first names"
author: "Wilson Waha"
date: 2022-05-06
description: "Since the creation of the Internet, people have accessed sites, created accounts requiring passwords. some people have difficulty creating strong passwords. A need for security is therefore felt. For..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/password-generator-from-first-names
---
Since the creation of the Internet, people have accessed sites, created accounts requiring passwords. some people have difficulty creating strong passwords. A need for security is therefore felt. For this we have set up a program capable of generating a password from an individual's first name.

```python
import string
import random

def pass_gen(firstname):

    """ Generate random password from a first name

    Args:
    firstname (str) : The first name to generate password


    Returns:
    str: generated password

    """

    symbols = list(string.ascii_letters + string.digits+"<!?/$*%-(_)#@&+=")

    l = len(firstname)                            # length of the first name

    # if the length is smaller than 8 we round it to 8 caracters
    diff = 8-l
    symbol_complete =""
    for i in range(diff):
        symbol_complete = symbol_complete + random.choice(symbols)

    a = lambda x : x+symbol_complete if(l<8) else x
    firstname = a(firstname)


    #let mix up the caracters of first name
    firstname = list(firstname) # convert the firstname in to list to shuffle it
    final_len = len(firstname)
    firstname_mix = random.sample(firstname, len(firstname))
    firstname_generate = ""
    for i in range(final_len):
        m = (i+1)%8
        firstname_generate = firstname_generate + symbols[m] + firstname_mix[i] + random.choice(symbols)
    firstname_generate = ''.join(random.sample(firstname_generate, len(firstname_generate)))

    return firstname_generate
```

Example of use

```python
in: pass_gen("DataInsight")
```

```python
out fDcgTvhvw/ted<hdngaiscaaIqibba!tX
```

Another example:

```python
in: pass_gen("Adama")
```

```python
out: Ba4c<ftYaAgte/hc-6addmbc
```

This fonction can generate a strong password from firsts Names

Important python concept

Lambda function: a lambda function is an anonymous function that can be helpful to perform a small task in only one line of code

example of use in our password generator program

```python
a = lambda x : x+ symbol_complete if(l<8) else x
```

Here lambda function help to complet the lenght of a first name to 8 characters for those whose the lenght is smaller than 8.
