---
title: "Natural Language Processing (NLP) with Python"
author: "Mahmoud Morsy"
date: 2022-07-21
description: "NLP is an exciting branch of AI that allows machines to break down and understand human language. Data scientists may often use NLP techniques to interpret text data for analysis. Alice Zhao walks..."
categories: ["NLP", "Python"]
wix-url: https://www.datainsightonline.com/post/natural-language-processing-nlp-with-python
---
NLP is an exciting branch of AI that allows machines to break down and understand human language. Data scientists may often use NLP techniques to interpret text data for analysis. Alice Zhao walks you through text preprocessing techniques, machine learning techniques, and Python libraries for NLP.

Text preprocessing techniques include tokenization, text normalization, and data cleaning. Once in a standard format, various machine learning techniques can be applied to better understand the data. This includes using popular modelling techniques to classify emails as spam or not or to score the sentiment of a tweet on Twitter. Newer, more complex techniques can also be used, such as topic modelling, word embeddings, or text generation with deep learning.

> *The limits of my language means the limits of my world. - Ludwig Wittgenstein*

Computers speak their own language, the binary language. Thus, they are limited in how they can interact with us humans; expanding their language and understanding our own is crucial to set them free from their boundaries.

NLP is an abbreviation for natural language processing, which encompasses a set of tools, routines, and techniques computers can use to process and understand human communications. Not to be confused with speech recognition, NLP deals with understanding the meaning of words other than interpreting audio signals into those words.

If you think NLP is just a futuristic idea, you may be shocked to know that we are likely to interact with NLP every day when we perform queries in Google when we use translators online when we talk with Google Assistant or Siri. NLP is everywhere, and implementing it in your projects is now very reachable thanks to libraries such as NLTK, which provide a huge abstraction of the complexity.

**Tokenization**

NLTK is a huge library that provides a lot of different tools to work with language. While some functions are available with the library itself, some modules require additional downloads. Punkt is a module to work with tokenization, which is the process of separating a paragraph into chunks or words, and it’s usually a first step in the process of text analysis. Before starting, make sure you download the module

```python
import nltk
nltk.download('punkt')
```

Now, let’s see it in action

```python
from nltk.tokenize import word_tokenize
Text = "Good morning, How you doing? Are you coming tonight?"Tokenized = word_tokenize(Text)
print(Tokenized)
```

Output

```python
['Good', 'morning', ',', 'How', 'you', 'doing', '?', 'Are', 'you', 'coming', 'tonight', '?']
```

This first function, word_tokenize will split a text into words and symbols, however, there’s more you can do with Punkt, such as separating a paragraph into sentences.

```python
from nltk.tokenize import sent_tokenize
Text = "Good morning, How you doing? Are you coming tonight?"Tokenized = sent_tokenize(Text)
print(Tokenized)
```

Output

```python
['Good morning, How you doing?', 'Are you coming tonight?']
```

If the first example wasn’t very impressive, this one definitely is. Here we start seeing a much more intelligent method that tries to split the text into simpler meaningful chunks.

**Stop words**

A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query. It’s important in certain situations to ignore such words, and thus having a dictionary of them can become really handy, especially when we need to deal with multiple languages. NLKT provides a module to work with step words, let’s download it next:

```python
import nltk
nltk.download('stopwords')
```

Stop words is a simple list of words, so we can operate with it very easily, for example by writing a small routing to get a list of words without stop words in it:

```python
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
Text = ["Good", "morning", "How", "you", "doing", "Are", "you", "coming", "tonight"]
for i in Text:
   if i not in stopwords:
       print(i)
```

Output:

```python
Good
morning
How
Are
coming
tonight
```

Since we are given a simple list of words, we can simply print it to see all of them for a particular language:

```python
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
print(stopwords)
```

**Stemming Words**

A word stem is the base or root form of a word, for example, the word “loving” has roots in the word “love”, or being” on the word “be”. Stemming is the process to which we transform a given word into its stem word. This is a very complex task to do, words can be written in many forms, and different words have different ways to get their stem. Thankfully, NLTK makes it really easy for us to achieve this, let’s see how:

```python
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["Loving", "Chocolate", "Retrieved", "Being"]
for i in words:
   print(ps.stem(i))
```

Output

```python
love
chocol
retriev
be
```

This simplification of a word can be very helpful in search engines to prevent different ways of writing the same word to be ignored on the search criteria.

**Counting Words**

Counting how many times each word appears can be very helpful in the context of text analysis. NLTK provides us a neat method to calculate the frequency of words in a text called FreqDist.

```python
import nltk
words = ["men", "teacher", "men", "woman"]
FreqDist = nltk.FreqDist(words)
for i,j in FreqDist.items():
   print(i, "---", j)
```

Output:

```python
men --- 2
teacher --- 1
woman --- 1
```

###### Word groups
Oftentimes we see some words being used together to give a specific meaning, for example, “let’s go”, “best performance” and others. In text analysis it is important to capture these words as pairs as seeing them together can make a big difference in the comprehension of the text.

**Bigrams**

NLTK provides a few methods to do exactly that, and we will start with bigrams, which is a method to extract pairs of connected words:

```python
words = "Learning python was such an amazing experience for me"word_tokenize = nltk.word_tokenize(words)
print(list(nltk.bigrams(word_tokenize)))
```

Output

```python
[('Learning', 'python'), ('python', 'was'), ('was', 'such'), ('such', 'an'), ('an', 'amazing'), ('amazing', 'experience'), ('experience', 'for'), ('for', 'me')]
```

Similarly, we can do the same for 3 words and more:

**Trigrams**

Bigrams are the two words that occur together always but trigrams are the same as bigrams but with three words and there is almost no difference in the code:

```python
words = "Learning python was such an amazing experience for me"print(list(nltk.trigrams(word_tokenize)))
```

Output

```python
[('Learning', 'python', 'was'), ('python', 'was', 'such'), ('was', 'such', 'an'), ('such', 'an', 'amazing'), ('an', 'amazing', 'experience'), ('amazing', 'experience', 'for'), ('experience', 'for', 'me')]
```

**Ngrams**

The Ngrams are also some words or letters or symbols that appear together in a single phrase or document such as the previous two methods bigrams and trigrams but here you can specify the word's numbers. Let’s see an example:

```python
print(list(nltk.ngrams(word_tokenize, 4)))
```

Output

```python
[('Learning', 'python', 'was', 'such'), ('python', 'was', 'such', 'an'), ('was', 'such', 'an', 'amazing'), ('such', 'an', 'amazing', 'experience'), ('an', 'amazing', 'experience', 'for'), ('amazing', 'experience', 'for', 'me')]
```

Though with the presented text the results may not seem very impressive, there are many use cases where Ngrams can be effectively used, for example for spam detection.
