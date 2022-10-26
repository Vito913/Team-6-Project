import tweepy
import configure as c
import os

os.environ["TOKEN"] = c.Bearer_Token
client = tweepy.client(bearer_token=c.Bearer_Token)

def auth():
    return os.getenv("TOKEN")


response = client.search_recent_tweets(q="from:twitterdev", max_results=10)

for tweet in response.data:
    print(tweet.text)
    