import tweepy

API_Key = "e4R54foYRXhCUezobTu7TE2ux"
API_Key_Secret = "4P7rwlspWhqyvvpgInuerOsoOehGo0ktupfprD7XGcQOpa6Ank"
access_token = "796403539748777984-FBPr9QhE33uptS0QTg9OeM2Pt6Rsqol"
access_token_secret = "FZ0KhTmQLhtFF5eYhJx3p6PQdZHEfox9CoTA3iSy6tb0u"

auth = tweepy.OAuth1UserHandler(
   API_Key, API_Key_Secret, access_token, access_token_secret
)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Verification error")


public_tweets = api.home_timeline()
for tweets in public_tweets:
    print(tweets.text)
    