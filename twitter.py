import tweepy
import configure as c

client = tweepy.client(bearer_token=c.Bearer_Token)


response = client.search_recent_tweets(q="from:twitterdev", max_results=10)

for tweet in response.data:
    print(tweet.text)