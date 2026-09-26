---
title: "Conversations Development using Advanced NLP techniques"
author: "Omar Mohamed"
date: 2022-06-10
description: "IntroductionHello and welcome to a new descriptive detailed tutor about the ParlAI code. ParlAI is a Dialog Research Software Platform, introducing ParlAI, an open-source software platform for dialog..."
categories: ["NLP"]
image: images/c4edc8_7001564236b24a90b137b48f7a0a835c.webp
wix-url: https://www.datainsightonline.com/post/conversations-development-using-advanced-nlp-techniques
---
##### Introduction

Hello and welcome to a new descriptive detailed tutor about the ParlAI code. ParlAI is a Dialog Research Software Platform, introducing ParlAI, an open-source software platform for dialog research implemented in Python, available at http://parl.ai. Its goal is to provide a unified framework for sharing, training and testing of dialog models, integration of Amazon Mechanical Turk for data collection, human evaluation, and online/reinforcement learning; and a repository of machine learning models for comparing with others' models, and improving upon existing architectures. Over 20 tasks are supported in the first release, including popular datasets such as SQuAD, bAbI tasks, MCTest, WikiQA, QACNN, QADailyMail, CBT, bAbI Dialog, Ubuntu, OpenSubtitles and VQA. Several models are integrated, including neural models such as memory networks, seq2seq and attentive LSTMs. Generally, In this tutorial we will:

- Chat with a neural network model!
- Show how to use common commands in ParlAI, like inspecting data and model outputs.
- See where to find information about many options.
- Show how to fine-tune a pretrained model on a specific task.

And other things as well you can do with the large scale project ParlAI that aim to change the perception of NLPs.

