---
title: "Cluster Analysis in Python"
author: "aya abdalsalam"
date: 2022-09-27
description: "How does Google News classify articles? By using unsupervised machine learning algorithm google Match frequent terms in articles to find similarity between this terms and put them in the same group..."
categories: ["Machine Learning", "Python", "Projects"]
image: images/d803c7_e168658961c347a68eed7404b69a5786.webp
wix-url: https://www.datainsightonline.com/post/cluster-analysis-in-python
---
### How does Google News classify articles?

By using unsupervised machine learning algorithm google

Match frequent terms in articles to find similarity between this terms and put them in the same group .Another example of clustering is segmentation of customers based on their spending habits.

### Clustering :It is often used as a data analysis technique for discovering interesting patterns in data, such as groups of customers based on their behavior.

you can cluster your customers based on their pur‐ chases, their activity on your website, and so on. This is useful to understand who your customers are and what they need, so you can adapt your products and marketing campaigns to each segment. For example, this can be useful in recommender systems to suggest content that other users in the same cluster enjoyed.

```python
x = [9, 6, 2, 3, 1, 7, 1, 6, 1, 7, 23, 26, 25, 23, 21, 23, 23, 20, 30, 23]
y = [8, 4, 10, 6, 0, 4, 10, 10, 6, 1, 29, 25, 30, 29, 29, 30, 25, 27, 26, 30]
```

```python
# Create a scatter plot
plt.scatter(x, y)

# Display the scatter plot
plt.show()
```

![](images/d803c7_e168658961c347a68eed7404b69a5786.webp)

K-Means :

![](images/d803c7_863c8dd8ebad4b969bf930f369623bb6.webp)

we have this data and we want to cluster it (make it groups) so we will find the center of each blob's and assign each blob to the nearest one to it

> Note: You need to identify the number of clusters

Elbow Method:This technique for choosing the best value for the number of clusters is rather coarse

![](images/d803c7_3572eacefa594e1eab2213be92c9314a.webp)

n_clusters = 4

![](images/d803c7_10d7193726dd461bb0f58eb6a035823b.webp)

n_clusters = 4,5 is much better than 6,7

#### How many dominant colors?

![](images/d803c7_559c4b6255134fe9819a77fefacc72d0.webp)

#### image consist of pixel

#### pixel contain 3 colors (red, green, blue )

```python
# Import image class of matplotlib
import matplotlib.image as img

# Read batman image and print dimensions
batman_image = img.imread('batman.jpg')
print(batman_image.shape)

# Store RGB values of all pixels in lists r, g and b
for pixel in batman_image:
    for temp_r, temp_g, temp_b in pixel:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)
```

```python
distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(batman_df[['scaled_red', 'scaled_blue', 'scaled_green']], i)
    distortions.append(distortion)

# Create a DataFrame with two lists, num_clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Create a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()
```

![](images/d803c7_22ba2fc757414b979420573510147b2a.webp)

n_clusters = 3 so it mains this image contain 3 colors so what are this colors?

```python
# Get standard deviations of each color
r_std, g_std, b_std= batman_df[['red', 'green', 'blue']].std()

for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    # Convert each standardized value to scaled value
    colors.append((
        scaled_r * r_std / 255,
        scaled_g * g_std / 255,
        scaled_b * b_std / 255
    ))

# Display colors of cluster centers
plt.imshow([colors])
plt.show()
```

![](images/d803c7_4034ba05bf464275a49303769cb48c99.webp)

Resourses : 1: file:///F:/mine/ITI/machien/2-Aur%C3%A9lien-G%C3%A9ron-Hands-On-Machine-Learning-with-Scikit-Learn-Keras-and-Tensorflow_-Concepts-Tools-and-Techniques-to-Build-Intelligent-Systems-O%E2%80%99Reilly-Media-2019.pdf

2:https://campus.datacamp.com/courses/cluster-analysis-in-python/clustering-in-real-world?ex=4
