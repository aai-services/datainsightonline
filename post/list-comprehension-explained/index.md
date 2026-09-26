---
title: "List Comprehension Explained"
author: "Ebrima Sise"
date: 2022-05-04
description: "Imagine you have a list named `prices` belowprices = [20, 25, 35, 40, 45, 70]And you want to implement a 5% discount on all the prices because of a promotion you are currently doing. Let's say you..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/list-comprehension-explained
---
Imagine you have a list named `prices` below

```python
prices = [20, 25, 35, 40, 45, 70]
```

And you want to implement a 5% discount on all the prices because of a promotion you are currently doing.
Let's say you have tens of thousands of products and the prices list above is just a subset of that price list. The computational time to execute this task will be high when you use the traditional for loops.

That is why we will discuss an alternative to for-loops called list comprehension. It's more compact syntactically and easier to follow. Also, it is more efficient in the runtime. But don't take my word for it, we will go through it together and you will see for yourself!

Back to our problem of fixing the discounted prices. We will begin with the traditional for loop.

```python
new_prices = []

for price in prices:
    discount = 0.05 * price # 5% discount
    price -= discount
    new_prices.append(price)

print(new_prices)
```

```python
output: [19.0, 23.75, 33.25, 38.0, 42.75, 66.5]
```

As you can see, there are about six lines of code to accomplish this simple task. We will now imitate this using the list comprehension logic and compare it at the end of the tutorial.

```python
lc_new_prices = [(price - (price * 0.05)) for price in prices]
```

```python
print(lc_new_prices)
```

```python
output: [19.0, 23.75, 33.25, 38.0, 42.75, 66.5]
```

Just two lines of code are able to accomplish exactly the same thing in List Comprehension! Isn't that amazing?
This is the reason it is advisable to avoid using traditional for-loops as much as possible.
There are times though when it is advisable to use the traditional for loops instead of the list comprehension. One such scenario could be when there is a need for a nested for-loop. Things can get pretty complicated when you try to use list comprehension for this.
The general syntax for list comprehension can be as follows:

Everything is in square brackets, []

- inside the square brackets, the first expression is the returned value
- Then followed by the expression for variable in list

  - Where variable can be named anything and list can be any list name variable.

### Runtime Efficiency

Now, we will check the efficiency of these two methods by running them in a function.

I will name the function, loop_efficiency1, and loop_efficiency2 to compare their runtimes.

```python
def loop_efficiency1(list):
    new_prices = []

    for price in list:
        discount = 0.05 * price # 5% discount
        price -= discount
        new_prices.append(price)

    return new_prices
```

Now that we implemented the first logic in a function, let's run the function to make sure that we are getting the same results.

```python
loop_efficiency1(prices)
```

```python
output: [19.0, 23.75, 33.25, 38.0, 42.75, 66.5]
```

Let's do the same for the list comprehension logic using the function named `loop_efficiency2`

```python
def loop_efficiency2(list):
    lc_new_prices = [(price - (price * 0.05)) for price in list]
    return lc_new_prices
```

Again, let's test it on the `prices` list to make sure we are getting the same results.

```python
loop_efficiency2(prices)
```

```python
output: [19.0, 23.75, 33.25, 38.0, 42.75, 66.5]
```

Great! Both functions work perfectly. We will now test their runtime efficiency

```python
%timeit loop_efficiency1(prices)
```

```python
output: 3.69 µs ± 1.37 µs per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

```python
%timeit loop_efficiency2(prices)
```

```python
output: 3.29 µs ± 762 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

The time it took for the traditional loop to run is 3.69 microseconds while the list comprehension only took 3.29 microseconds!

Though the slightly minimal difference, in this case, the latter still outperforms the former on that front as well.

### Final Thought

Avoid using traditional loops as much as possible and only use them when it is absolutely necessary.
