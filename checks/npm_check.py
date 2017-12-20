# coding=utf-8
"""
Created on 2017-07-17

@Filename: npm_check
@Author: Gui


"""
import requests


class EPNpm(object):
    def __init__(self):
        pass

    def check(self):
        print(self._get_latest_intl())
        print(self._get_latest_md())
        print(self._get_latest_auth())
        print(self._get_latest_chatting())
        print(self._get_latest_epds())
        print(self._get_latest_event())
        print(self._get_latest_message())
        print(self._get_latest_order())
        print(self._get_latest_user())

    def _get_latest_intl(self):
        res = requests.get('http://npm.e-ports.com/epui-intl/latest')
        intl = {'epui-intl': res.json()['version']}
        return intl

    def _get_latest_md(self):
        res = requests.get('http://npm.e-ports.com/epui-md/latest')
        md = {'epui-md': res.json()['version']}
        return md

    def _get_latest_auth(self):
        res = requests.get('http://npm.e-ports.com/ep-api-auth/latest')
        auth = {'ep-api-auth': res.json()['version']}
        return auth

    def _get_latest_chatting(self):
        res = requests.get('http://npm.e-ports.com/ep-api-chatting/latest')
        chatting = {'ep-api-chatting': res.json()['version']}
        return chatting

    def _get_latest_epds(self):
        res = requests.get('http://npm.e-ports.com/ep-api-epds/latest')
        epds = {'ep-api-epds': res.json()['version']}
        return epds

    def _get_latest_event(self):
        res = requests.get('http://npm.e-ports.com/ep-api-event/latest')
        event = {'ep-api-event': res.json()['version']}
        return event

    def _get_latest_message(self):
        res = requests.get('http://npm.e-ports.com/ep-api-message/latest')
        message = {'ep-api-message': res.json()['version']}
        return message

    def _get_latest_order(self):
        res = requests.get('http://npm.e-ports.com/ep-api-order/latest')
        order = {'ep-api-order': res.json()['version']}
        return order

    def _get_latest_user(self):
        res = requests.get('http://npm.e-ports.com/ep-api-user/latest')
        user = {'ep-api-user': res.json()['version']}
        return user


if __name__ == '__main__':
    npm = EPNpm()
    npm.check()
    print(EPNpm.__name__)
    print(EPNpm.__doc__)
    print(EPNpm.__dict__)
    print(EPNpm.__bases__)
    print(EPNpm.__module__)
    print(EPNpm.__class__)
    print(npm.__class__)
