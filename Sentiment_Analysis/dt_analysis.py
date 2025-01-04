import tweepy
import pandas as pd
import re
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import download 

nltk.download('vader_lexicon')

from dotenv import load_dotenv
import os
load_dotenv()
#authenticating my twitter development account
def authenticate_twitter():
    api_key = os.getenv("API_KEY")
    api_key_secret = os.getenv("API_SECRET")
    api_access = os.getenv("ACCESS_TOKEN")
    api_access_secret = os.getenv("ACCESS_SECRET")
    authenticate = tweepy.OAuthHandler(api_key,api_key_secret)
    authenticate.set_access_token(api_access,api_access_secret)
    return tweepy.API(authenticate, wait_on_rate_limit = True)

api = authenticate_twitter()
