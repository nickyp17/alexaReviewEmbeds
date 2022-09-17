import pandas as pd
import cohere

reviews_df = pd.read_table('amazon_reviews.tsv')
review_list = list(reviews_df.verified_reviews)

co = cohere.Client('QFBgGBv3qZJdCdYH5zVZvF0sbwC8Ma1r7xsWjZEJ')
embeds = co.embed(
    model='cohere-toxicity',
    texts=review_list
)

