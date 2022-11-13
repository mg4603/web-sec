from requests import post
from pathlib import Path
from ratelimit import limits, sleep_and_retry

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120
url = ''
headers = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Referer': ''
}
cookies = {
    'session': 'SESSION-TOKEN'
}

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_user_call(url, user, headers, cookies):
    return post(
        url=url,
        data={'username': user, 'password': 'asdf'},
        headers=headers,
        cookies=cookies
    )

