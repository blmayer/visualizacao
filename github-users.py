#!/usr/local/bin/python3

from requests import get as Get

api_url = 'https://api.github.com/users/'
users = [u['login'] for u in Get(api_url+'blmayer/following').json()]

user_info = {}
for u in users:
    user_info[u] = {
        'following': len(Get(api_url+f'{u}/following').json()),
        'followers': len(Get(api_url+f'{u}/followers').json())
    }
