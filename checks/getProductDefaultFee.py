# coding=utf-8
"""
Created on 2016年12月6日

@author: EP-Admin
"""
import epMongo
import utils

if __name__ == '__main__':
    epmongo = epMongo.EPMongo()
    dictProducts = utils.get_name_code_dict_in_products(epmongo)
    dictFees = utils.get_product_fee_dict_in_fees(epmongo)
    utils.line()
    for i, (_name, _code) in dictProducts.items():
        print(i, _name, '->', _code)
    flag = True
    while flag:
        utils.line()
        p = input('Please input the product number(as below), "Q" to exit: ')
        if p.upper() == 'Q':
            flag = False
        else:
            name, code = dictProducts.get(int(p))
            if code in dictFees.keys():
                print(name, '->', code, dictFees[code])
            else:
                print(p, name, '->', code, 'has no default fee.')