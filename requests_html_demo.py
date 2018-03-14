# coding=utf-8
"""
Created on 2018-02-26

@Filename: requests_html_demo
@Author: Gui


"""
from requests_html import session

r = session.get('https://python.org/')
print(r.html.links)
