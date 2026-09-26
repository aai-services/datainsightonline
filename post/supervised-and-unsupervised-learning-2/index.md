---
title: "Supervised and Unsupervised Learning"
author: "James Owusu-Appiah"
date: 2022-06-30
description: "What Is Supervised Learning?A function that maps an input to an output is learned through supervised learning using sample input-output pairs. From labeled training data made up of a collection of..."
categories: ["Machine Learning"]
wix-url: https://www.datainsightonline.com/post/supervised-and-unsupervised-learning-2
---
## What Is Supervised Learning?
A function that maps an input to an output is learned through supervised learning using sample input-output pairs. From labeled training data made up of a collection of training instances, it infers a function. The two main types of supervised learning includes:

1. Classification
2. Regression

### Classification
A set of data is essentially divided into classes using the supervised learning concept of classification in machine learning. Speech recognition, face detection, handwriting recognition, document categorization, etc., are some of the most prevalent classification issues. The **3** main types of classification are:

1. **Binary classification:** This entails those classification tasks that entail just two class labels.
2. **Multiclass classification:** It is the problem of classifying instances into one of three or more classes.
3. **Multilabel classification:** It is a problem where in making predictions given an input may belong to more than one label.

The **5** algorithms for classification include:

1. **Logistic Regression:** One of two categories is produced by the analysis of independent variables to produce the binary outcome. The dependent variable is usually categorical, although the independent variables might be either category or quantitative.
2. **Naive Bayes:** Naive Bayes determines the likelihood that a data point falls into a particular category or not.
3. **K-Nearest Neighbors:** It is a pattern recognition algorithm that uses training datasets to find the k closest relatives in future examples.
4. **Decision Tree:** Categories inside categories are created, enabling organic classification with minimal human oversight.
5. **Support Vector Machines:** It uses tags for the data and then assigns a hyperplane that best separates the tags.

### Implementation Of Some Of The Algorithms In Code
### Logistic Regression
```python
#Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#Creating a pandas dataframe of age and have_insurance columns
df = pd.DataFrame({'age':[22, 29, 31, 35, 39, 18, 27, 45, 52, 70, 62, 89, 19, 44, 28, 37, 55, 49, 51, 77], 'bought_insurance' :[0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1]})

#Splitting data into train set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)

#Importing the logistic regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#Fitting the model with the training set
model.fit(X_train, y_train)

#Predicting for x_test with Logistic Regression model created
y_predicted = model.predict(X_test)

y_predicted
```

**Output:** array([1, 1, 1, 1])

### Naive Bayes
```python
#Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#Uploading file from local to google collab
from google.colab import files
files.upload()

#Reading the csv file
df = pd.read_csv("/content/titanic.csv")

#Dropping some columns
df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)

#Creating input and target variables
inputs = df.drop('Survived',axis='columns')
target = df.Survived

#Getting dummy values for sex column
dummies = pd.get_dummies(inputs.Sex)

#Merging dummies with the actual inputs
inputs = pd.concat([inputs,dummies],axis='columns')

#Leaving only the female column since it is enough to show the sex of the data
inputs.drop(['Sex','male'],axis='columns',inplace=True)

#Checking for any  column with missing values
inputs.columns[inputs.isna().any()]

#Filling missing age values with the mean age
inputs.Age = inputs.Age.fillna(inputs.Age.mean())

#Splitting data into test and split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)

#Creating the Naive Bayes classifier
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

#Training the model with the training dataset
model.fit(X_train,y_train)

#Predicting for X_test set
model.predict(X_test[0:10])
```

**Output:** array([1, 0, 1, 1, 1, 0, 0, 1, 0, 0])

### K-Nearest Neighbors
```python
#Importing the necessary libraries
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()

 #Loading data as a DataFrame
df = pd.DataFrame(iris.data,columns=iris.feature_names)

#Setting up the target column
df['target'] = iris.target

#Creating the flower_name column
df['flower_name'] =df.target.apply(lambda x: iris.target_names[x])

#Setting X and y values
X = df.drop(['target', 'flower_name'], axis='columns')
y = df.target

#Splitting data into train and test dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#Creating the KNN with 10 neighbors
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)

#Training the model with the training datasets
knn.fit(X_train, y_train)

#Predicting a value
knn.predict([[4.8,3.0,1.5,0.3]])
```

**Output:** array([0])

