import tweepy
import configparser
import pandas as pd

# Initiate the parser
config = configparser.ConfigParser()
config.read('config.ini')


#---------------- API KEYs ----------------
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
column = ["text","user_name","created_at","number_of_likes"]
data = []


#client initialization
client = tweepy.Client(bearer_token=bearer_token)


# gets the tweets for the query and appends them to the a dataframe that is printed to a csv file
def get_tweet_dataframe(query):
    all_tweets = []
    tweets = api.search_tweets(query, count=10)#result_type="popular"
    for tweet in tweets:
        all_tweets.append([tweet.text,tweet.user.screen_name,tweet.created_at,tweet.favorite_count])
    df = pd.DataFrame(all_tweets, columns=column)
        
    df.to_csv("tweets.csv",mode='a')
    return df

