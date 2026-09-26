---
title: "Classes in python"
author: "Wilson Waha"
date: 2022-05-06
description: "A mold is an object that always produces elements of the same shape. In the same way a class is a container which allows to create elements of the same form called objects. As we can create a cake..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/classes-in-python-1
---
A mold is an object that always produces elements of the same shape. In the same way a class is a container which allows to create elements of the same form called objects. As we can create a cake from a mold, we can also create objects (class instances) from a class. A class can have properties that describe it and method that give it behavior.

```python
class student_info:
    """
    This class contains necessary informations about a student
    """

    student_id = ""
    firstname = ""
    lastname = ""
    grade = ""
    school = ""
    faculty =""

    # constructor
    def __init__(self,s_id,fn,ln,grade, sh, fa):

        self.student_id = s_id
        self.firstname = fn
        self.lastname = ln
        self.grade = grade
        self.school = sh
        self.faculty = fa


    # methods to access informations about a student (getters)

    def get_student_id(self):
        return self.student_id

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname


    def get_grade(self):
        return self.grade

    def get_school(self):
        return self.school

    def get_faculty(self):
        return self.faculty

    # Method to modify student information (setter)

    def set_student_id(self,st_id):
        self.student_id = st_id

    def set_firstname(self,firstN):
        self.firstname = firstN

    def set_lastname(self,lastN):
        self.lastname = lastN


    def set_grade(self,grad):
        self.grade = grad

    def set_school(self,sch):
        self.school = sch

    def set_faculty(self,fac):
        self.faculty = fac
```

Illustration: we create two instances of class student

```python
in: stud1 = student_info("DI2122S82","Adama", "wilson", 5, "dataInsight","computer science")
stud2 = student_info("DI2122S04", "Traore", "Lucas", 2, "DataInsight", "Mathematics")
```

we get some information about stud1

```python
in: stud1.get_student_id(), stud.get_school(), stud.get_faculty(), stud.get_firstname(), stud.get_lastname()
```

```python
out: ('DI2122S82', 'dataInsight', 'computer science', 'Adama', 'wilson')
```

We modify the id of stud1

```python
in: stud1.set_student_id("DI212265")
```

Access to the new id of stud1

```python
in: stud1.get_student_id()
```

```python
out: 'DI212265'
```
