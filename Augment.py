import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import pprint
from textblob import TextBlob
import os
import twitter_credentials

from twarc import Twarc

from m3inference import M3Twitter
from m3inference import get_lang

class Sentiment():
    """
    Functionality for analyzing and categorizing content from tweets.
    """
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))

        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

if __name__ == '__main__':
    PATH = "/Users/neilyeung/Desktop/DM_Final_Proj/data/testing/"
    final_df = pd.read_json(PATH + "2020-04-1_clean-dataset.jsonl", lines=true)

    # Polarity
    sent = Sentiment()
    final_df['sentiment'] = np.array([sent.analyze_sentiment(tweet) for tweet in final_df['full_text']])

    # M3Inference
    m3twitter = M3Twitter(cache_dir="twitter_cache")
    m3twitter.transform_jsonl(input_file = "test/twitter_cache/2020-04-1_clean-dataset.jsonl",output_file = "test/twitter_cache/m3_input.jsonl")
    m3twitter.infer("test/twitter_cache/m3_input.jsonl"))

    m3_df = pd.read_json(PATH + "test/twitter_cache/m3_input.jsonl", lines=true)

    # TO DO: Test how the data frame looks on
