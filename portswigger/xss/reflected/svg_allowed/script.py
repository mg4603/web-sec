from ratelimit import limits, RateLimitException, sleep_and_retry
from pathlib import Path
from requests import get

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120
url = 'https://INSTANCE-ID.web-security-academy.net/'

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_tag_call(url, tag):
    return get(f'{url}<{tag}>')
    