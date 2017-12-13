# coding=utf-8
"""
Created on 2017年3月3日

@author: EP-Admin
"""
import redis


class EPRedis(object):
    REDIS_PREFIX_EPSES_DEVICE = "EPSES:DEVICE:"
    REDIS_PREFIX_EPSES_USER = "EPSES:USER:"
    REDIS_PREFIX_EPSES_SESSION = "EPSES:"

    def __init__(self, host="192.168.30.101'", port=6379, db=0):
        self.__r = redis.StrictRedis(host, port, db)
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
