import base64
from dotenv import load_dotenv
load_dotenv()
import os
#dotenv is used to grab the consumer_key and consumer_secret from the .env file
api_key=os.environ['consumer_key']
api_secret=os.environ['consumer_secret']
#bellow code is partially from https://benalexkeen.com/interacting-with-the-twitter-api-using-python/
key_secret =  '{}:{}'.format(api_key, api_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')


import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# Check status code okay
auth_resp.status_code

# Keys in data response are token_type (bearer) and access_token (your access token)
auth_resp.json().keys()

access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'q': 'Corn',
    'result_type': 'popular',
    'count': 1,
    'lang': 'en'
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

search_resp.status_code
tweet_data = search_resp.json()
for x in tweet_data['statuses']:
    y = x['id_str']

html_output = """<!DOCTYPE html>
<head></head>
<body>
<blockquote class="twitter-tweet"><a href="https://twitter.com/x/status/"""+y+"""></a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</body>"""
f = open("index.html", "w")
f.write(html_output)
f.close()
