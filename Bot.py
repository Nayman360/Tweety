import tweepy
import time
import os
import random
from getpass import getpass

# Display author on launch
print("Script by: COPYNINJA")

# Prompt for Twitter API credentials
def get_credentials():
    print("Please enter your Twitter API credentials.")
    api_key = input("API Key: ")
    api_secret_key = input("API Secret Key: ")
    access_token = input("Access Token: ")
    access_token_secret = input("Access Token Secret: ")
    return api_key, api_secret_key, access_token, access_token_secret

# Authenticate to Twitter
def authenticate(api_key, api_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

# Load tweets from a text file
def load_tweets(file_path="tweets.txt"):
    with open(file_path, "r") as file:
        tweets = [line.strip() for line in file if line.strip()]
    return tweets

# Choose a random image from the 'pic' folder
def choose_random_image(folder_path="pic"):
    images = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    return random.choice(images) if images else None

# Post a tweet with optional image
def post_tweet(api, content, image_path=None):
    try:
        if image_path:
            api.update_status_with_media(status=content, filename=image_path)
            print("Tweet with image posted successfully!")
        else:
            api.update_status(content)
            print("Tweet posted successfully!")
    except tweepy.TweepError as e:
        print(f"Error: {e}")

# Prompt user for time interval
def get_time_interval():
    print("\nSet time interval between tweets (in seconds):")
    try:
        interval = int(input("Enter interval in seconds: "))
        return interval
    except ValueError:
        print("Invalid input. Setting default interval of 1 hour (3600 seconds).")
        return 3600

def main():
    # Get credentials and authenticate
    api_key, api_secret_key, access_token, access_token_secret = get_credentials()
    api = authenticate(api_key, api_secret_key, access_token, access_token_secret)

    # Load tweets and set interval
    tweets = load_tweets()
    interval = get_time_interval()

    # Post tweets at specified intervals
    for tweet in tweets:
        image_path = choose_random_image()  # Choose a random image for each tweet
        post_tweet(api, tweet, image_path)
        time.sleep(interval)

if __name__ == "__main__":
    main()
