import json
import os
from datetime import datetime

import nba
import twitter


def main():
    twitter_test()


def nba_test():
    news = nba.get_news(5)
    if (news == []):
        print("shempty")
        return 0

    for a in news:
        print(f"Site: {a['source']}")
        print(a['title'])
        print()


def twitter_test():
    # Set auth token
    os.environ['TOKEN'] = '<ADD_BEARER_TOKEN>'
    
    # Example usage
    tweets = twitter.get_tweets_from_user(twitter.NBA_ACCOUNTS["wojespn"], "2022-04-19T00:00:00.00Z", "2022-04-19T18:33:23.49Z", 5)
    for tweet in tweets["data"]:
        tweet_content = tweet["text"]
        tweet_date = tweet["created_at"]
        
        print(f"Tweet by @wojespn at {tweet_date}")
        print(tweet_content)
        print()
        
if __name__ == "__main__":
    main()
