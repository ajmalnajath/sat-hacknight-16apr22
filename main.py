from re import T
from time import time
from traceback import print_tb
import tweepy

# authentication with twitter
auth = tweepy.OAuthHandler("g9yShVdrzNeGJFoqBk1dPZMqu", "QIqdJW6BEgstSL9r6qWtiECp5eWo79f6hJMVAbXU4dohZ9tzRy")
auth.set_access_token("1515352170597695492-QGMp3kNArypahQE6n77PlpYyjV3Z2K", "SH5GhmG4cyubEeGcXcTSmlPvvq7KyXma83WD5FIwk6Iqr")
api = tweepy.API(auth)

mentions = api.mentions_timeline()

print(mentions)

'''
tweet_id = ''

for mention in mentions:
    tweet_id = mention.id
    print(tweet_id)

status = api.get_status(tweet_id, tweet_mode="extended")
try:
    print(status.retweeted_status.full_text)
except AttributeError:  # Not a Retweet
    print(status.full_text)
'''