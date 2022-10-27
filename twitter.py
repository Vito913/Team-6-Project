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

bearer_token = config['twitter']['bearer_token']

consumer_id = config['twitter']['consumer_id']
consumer_secret = config['twitter']['consumer_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# dataframe seatup
column = ["id","text"]
data = []


client = tweepy.Client(bearer_token=bearer_token)





# gets the tweets for the query and appends them to the a dataframe
def get_tweet_dataframe(query):
    all_tweets = []
    tweets = client.search_recent_tweets(query, max_results=10)
    for tweet in tweets:
        print(tweet)
        parsed_tweet = {}
        parsed_tweet["author"] = tweet.user.name
        parsed_tweet["text"] = tweet.text
        parsed_tweet["number_of_likes"] = tweet.favorite_count
        parsed_tweet["retweets"] = tweet.retweet_count
        date = tweet["created_at"] = tweet.created_at
        all_tweets.append(parsed_tweet)
    df = pd.DataFrame(all_tweets, columns=column)
    df.to_csv("tweets.csv")
    return df

print(get_tweet_dataframe("test"))