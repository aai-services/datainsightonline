---
title: "How Regularization Affects Training and Test Accuaracy Of A Logistic Regression Module."
author: "mrbenjaminowusu"
date: 2022-04-04
description: "In this blog, we will be discussing logistic regression classifier and how regularization affects the accuracy of its performance module.What is Logistic Regression?It is a classification algorithm..."
categories: ["Machine Learning"]
image: images/996a18_773ea33b3e1f49e6a452beaab6659467.webp
wix-url: https://www.datainsightonline.com/post/how-regularization-affects-training-and-test-accuaracy-of-a-logistic-regression-module
---
In this blog, we will be discussing logistic regression classifier and how regularization affects the accuracy of its performance module.

What is Logistic Regression?

It is a classification algorithm in machine learning that uses one or more independent variables to determine an outcome. The outcome results in two possible values 0 and 1. Although initially devised for two-class or binary response problems, this method can be generalized to multiclass problems. Logistic regression is the correct type of analysis to use when you’re working with binary data. A data is binary data when the output or dependent variable results in only two possible outcomes.

In this blog, we will be using the breast cancer dataset. The dataset has already been preprocessed. So there will not be any need for data cleansing. We import all the necessary libraries.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
```

We split our data into X_train, X_test, y_train, y_test and set the test size to 40% of our data We scale the breast cancer data so that features with large values do not unduly influence our model. Instantiate the logistic regression model and assign it to the variable *logreg.* Then we fit the training data into our module.

```python
X_train,X_test,y_train,y_test=train_test_split(scale(breast_cancer.data),breast_cancer.target,test_size=0.4,random_state=7)
logreg=LogisticRegression()
logreg.fit(X_train, y_train)
```

We print out the train and test scores.

```python
print("Training set score: {:.3f}".format(logreg.score(X_train, y_train)))
print("Test set score: {:.3f}".format(logreg.score(X_test, y_test)))
```

Output:

```python
Training set score: 0.99
Test set score: 0.97
```

The module produced quite a good performance, with training accuracy of 99% and testing accuracy of 97%. The training score is 2% higher than the testing score, which means it is likely we are overfitting. This problem leads us to regularization that combats overfitting by making the model coefficients smaller.

What is Regularization

Regularization is a technique used to reduce errors by fitting the function appropriately on the given training set to avoid overfitting. we can think of regularization as a penalty against complexity. Increasing the regularization strength penalizes larger weight coefficients. We do not want the model to memorize and reproduce the same results from the training dataset. We want a model that generalizes well to new, unseen data.

In scikit-learn, the logistic regression module has a hyperparameter "C" which is the inverse of the regularization strength. Therefore a large C value means less regularization and a small C value means more regularization.

Let's now examine how regularization influences the accuracy of training and test dataset. With the Breast Cancer dataset already split into training and test. We instantiate two logistic regression models. The first with weak regularization by setting the hyperparameter C to 100. The other a with strong regularization by setting the hyperparameter C to 0.001. We then fit both models. Next, we compute training and test accuracies for both weak regularization(C=100) and strong regularization( C=0.001)

Weak regularization:

```python
logreg_100=LogisticRegression(C=100)
logreg_100.fit(X_train, y_train)
print("Training set score: {:.2f}".format(logreg_100.score(X_train, y_train)))
print("Test set score: {:.2f}".format(logreg_100.score(X_test, y_test))
```

Output:

```python
Training set score: 1.00
Test set score: 0.96
```

Strong regularization:

```python
logreg_001=LogisticRegression(C=0.001)
logreg_001.fit(X_train,y_train)
print("Training set score: {:.2f}".format(logreg_001.score(X_train, y_train)))
print("Test set score: {:.2f}".format(logreg_001.score(X_test, y_test)))
```

The model with weak regularization (C= 100) gets a higher training. accuracy. When we add regularization, we're modifying the loss function to penalize large coefficients, which distracts from the goal of optimizing accuracy. The larger the regularization penalty (or the smaller we set C), the more we deviate from our goal of optimizing training accuracy. Hence, training accuracy goes down.

Now looking at the test scores, we can observe that regularization has improved it. But why does it improve test accuracy? Let's imagine not having access to a particular feature; that's like setting the corresponding coefficient of the feature to zero. Regularizing is like a compromise between not using the feature at all and fully using it.

There are also different kinds of regularization like the Lasso and Ridge which this blog does not cover.

References

[DataCamp Linear Classifiers Course](https://campus.datacamp.com/courses/linear-classifiers-in-python/logistic-regression-3?ex=1)

[How to Identify Overfitting Machine Learning Models in Scikit-Learn (machinelearningmastery.com)](https://machinelearningmastery.com/overfitting-machine-learning-models/)

The code in this blog was written in my [Github repository](https://github.com/Storerun/log_reg/blob/main/logistic_reg.ipynb).

Do connect with me on [LinkedIn](https://www.linkedin.com/in/benjamin-owusu-a8a676218/)

Photo by [Annie Spratt](https://unsplash.com/@anniespratt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/logistic-regression?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
