# coding=utf-8
'''
Created on 2016年12月6日

@author: EP-Admin
'''
import epMongo
import utils


if __name__ == '__main__':
    epmongo = epMongo.EPMongo()
    
    utils.line()
    dict1 = utils.get_product_fee_dict_in_fees(epmongo)
    codesList1 = dict1.keys()
    print('inFees', codesList1)
    
    utils.line()
    dict2 = utils.get_name_code_dict_in_products(epmongo)
    codesList2 = [code for (name, code) in dict2.values()]
    print('inProducts',  codesList2)
    
    utils.line()
    invalidItems = [a for a in codesList1 if a not in codesList2]
    print('invalidItems(in Fees but not in Products):', invalidItems)