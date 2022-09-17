import pandas as pd
import cohere
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans


print("\nGetting reviews from tsv")
reviews_df = pd.read_table('amazon_reviews.tsv')
review_list = list(reviews_df.verified_reviews)[0:10]
print("\n\tSize of reviews list: ", len(review_list))

print("\nGetting cohere embed for each review")
co = cohere.Client('QFBgGBv3qZJdCdYH5zVZvF0sbwC8Ma1r7xsWjZEJ')
embeds = co.embed(
    model='cohere-toxicity',
    texts=review_list
)

embeds_array = np.array(embeds.embeddings)
tsne = TSNE(n_components=2, perplexity=9.0)
two_d_vectors = tsne.fit_transform(embeds_array)

kmeans = KMeans(n_clusters=5)

label = kmeans.fit_predict(two_d_vectors)
