---
title: "Telephone code App zone 6 (oceanic)"
author: "Lucien Dikla Ngueleo"
date: 2022-05-06
description: "GeneralityAn international dialing code is a telephone prefix used in the telephone numbers of countries or regions that are members of the International Telecommunication Union. The area code..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/telephone-code-app-zone-6-oceanic
---
**Generality**

**An international dialing code** is a telephone prefix used in the telephone numbers of countries or regions that are members of the International Telecommunication Union. The area code indicates the country where the owner of the number is located

```python
def phone_code_ocean(county):
  dic_code_ocean = {
    "Australia" :"61",
    "Fiji" :"679",
    "Marianas" :"1-670",
    "Niue" :"683",
    "New Caledonia": "687",
    "New Zealand" :"64",
    "Papua New Guinea" :"675",
    "French Polynesia" :"689",
    "Solomon Islands": "677"}
 return dic_code_ocean.get(county, "country not found")
```

*Example of use*

```python
print(phone_code_ocean("Australia"))
```

**out**

```python
 61
```

*Example of use*

```python
print(phone_code_ocean("cameroon"))
```

**out**

```python
country not found
```

**important concepts in python**

**A** **dictionary** in python is a kind of list but instead of using indexes, we use alphanumeric keys.

**The** **get()** method allows you to retrieve a value from a dictionary and if the key is not found you can give a value to return by default country not found
