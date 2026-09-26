---
title: "Python Focus - A Simple Website Blocker App"
author: "Joana Owusu-Appiah"
date: 2021-09-22
description: "I doubt I'll keep track, but this is my second post here.For those who are easily sidetracked by social media and other websites, what if there was a method to keep your attention until after your..."
categories: ["Python"]
image: images/b8e7be_0e0ecedc91ba4f80be080a8da195416c.webp
wix-url: https://www.datainsightonline.com/post/python-focus-a-simple-website-blocker-app
---
![](images/b8e7be_0e0ecedc91ba4f80be080a8da195416c.webp)

I doubt I'll keep track, but this is my second post here.

For those who are easily sidetracked by social media and other websites, what if there was a method to keep your attention until after your potentially productive hours?

This application; a ***website blocker***, is fed a list of websites, given a time limit, and only enables the websites to load once the time limit has elapsed. The good news is that it can be accomplished with only a few lines of code. Let's get our hands dirty with some coding.

## **Tip**:

There is a file called host.txt. It is an operating system file that maps website hostnames to your computer's localhost addresses. The following commands can be used by Linux users to see the contents of their hosts.txt file:

```python
$$ cd /etc
$$ vim hosts
```

The following text or something close would be printed:

```python

# Host Database

# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.

127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost
```

The software writes the selected websites to the 'host.txt' file and 'stops' those websites from functioning in your browser until the specified period has passed.

For the code and its implementation, we begin by importing the requisite libraries.

```python
# run script as root
import time
from datetime import datetime as dt
```

Moving on to changing the path of the host and specifying the number of websites.

```python
# change hosts path
# this part is perculiar to one's OS
# mine is Linux

hosts_path = '/etc/hosts'

# localhost's IP
redirect = "127.0.0.1"

# websites that we want to block
website_list = ['wwww.facebook.com', 'facebook.com']
```

A while loop is used to establish the time for working hours at the start. As a result, the specified websites should be "ignored" when the program is active and the current time is inside work hours.

The subsequent 'else' statement that follows the code below, truncates or 'eliminates' the specified websites from the hosts.txt file, allowing them to run, after the time restriction has expired.

```python
while True:
    # time of work
    if dt(dt.now().year, dt.now().month, dt.now().day,8)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
      # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
```

Further work would enable the user to add items to a list via a user interface, as well as pick the number of hours needed away from the websites.

The entire notebook is available [here](https://github.com/Joana-Mansa/_website_blocker2).
