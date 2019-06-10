import json
from pprint import pprint

print('Start getting unfollowers.')

with open('followers.json', 'r') as f:
    followers = json.load(f)

with open('subscriptions.json', 'r') as f:
    subscriptions = json.load(f)

unfollowers = []

for s in subscriptions:
    if s not in followers.keys():
        unfollowers.append(subscriptions[s]['username'])
        print('Subscription {} not in followers => add to unfollowers'.format(s))

with open('unfollowers.txt', 'w') as f:
    f.write('\n'.join(unfollowers))

print('Finish getting unfollowers:)')