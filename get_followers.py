import json
from pprint import pprint
import subprocess
import time
import urllib.parse
import sys


base_url = 'https://www.instagram.com/graphql/query/?'

command_template = """curl '{url}' -H 'cookie: mid=XPbBggAEAAG0sSTlc9ocHIgdJa9N; csrftoken=H661LUAaOXR8N0rrnKlebq9INrXcX8eB; shbid=3433; shbts=1559675352.786263; ds_user_id=8528156345; sessionid=8528156345%3AvFM7xD8GtJM848%3A15; rur=PRN; urlgen="{{\"93.170.68.19\": 43656}}:1hYEoK:BZcdJ09tV3PhOHFurZA55XSgd9c"' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' -H 'accept: */*' -H 'referer: https://www.instagram.com/vlad9__kandyba/followers/' -H 'authority: www.instagram.com' -H 'x-requested-with: XMLHttpRequest' -H 'x-ig-app-id: 936619743392459' --compressed > json_followers/followers_{index}.json"""

index = 1
after = None

followers_processed = 0

while True:
    after_value = f', "after": "{after}"' if after else ''
    variables = f'{{"id":"{sys.argv[1]}","include_reel":true,"fetch_mutual":false,"first":50{after_value}}}'

    get_params = {
        'query_hash': 'c76146de99bb02f6415203be841dd25a',
        'variables': variables
    }

    ws_url = base_url + urllib.parse.urlencode(get_params)
    
    result = subprocess.run(command_template.format(url = ws_url, index = index), shell = True)
    
    if result.returncode != 0:
        exit('Returncode != 0 => exit')

    with open(f'json_followers/followers_{index}.json', 'r') as f:
        data = json.load(f)

    after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']

    all_followers = data['data']['user']['edge_followed_by']['count']
    followers_processed += len(data['data']['user']['edge_followed_by']['edges'])

    print(f'Processed {followers_processed}/{all_followers}')

    next_page = data['data']['user']['edge_followed_by']['page_info']['has_next_page']

    if not next_page:
        print('Finish :)')
        break

    index += 1
    time.sleep(2 if index % 10 != 0 else 5)