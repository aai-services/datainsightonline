---
title: "Control flow (If, for loop, while loop) and List"
author: "Sakayo Toadoum Sari"
date: 2021-10-07
description: "If statementAn \"if\" statement tests a condition and then reacts to that condition. If the condition is true, the next action is performed. You can test several conditions at the same time and respond..."
categories: ["Python"]
image: images/b94828_cbf1d7cb253f4cc9bbf17da7e2df724c.webp
wix-url: https://www.datainsightonline.com/post/control-flow-if-for-loop-while-loop-and-list
---
### If statement
An "if" statement tests a condition and then reacts to that condition. If the condition is true, the next action is performed. You can test several conditions at the same time and respond appropriately to each one using "if" statement.

#### Example
```python
# A list of desserts I like.
desserts = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
favorite_dessert = 'apple crisp'

#Display the desserts and let others know my favourite.
for dessert in desserts:
    if dessert == favorite_dessert:
        # this dessert is my favorite, let everyone know!
        print("%s is my favorite dessert!" % dessert.title())
    else:
        # I like these desserts, but they are not my favourite.
        print("I like %s." % dessert)
```

```python
I like ice cream.
I like chocolate.
Apple Crisp is my favorite dessert!
I like cookies.
```

**What happens in this programme?**

- The program starts with a list of desserts, and one dessert is identified as a favourite.
- The for loop goes through all the desserts.
- Within the for loop, each item in the list is tested.

  - If the current value of the dessert is equal to the value of favorite_dessert, a message is printed indicating that this is my favorite dessert.
  - If the current value of dessert is not equal to the value of favorite_dessert, a message is printed indicating that I just like this dessert. You can test as many conditions as you like in an if statement.

**Logical test**

- equality (==)
- inequality (!=)
- other inequalities

  - greater than (>)
  - greater than or equal to (>=)
  - less than (<)
  - less than or equal to (<=)

- You can test if an element is in the list.

**Equality**

Two elements are equal if they have the same value. You can test for equality between numbers, strings and some objects that you will discover later. Some of these results can be surprising, so consider the examples below carefully.
In Python, as in many programming languages, two equal signs are used to test for equality.
Be careful! Be careful not to accidentally use a single equal sign, which can really mess things up, because that equal sign actually gives your object the value you are testing for!

```python
3 == 5

False

5 == 5.0
True

'eric' == 'eric'
True

'Eric' == 'eric'

False

'Eric'.lower() == 'eric'.lower()

True
```

**Inequality**

Two elements are unequal if they do not have the same value. In Python, we test the inequality by using the exclamation mark and the equal sign.

```python
3 != 5
True

5 != 5
False

'Eric' != 'eric'
True
```

#### Other inequalities

Other inequalities are: less, grater, grather or equal...

```python
5 > 3
True

5 >= 3
True

3 >= 3
True
```

#### Checking whether an item belongs to the list

We will use "in" to check whether an item belongs to the list or not

```python
vowels = ['a', 'e', 'i', 'o', 'u']
'a' in vowels

True

vowels = ['a', 'e', 'i', 'o', 'u']
'b' in vowels

False
```

**if-elif...else**

You can test any set of conditions, and you can test your conditions in any combination.

The simplest test has a single if statement, and a single statement to execute if the condition is true.

```python
dogs = ['willie', 'hootz', 'peso', 'juno']

if len(dogs) > 5:
    print("Wow, we have a lot of dogs here!")
```

Nothing happen here because the condition is not true.that there are no errors. The condition len(dogs) > 5 is evaluates to False, and the program skips to all lines after the if block.

```python
dogs = ['willie', 'hootz', 'peso', 'juno']

if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")

 Wow, we have a lot of dogs here!
```

**If-else condition**

Often you will want to answer a test in more than one ways. If the test is True, you will want to do one thing. If the test evaluates to false, you will want to do something else. The if-else structure allows you to do this easily. This is what it looks like:

```python
dogs = ['willie', 'hootz', 'peso', 'juno']

if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Ok, that's a reasonable number of dogs.")

Wow, we have a lot of dogs here!
```

```python
dogs = ['willie', 'hootz', 'peso', 'juno']

if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Ok, that's a reasonable number of dogs.")

Ok, that's a reasonable number of dogs.
```

Often you will want to test a series of conditions, rather than a simple "**or else**" situation. To do this, you can use a series of if-elif-else statements.

There is no limit to the number of conditions you can test. You always need an if statement to start the string, and you can never have more than one else statement. But you can have as many elif statements as you like.

dogs = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']

```python
if len(dogs) >= 5:
    print("Wow, we might open as well a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, that's a reasonable number of dogs.")

Wow, we might open as well a dog hostel!
```

It is important to note that in the situations like this, only the first test is evaluated. In an if-elif-else statement, when one test passes, the other conditions are ignored.

```python
dogs = ['willie', 'hootz', 'peso', 'monty']

if len(dogs) >= 5:
    print("Wow, we might open as well a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, that's a reasonable number of dogs.")

Wow, we might open as well a dog hostel!
```

```python
dogs = ['willie', 'hootz']

if len(dogs) >= 5:
    print("Wow, we might open as well a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, that's a reasonable number of dogs.")

Okay, that's a reasonable number of dogs.
```

**Boucle for**

The for loop statement is the most widely used iteration mechanism in Python.
Almost any structure in Python can be iterated (element by element) by a for loop
a list, a tuple, a dictionary...

```python
s = "Toadoum"
for i in s:
    print(i)

T
o
a
d
o
u
m
```

Python uses indentation to decide what is inside the loop and what is outside the loop. The code inside the loop will be executed for each item in the list. The code that is not indented, that comes after the loop, will be executed once, like normal code.

```python
chiens = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in chiens:
    print(dog)

border collie
australian cattle dog
labrador retriever
```

**Boucle While**

A while loop tests an initial condition. If this condition is true, the loop starts to run. Each time the loop ends, the condition is re-evaluated. As long as the condition remains true, the loop continues to execute. As soon as the condition becomes false, the loop stops executing.

- Every while loop needs an initial condition that need to be true to start.
- The while statement includes a condition to be tested.
- All the code in the loop runs as long as the condition remains true.
- As soon as something in the loop changes the condition so that the test no longer passes, the loop stops running.
- Any code defined after the loop will run at that point.

```python
# Player power starts at 5.
power = 5

# The player can continue to play as long as his power is greater than 0.
while power > 0:
    print("you are still playing, because your power is %d." % power)
    # The code for your game is here, and includes the challenges that make it
    # possible to lose power.
    # We can represent this by simply removing power.
    power = power - 1

print("No, your power is zero.")

you are still playing, because your power is 5.
you are still playing, because your power is 4.
you are still playing, because your power is 3.
you are still playing, because your power is 2.
you are still playing, because your power is 1.
No, your power is zero.
```

**Lists**

Python offers a range of compound data types often referred as sequences. List is one of the most frequently used and very versatile data types used in Python.

In Python programming, a list is created by placing all the items (elements) inside square brackets [], separated by commas.
It can have any number of items and they may be of different types (integer, float, string etc.).

```python
f="boujour maman comment vas-tu"
h=f.split()
print(f)

['boujour', 'maman', 'comment', 'vas-tu']
```

```python
# Selection of an element using indices
x = ["a", "b", "c", "d"]
x[1]

empty_list= []
```
