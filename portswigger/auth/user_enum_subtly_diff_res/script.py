from ratelimit import limits, RateLimitException, sleep_and_retry
from requests import post
from pathlib import Path

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120

url = ''
headers = {

}
cookies = {

}

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_user_call(url, user, headers, cookies):
    pass

def enumerate_user(url, user_file_list, headers, cookies):
    pass

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_pass_call(url, user, password, headers, cookies):
    pass
