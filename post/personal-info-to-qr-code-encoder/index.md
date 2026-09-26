---
title: "Personal Info to QR Code Encoder"
author: "NaumanKhanKhattak"
date: 2021-09-22
description: "A QR code or Quick Response code is a type of matrix barcode or two-dimensional barcode invented in 1994 by the Japanese automotive company Denso Wave. A barcode is a machine-readable optical label..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/personal-info-to-qr-code-encoder
---
A **QR code** or **Quick Response code** is a type of matrix barcode or two-dimensional barcode invented in 1994 by the Japanese automotive company Denso Wave. A barcode is a machine-readable optical label that contains information about the item to which it is attached. In practice, QR codes often contain data for a locator, identifier, or tracker that points to a website or application. A QR code uses four standardized encoding modes (numeric, alphanumeric, byte/binary, and kanji) to store data efficiently; extensions may also be used.

In this mini python project we will write a program to encode personal info into a QR Code.

**Step: 1**

Firstly, opening jupyter notebook and importing a qrcode library for ***QR*** code generator.

```python
import qrcode
```

**Step: 2**

Secondly, we would take the inputs from user. For example, personal information. i,e name and id. Here in second line we can also force the user to enter the id in only numbers by just using int() function.

```python
your_name=input("Enter your name:")
your_id=input("Enter your id:")
```

**Step: 3**

Third, and most important step is to convert that info into a ***QR*** code with qrcode.make function and giving the information as a string. The second line in below cell takes input for a file name on which QR code image should be saved. The third line saves the QR code image with that filename through im.save() function.

```python
img = qrcode.make(your_name+":"+your_id)
f_name=input("Enter a name for QR image file must use the '.png' at the end.")
img.save(f_name)
```

**Step: 4**

Now if you want to show the ***QR*** code image, it could be done with img.show() function.

```python
img.show()
```

This is the end of a very simple QR Code generator program in python
