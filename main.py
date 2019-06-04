import subprocess


subprocess.run('sudo rm -rf json_followers/*', shell = True)
subprocess.run('sudo rm -rf json_subscriptions/*', shell = True)

user_id = int(input('Input a user ID: '))

subprocess.run(f'python3 get_followers.py {user_id}', shell = True)
subprocess.run(f'python3 get_subscriptions.py {user_id}', shell = True)

subprocess.run('python3 parse_followers.py', shell = True)
subprocess.run('python3 parse_subscriptions.py', shell = True)

subprocess.run('python3 get_unfollowers.py', shell = True)