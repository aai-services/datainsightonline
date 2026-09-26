---
title: "Website Blocker App using Python"
author: "Tahani Reesh"
date: 2021-09-22
description: "Many people these days struggling with forcing on their work or study and easily distracted by Social media.And you will learn and build your own website blocker to block certain selected sites that..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/website-blocker
---
Many people these days struggling with forcing on their work or study and easily distracted by Social media.

And you will learn and build your own website blocker to block certain selected sites that distract you during working hours and be more productive

**Requirements**

First there are so some requirements . So we are going to use the **time** and **Datetime** Module only which comes by default with the Python Standard Library therefore you don’t need to install anything.

**How do we block sites?**

Every operating system has a host file and it’s on this file where we are going to add a list of websites we want to block by redirecting them to 127.0.0.1 (localhost).

We will add website URLs to the host file and mapping them to the localhost thus preventing you from accessing the real site during working hours.

For example:

Instead of adding [*www.youtube.com*](http://www.facebook.com/) we are going to add *127.0.0.1* [*www.youtube.com*](http://www.facebook.com/), therefore whenever a user tries to access the website during working hours will be directed to the localhost.

```python
if working_time:add mapped websites url to host fileelse:remove the website files from the host file
```

#### Location of host file

**Host file** that we need to edit is stored on different path depending on the Operating system you’re using

**For those in Linux**

```python
Linux_host = "/etc/hosts"
```

**For those in window**

```python
indow_host = r"C:\Windows\System32\drivers\etc\hosts"
```

**For those in Mac**

```python
MacOs_host = '/private/etc/hosts'
```

### Building our Website Blocker
Importing modules and pre-configuring

```python
import time

from datetime import datetime as dt

​sites_to_block = ['www.facebook.com',  'facebook.com','www.youtube.com', 'youtube.com','www.gmail.com', 'gmail.com']

​Linux_host = '/etc/hosts'
Window_host = r"C:\Windows\System32\drivers\etc\hosts"redirect = "127.0.0.1"
```

We then required to add the sites to be blocked during studying or working hours and remove them when it is not, that as shown in the source code below

```python
import time
from datetime import datetime as dt​

sites_to_block = ['www.facebook.com',  'facebook.com','www.youtube.com', 'youtube.com','www.gmail.com', 'gmail.com']
​Linux_host = '/etc/hosts'
MacOs_host = '/private/etc/hosts'
Window_host = r"C:\Windows\System32\drivers\etc\hosts"

default_hoster = Linux_host
redirect = "127.0.0.1"​

def block_websites(start_hour , end_hour):
       while True:
          if dt(dt.now().year, dt.now().month, dt.now().day,start_hour)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end_hour):
          print("Do the work ....")
          with open(default_hoster, 'r+') as hostfile:
          hosts = hostfile.read()
          for site in  sites_to_block:
             if site not in hosts:
               hostfile.write(redirect+' '+site+'\n')
  else:
           with open(default_hoster, 'r+') as hostfile:
           hosts = hostfile.readlines()
           hostfile.seek(0)
           for host in hosts:
              if not any(site in host for site in       sites_to_block):
               hostfile.write(host)
               hostfile.truncate()
               print('Good Time')time.sleep(3)​if __name__ == '__main__':block_websites(9, 12)
```

The function receives two-parameter, One is the starting time on which for testing I set as 9 am and the ending time for a job.

This can be helpful if you have a new year's resolution to consume less social media. and Good Luck!
