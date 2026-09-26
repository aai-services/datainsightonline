---
title: "File Handling in Python"
author: "Tahani Reesh"
date: 2021-10-06
description: "In Python, there are several methods for creating, reading, updating, and deleting files. In this post, we will learn how file operations in Python. More specifically, opening a file, reading from..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/file-handling-in-python
---
In Python, there are several methods for creating, reading, updating, and deleting files. In this post, we will learn how file operations in Python. More specifically, opening a file, reading from that file, writing into that file, closing the file.

In this file handling , we will learn:

- How to Open a Text File in Python
- How to Write a Text File in Python
- How to Append to a File in Python
- How to Create a Text File in Python
- How to Close Files in Python

## 1. open() function and different modes
We use **open ()** function in Python to open a file in read or write mode.

This function returns a file object, also called a handle, as it is used to read or modify the file accordingly. However, in order to perform a particular operation, we have to have to specify the mode in which we within the open function.

**The syntax :**

```python
file_object  = open("filename", "mode")
```

Below, I have listed the some important modes in Python:

- **r:** Opens a file for reading.
- **w:** Opens a file for writing. Creates a new file if it does not exist or resets the file if it exists.
- **a:** Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
- **w+**: Opens the file for both reading and writing.
- **b:** Opens in binary mode. We will come to this later.

In this example, the open command will open the file in the read mode

```python
# a file named "story", will be opened with the reading mode
File =open('story.txt','r')
```

## 2. Python file write() function

The file write() function writes a sequence of strings to the file. If the file has already content in there, then it will overwrite it.

```python
mainFile = 'add.txt'
file = open(mainFile, 'w')
file.write('AppDividend  \n')
```

## 3. Append to a File in Python
Let’s see how the append mode works:

```python
File = open(' text.txt','a')
File.write(" this will add this line")
file.close()
```

## 4. Create a new file in Python
We can also create a new file in Python. Let us see the following code.

```python
mainFile = 'new.txt'
file = open(mainFile, 'x')
```

The above code will create a new empty file called **new.txt.**

## 5. Close a File in Python
After performing the file operations, we can close that file by calling the **close()** function on that file

```python
mainFile = 'new.txt'
file = open(mainFile, 'x')
file.write('a file \n')
file.close()
```

The above code will create a new file called **new.txt** and add the content inside it and then write the content inside that file and close that file.

There are also various other functions that help to manipulate the files and its contents. One can explore various other functions in Python Docs.

Check out the code used here in [my GitHub](https://github.com/tahanijaber/Files_in_python). Thank you for reading!
