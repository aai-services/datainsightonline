---
title: "Let's deal with some text data"
author: "Hamza kchok"
date: 2022-05-08
description: "Back in recent posts, I mentioned one indisputable fact about the current machine learning models. They deal with numbers. In the case of images, they digitally exist as matrices of numbers (pixel..."
categories: ["General"]
image: images/56dba0_38e2d91131e14db7a021c87abfffa64d.webp
wix-url: https://www.datainsightonline.com/post/let-s-deal-with-some-text-data
---
Back in recent posts, I mentioned one indisputable fact about the current machine learning models. They deal with **numbers**. In the case of images, they digitally exist as matrices of numbers (pixel intensity ranging from 0-1 or 0-255). **They don't understand string variables**, Boolean variables (unless encoded as 0-1), or categorical variables. The input is always numbers. That's why we come up with **preprocessing steps** to manage this.

Now you'd say, hey wait google translation AI takes text as input. That's true. Well, partially true. It preprocesses the text you feed it before running any inference on it. Just like preprocessing for other variables, **text data must be processed.**

This takes us to talk about a fairly hyped branch of AI: **Natural Language Processing**. This AI branch takes care of the analyzing and processing text data in hope to extract data from text files/datasets. Some applications include: Text summary, Sentiment classification, speech recognition, etc. The more the NLP field advances, the better a machine can interpret a human being.

In this blog we'll explore two parts of the NLP process:

- **Preprocessing text data:** This will include some tips and steps to take to prepare/preprocess the text data prior to transforming the data.
- **Transforming text data for model input:** This will include some variants of transformations for the text data to become interpretable by machine learning models.

#### I- Preprocessing text data.

**1- Lowercasing the data**:

If I were to ask you what's the different between "Word" and "word" in terms of understanding the word, chances are you'd say they're the same thing. To a machine that doesn't understand words, they aren't the same. One way to circumvent this is to simply ensure that all text is fed to the transformation steps as lowercase text only. This step helps eliminate any redundancy in words. To achieve this, this sample code is more than enough.

```python
text  = text.lower()
```

In a dataframe, you simple map this function to each row in the column of interest.

```python
df["text"] = df["text"].apply(lambda row: row.upper())
```

**2- Removing punctuation**

Punctuation is another source of extra "noise" in our data. They don't really add much value to the text data fed to the AI models. Even though for us, they are fairly important. Not only they don't serve any important roles, they add redundancies to the data. A simple example for this is "**WordA**" vs "**WordA,**". Just adding that comma will result in two different words when it comes to the transformation part.

In the string library of python, there is a property named **punctuation** that holds all the punctuation symbols.

