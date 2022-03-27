import requests
import pickle
import json
import os

from datetime import datetime
from pathlib import Path


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

# hashtags = [
#         '#MenasFuera', 
#         '#PrimeroVox',
#         '#TeamVox',
#         '#SoloQuedaVox',
#         '#VoxExtremaNecesidad',
#         '#MenasNo',
#         '#Stopislam',
#         '#morosfuera'
#         ]
 

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    # Load terms
    with open(Path('data', 'tweets_lookup_terms.pickle'), 'rb') as f:
        terms = pickle.load(f)

    tweets = {}
    for term in terms:
        print(f'Searching for {term}')
        query_params = {
                'query': f'{term} -is:retweet lang:es',
                'tweet.fields': 'text'
                }
        tweets[term] = connect_to_endpoint(search_url, query_params)

    timestamp = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

    with open(Path('data', f'tweets_{timestamp}.json'), 'w', encoding='utf-8') as f:
        json.dump(tweets, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
