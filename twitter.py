import os
from sqlite3 import connect
import json
import requests


NBA_ACCOUNTS = {"wojespn": "50323173", "NBA": "19923144", "NBAPR": "130599831", "CBSSportsNBA": "158426128", "NBAOfficial": "423868716"}
MLB_ACCOUNTS = {"MLB": "18479513", "CBSSportsMLB": "151532796", "theScoreMLB": "825616722", "MLBONFOX": "22819823"}


def auth():
    return os.getenv("TOKEN")


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def create_url(userID, start_date, end_date, max_results = 10):
    search_url = "https://api.twitter.com/2/users/" + userID + "/tweets"

    query_params = {'start_time': start_date,
                    'end_time': end_date,
                    'tweet.fields': 'created_at',
                    'max_results': max_results}
    
    return (search_url, query_params)


def get_tweets_from_user(userID: str, start_date: str, end_date: str, max_results: int = 10):
    if not userID.isnumeric():
        raise Exception(f"Nonnumeric user ID: {userID}")
    if max_results < 5 or max_results > 100:
        raise Exception(f"max_results value [{max_results}] is not between 5 and 100")
    
    bearer_token = auth()
    headers = create_headers(bearer_token)
    search_url, params = create_url(userID, start_date, end_date, max_results)

    return connect_to_endpoint(search_url, headers, params)


def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    content = response.json()
    response.close()
    return content
