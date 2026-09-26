---
title: "simple arithmetic calculator by python"
author: "Alaa Mohamed"
date: 2021-09-20
description: "Everyone need simple calculator in his daily life so in this program we calculate simple calculation like addition, subtraction …In this program I start by taking two number from the user and the..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/simple-arithmetic-calculator-by-python
---
![](images/3673b9_00ba85ce8e2247f79aa840fc8307e916.webp)

Everyone need simple calculator in his daily life so in this program we calculate simple calculation like addition, subtraction …

In this program I start by taking two number from the user and the operator that he need

```python
fnum=float(input("Enter Your First Number"))
snum=float(input("Enter Your Second Number"))
op=input("Enter Your Operator")
```

then I use if condition to calculate the Arithmetic operation :

\*addition operation:

```python
if op =="+":
add=fnum+snum
print("The Result is"+ str(add))
```

\*subtraction operation:

```python
elif op=="-":
sub=fnum-snum
print("The Result is"+ str(sub))
```

\*multiplication operation:

```python
elif op=="*":
multi=fnum*snum
print("The Result is"+ str(multi))
```

```python
*division operation:
```

```python
elif op=="/":
div=fnum/snum
print("The Result is"+ str(div))
```

\* reminder operation:

```python
elif op=="%":
rem=fnum%snum
print("The Result is"+ str(rem))
```

program code:

```python
fnum=float(input("Enter Your First Number"))
snum=float(input("Enter Your Second Number"))
op=input("Enter Your Operator")
if op =="+":
add=fnum+snum
print("The Result is"+ str(add))
elif op=="-":
sub=fnum-snum
print("The Result is"+ str(sub))
elif op=="*":
multi=fnum*snum
print("The Result is"+ str(multi))
elif op=="/":
div=fnum/snum
print("The Result is"+ str(div))
elif op=="%":
rem=fnum%snum
print("The Result is"+ str(rem))
```