```python
print(string.punctuation)
###OUTPUT###
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

Now, we could loop over all the text lines in our data and eliminate the symbols one by one. But, this solution lacks in both performance and elegance. This is where **Regex (Regular Expressions**) come into play.

Regular expressions denote patterns that we want to look for in our data. Let's say for example, we want to extract "**35.98**" from "**Distance: 35.98 km**". Our focus would be to look for the digits followed by a float points and other digits. This can be summarized in the following pattern "**\d+\.\d+**". **d+** means one or multiple(+) digits.

One starting point to better understand regex is to take a look at the [documentation](http://docs.python.org/3/library/re.html) of **re** library.

To achieve this, we need the **sub** function in the regex library. This function **replaces the matched patterns with a target value** in our text data. The code sample below shows how to remove punctuation from text data.

```python
new_text= re.sub(r'['+string.punctuation+']', '', text.lower())
print(new_text)
```

In the case of a dataframe, you can apply the same line of code to each row in the column of interest.

```python
df["text"] = df["text"].apply(lambda row: re.sub(r'['+string.punctuation+']', '', row.lower())
```

**3- Removing extra spaces**

Depending on the transformations to be applied after preprocessing your data, removing whitespaces could be a helpful step. Specially when using **ngrams (groups for words)** after **tokenizing** the text data. They could create faulty tokens. Removing extra spaces comes to the simple task of **replacing every two or more spaces with 1 space**. The process will ensure that there is only 1 space every two words.

```python
no_extra_space = re.sub(' +',' ',text)
```

As usual, for dataframes, you just use the **apply** function to the text in question.

**4- Removing stop words**

When it comes to extracting features from text data, you'll want to focus on extracting the most important information. A lot of words (in most languages or all even) are really common and don't hold a lot of value information-wise. These are known as **Stop words**. We can get a list of these words from the package **nltk** (**Natural Language ToolKit)**.

The code sample below shows the process of downloading the

```python
import nltk
nltk.download('stopwords')
stopword = stopwords.words('english')
print(stopword)
new_text = " ".join([word for word in str(text.lower()).split() if word not in stopword])
print(new_text)
```

As usual, for dataframes, you just use the **apply** function to the text in question.

This is an output sample from a paragraph I took from this blog post.

**Input:**

```python
If I were to ask you what's the different        between "Word" and "word" in terms of understanding _-_-_-_the word, chances are you'd say they're-- the same thing--. To a machine that doesn't *understand.. words, they aren't the same.  One way to circumvent this is to simply ensure that all text is fed to the transformation steps as lowercase text only. This step helps eliminate any redundancy in words. To achieve this, this sample code is more than enough
```

**Output after applying steps 1 to 4:**

```python
ask whats different word word terms understanding word chances youd say theyre thing machine doesnt understand words arent one way circumvent simply ensure text fed transformation steps lowercase text step helps eliminate redundancy words achieve sample code enough
```

As we can see, it removed a lot of noise. One thing to notice, that there are stop words that made it through. This is because when the punctuation was removed first, they didn't match the stop words list.

For the intermediate outputs of these code samples, you can check [the notebook.](https://github.com/zqngetsu96/DataInsight_Assignments_and_projects/blob/main/Bi-weekly-blog-codes/Processing%20text%20data.ipynb)

**II- Preparing the text features (Tokenizing)**

First let's create our new dataset. We'll be using the "Us Presidential Inauguration Addresses". We'll be applying to it the same steps we mentioned above combined in one function.

```python
def final_clean(row):
    row = " ".join([word for word in str(row.lower()).split() if word not in stopword])
    row = re.sub(r'['+string.punctuation+']', '', row)
    no_extra_space = re.sub(' +',' ',row)
    return row
```

Loading the data and cleaning it:

```python
text_df = pd.read_csv('inaugural_speeches.csv')

text_df['clean_text'] = text_df['text'].apply(lambda row: final_clean(row))
text_df.head()
```

One way (Can be seen as an intermediate step) of extracting the features from the text is to figure out the frequency of certain words in the text. This can be an important information to define the theme of the document or the sentiment in text. To achieve this, we make use of the **CountVectorizer** class in Scikit-Learn. The code sample below depicts how this can be done.

```python
 # Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Instantiate CountVectorizer
cv = CountVectorizer(min_df=0.1,max_df=0.9,stop_words='english',ngram_range=(1,3)) #Instantiate the Count Vectorizer
#min_df : the minimum frequency of words in dataset
#max_df : the maximum frequency of words in dataset
#stop_words: words to ignore (defined above in post)
#ngram_range: check explanation below code sample

# Fit the vectorizer
cv.fit(text_df['clean_text']) #Get the count of words in dataset
cv_transformed = cv.transform(text_df['clean_text']) #Transform the data into an array of word counts array
cv_array = cv_transformed.toarray() #Create numpy array of the values
# Print feature names
print(cv.get_feature_names()) #Get the list of the counted(relevant) words
cv_df = pd.DataFrame(cv_array,            columns=cv.get_feature_names()).add_prefix('Word_c_') #Create a dataframe from the array of words counts using the words as columns
```

That looks like a lot of code. But it can be summarized to the following steps.

1. **Create the CountVectorizer:** The **ngram_range** parameter explains the minimum and maximum combination of words to be counted. For example: "Word one" is a 2-gram feature.
2. **Feed it the dataset**
3. **Create a word count array:** The output is sparse (has a lot of zeros) array that holds the count of each word per row in the dataframe (the array shape is **(text_samples x counted words)**
4. **Create a dataframe using the output and counted words (optional, but used for verification purposes)**

**The output of the word counter can already be used as input for machine learning models**. But, the effect of **common words can end up skewing the data**. For mitigate the effect we can the **TF-IDF (Term Frequency - Inverse Document Frequency)** vectorizer instead.

This **TF-IDF Vectorizer** applies weights to words that are not that common to mitigate the skewing that can happen due to common words).

It works by applying the **Count Vectorizer as a first step** to the text data we processed and then **applies its transformation to de-skew the data.**

To steps to applying the TF-IDF are fairly similar to the ones we wrote for the Count Vectorizer.

```python
# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# Instantiate TfidfVectorizer
tv = TfidfVectorizer(stop_words='english',max_df=0.8,min_df=0.1,ngram_range=(1,3))

#min_df : the minimum frequency of words in dataset
#max_df : the maximum frequency of words in dataset
#stop_words: words to ignore (defined above in post)
#ngram_range: explained above

# Fit the vectroizer and transform the data
tv_transformed = tv.fit_transform(text_df['clean_text'])
#transform the text into features

# Create a DataFrame with these features
tv_df = pd.DataFrame(tv_transformed.toarray(),
                     columns=tv.get_feature_names()).add_prefix('TFIDF_') ##Create dataframe with words as columns and weights as rows
tv_df.head()
```

Feel free to check [the notebook](https://github.com/zqngetsu96/DataInsight_Assignments_and_projects/blob/main/Bi-weekly-blog-codes/Processing%20text%20data.ipynb) for the outputs. This is to keep the blog post crispy clean.

For now, that's all folks. I hope this article was worth reading and helped you acquire a new information.
