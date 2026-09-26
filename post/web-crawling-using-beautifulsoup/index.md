---
title: "Web Crawling using BeautifulSoup"
author: "Omar Mohamed"
date: 2022-07-15
description: "Hello everyone, hope that you're having a great time. Today we are going to talk about a very interesting yet crucial topic, that is Web Crawling, but before getting caught into details let's first..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/web-crawling-using-beautifulsoup
---
Hello everyone, hope that you're having a great time. Today we are going to talk about a very interesting yet crucial topic, that is Web Crawling, but before getting caught into details let's first put that definition into simple words. Simply, a Web Crawler, sometimes called a spider or Spider-Bot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web and that is typically operated by search engines for the purpose of Web indexing. It can be considered as a spider doing the research for you and providing you with every found detail. Regarding how it works, a Web crawler starts with a list of URLs to visit. As the crawler visits these URLs, by communicating with web servers that respond to those URLs, it identifies all the hyperlinks in the retrieved web pages and adds them to the list of URLs to visit until it visits every URL and collects the information needed. To help with that, there are some libraries like Beautiful Soup, let's get into that in details. But basically, Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping and web crawling. I do think we are now ready to get into our article as we know the basic info, and we have our notebook for it. Note that, this notebook is not mine, it's a part of a web scraping series by Rimetchell that I'd personally recommend, check out the link for the notebook [here](https://github.com/REMitchell/python-scraping/blob/master/Chapter03-web-crawlers.ipynb).

### Web Crawling

For web scraping to work in Python, we're going to perform three basic steps:

1. Extract the HTML content using the requests library.
2. Analyze the HTML structure and identify the tags which have our content.
3. Extract the tags using Beautiful Soup and put the data in a Python list and from which extracting and crawling the articles from the URLs.

Let's not waste our time and start to get our momentum going. We firstly import the library and have a url to crawl it.

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

