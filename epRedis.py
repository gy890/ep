# coding=utf-8
"""
Created on 2017年3月3日

@author: EP-Admin
"""
import redis


class EPRedis(object):
    REDIS_PREFIX_EPSES_DEVICE = b"EPSES:DEVICE:"
    REDIS_PREFIX_EPSES_USER = b"EPSES:USER:"
    REDIS_PREFIX_EPSES_SESSION = b"EPSES:"

    def __init__(self, host="192.168.30.102", port=7000, db=0):
        self.__r = redis.StrictRedis(host, port, db)
        print(self.__r.hgetall('EPSES:USER:5a1bce08baefca0700cc73d3'))
        self.__keys = self.__r.keys()

    def get_user_keys_without_prefix(self):
        user_keys = []
        for each in self.__keys:
            if EPRedis.REDIS_PREFIX_EPSES_USER in each:
                user_keys.append(each.split(EPRedis.REDIS_PREFIX_EPSES_USER)[1])
        return user_keys

    def get_device_keys_without_prefix(self):
        device_keys = []
        for each in self.__keys:
            if EPRedis.REDIS_PREFIX_EPSES_DEVICE in each:
                device_keys.append(each.split(EPRedis.REDIS_PREFIX_EPSES_DEVICE)[1])
        return device_keys

    def get_session_keys_without_prefix(self):
        session_keys = []
        for each in self.__keys:
            if EPRedis.REDIS_PREFIX_EPSES_SESSION in each:
                session_keys.append(each.split(EPRedis.REDIS_PREFIX_EPSES_SESSION)[1])
        return session_keys


redis = EPRedis()

# sessions = redis.get_session_keys_without_prefix()
# user_sessions = redis.get_user_keys_without_prefix()
# device_sessions = redis.get_device_keys_without_prefix()
# print(len(sessions), sessions)
# print(len(user_sessions), user_sessions)
# print(len(device_sessions), device_sessions)
# for each in sessions:
#     print(each)
