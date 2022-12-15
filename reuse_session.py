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
        print(f'reuse session to access google.com {i + 1} times response time: {request_time} s')


# open new session every request
# open new session to access google.com 1 times response time: 1.236115003 s
# open new session to access google.com 2 times response time: 0.928019769 s
# open new session to access google.com 3 times response time: 0.9133083279999998 s
# open new session to access google.com 4 times response time: 0.9246053819999998 s
# open new session to access google.com 5 times response time: 0.9143969910000003 s
# reuse session
# reuse session to access google.com 1 times response time: 0.9142738250000004 s
# reuse session to access google.com 2 times response time: 0.35572824599999997 s
# reuse session to access google.com 3 times response time: 0.3535390610000002 s
# reuse session to access google.com 4 times response time: 0.357659398 s
# reuse session to access google.com 5 times response time: 0.3502490379999994 s


if __name__ == '__main__':
    main()
