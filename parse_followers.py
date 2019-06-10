import glob
import json
from pprint import pprint


files = glob.glob('json_followers/*.json')
followers = {}

print('Start parsing followers.')

for f in files:
    with open(f, 'r') as f:
        data = json.load(f)

    for user in data['data']['user']['edge_followed_by']['edges']:
        followers[user['node']['id']] = {
            'id': user['node']['id'],
            'username': user['node']['reel']['owner']['username']
        }

with open('followers.json', 'w') as f:
    json.dump(followers, f)

print('Finish parsing followers:)')