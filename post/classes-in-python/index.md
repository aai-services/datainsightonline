---
title: "Classes in Python"
author: "Thiha Naung"
date: 2021-09-26
description: "In Object-oriented Programming, classes are written, and based on these classes, objects are created. When creating objects based on these classes, each object is automatically equipped with the..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/classes-in-python
---
In **Object-oriented Programming, classes** are written, and based on these classes, **objects** are created. When creating objects based on these classes, each object is automatically equipped with the general behavior of the class and then, each object can be given unique characteristics as you wish.

For using classes that were created by other developers, there are two important concepts; **attributes** and **methods**. Attributes are characteristics or properties of the class; in other words, they are NOUNS. Methods are what they can do for; or functions that are belonged to that class; or in other words, they are VERBS.

For example, in the real-world, let's say you buy a car, the brand name, color, engine type, size of the cars are attributes. Driving the car or moving from one place to another is a method.

How can we create classes? Let's say, create a simple bank account class.

```python
class Account:
    """A simple bank account"""
    def __init__(self, owner, balance):
        """Initialize attributes to describe bank account"""
        self.owner = owner
        self.balance = balance
```

The **init()** method is a special method of Python that runs automatically whenever we create an object from that class. Making an object from a class is called **instantiation**. In this method, we have three parameters. The 'self' parameter is required in the method definition and it must come first before the others. Every method call associated with an instance passes the self and the individual instances access to the attributes and methods of that class. Let's create an account object.

```python
account_1 = Account('Michael', 1000)
```

**How can I access the attributes of that class?**

```python
account_1.owner
```

```python
'Michael'
```

```python
account_1.balance
```

```python
1000
```

Next, let's talk about **methods**. Methods are functions that are belonged to that class.

```python
class Account:
    """A simple bank account"""
    def __init__(self, owner, balance=0):
        """Initialize attributes to describe bank account"""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Successful! \nYour current balance is {self.balance}")

    def withdrawl(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Withdrawl Successful! \nYour current balance : {self.balance}")
        else:
            print("Funds Not Enough!")
```

In this example, I added two methods; deposit and withdrawal. Writing methods are the same as writing functions, but don't forget to add 'self'. So, what will the deposit do? I added the default balance to zero. When the 'deposit' method is called, it will add that amount to the balance and print the current balance. The withdrawal method will deduct the amount from the balance if the balance is more than the withdrawal amount. Else, it will print funds not enough. So, let's see action.

```python
# I will create second object.
account_2 = Account('John')
# I will pass only one parameter, as balance is default to zero.
account_2.owner
```

```python
'John'
```

```python
account_2.balance
```

```python
0
```

```python
# The balance is 0. Let's see withdrawl method works or not.
account_2.withdrawl(100)
```

```python
Funds Not Enough!
```

```python
# ok it works. Let's add some money.
account_2.deposit(1000)
```

```python
Deposit Successful!
Your current balance is 1000
```

```python
# add 1000 and balance is now 1000. Let's withdrwal some.
account_2.withdrawl(500)
```

```python
Withdrawl Successful!
Your current balance : 500
```

That's the basics of the classes. In Python we almost always use classes. Keep in mind, basic of the classes are attributes and methods. For example, in pandas, **index, columns, dtype, shape** are attributes and **groupby(), apply(), head(), describe()** are methods. This is just the introduction of the introduction of the classes.
