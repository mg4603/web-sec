from requests import post
from ratelimit import limits, RateLimitException, sleep_and_retry

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120
url = 'HTTPS://LAB-INSTANCE.web-security-academy.net/cart'
headers = {
    'Content-Length': '34'
}
cookies = {
    'session': 'SESSION-COOKIE'
}

data = {
    'productId': '1',
    'quantity': '99',
    'redir' : 'cart'
}

# 150 times
@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_call():
    pass