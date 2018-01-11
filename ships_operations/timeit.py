# coding=utf-8
"""
Created on 2017-12-19

@Filename: timeit
@Author: Gui


"""
import time
import logging

logger = logging.basicConfig(level=logging.DEBUG,
                             format='%(asctime)s %(levelname)s: %(message)s')


def timeit(func):
    def wrapped(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        t = '%.3f' % (t2 - t1)
        logging.debug('{} costs {} s.'.format(func.__name__, t))
        return result

    return wrapped
