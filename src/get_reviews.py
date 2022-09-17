import cohere
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_table('amazon_reviews.tsv')
review_list = list(reviews)
co = cohere.Client('QFBgGBv3qZJdCdYH5zVZvF0sbwC8Ma1r7xsWjZEJ')
embed = co.embed(
    model='cohere-toxicity',
    texts=review_list
)
embed_array = np.array(embed.embeddings)

pca = PCA(2)

df = pca.fit_transform(embed_array)

kmeans = KMeans(n_clusters=10)

label = kmeans.fit_predict(df)

unique_labels = np.unique(label)

for i in unique_labels:
    plt.scatter(df[label == i, 0], df[label == i, 1], label=i)
plt.legend()
plt.show()