>>>
/wiki/Wikipedia:Protection_policy#semi
#mw-head
#p-search
/wiki/Kevin_Bacon_(disambiguation)
/wiki/File:Kevin_Bacon_SDCC_2014.jpg
/wiki/San_Diego_Comic-Con
/wiki/Philadelphia
/wiki/Pennsylvania
/wiki/Kyra_Sedgwick
/wiki/Sosie_Bacon
/wiki/Edmund_Bacon_(architect)
/wiki/Michael_Bacon_(musician)
http://baconbros.com/
#cite_note-1
#cite_note-actor-2
/wiki/Footloose_(1984_film)
/wiki/JFK_(film)
/wiki/A_Few_Good_Men
/wiki/Apollo_13_(film)
/wiki/Mystic_River_(film)
/wiki/Sleepers
/wiki/The_Woodsman_(2004_film)
/wiki/Fox_Broadcasting_Company
/wiki/The_Following
/wiki/HBO
/wiki/Taking_Chance
/wiki/Golden_Globe_Award
/wiki/Screen_Actors_Guild_Award
/wiki/Primetime_Emmy_Award
/wiki/The_Guardian
/wiki/Academy_Award
#cite_note-3
/wiki/Hollywood_Walk_of_Fame
#cite_note-4
....
...
```

Let us try to understand this piece of code in brief.

- First of all import the requests library.
- Then, specify the URL of the webpage you want to scrape.
- Send a HTTP request to the specified URL and save the response from server in a response object called 'html'.
- Now, the link is iterated to get every information crawled from the URL.

If we check out the URL of Wikipedia page we can find a lot of sections to read from, this could lead to having a messy data, let's crawl into the Content only.

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

>>>
/wiki/Kevin_Bacon_(disambiguation)
/wiki/San_Diego_Comic-Con
/wiki/Philadelphia
/wiki/Pennsylvania
/wiki/Kyra_Sedgwick
/wiki/Sosie_Bacon
/wiki/Edmund_Bacon_(architect)
/wiki/Michael_Bacon_(musician)
/wiki/Footloose_(1984_film)
/wiki/JFK_(film)
/wiki/A_Few_Good_Men
/wiki/Apollo_13_(film)
/wiki/Mystic_River_(film)
/wiki/Sleepers
/wiki/The_Woodsman_(2004_film)
/wiki/Fox_Broadcasting_Company
/wiki/The_Following
/wiki/HBO
/wiki/Taking_Chance
/wiki/Golden_Globe_Award
/wiki/Screen_Actors_Guild_Award
/wiki/Primetime_Emmy_Award
/wiki/The_Guardian
/wiki/Academy_Award
/wiki/Hollywood_Walk_of_Fame
/wiki/Social_networks
/wiki/Six_Degrees_of_Kevin_Bacon
/wiki/SixDegrees.org
/wiki/Philadelphia
/wiki/Edmund_Bacon_(architect)
/wiki/Pennsylvania_Governor%27s_School_for_the_Arts
/wiki/Bucknell_University
/wiki/Glory_Van_Scott
/wiki/Circle_in_the_Square
/wiki/Nancy_Mills
/wiki/Cosmopolitan_(magazine)
/wiki/Fraternities_and_sororities
/wiki/Animal_House
/wiki/Search_for_Tomorrow
/wiki/Guiding_Light
/wiki/Friday_the_13th_(1980_film)
/wiki/Phoenix_Theater
/wiki/Flux
/wiki/Second_Stage_Theatre
/wiki/Obie_Award
/wiki/Forty_Deuce
/wiki/Slab_Boys
/wiki/Sean_Penn
/wiki/Val_Kilmer
/wiki/Barry_Levinson
/wiki/Diner_(film)
/wiki/Steve_Guttenberg
/wiki/Daniel_Stern_(actor)
/wiki/Mickey_Rourke
/wiki/Tim_Daly
/wiki/Ellen_Barkin
/wiki/Footloose_(1984_film)
/wiki/James_Dean
/wiki/Rebel_Without_a_Cause
/wiki/Mickey_Rooney
/wiki/Judy_Garland
/wiki/People_(American_magazine)
/wiki/Typecasting_(acting)
/wiki/John_Hughes_(filmmaker)
/wiki/She%27s_Having_a_Baby
/wiki/The_Big_Picture_(1989_film)
/wiki/Tremors_(film)
/wiki/Joel_Schumacher
/wiki/Flatliners
/wiki/Elizabeth_Perkins
/wiki/He_Said,_She_Said
/wiki/The_New_York_Times
/wiki/Oliver_Stone
/wiki/JFK_(film)
/wiki/A_Few_Good_Men_(film)
/wiki/Michael_Greif
/wiki/Golden_Globe_Award
/wiki/The_River_Wild
/wiki/Meryl_Streep
/wiki/Murder_in_the_First_(film)
/wiki/Blockbuster_(entertainment)
/wiki/Apollo_13_(film)
/wiki/Sleepers_(film)
/wiki/Picture_Perfect_(1997_film)
/wiki/Losing_Chase
/wiki/Digging_to_China
/wiki/Payola
/wiki/Telling_Lies_in_America_(film)
/wiki/Wild_Things_(film)
/wiki/Stir_of_Echoes
/wiki/David_Koepp
/wiki/Taking_Chance
/wiki/Paul_Verhoeven
/wiki/Hollow_Man
/wiki/Colin_Firth
/wiki/Rachel_Blanchard
/wiki/M%C3%A9nage_%C3%A0_trois
/wiki/Where_the_Truth_Lies
/wiki/Atom_Egoyan
/wiki/MPAA
/wiki/MPAA_film_rating_system
/wiki/Pedophile
/wiki/The_Woodsman_(2004_film)
/wiki/HBO_Films
/wiki/Taking_Chance
/wiki/Michael_Strobl
/wiki/Desert_Storm
/wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
/wiki/Matthew_Vaughn
/wiki/Sebastian_Shaw_(comics)
/wiki/Dustin_Lance_Black
/wiki/8_(play)
/wiki/Perry_v._Brown
/wiki/Proposition_8
/wiki/Charles_J._Cooper
/wiki/Wilshire_Ebell_Theatre
/wiki/American_Foundation_for_Equal_Rights
/wiki/The_Following
/wiki/Saturn_Award_for_Best_Actor_on_Television
/wiki/Huffington_Post
/wiki/Tremors_(film)
/wiki/EE_(telecommunications_company)
/wiki/United_Kingdom
/wiki/Egg_as_food
/wiki/Kyra_Sedgwick
/wiki/PBS
/wiki/Lanford_Wilson
/wiki/Lemon_Sky
/wiki/Pyrates
/wiki/Murder_in_the_First_(film)
/wiki/The_Woodsman_(2004_film)
/wiki/Loverboy_(2005_film)
/wiki/Sosie_Bacon
/wiki/Upper_West_Side
/wiki/Manhattan
/wiki/Tracy_Pollan
/wiki/The_Times
/wiki/Will.i.am
/wiki/It%27s_a_New_Day_(Will.i.am_song)
/wiki/Barack_Obama
/wiki/Ponzi_scheme
/wiki/Bernard_Madoff
/wiki/Finding_Your_Roots
/wiki/Henry_Louis_Gates
/wiki/Six_Degrees_of_Kevin_Bacon
/wiki/Trivia
/wiki/Big_screen
/wiki/Six_degrees_of_separation
/wiki/Internet_meme
/wiki/SixDegrees.org
/wiki/Bacon_number
/wiki/Internet_Movie_Database
/wiki/Paul_Erd%C5%91s
/wiki/Erd%C5%91s_number
/wiki/Paul_Erd%C5%91s
/wiki/Bacon_number
/wiki/Erd%C5%91s_number
/wiki/Erd%C5%91s%E2%80%93Bacon_number
/wiki/The_Bacon_Brothers
/wiki/Michael_Bacon_(musician)
/wiki/Music_album
/wiki/Golden_Globe_Awards
/wiki/Golden_Globe_Award_for_Best_Supporting_Actor_%E2%80%93_Motion_Picture
/wiki/The_River_Wild
/wiki/Broadcast_Film_Critics_Association_Awards
/wiki/Broadcast_Film_Critics_Association_Award_for_Best_Actor
/wiki/Murder_in_the_First_(film)
/wiki/Screen_Actors_Guild_Awards
/wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
/wiki/Apollo_13_(film)
/wiki/Screen_Actors_Guild_Awards
/wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Supporting_Role
/wiki/Murder_in_the_First_(film)
....
...
```

