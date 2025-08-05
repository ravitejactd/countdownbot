import datetime
import os
import tweepy

# --- CONFIG ---
TARGET_DATE = datetime.datetime(2025, 8, 27)  # Event date (change if needed)
# --------------

def main():
    today = datetime.datetime.now()
    delta = TARGET_DATE - today
    days_left = delta.days

    if days_left < 0:
        print("Target date already passed.")
        return

    message = f"{days_left}"
    print("Tweeting:", message)

    client = tweepy.Client(
        consumer_key=os.getenv("API_KEY"),
        consumer_secret=os.getenv("API_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_SECRET")
    )

    client.create_tweet(text=message)

if __name__ == "__main__":
    main()
