import tweepy
import pandas as pd
import re
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import download 

nltk.download('vader_lexicon')

#authenticating my twitter development account
def authenticate_twitter(api_key, api_key_secret, access_token, access_token_secret):
    authenticate = tweepy.OAuthHandler(api_key, api_key_secret)
    authenticate.set_access_token(access_token,access_token_secret)
    return tweepy.API(authenticate, wait_on_rate_limit=True)


