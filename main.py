import subprocess
import requests

def get_id(username):
	url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+username+"&rank_token=0.3953592318270893&count=1"
	response = requests.get(url)
	respJSON = response.json()
	try:
		user_id = str( respJSON['users'][0].get("user").get("pk") )
		return user_id
	except:
		return False

subprocess.run('sudo rm -rf json_followers/*', shell = True)
subprocess.run('sudo rm -rf json_subscriptions/*', shell = True)

username = input('Input a username: ')
user_id = get_id(username)

if not user_id:
    exit('User id => 0 => exit')

subprocess.run(f'python3 get_followers.py {user_id}', shell = True)
subprocess.run(f'python3 get_subscriptions.py {user_id}', shell = True)

subprocess.run('python3 parse_followers.py', shell = True)
subprocess.run('python3 parse_subscriptions.py', shell = True)

subprocess.run('python3 get_unfollowers.py', shell = True)

print('Finish :)')