#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# # From scratch

# In[24]:


mu_1, sigma_1 = 8, 1.5
group_1_x = np.random.normal(mu_1, sigma_1, 20)
group_1_y = np.random.normal(mu_1, sigma_1, 20)
group_1 = (group_1_x, group_1_y)
average_point_1 = [np.mean(group_1_x), np.mean(group_1_y)]

mu_2, sigma_2 = 15, 1.5
group_2_x = np.random.normal(mu_2, sigma_2, 20)
group_2_y = np.random.normal(mu_2, sigma_2, 20)
group_2 = (group_2_x, group_2_y)
average_point_2 = [np.mean(group_2_x), np.mean(group_2_y)]

mu_3, sigma_3 = 2, 1.5
group_3_x = np.random.normal(mu_3, sigma_3, 20)
group_3_y = np.random.normal(mu_3, sigma_3, 20)
group_3 = (group_3_x, group_3_y)
average_point_3 = [np.mean(group_3_x), np.mean(group_3_y)]

num_pts = 3
groups = [group_1, group_2, group_3]
averages = [average_point_1, average_point_2, average_point_3]
colors = ["red", "blue", "green"]
for i in range(num_pts):
    plt.scatter(groups[i][0], groups[i][1], color=colors[i])
    plt.scatter(averages[i][0], averages[i][1], color="orange", linewidths=5)
    
plt.xlim(0,20)
plt.ylim(0,20)
plt.show()


# # Using scikit learn

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
get_ipython().run_line_magic('matplotlib', 'inline')
X= -2 * np.random.rand(100,2)
X1 = 1 + 2 * np.random.rand(50,2)
X[50:100, :] = X1
plt.scatter(X[ : , 0], X[ :, 1], s = 50, c = "b")
plt.show()

Kmean = KMeans(n_clusters=2)
Kmean.fit(X)
Kmean.cluster_centers_
plt.scatter(X[ : , 0], X[ : , 1], s =50, c="b")
plt.scatter(-0.94665068, -0.97138368, s=200, c="g", marker="s")
plt.scatter(2.01559419, 2.02597093, s=200, c="r", marker="s")
plt.show()
Kmean.labels_
sample_test=np.array([-3.0,-3.0])
second_test=sample_test.reshape(1, -1)
Kmean.predict(second_test)


# In[6]:


X = np.random.random((100,128))

Kmean = KMeans(n_clusters=2)
Kmean.fit(X)
print(Kmean.cluster_centers_)
print(Kmean.labels_)

