import sys
import json
import pandas as pd
import datetime
from requests_oauthlib import OAuth1
import tweepy
from pymongo import MongoClient
import requests.packages.urllib3
import logging

requests.packages.urllib3.disable_warnings() # Disable requests warning messages

urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)

logger = logging.getLogger('project_fletcher')
hdlr = logging.FileHandler('/home/jaysips/fletcher_status.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

# Twitter account key data from twitter_config file
consumer_key = "W6GCcoDSbTKtZJHdHhKKAyZar"
consumer_secret = "ktxfDOfCqq3rR9RZpcem2yuw8yZ2NDPHYmLvNWR0lg6X8PCi5A"
access_token = "2569831680-UgH5fqSCHE2W0vcY1LgSnwvh1Jv2qxAEWQLUP28"
access_token_secret = "MgHNrMq2Lx9PLexU0s6AEesAvUs5RvnLVhshuqd2pAfwd"

"""
Modify the tweepy StreamListener class to provide additional functionality.
Every time the stream receives data it will connect to MongoDB, iniate a
MongoDB database, write the data to a json file and and insert the json file into
a collection in the the database.
"""
class StreamListener(tweepy.StreamListener):
    """
    tweepy.StreamListener is a class provided by tweepy used to access
    the Twitter Streaming API. It allows us to retrieve tweets in real time.
    """
    def on_connect(self):
        """Called when the connection is made"""
        #timestr = strftime("%Y-%m-%d %H:%M:%S", localtime())
        #print(timestr)
        #print("You're connected to the Twitter streaming server...Ctrl-C to stop the stream")
        logger.info("Connected to the Twitter streaming service")


    def on_error(self, status_code):
        """This is called when an error occurs"""
        #timestr = strftime("%Y-%m-%d %H:%M:%S", localtime())
        #print(timestr)
        #print('Error: ' + repr(status_code), 'stream disconnected')
        logger.error(repr(status_code), "Stream disconnected")
        return False

    def on_data(self, data):
        """This will be called each time we receive stream data"""
        client = MongoClient('localhost', 27017)

        # Use fletcher database
        db = client.fletcher

        # Decode JSON
        datajson = json.loads(data)

        # We only want to store tweets in English
        if "lang" in datajson and datajson["lang"] == "en":
            # Store tweet info into the oscartweets collection.
            db.oscartweets.insert(datajson)


if __name__ == '__main__':
    try:
        # Authenticating
        auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth1.set_access_token(access_token, access_token_secret)

        # Start the stream
        my_listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
        streamer = tweepy.Stream(auth=auth1, listener=my_listener)

        # Filter the Twitter stream to capture only tweets related to the European Union
        streamer.filter(track=['#Oscars2016'])

    except KeyboardInterrupt:
        logger.info("Interrupt received...stopping stream")
        sys.exit()