### Decision Tree
```python
#Importing pandas
import pandas as pd

#Importing from local to google colab
from google.colab import files
files.upload()

#Reading the salaries csv file
df = pd.read_csv("/content/salaries.csv")

#Setting the inputs and target variables
inputs = df.drop('salary_more_then_100k',axis='columns')
target = df['salary_more_then_100k']

#Using the Label Encoder preprocessing technique
from sklearn.preprocessing import LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

#Setting up the columns
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

#Dropping columns that will not be needed
inputs_n = inputs.drop(['company','job','degree'],axis='columns')

#Creating the Decision Tree Classifier model
from sklearn import tree
model = tree.DecisionTreeClassifier()

#Fitting model
model.fit(inputs_n, target)

#Predicting for new data
model.predict([[2,1,0]])
```

**Output:** array([0])

### Regression
Regression is a method for determining how independent features or variables relate to a dependent feature or result. It is used where an algorithm is needed to predict continuous outcomes. By anticipating the data, analyzing the time series, and identifying the causal impact relationships between the variables, his technique is typically utilized to predict the outputs. Some types of regression include:

1. **Linear Regression:** It comprises of two variables that are linearly related to one another: a predictor and a dependent.
2. **Ridge Regression:** It is used when usually there is a high correlation between independent variables since in case the collinearity is very high, there can be some bias value.
3. **Lasso Regression:** It performs regularization along with feature extraction.
4. **Polynomial Regression:** It is similar to multiple linear regression with a little modification. In polynomial regression, the relationship the dependent and independent variable is of the n-th degree.
5. **Bayesian Linear Regression:** It uses the Bayes theorem to find out the value of regression coefficients.

### Implementation Of Some of The Algorithms In Code
### Linear Regression
```python
#Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#Creating a pandas dataframe of area and their corresponding prices
df = pd.DataFrame({'area':[2600, 2950, 3120, 3500, 3925], 'price' :[550000, 565010, 615000, 680010, 724000]})

#Creating X values
X = df.drop('price', axis='columns')

#Creating Y values
Y = df.price

# Create linear regression object
reg = linear_model.LinearRegression()
reg.fit(X,Y)

#Predicting price of a home with area = 3350 sqr ft
reg.predict([[3350]])
```

**Output:** array([645511.26534448])

### Ridge Regression
```python
#Loading the Melbourne dataset
dataset = pd.read_csv('/content/Melbourne_housing_FULL.csv')

#Useful columns
cols_to_use = ['Suburb', 'Rooms', 'Type', 'Method', 'SellerG', 'Regionname', 'Propertycount', 'Distance', 'CouncilArea', 'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'Price']

dataset = dataset[cols_to_use]

#Columns to fill with 0 for missing values
cols_to_fill_zero = ['Propertycount', 'Distance', 'Bedroom2', 'Bathroom', 'Car']

#Filling columns with 0
dataset[cols_to_fill_zero] = dataset[cols_to_fill_zero].fillna(0)

#Filling landsize and building area columns with their mean values
dataset['Landsize'] = dataset['Landsize'].fillna(dataset.Landsize.mean())

dataset['BuildingArea'] = dataset['BuildingArea'].fillna(dataset.BuildingArea.mean())

#Dropping all missing values
dataset.dropna(inplace=True)

#Creating one hot encoding
dataset = pd.get_dummies(dataset, drop_first = True)

#Setting X and y values
X= dataset.drop('Price', axis=1)
y = dataset['Price']

#Splitting dataset into train and test with 30% test
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=2)

#Implementing L1 regularization with Lasso
from sklearn.linear_model import Ridge

ridge_reg = Ridge(alpha=50, max_iter=100, tol=0.1)

ridge_reg.fit(train_x, train_y)

#Checking score with test data
ridge_reg.score(test_x, test_y)

#Checking score with train data
ridge_reg.score(train_x, train_y)
```

**Output:**

0.6670848945194958

0.6622376739684328

### Lasso Regression
```python
#Loading the Melbourne dataset
dataset = pd.read_csv('/content/Melbourne_housing_FULL.csv')

#Useful columns
cols_to_use = ['Suburb', 'Rooms', 'Type', 'Method', 'SellerG', 'Regionname', 'Propertycount', 'Distance', 'CouncilArea', 'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'Price']

dataset = dataset[cols_to_use]

#Columns to fill with 0 for missing values
cols_to_fill_zero = ['Propertycount', 'Distance', 'Bedroom2', 'Bathroom', 'Car']

#Filling columns with 0
dataset[cols_to_fill_zero] = dataset[cols_to_fill_zero].fillna(0)

#Filling landsize and building area columns with their mean values
dataset['Landsize'] = dataset['Landsize'].fillna(dataset.Landsize.mean())

dataset['BuildingArea'] = dataset['BuildingArea'].fillna(dataset.BuildingArea.mean())

#Dropping all missing values
dataset.dropna(inplace=True)

#Creating one hot encoding
dataset = pd.get_dummies(dataset, drop_first = True)

#Setting X and y values
X= dataset.drop('Price', axis=1)
y = dataset['Price']

#Splitting dataset into train and test with 30% test
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=2)

#Implementing L1 regularization with Lasso
from sklearn.linear_model import Lasso

lasso_reg = Lasso(alpha=50, max_iter=100, tol=0.1)

lasso_reg.fit(train_x, train_y)

#Checking score with test data
lasso_reg.score(test_x, test_y)

#Checking score with train data
lasso_reg.score(train_x, train_y)
```

