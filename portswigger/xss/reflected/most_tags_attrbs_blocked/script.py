from requests import get
from ratelimit import limits, RetryLimitException, sleep_and_retry

url = 'https://INSTANCE-ID.web-security-academy.net/?search='

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_tag_call(url, tag):
    return get(url + tag)
