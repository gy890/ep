# coding=utf-8
"""
Created on 2016年12月6日

@author: EP-Admin
"""
from bson.json_util import loads


def line():
    print('*'*64)


# dict {u'PTFRWKPMT': {u'CTTNCG': 100, u'CTHGCG': 50}, u'PTOFFHBKSV': {u'CTSVCG':...}}
def get_product_fee_dict_in_fees(epmongo):
    fees_results = epmongo.get_collection('fees')
    dict_fees = loads(fees_results[0])  # fees只有一条document
    return dict_fees['fee']


# dict {1: (u'SPRO/Sludge/Garbage', u'PTSPSLGA'), 2: (u'SPRO', u'PTSPRO'), ...}
def get_name_code_dict_in_products(epmongo):
    products_results = epmongo.get_collection('products')
    dict1 = {}
    i = 1
    for p in products_results:
        name = loads(p)['name']
        code = loads(p)['code']
        dict1[i] = (name, code)
        i += 1
    return dict1