**Output:**

0.6636111369404489

0.6766985624766824

## What Is Unsupervised Learning?
Unsupervised learning is learning that uses machine learning algorithms to analyze and cluster unlabeled datasets. They discover hidden patterns without the need for human intervention. It is the appropriate solution for exploratory data analysis, cross-selling techniques, consumer segmentation, and image identification due to its capacity to find similarities and differences in information. The two main types of unsupervised learning include:

1. Clustering
2. Association

### Clustering
Finding a structure or pattern in a set of uncategorized data is the main goal of clustering. If there are any natural clusters (groups) in your data, clustering algorithms will process them and find them. The different types of clustering are:

1. **Exclusive clustering:** Data is grouped so that one data can only belong to one cluster. Example is K-Means clustering.
2. **Agglomerative clustering:** In this type of clustering, every data is a cluster. Iterative unions between the two nearest clusters reduce the number of clusters.
3. **Overlapping clustering:** Fuzzy sets is used to cluster data. Each point may belong to two or more clusters with separate degree of membership.
4. **Probabilistic clustering:** Uses probability distribution to create the clusters.

The various types of clustering algorithms include:

1. **Hierarchical clustering:** This algorithm builds a hierarchy of clusters. It begins with all the data which is assigned to a cluster of their own.
2. **K-Means clustering:** This approach for iterative clustering aids in determining the highest value for each iteration. The desired number of clusters is initially chosen. Data is grouped into k groups using this clustering technique.
3. **Principal Component Analysis:** In case of a higher-dimensional space, there should be a selection basis for that space known as the principal component. The subset you select constitute a new space which is small in size compared to original space.

### Implementation Of Algorithms In Code
### K-Means Clustering
```python
#Importing necessary libraries
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
%matplotlib inline

#Uploading file from local to google colal
from google.colab import files
files.upload()

#Loading the income csv file
df = pd.read_csv("/content/income.csv")

#Setting up the MinMax Scaler
scaler = MinMaxScaler()

scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])

#Creating the KMeans cluster model and fitting it and predicting
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])

#Creating a cluster column for the predicted values
df['cluster']=y_predicted

#Showing the cluster centers
km.cluster_centers_
```

**Output:** array([[0.85294118, 0.2022792 ],

[0.72268908, 0.8974359 ],

[0.1372549 , 0.11633428]])

### Principal Component Analysis
```python
#Importing needed libraries
from sklearn.datasets import load_digits
import pandas as pd

dataset = load_digits()

#Reshaping the dataset
dataset.data[0].reshape(8,8)

#Making a dataframe
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

#Setting X and y values
X = df
y = dataset.target

#Using standard scaler preprocessing technique
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Splitting dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=30)

#Fitting and scoring a Logistic Regression model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
model.score(X_test, y_test)

#Using PCA such that 95% of variance is maintained
from sklearn.decomposition import PCA

pca = PCA(0.95)
X_pca = pca.fit_transform(X)

#Splitting PCA components into train and test set
X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=30)

#Fitting and scoring a Logistic Regression model with the PCA components
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)
```

**Output:** 0.9694444444444444

### Association
You can create associations between data elements in sizable databases using association rules. In huge databases, this unsupervised technique seeks to identify intriguing correlations between variables. Examples include:

1. People that buy a new home most likely to buy new furniture.
2. Groups of shopper based on their browsing and purchasing histories.
3. Movie group by the rating given by movies viewers.

## Differences Between Supervised and Unsupervised Learning
|  |  |  |
| --- | --- | --- |
| **Parameters** | **Supervised Learning** | **Unsupervised Learning** |
| Input Data | Algorithms are trained using labeled data. | Algorithms are used against data which is not labeled. |
| Computational Complexity | Supervised learning is simpler. | Unsupervised learning is computationally complex. |
| Accuracy | High accuracy and trustworthy. | Less accurate and trustworthy method. |

Link to GitHub repository containing all the code:

<https://github.com/Jegge2003/supervised_unsupervised_learning>