Data crawling is not limited to crawling info in a certain URL, but can also crawl info from all across a site, let's check this out.

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')

>>>
Main Page
<p>The <b><a href="/wiki/Finnish_Civil_War" title="Finnish Civil War">Finnish Civil War</a></b> (27 January – 15 May 1918) marked the transition from the <a href="/wiki/Grand_Duchy_of_Finland" title="Grand Duchy of Finland">Grand Duchy of Finland</a>, part of the <a href="/wiki/Russian_Empire" title="Russian Empire">Russian Empire</a>, to an independent state. Arising during <a href="/wiki/World_War_I" title="World War I">World War I</a>, it was fought between the Reds, led by the <a href="/wiki/Social_Democratic_Party_of_Finland" title="Social Democratic Party of Finland">Social Democratic Party</a>, and the Whites, led by the conservative <a href="/wiki/Senate_of_Finland" title="Senate of Finland">Senate</a>. In February 1918, the Reds carried out an unsuccessful offensive, supplied with weapons by <a class="mw-redirect" href="/wiki/Soviet_Russia" title="Soviet Russia">Soviet Russia</a>. A counteroffensive by the Whites began in March, reinforced by the <a href="/wiki/German_Empire" title="German Empire">German Empire</a>'s military detachments in April. The decisive engagements were the battles of <a href="/wiki/Battle_of_Tampere" title="Battle of Tampere">Tampere</a> and <a href="/wiki/Battle_of_Vyborg" title="Battle of Vyborg">Vyborg</a>, won by the Whites, and the battles of <a href="/wiki/Battle_of_Helsinki" title="Battle of Helsinki">Helsinki</a> and <a href="/wiki/Battle_of_Lahti" title="Battle of Lahti">Lahti</a>, won by German troops, leading to overall victory for the Whites and the German forces. The 39,000 casualties included <a class="mw-redirect" href="/wiki/Political_terror" title="Political terror">political terror</a> deaths. Although the Senate and Parliament were initially pressured into accepting the <a href="/wiki/Prince_Frederick_Charles_of_Hesse" title="Prince Frederick Charles of Hesse">brother-in-law</a> of German Emperor <a class="mw-redirect" href="/wiki/William_II,_German_Emperor" title="William II, German Emperor">William II</a> as the <a href="/wiki/Kingdom_of_Finland_(1918)" title="Kingdom of Finland (1918)">King of Finland</a>, the country emerged within a few months as an independent, democratic republic. The war would divide the nation for decades. (<a href="/wiki/Finnish_Civil_War" title="Finnish Civil War"><b>Full article...</b></a>)</p>
This page is missing something! No worries, we will continue!
--------------------
/wiki/Wikipedia
Wikipedia
<p><b>Wikipedia</b> (<span class="nowrap"><span class="IPA nopopups noexcerpt"><a href="/wiki/Help:IPA/English" title="Help:IPA/English">/<span style="border-bottom:1px dotted"><span title="/ˌ/: secondary stress follows">ˌ</span><span title="'w' in 'wind'">w</span><span title="/ɪ/: 'i' in 'kit'">ɪ</span><span title="'k' in 'kind'">k</span><span title="/ɪ/: 'i' in 'kit'">ɪ</span><span title="/ˈ/: primary stress follows">ˈ</span><span title="'p' in 'pie'">p</span><span title="/iː/: 'ee' in 'fleece'">iː</span><span title="'d' in 'dye'">d</span><span title="/i/: 'y' in 'happy'">i</span><span title="/ə/: 'a' in 'about'">ə</span></span>/</a></span><small class="nowrap"> (<span class="unicode haudio"><span class="fn"><span style="white-space:nowrap"><a href="/wiki/File:GT_Wikipedia_BE.ogg" title="About this sound"><img alt="About this sound" data-file-height="20" data-file-width="20" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/11px-Loudspeaker.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/17px-Loudspeaker.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/22px-Loudspeaker.svg.png 2x" width="11"/></a> </span><a class="internal" href="//upload.wikimedia.org/wikipedia/commons/0/01/GT_Wikipedia_BE.ogg" title="GT Wikipedia BE.ogg">listen</a></span></span>)</small></span> <a href="/wiki/Help:Pronunciation_respelling_key" title="Help:Pronunciation respelling key"><i title="English pronunciation respelling"><span style="font-size:90%">WIK</span>-i-<span style="font-size:90%">PEE</span>-dee-ə</i></a> or <span class="nowrap"><span class="IPA nopopups noexcerpt"><a href="/wiki/Help:IPA/English" title="Help:IPA/English">/<span style="border-bottom:1px dotted"><span title="/ˌ/: secondary stress follows">ˌ</span><span title="'w' in 'wind'">w</span><span title="/ɪ/: 'i' in 'kit'">ɪ</span><span title="'k' in 'kind'">k</span><span title="/i/: 'y' in 'happy'">i</span><span title="/ˈ/: primary stress follows">ˈ</span><span title="'p' in 'pie'">p</span><span title="/iː/: 'ee' in 'fleece'">iː</span><span title="'d' in 'dye'">d</span><span title="/i/: 'y' in 'happy'">i</span><span title="/ə/: 'a' in 'about'">ə</span></span>/</a></span><small class="nowrap"> (<span class="unicode haudio"><span class="fn"><span style="white-space:nowrap"><a href="/wiki/File:GT_Wikipedia_AE.ogg" title="About this sound"><img alt="About this sound" data-file-height="20" data-file-width="20" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/11px-Loudspeaker.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/17px-Loudspeaker.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/22px-Loudspeaker.svg.png 2x" width="11"/></a> </span><a class="internal" href="//upload.wikimedia.org/wikipedia/commons/4/4c/GT_Wikipedia_AE.ogg" title="GT Wikipedia AE.ogg">listen</a></span></span>)</small></span> <a href="/wiki/Help:Pronunciation_respelling_key" title="Help:Pronunciation respelling key"><i title="English pronunciation respelling"><span style="font-size:90%">WIK</span>-ee-<span style="font-size:90%">PEE</span>-dee-ə</i></a>) is a free <a href="/wiki/Online_encyclopedia" title="Online encyclopedia">online encyclopedia</a> with the mission of allowing anyone to edit articles.<sup class="reference" id="cite_ref-6"><a href="#cite_note-6">[3]</a></sup><sup class="noprint Inline-Template" style="white-space:nowrap;">[<i><a href="/wiki/Wikipedia:Verifiability" title="Wikipedia:Verifiability"><span title="The material near this tag failed verification of its source citation(s). (January 2018)">not in citation given</span></a></i>]</sup> Wikipedia is the largest and most popular general <a href="/wiki/Reference_work" title="Reference work">reference work</a> on the Internet,<sup class="reference" id="cite_ref-Tancer_7-0"><a href="#cite_note-Tancer-7">[4]</a></sup><sup class="reference" id="cite_ref-Woodson_8-0"><a href="#cite_note-Woodson-8">[5]</a></sup><sup class="reference" id="cite_ref-9"><a href="#cite_note-9">[6]</a></sup> and is ranked the fifth-most popular website.<sup class="reference" id="cite_ref-Alexa_siteinfo_10-0"><a href="#cite_note-Alexa_siteinfo-10">[7]</a></sup> Wikipedia is owned by the nonprofit <a href="/wiki/Wikimedia_Foundation" title="Wikimedia Foundation">Wikimedia Foundation</a>.<sup class="reference" id="cite_ref-11"><a href="#cite_note-11">[8]</a></sup><sup class="reference" id="cite_ref-12"><a href="#cite_note-12">[9]</a></sup><sup class="reference" id="cite_ref-13"><a href="#cite_note-13">[10]</a></sup></p>
This page is missing something! No worries, we will continue!
--------------------
/wiki/Wikipedia:Protection_policy#semi
Wikipedia:Protection policy
<p>Wikipedia is built around the principle that <a href="/wiki/Wiki" title="Wiki">anyone can edit it</a>, and it therefore aims to have as many of its pages as possible open for public editing so that anyone can add material and correct errors. However, in some particular circumstances, because of a specifically identified likelihood of damage resulting if editing is left open, some individual pages may need to be subject to technical restrictions (often only temporary but sometimes indefinitely) on who is permitted to modify them. The placing of such restrictions on pages is called <b>protection</b>.</p>
This page is missing something! No worries, we will continue!
...
```

It searches all pages that contains information, seeks all pages and checks if the page still exists though can be crawled, or does not exist anymore.

For more of a general crawling step, this code to crawl over the entire internet, it's an additional part.

```python
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#Retrieves a list of all Internal links found on a page
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

#Retrieves a list of all external links found on a page
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" that do
    #not contain the current URL
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,
                                    len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')
```

Having a random external link for that case.

### Final Thoughts

With the website content in a Python list, we can now do cool stuff with it. We could return it as JSON for another application or convert it to HTML with custom styling or even print the data or save it in a txt file. Thus, web crawling is very efficient for large scaled information seeking tasks.

### Data Resources

[Wikipedia](https://en.wikipedia.org/wiki/Web_crawler)

[GeekForGeeks](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
