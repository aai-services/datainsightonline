---
title: "Fibonacci Sequence Generator using Python"
author: "Aldwin Dave Conahap"
date: 2021-09-19
description: "This blog post demonstrates how to generate a Fibonacci sequence in Python. Fibonacci sequence is a series of numbers wherein the numbers are the sum of its two preceding numbers, i.e.,It interests..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/fibonacci-sequence
---
This blog post demonstrates how to generate a Fibonacci sequence in Python. [Fibonacci sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html) is a series of numbers wherein the numbers are the sum of its two preceding numbers, i.e.,

It interests mathematicians as it appears in nature, e.g., in flower petals, galaxies, hurricanes, [etc](https://www.mathnasium.com/examples-of-the-golden-ratio-in-nature). It is named through the claimed discovery of famous Italian mathematician, [Leonardo Fibonacci](https://mathshistory.st-andrews.ac.uk/Biographies/Fibonacci/).

Now, let's generate a Fibonacci sequence using Python!

The following line of codes lets the user input a range. If the inputted range is not a positive integer, it lets the user try to input again.

```python
try:
    Range = int(input("Enter a range: 1 to "))

except ValueError:
    print("\nInvalid input! Please input a positive integer only.")
    Range = int(input("Enter a range: 1 to "))
```

Next, the program defines a function that performs the operations to generate the sequence. It defines variables 'previous_number' and 'current_number', and initiates its values to 0 and 1, respectively. After that, it creates a list where the succeeding numbers to append appears. Then, it runs in a loop up until the current value does not exceed the range inputted by the user. Followingly, it adds up the previous number and the current number to produce a new number to append in the sequence. It also creates a condition that determines whether the current number is still in range. Then, it returns the list of the Fibonacci sequence generated.

```python
def fibonacci(Range):
    previous_number, current_number = 0, 1

    fibonacci=[1,]

    while current_number < Range:

        previous_number += current_number
        current_number += previous_number

        fibonacci.append(previous_number)

        if current_number < Range:
            fibonacci.append(current_number)
        else:
            break

    return fibonacci
```

Lastly, the program calls the created function that executes to generate the sequence, and display the result.

```python
print("Sequence = " + str(fibonacci(Range)))
```

That is all! We have generated a Fibonacci sequence using Python.
