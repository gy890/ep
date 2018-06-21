# coding=utf-8
"""
Created on 2018-05-24

@Filename: get_products
@Author: Gui


"""
import json

with open('a.json') as f:
    d = json.load(f)
    product = {}
    for each in d:
        k = each['code']
        v = each['name']
        product[k] = v
    print(product)
