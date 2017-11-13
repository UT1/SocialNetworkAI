import tweepy, sys, time
from random import randint
from credentials import *

class twitter_bot:
    def send_message(this):
        auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
        auth.set_access_token(Access_token, Access_token_secret)
        api = tweepy.API(auth)

        print "Username of DM's receiver:"
        i=raw_input();
        print "Enter the message you want to send:"
        message=raw_input();
        s = api.send_direct_message(screen_name=i,text=message)

    def send_tweet(this):
        auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
        auth.set_access_token(Access_token, Access_token_secret)
        api = tweepy.API(auth)

        print "Enter the tweet you wnat to post:"

        message=raw_input();
        s = api.update_status(message)
s=twitter_bot();
#s.send_tweet();
s.send_message();
print "Done";
