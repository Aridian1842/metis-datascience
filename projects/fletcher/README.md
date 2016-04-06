##Project Fletcher  
####*State of the (EU)nion:  Topic Modeling with Twitter Data*  

**Files in this repo:**  
*fletcher_notebook.ipynb:*  IPython notebook with the data processing and analysis.    
*project_fletcher.py:*  Python script for collecting tweets via the Twitter Streaming API and loading into MongoDB.  
*fletcher_slides.pdf:*  slides developed for project presentation.  

**Project Description:**  
This project focused on applying unsupervised learning and natural language processing (NLP).  I decided to focus on collecting Twitter data relating to the European Union (EU).  Given the current turmoil in Europe regarding the Syrian refugee crisis, and the upcoming UK referendum on leaving the EU, I wanted to examine what the "Twitter-verse" was saying regarding the EU.  The basic premise was:  assume you were a consultant for a U.S. client who was looking to expand operations into Europe.  While the financial data looked promising, your task was to examine the geo-political situation and provide a recommendation.  

Twitter can be leveraged as a real-time news source, often providing updates on current events before the traditional media.  Of course, this assumes you are following accounts that tweet such information, or search relevant hashtags.  Hashtags are essentially Twitter's version of topic modeling (spam notwithstanding).  But I went into this project assuming I had none of this information.  My goal was to leverage the Streaming API and collect all tweets pertaining to the EU, using just the keywords "European Union and EU", and then apply K-Means Clustering and Latent Dirichlet Allocation (LDA) to determine relevant topics from all the tweets collected.  

*Data Acquisition:*  Python script running remotely on AWS EC2 instance, using the Tweepy library to access the Streaming API.  Tweets were collected and loaded into a MongoDB NoSQL database also hosted on EC2.  
*Pre-processing and Analysis:*  I had to perform a mongoexport from the EC2 to my local machine, due to the size of the database, the PyMongo library was unable to extract the data directly from MongoDB without hanging up the kernel.  Pandas was used to clean and transform the data for analysis.  Finally, K-Means Clustering via scikit-learn and LDA topic modeling via the pyLDAvis library was performed.  
*Visualization:*  For the presentation, I created a 3D world globe in D3 plotting all the tweets that were geo-referenced to show the areas of the world generating the most tweets on the topic.  Obviously, focusing on the European Union, most tweets were from Europe, with the largest concentration from the UK, where the referendum issue persists as a top news item.  
