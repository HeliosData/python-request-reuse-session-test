import time

import requests


def main():
    print('open new session every request')
    for i in range(5):
        start = time.perf_counter()
        requests.get('https://google.com')
        request_time = time.perf_counter() - start
        print(f'open new session to access google.com {i + 1} times response time: {request_time} s')

    print('reuse session')
    # reference: https://requests.readthedocs.io/en/latest/user/advanced/#session-objects
    s = requests.session()
    for i in range(5):
        start = time.perf_counter()
        s.get('https://google.com')
        request_time = time.perf_counter() - start
        print(f'reuse session to access google.com {i+1} times response time: {request_time} s')


if __name__ == '__main__':
    main()