Here is the Github [link](https://github.com/omarmohamed2011/DataCamp-ParlAI-tutor/blob/main/DataCamp21_6_10_ParlAI_Tutorial.ipynb).

![](images/c4edc8_7001564236b24a90b137b48f7a0a835c.webp)

##### Requirements

Install the packages required for the parlai.

```python
!pip install -q parlai
!pip install -q subword_nmt # extra requirement
```

This is going to take a little while, don't forget to use your gpu for later steps.

We can start now after having our requirements to try to use the model for chatting.

##### Model Chatting

We import the model interactive main and using it to answer questions, then taking a look at some data.
We can look at look into a specific dataset. Let's look into the "empathetic dialogues" dataset, which aims to teach models how to respond with text expressing the appropriate emotion. We have over existing 80 datasets in ParlAI.

```python
# Import the Interactive script
from parlai.scripts.interactive import Interactive

# call it with particular args
Interactive.main(
    # the model_file is a filename path pointing to a particular model dump.
    # Model files that begin with "zoo:" are special files distributed by the ParlAI team.
    # They'll be automatically downloaded when you ask to use them.
    model_file='zoo:tutorial_transformer_generator/model'
)

# The display_data script is used to show the contents of a particular task.

from parlai.scripts.display_data import DisplayData
DisplayData.main(task='empathetic_dialogues', num_examples=5)

>>> output:
- - - NEW EPISODE: empathetic_dialogues - - -
-I remember going to see the fireworks with my best friend. It was the first time we ever spent time alone together. Although there was a lot of people, we felt like the only people in the world.
=Was this a friend you were in love with, or just a best friend?
-This was a best friend. I miss her.
=Where has she gone?
-We no longer talk.
=Oh was this something that happened because of an argument? - - - NEW EPISODE: empathetic_dialogues - - -
-Was this a friend you were in love with, or just a best friend?
=This was a best friend. I miss her. Where has she gone?    We no longer talk.
21:19:45 | loaded 39057 episodes with a total of 64636 examples
```

We can instead ask to see fewer examples, and get them from the valid set.

```python
DisplayData.main(task='empathetic_dialogues', num_examples=3, datatype='valid')

>>> output:
- - - NEW EPISODE: empathetic_dialogues - - -
-Today,as i was leaving for work in the morning,i had a tire burst in the middle of a busy road. That scared the hell out of me!
=Are you fine now?
-Yeah,i'm doing alright now, but with minor injuries.    =Cool :) Is your car damaged a lot? - - -
NEW EPISODE: empathetic_dialogues - - -
-A few weeks ago, I was walking through my hallway, minding my own business, when all of a sudden a hand reached out from under a table and grabbed my ankle. I was so surprised. I thought i was got. Turns out, it was my son.
=That's funny, hope he didn't give you a heart attack.
21:19:49 | loaded 2769 episodes with a total of 5738 examples
```

##### Training a model

Well it's one thing looking at data, but what if we want to train our own model (from scratch)? Let's train a very simple seq2seq LSTM with attention, to respond to empathetic dialogues.

To get some extra performance, we'll initialize using GloVe embeddings, but we will cap the training time to 2 minutes for this tutorial. It won't perform very well, but that's okay.

```python
# we'll save it in the "from_scratch_model" directory
!rm -rf from_scratch_model
!mkdir -p from_scratch_model

from parlai.scripts.train_model import TrainModel
TrainModel.main(
    # we MUST provide a filename
    model_file='from_scratch_model/model',
    # train on empathetic dialogues
    task='empathetic_dialogues',
    # limit training time to 2 minutes, and a batchsize of 16
    max_train_time=2 * 60,
    batchsize=16,

    # we specify the model type as seq2seq
    model='seq2seq',
    # some hyperparamter choices. We'll use attention. We could use pretrained
    # embeddings too, with embedding_type='fasttext', but they take a long
    # time to download.
    attention='dot',
    # tie the word embeddings of the encoder/decoder/softmax.
    lookuptable='all',
    # truncate text and labels at 64 tokens, for memory and time savings
    truncate=64,
)
```

If you don't like the performance and thinking of a better BLEU score, we can finetune the model instead of training it from scratch.

```python
!rm -rf from_pretrained
!mkdir -p from_pretrained

TrainModel.main(
    # similar to before
    task='empathetic_dialogues',
    model='transformer/generator',
    model_file='from_pretrained/model',

    # initialize with a pretrained model
    init_model='zoo:tutorial_transformer_generator/model',

    # arguments we get from the pretrained model.
    # Unfortunately, these must be looked up separately for each model.
    n_heads=16, n_layers=8, n_positions=512, text_truncate=512,
    label_truncate=128, ffn_size=2048, embedding_size=512,
    activation='gelu', variant='xlm',
    dict_lower=True, dict_tokenizer='bpe',
    dict_file='zoo:tutorial_transformer_generator/model.dict',
    learn_positional_embeddings=True,

    # some training arguments, specific to this fine-tuning
    # use a small learning rate with ADAM optimizer
    lr=1e-5, optimizer='adam',
    warmup_updates=100,
    # early stopping on perplexity
    validation_metric='ppl',
    # train at most 10 minutes, and validate every 0.25 epochs
    max_train_time=600, validation_every_n_epochs=0.25,

    # depend on your gpu. If you have a V100, this is good
    batchsize=12, fp16=True, fp16_impl='mem_efficient',

    # speeds up validation
    skip_generation=True,

    # helps us cram more examples into our gpu at a time
    dynamic_batching='full',
)
```

We can now check the model prediction and check out how well it performs:

```python
from parlai.scripts.display_model import DisplayModel
DisplayModel.main(
    task='empathetic_dialogues',
    model_file='from_pretrained/model',
    num_examples=2,
    skip_generation=False,
)

>>> output:

[ warning: overriding opt['num_examples'] to 2 (previously: None )]
[ warning: overriding opt['skip_generation'] to False (previously: True )]
[ Using CUDA ]
Dictionary: loading dictionary from from_pretrained/model.dict
[ num words =  54944 ]
Total parameters: 87,508,992 (87,508,992 trainable)
[ Loading existing model params from from_pretrained/model ]
[creating task(s): empathetic_dialogues]
[EmpatheticDialoguesTeacher] Only use experiencer side? True, datatype: valid
- - - NEW EPISODE: empathetic_dialogues- -
- Today,as i was leaving for work in the morning,i had a tire burst in the middle of a busy road. That scared the hell out of me!
=labels: Are you fine now?
-model: oh no ! that ' s terrible ! did you get a new tire ? Yeah,i'm doing alright now, but with minor injuries.     =labels: Cool :) Is your car damaged a lot?
-model: that ' s good . i hope you are okay .
```

##### Final thoughts

In this tutorial we have discussed several Dialogue Conversational NLP applications using Parlai, beginning with chatting with a neural network model, going across showing how to use common commands in ParlAI, like inspecting data and model outputs, seeing where to find information about many options, and one more thing to show easily how to fine-tune a pretrained model on a specific task. I think of this as a very advantageable pipeline that you can use in not only empathetic dialogues but also in other temps. Hope you enjoyed this article and until next time
