---
title: "Bill Splitter"
author: "aya abdalsalam"
date: 2022-01-09
description: "small game play it to go away form paying bill and make your friends pay for you randomly"
categories: ["General"]
image: images/d803c7_d969afc5ce3649628e098c4ed368534b.webp
wix-url: https://www.datainsightonline.com/post/bill-splitter
---
Eating With Your Friends is a beautiful Thing going and playing with them give you a power of the day and make you happy, but the bill is the big problem😂

So why not make small app that take one of your Friends randomly and make he or she the victim of the bill why not

Let's play🤝

```python
import random
class BillSplitter:
    def __init__(self):
        self.size = 0
        self.freinds = {}

    def check_numberOfFreinds(self):
        print("Enter the number of friends joining (including you):")
        self.size = int(input())
        if self.size <=0:
            print("No one is joining for the party")
        else:
            print("Enter the name of every friend (including you), each on a new line:")
            for i in range(self.size):
                x = input()
                self.freinds[x]= 0
            print()
            billValue = int(input("Enter the total bill value:"))
            print()
            luck = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
            print()
            if luck == "Yes":
                name = random.choice(list(self.freinds.keys()))
                print(name +" is the lucky one!")
                for key, value in self.freinds.items():
                    if key == name:
                        self.freinds.update({key: 0})

                everyOneValue = round(billValue/(self.size - 1), 2)
                for key, value in self.freinds.items():
                    if key != name:
                        self.freinds.update({key: everyOneValue})
                print(self.freinds)
                print()
            elif luck == "No":
                print("No one is going to be lucky")
                everSplitteryOneValue = round(billValue/self.size,2)
                for key, value in self.freinds.items():
                    self.freinds.update({key: everSplitteryOneValue})
                print(self.freinds)
BillSplitter().check_numberOfFreinds()
```

output:

case 1: use Luck method

```python
Enter the number of friends joining (including you):
2
Enter the name of every friend (including you), each on a new line:
aya
waleed

Enter the total bill value:300

Do you want to use the "Who is lucky?" feature? Write Yes/No:
Yes

aya is the lucky one!
{'aya': 0, 'waleed': 300.0}
```

```python
case 2: luck =No
```

```python
Enter the number of friends joining (including you):
2
Enter the name of every friend (including you), each on a new line:
aya
waledd

Enter the total bill value:400

Do you want to use the "Who is lucky?" feature? Write Yes/No:
No

No one is going to be lucky
{'aya': 200.0, 'waledd': 200.0}
```

let's discuss our app one part by one

First import **random**

we make a class **BillSplitter** which is the father of the project . To create a class we use the keyword **class**

Every class should has the __**init__**() method

The __**init__**() function is called automatically every time the class is being used to create a new object. The **Self** keyword refer to class variables and you can call it anything to need but self is the most.

we make a dictionary **freinds** to add to it every name of friends
