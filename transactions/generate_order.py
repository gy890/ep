# coding=utf-8
"""
Created on 2018-01-18

@Filename: generate_order
@Author: Gui


"""
import sys
import datetime
import logging
import collections
import requests
import json
import timeit


@timeit.timeit
def generate_params(order_type=1):
    """
    读取委托方账号，代理方账号，订单参数
    :return: consigner, consignee, order_params
    """
    if order_type not in [1, 2, 3]:
        sys.exit('order_type must be in [1, 2, 3].')
    from yaml import load
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader
    with open('dev.yml') as f:
        config = f.read()
    config = load(config, Loader)

    url = config['url']
    consigner = {}
    consignee = {}
    consigner['username'] = config['consigner'][0]['username']
    consigner['password'] = config['consigner'][0]['password']
    consignee['username'] = config['consignee'][0]['username']
    consignee['password'] = config['consignee'][0]['password']

    order = {}
    arrival_time = (datetime.datetime.utcnow() + datetime.timedelta(days=30)).isoformat()
    order['arrivalTime'] = arrival_time
    arrival_port = config['ports'][0]['id']
    order['arrivalPort'] = arrival_port

    products = config['products']
    if order_type == 1:
        products.pop('PTIF')
        products.pop('PTCPD')
        products.pop('PTOL')
        order['type'] = config['ordertypes'][0]['id']
        order['shipyard'] = list(config['ports'][0]['shipyards'].keys())[0]
    if order_type == 2:
        products.pop('PTCPD')
        products.pop('PTOL')
        order['type'] = config['ordertypes'][1]['id']
        order['shipyard'] = list(config['ports'][0]['shipyards'].keys())[1]
    if order_type == 3:
        products.pop('PTIF')
        products.pop('PTOF')
        order['type'] = config['ordertypes'][2]['id']
        order['terminal'] = list(config['ports'][0]['terminals'].keys())[0]

    products_ordered = collections.OrderedDict()
    for k, v in sorted(products.items(), key=lambda products: products[0]):
        products_ordered[k] = v
    order_params = {'order': order, 'orderEntries': products_ordered}
    port_services = [order_params]

    params = {'anonymous': False}
    params.setdefault('ship', config['ships'][0])
    params.setdefault('portAndServices', port_services)
    request_param = {}
    request_param.setdefault('params', params)

    agent = {}
    agent.setdefault('_id', config['consignee'][0]['account'])
    agent.setdefault('name', config['consignee'][0]['account_name'])
    agent.setdefault('email', config['consignee'][0]['username'])

    return url, consigner, consignee, request_param, agent


@timeit.timeit
def get_cookie(url, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'}
    payload = {
        'action': 'login',
        'request': data
    }
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    cookie = res.headers['x-session-id']
    return cookie


@timeit.timeit
def add_inquiry_orders(url, data, cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'addInquiryOrders',
        'request': data
    }
    # print(json.dumps(payload))
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    return res.json()


@timeit.timeit
def create_inquiry_orders(url, agent, order_id, cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'createInquiryOrders',
        'request': {'params': {'accIds': [agent], 'orderId': order_id}}
    }
    # print(json.dumps(payload))
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    return res.json()


@timeit.timeit
def findOrder_by_id(url, order_id, cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'findOrderById',
        'request': {'id': order_id}
    }
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    return res.json()


@timeit.timeit
def find_inquiry_order_by_id(url, inquiry_order_id, cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'findInquiryOrderById',
        'request': {'id': inquiry_order_id}
    }
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    return res.json()


@timeit.timeit
def set_order_quotation(url, inquiry_order_id, order_id, cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'setOrderQuotation',
        'request': {'id': inquiry_order_id, 'orderId': order_id}
    }
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    return res.json()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    url, consigner, consignee, order_param, agent_params = generate_params(order_type=1)
    cookie = get_cookie(url, consigner)
    logging.info('--> Consigner[%s] logined' % consigner['username'])
    order_id = add_inquiry_orders(url, order_param, cookie)['response']['entries'][0]
    logging.info('--> Consigner create inquiry order: %s' % order_id)
    logging.info(create_inquiry_orders(url, agent_params, order_id, cookie))
    logging.info('--> Consigner publish inquiry to %s(%s)' % (agent_params['name'], agent_params['_id']))
    inquiry_id = findOrder_by_id(url, order_id, cookie)['response']['inquiryOrder'][0]['_id']
    logging.info('--> Get inquiry_order_id: %s' % inquiry_id)

    cookie2 = get_cookie(url, consignee)
    logging.info('--> Consignee[%s] logined' % consignee['username'])
    order_id2 = find_inquiry_order_by_id(url, inquiry_id, cookie2)['response']['_id']
    logging.info('--> Consignee get order_id: %s' % order_id2)
    logging.info(set_order_quotation(url, inquiry_id, order_id2, cookie2))
    logging.info('--> Consignee set order[%s] quoted' % order_id2)

    order_id3 = find_inquiry_order_by_id(url, inquiry_id, cookie)['response']['_id']
    logging.info('--> order: %s' % order_id3)
