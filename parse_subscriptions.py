import glob
import json
from pprint import pprint


files = glob.glob('json_subscriptions/*.json')
followers = {}

print('Start parsing subscriptions.')

for f in files:
    with open(f, 'r') as f:
        data = json.load(f)

    for user in data['data']['user']['edge_follow']['edges']:
        followers[user['node']['id']] = {
            'id': user['node']['id'],
            'username': user['node']['reel']['owner']['username']
        }

with open('subscriptions.json', 'w') as f:
    json.dump(followers, f)

print('Finish parsing subscriptions:)')