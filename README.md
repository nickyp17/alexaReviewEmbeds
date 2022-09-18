# Consensus

Consensus aims to revolutionize the manner by which buyers evaluate products. Through the use of Co:here, Consensus groups similar reviews together, and uses these groups to generate an abridged consensus for opinions regarding the product. This is an arguably superior system to those offered by most digital marketplaces, as it emphasizes user experiences as opposed to ratings, which can be both subjective and restrictive.

# Inspiration

Our inspiration for Consensus arose from a shared frustration at the lacklustre nature of the current Amazon review/rating system. As it currently stands, the five-star system offers only a surface-level outlook into consumer experiences. Certain products with numerous five-star reviews may actually suffer from severe flaws that are only discussed in the depths of user reviews that most prospective buyers will never actually read. Consensus offers an additional dimension to the rating system by grouping and summarizing key points, ensuring every user review is considered.

# What it does

Consensus anonymously takes in product reviews, groups them by meaning, and then provides a short description that accurately represents the whole. This means Consensus can reduce hundreds of reviews into a few staple points. We use a scatter plot to clearly demonstrate the grouping process to both consumers and vendors, thereby providing the former with a realistic insight into the product, and the latter with potential areas of development.

# How we built it

We initially started on attempting to utilize the vectors produced by Co:Here embed API and real Amazon reviews to create a scatter plot. This plot process came with first using PCA to reduce the vectors to two-dimensions, and then using K-means clustering to create unlabeled clusters. After being able to produce a scatter plot, we needed to devise a plan to extract the labels for these clusters. To do this, we decided to use another part of Co:Here’s API, the generate feature. We created prompts comprised of various products reviews and their collective summaries to utilize the generate feature. These prompts were fed into the generate classifier to create a shorter version of the reviews held in each of the K-means review embedding clusters. We then passed these newly generated summaries for the clusters to utilize in our scatter plot creating an improved legend and a more readable graph. 

# Challenges we faced

This undertaking was certainly fraught with challenges for a variety of reasons. The process of accruing the data and clustering them semantically proved to be a difficult due to the novelty of the task. Prior to this project, none of us had necessarily heard of or implemented data clustering into our projects, so we were forced to dedicate a substantial portion of our time to researching such methods. Thankfully, Co:here provides an intuitive API upon which we based our solution.

After successfully clustering the Amazon reviews based on their semantic content, the next step was to devise a method to extract the grouped data points into separate containers/data structures. There was no obvious trivial approach to this problem, so we again found ourselves in a position where we needed to innovate a creative solution to a seemingly insurmountable problem.

# Accomplishments we're proud of

- Utilizing many different aspects of Co:here’s API to reach our desired outcome
- Learning more about NLP and clustering of word embeddings
- Solving a real world problem through the use of ML
- Combining both graphing and Co:here data analysis

# What we learned

- How to use K-means clustering to group data
- How to utilize the embed and generate features of Co:here’s API
- Details regarding linear dimensionality reduction technique such as PCA and t-SNE

# The future of Consensus

There are numerous ways that Consensus can be improved. Comparing different products (both generally and based on specific requests), improving the summarizer AI, and implementing customizable review searching options are all things we’d like to implement in the future. The nature of Consensus allows it to thrive as both a web application, and as a browser extension, so implementing these would be the next step for Consensus to take.

While Consensus represents a substantial step toward simply enhancing the e-commerce experience, there are several features that can be implemented to revolutionize it.  Additionally, although originally pictured as a web application, we believe that Consensus would thrive as a browser extension; allowing users to access Co:here analysis during their shopping experience would streamline the entire experience. Finally, we also think that Consensus will put more power in the hand of those closest to the products, as the summarized user reviews may serve as constructive feedback and result in an ever-improving product.
