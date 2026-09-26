---
title: "Python concepts: Classes"
author: "Hamza kchok"
date: 2021-10-06
description: "Hello there, I guess this is your chance of discovering the OOP side of python. Oh wait? what's OOP? Object-Oriented Programming is an approach that focuses on using objects and classes as same as..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-classes
---
Hello there,
I guess this is your chance of discovering the OOP side of python. Oh wait? what's OOP? **Object-Oriented Programming** is an approach that focuses on using objects and classes as same as other general programming languages. This mainly allows for really efficient reusability and It is very easy to create classes and objects in Python. "Wait... Classes and objects? But I don't know what you're talking about".
Well dear reader, hop along this mini-journey to discover what I am talking about.

#### Class definition

First, let's begin with **classes.** The easiest way to describe classes is to compare them to "blueprints". Before you build a house, what do you do? Make a blueprint! Before you make an electronics device what do you do? Yes, you make a blueprint! The blueprint in essence describes 3 things:

What are its attributes: The attributes are what describes the class. For example, a coffee maker has a certain amount of water and ground coffee.

What are its methods: The methods are the functions that the class holds, like a coffee maker, it **makes** coffee following some steps.

Let's see how this is done in python.

```python
class class1(object):
    'This is a class showing a basic definition squeleton in OOP'
    def __init__(self):
        print('this is my constructor, am now a class 1 object!')
        self.value1 = 'value 1'
        self.value2 = 2

    def show_my_attributes(self):
        print('this is value 1: "{}"'.format(self.value1))
        print('this is value 2: "{}"'.format(self.value2))

    def method_to_inherit(self,x):
        print('this is class1 displaying a value: {}<a'.format(x))

    def method_to_change(self):
        print('This method will be changed later')
```

Okay first things first, we keep seeing a lot of **self** keywords in the code. Well, that is a pointer. wait, a what? Just like after making the blueprint, we start building the house. For a class, an object is born later on. and to keep track of every object out there and not mess up different houses with everyone's furniture, we use the **self** pointer to say, "that's **my** attribute"

Also, there is the "__init__" part at the start of the code. That's we start describing what the class should have and eventually do. It's called **initialization.** It takes place when an object is being made. For example, the coffee maker would check its water and coffee, note it down, and heat the water before waiting for you to choose when should that much-needed coffee be made.

Finally, we can see some attributes like value1 and value2 being saved and some defined methods (although the methods' names are suggesting we will get to the fun part soon). Let's see how we can make an object and check its behavior

```python
c = class1()
print('_____________________________________________')
c.show_my_attributes()
print('_____________________________________________')
c.method_to_inherit(50)
print('_____________________________________________')
c.method_to_change()

""" The output
this is my constructor, am now a class 1 object!
_____________________________________________
this is value 1: "value 1"
this is value 2: "2"
_____________________________________________
this is class1 displaying a value: 50<a
_____________________________________________
This method will be changed later
"""
```

As you can see, it's fairly simple to use, hence the reason it was made. You can imagine how for much bigger classes this can simplify things.

#### Inheritance

Now let's think about this case for a while, say we have 10 houses but each with small differences, Couldn't we make a general blueprint which we can easily copy 10 times and then add the small differences to each? Well, yes we can!

This is where we get to the "reusability" part, This is called inheritance. Basically just like we inherit traits from our parents, **Child** Classes inherit the attributes and methods of **Parent** classes.

Let's see how that can happen, we'll make a child class called **class2**  and see how it behaves:

```python
class class2(class1):
    def __init__(self):
        super().__init__()
        print('After getting the attribute of my main class I can add other ones that are mine')
        self.value3 = 3

    def method_to_change(self):
        print('This class has changed me!')


d = class2()
print('_____________________________________________')
d.method_to_inherit(30)
print('_____________________________________________')
d.show_my_attributes()
print('_____________________________________________')
d.method_to_change()

""" The output
this is my constructor, am now a class 1 object!
After getting the attribute of my main class I can add other ones that are mine
_____________________________________________
this is class1 displaying a value: 30
_____________________________________________
this is value 1: "value 1"
this is value 2: "2"
_____________________________________________
This class has changed me!
"""
```

Okay, so we can notice some things here.

**class class2(class1):** The **class1** argument is how we specify the parent class. Also note that we can inherit multiple classes as such:
**class3(class1,class2,class_x,[other_classes])**

First, when we called the "super().__init__()", we ran the parent class constructor, that way we can do the same initialization the parent class goes through without rewriting it. Moreover, we can add other behaviors to follow that like adding a new attribute **value3**.

We can easily call the **class1** methods through our **class2** object. But, in certain cases we want the behavior of a certain method to change. Let's say I want an automatic garage instead of a manual one. Well back in the code snippet I just showed you, check the output "**method_to_change"** in the parent class vs the output in the child class. As you can see, we can totally **Override** any method we want to adapt to the child class.

**Operator Overload and predefined attributes**

Finally, I'll go through the first part which is the attributes that come with the class.

- **__dict__** − Dictionary containing the class's namespace.
- **__doc__** − Class documentation string or none, if undefined.
- **__name__** − The class name.
- **__module__** − Module name in which the class is defined. (for example: __main___)
- **__bases__** − This contains the list of base classes (if any)

You can check their outputs in the jupyter notebook included else it's gonna be a mess in here. We wouldn't want that, would we?

So, let's say we have some operations that we want to change for example the "+" operator of our new defined classes. Can we do that?
Again, you guess right, yes we can!

Check this code snippet showing how we can change addition to fit our class's needs

```python
class numbers(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return numbers(self.a + other.a,self.b + other.b)

first = numbers(5,2)
second = numbers(6,8)
new = first + second
print('These are the new attributes: a:{} b:{}'.format(new.a,new.b))

""" The output
These are the new attributes: a:11 b:10
"""
```

In this case, the addition was changed to adding the attributes to each other when adding two created objects. But there are other operators that we can overload like subtraction, division, etc...

I hope reading this article was worth your time. You can check the notebook at this [link](https://github.com/zqngetsu96/DataInsight_Assignments_and_projects/blob/main/Assignment%202/Python%20Classes.ipynb).

Thank you for your time.
