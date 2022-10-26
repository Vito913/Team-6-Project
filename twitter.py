import tweepy
import configparser
import pandas as pd
import helpers as h


config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_query_tweets(query, count=10):
    return api.search(q=query, count=count)

column = ["name", "text","likes","retweets","date"]
data = []

# gets the tweets for the query and appends them to the a dataframe
def get_tweet_dataframe(query):
    tweets = get_query_tweets(query)
    for tweet in tweets:
        name = tweet.user.screen_name
        text = tweet.text
        likes = tweet.favorite_count
        retweets = tweet.retweet_count
        date = tweet.created_at
        data.append([name, text, likes, retweets, date])
    df = pd.DataFrame(data, columns=column)
    df.to_csv("tweets.csv")
    return df