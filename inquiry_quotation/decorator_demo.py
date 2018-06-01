# coding=utf-8
"""
Created on 2018-05-29

@Filename: decorator_demo
@Author: Gui


"""
from functools import wraps
import requests

cookie = 'EWRETETETEWT'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


def role_a(cookie):
    def decorate(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            result = func(cookie, *args, **kwargs)
            return result

        return wrapped

    return decorate


@role_a(None)
def f(cookie, data):
    header = HEADERS.copy()
    if cookie:
        header.setdefault('cookie', cookie)
    res = requests.post('http://httpbin.org/post', data=data, headers=header)
    return res


data = {'key': 'value'}
r = f(data)
print(r.request.headers.get('cookie'))
