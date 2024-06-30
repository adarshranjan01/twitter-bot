import tweepy
import time
from secrets import *

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def check_mentions(api, keywords, since_id):
    print("Checking mentions...")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if any(keyword in tweet.text.lower() for keyword in keywords):
            print(f"Responding to tweet {tweet.id} from {tweet.user.screen_name}")
            api.update_status(
                status="Hi! This is a Twitter bot responding to your mention.",
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
    return new_since_id

def main():
    since_id = 1  # Replace with your initial since_id
    while True:
        since_id = check_mentions(api, ["@your_twitter_handle"], since_id)
        print("Waiting...")
        time.sleep(60)  # Adjust as needed
        if __name__ == "__main__":
            main()

