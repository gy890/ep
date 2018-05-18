# coding=utf-8
"""
Created on 2018-05-02

@Filename: add_inquiry_order
@Author: Gui


"""
import logging
import datetime
import requests
import json
import timeit
import ORDERTYPES
import PRODUCTS
import SHIPSPORTS
import USERS

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


class OrderTypeNotExistsExcepiton(Exception):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        exception_msg = self.msg
        return exception_msg


@timeit.timeit
def get_cookie(data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'}
    payload = {
        'action': 'login',
        'request': data
    }
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    cookie = res.headers['x-session-id']
    return cookie


@timeit.timeit
def generate_inquiry_order_params(order_type):
    request_params = {}
    order_info = ORDERTYPES.ORDER_TYPES.get(order_type)
    if not order_info:
        raise OrderTypeNotExistsExcepiton('No order_type {}'.format(order_type))
    if order_type in ['OTNB', 'OTDD']:
        request_params.setdefault('orderInfo', {"ship": SHIPSPORTS.SHIP, "arrivalPort": SHIPSPORTS.SHANGHAI.get('_id'),
                                                "arrivalTime": (datetime.datetime.utcnow() + datetime.timedelta(
                                                    days=30)).isoformat(),
                                                "orderType": order_info.get('_id'),
                                                "shipyard": SHIPSPORTS.SHIPYARDS[0]})
    else:
        request_params.setdefault('orderInfo', {"ship": SHIPSPORTS.SHIP, "arrivalPort": SHIPSPORTS.SHANGHAI.get('_id'),
                                                "arrivalTime": (datetime.datetime.utcnow() + datetime.timedelta(
                                                    days=30)).isoformat(),
                                                "orderType": order_info.get('_id'),
                                                "terminal": SHIPSPORTS.TERMINALS[0]})
    default_products = order_info.get('defaults')
    products_info = ['PTOT']
    if default_products:
        products_info.extend(default_products[:])
    request_params.setdefault('products', products_info)
    request_params.setdefault('productConfig', PRODUCTS.PTOT2)
    return request_params


@timeit.timeit
def add_inquiry_order(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'addInquiryOrder',
        'request': data
    }
    logging.debug('[addInquiryOrder] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


def _omit_product(order_type):
    all = PRODUCTS.PRODUCTS_CONFIG.copy()
    if order_type in ['OTOPA', 'OTOT', 'OTMVS']:
        all.pop('PTIF')
        all.pop('PTOF')
        all.pop('PTOL')
        return all
    if order_type in ['OTPCD', 'OTPCL']:
        all.pop('PTIF')
        all.pop('PTOF')
        return all
    if order_type in ['OTNB']:
        all.pop('PTOL')
        all.pop('PTIF')
        return all
    if order_type in ['OTRV', 'OTDV', 'OTDD', 'OTBK', 'OTCL', 'OTCD']:
        all.pop('PTOL')
        return all


@timeit.timeit
def generate_add_order_entry_and_config_to_order(order_type, ship_type, order_id, k, v):
    config = v.copy()
    if k in ['PTIF', 'PTOF']:
        if order_type not in ['OTCL', 'OTCD']:  # 没有货物信息
            config.pop('cargoName')
            config.pop('cargoType')
            config.pop('cargoWeight')
            config.pop('cargoVolume')
            config.pop('shipDraft')
            config['isComplete'] = True
        elif ship_type == 'STGC':  # 有货物信息判断船舶类型
            config.pop('cargoName')
        else:
            config.pop('cargoType')
            config.pop('cargoVolume')
    request_params = {"id": order_id, "product": k, "config": config}
    return request_params


@timeit.timeit
def add_order_entry_and_config_to_order(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'addOrderEntryAndConfigToOrder',
        'request': data
    }
    logging.debug('[addOrderEntryAndConfigToOrder] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def generate_add_real_inquiry_order_params(order_type, order_id):
    request_params = {}
    order_info = ORDERTYPES.ORDER_TYPES.get(order_type)
    if not order_info:
        raise OrderTypeNotExistsExcepiton('No order_type {}'.format(order_type))
    if order_type in ['OTNB', 'OTDD']:
        request_params.setdefault('params', {"ship": SHIPSPORTS.SHIP, "arrivalPort": SHIPSPORTS.SHANGHAI.get('_id'),
                                             "arrivalTime": (datetime.datetime.utcnow() + datetime.timedelta(
                                                 days=30)).isoformat(),
                                             "orderType": order_info.get('_id'),
                                             "shipyard": SHIPSPORTS.SHIPYARDS[1]})
    else:
        request_params.setdefault('params', {"ship": SHIPSPORTS.SHIP, "arrivalPort": SHIPSPORTS.SHANGHAI.get('_id'),
                                             "arrivalTime": (datetime.datetime.utcnow() + datetime.timedelta(
                                                 days=30)).isoformat(),
                                             "orderType": order_info.get('_id'),
                                             "terminal": SHIPSPORTS.TERMINALS[1]})
    request_params.setdefault('id', order_id)
    return request_params


@timeit.timeit
def add_real_inquiry_order(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'addRealInquiryOrder',
        'request': data
    }
    logging.debug('[addRealInquiryOrder] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def find_order_by_id(data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
    }
    payload = {
        'action': 'findOrderById',
        'request': data
    }
    logging.debug('[findOrderById] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def generate_product_config(order_type, ship_type, entry_id, entry_v, order_id, order_v, product_config_id,
                            product_code):
    request_params = {}
    request_params.setdefault('orderEntryId', entry_id)
    request_params.setdefault('orderEntry_v', entry_v)
    request_params.setdefault('orderId', order_id)
    request_params.setdefault('order_v', order_v)

    all = PRODUCTS.PRODUCTS_CONFIG
    v = all.get(product_code)
    config = v.copy()
    if product_code in ['PTIF', 'PTOF']:  # 判断是不是inward-outward
        if order_type not in ['OTCL', 'OTCD']:  # 没有货物信息
            config.pop('cargoName')
            config.pop('cargoType')
            config.pop('cargoWeight')
            config.pop('cargoVolume')
            config.pop('shipDraft')
            config['isComplete'] = True
        elif order_type in ['OTCL', 'OTCD'] and ship_type == 'STGC':  # 有货物信息判断船舶类型
            config.pop('cargoName')
        elif order_type in ['OTCL', 'OTCD'] and ship_type != 'STGC':
            config.pop('cargoType')
            config.pop('cargoVolume')
    else:
        pass
    config['_id'] = product_config_id
    request_params.setdefault('productConfig', config)
    return request_params


@timeit.timeit
def update_product_config(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'updateProductConfig',
        'request': data
    }
    logging.debug('[updateProductConfig] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def generate_create_inquiry_orders_params(order_id, anonymous=False):
    params = {}
    params.setdefault('orderId', order_id)
    params.setdefault('anonymous', anonymous)
    params.setdefault('accIds', USERS.ACCIDS)
    request_params = {}
    request_params.setdefault('params', params)
    return request_params


@timeit.timeit
def create_inquiry_orders(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'createInquiryOrders',
        'request': data
    }
    logging.debug('[createInquiryOrders] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def _find_inquiry_orders_by_order_id(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'findInquiryOrdersByOrderId',
        'request': data
    }
    logging.debug('[findInquiryOrdersByOrderId] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def get_inquiry_order(consigner_cookie, order_id):
    request_data = {'orderId': order_id}
    consignee_id = USERS.ACCIDS[1]['_id']
    for inquiry_order in _find_inquiry_orders_by_order_id(consigner_cookie, request_data).json()['response']:
        consignee = inquiry_order['consignee']['_id']
        if consignee == consignee_id:
            return inquiry_order.get('_id')


@timeit.timeit
def find_inquiry_order_by_id(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'findInquiryOrderById',
        'request': data
    }
    logging.debug('[findInquiryOrderById] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


def _cost_type_tags_check(order_type, cost_type):
    flag = True
    if 'tags' in cost_type.keys():
        tags = [tag['orderTypeCode'] for tag in cost_type['tags']]
        if order_type not in tags:
            flag = False
    return flag


def generate_product_costs(order_type, order_id, inquiry_order_id, currency, product_id, entry_id, cost_types):
    params = {}
    request_params = {}
    costItemsEstimated = []
    amountEstimated = 0
    for c in cost_types:
        DESCRIPTION = 'This is description.\nThis is description.'
        AMOUNT = 1
        one = {}
        if _cost_type_tags_check(order_type, c):
            one.setdefault('product', product_id)
            one.setdefault('amount', AMOUNT)
            one.setdefault('amountRMB', AMOUNT * currency)
            one.setdefault('description', DESCRIPTION)
            one.setdefault('costType', c['costType']['_id'])
            if c['costType']['_id'] == '56651b9c5b4f53742b804e73':
                one.setdefault('subName', 'my name is others')
            amountEstimated = amountEstimated + AMOUNT
            costItemsEstimated.append(one)
    params.setdefault('amountEstimated', amountEstimated)
    params.setdefault('costItemsEstimated', costItemsEstimated)
    params.setdefault('orderEntryId', entry_id)
    params.setdefault('id', inquiry_order_id)
    params.setdefault('orderId', order_id)
    request_params.setdefault('params', params)
    return request_params


@timeit.timeit
def update_inquiry_order_cost_items(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'updateInquiryOrderCostItems',
        'request': data
    }
    logging.debug('[updateInquiryOrderCostItems] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def set_order_quotation(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'setOrderQuotation',
        'request': data
    }
    logging.debug('[setOrderQuotation] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


@timeit.timeit
def generate_appointment_agent_params(checked_service_items, order_id, inquiry_order_id):
    params = {}
    params.setdefault('consignee', USERS.APPOINTMENT_CONSIGNEE)
    params.setdefault('accIds', USERS.APPOINTMENT_ACCIDS)
    params.setdefault('instruction', 'instruction, instruction, instruction')
    params.setdefault('ship', SHIPSPORTS.SHIP['_id'])
    params.setdefault('isPostalAddress', False)
    params.setdefault('address', ["mail@mail.com", "mail2@mail.com"])
    params.setdefault('order', order_id)
    params.setdefault('orderId', order_id)
    params.setdefault('inquiryOrderId', inquiry_order_id)
    params.setdefault('payStatus', 2)
    params.setdefault('checkedServiceItems', checked_service_items)
    request_params = {}
    request_params.setdefault('params', params)
    return request_params


@timeit.timeit
def appointment_agent(cookie, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
        'x-session-id': cookie,
    }
    payload = {
        'action': 'appointmentAgent',
        'request': data
    }
    logging.debug('[appointmentAgent] {}'.format(payload))
    res = requests.post('http://dev.e-ports.com/api/', data=json.dumps(payload), headers=headers)
    logging.debug(res.elapsed)
    logging.debug(res)
    return res


def main():
    # order_type = 'OTBK'
    order_type = 'OTCD'
    # order_type = 'OTPCD'
    # order_type = 'OTOPA'

    # order_type = "OTDV"
    # order_type = "OTMVS"
    # order_type = "OTPCL"
    # order_type = "OTNB"
    # order_type = "OTCD"
    # order_type = "OTRV"
    # order_type = "OTBK"
    # order_type = "OTDD"
    # order_type = "OTPCD"
    # order_type = "OTCL"
    # order_type = "OTOPA"
    # order_type = "OTOT"

    consigner_cookie = get_cookie(USERS.CONSIGNER)

    logging.info('--> addInquiryOrder...')
    inquiry_order_params = generate_inquiry_order_params(order_type)
    res = add_inquiry_order(consigner_cookie, inquiry_order_params).json()
    order_id = res['response']['_id']
    ship_type = res['response']['ship']['type']

    logging.info('--> addOrderEntryAndConfigToOrder...')
    products = _omit_product(order_type)
    for k, v in products.items():
        data = generate_add_order_entry_and_config_to_order(order_type, ship_type, order_id, k, v)
        logging.info('Add service {{{}}}'.format(k))
        add_order_entry_and_config_to_order(consigner_cookie, data).json()

    add_real_inquiry_order_params = generate_add_real_inquiry_order_params(order_type, order_id)
    add_real_inquiry_order(consigner_cookie, add_real_inquiry_order_params)

    # input('Press any key to continue')

    # logging.info('--> updateProductConfig...')
    # res = find_order_by_id({'id': order_id}).json()
    # order_v = res['response']['__v']
    # for i, entry in enumerate(res['response']['orderEntries'], 1):
    #     product_config_id = entry['productConfig']['_id']
    #     product_code = entry['product']['code']
    #     entry_id = entry['_id']
    #     entry_v = entry['__v']
    #     if product_code != 'PTAGT':
    #         product_config = generate_product_config(order_type, ship_type, entry_id, entry_v, order_id, order_v,
    #                                                  product_config_id, product_code)
    #         logging.info('Update service {{{}}}'.format(product_code))
    #         res = update_product_config(consigner_cookie, product_config).json()
    #         order_v = res['response']['__v']

    # input('Press any key to continue')

    logging.info('--> createInquiryOrders...')
    create_inquiry_orders_params = generate_create_inquiry_orders_params(order_id)
    create_inquiry_orders(consigner_cookie, create_inquiry_orders_params)

    inquiry_order_id = get_inquiry_order(consigner_cookie, order_id)  # 获取inquiryOrder._id

    consignee_cookie = get_cookie(USERS.CONSIGNEE)
    logging.info('--> findInquiryOrderById...')
    res = find_inquiry_order_by_id(consignee_cookie, {'id': inquiry_order_id}).json()
    currency = res['response']['currentExchange']  # 获取汇率，用于代理方报价

    logging.info('--> updateInquiryOrderCostItems...')
    for i, entry in enumerate(res['response']['orderEntries'], 1):
        product_id = entry['orderEntry']['product']['_id']
        entry_id = entry['_id']
        cost_types = entry['orderEntry']['productConfig']['products'][0]['product']['costTypes']
        product_code = entry['orderEntry']['product']['code']
        logging.info('Quote service {{{}}}'.format(product_code))
        cost_config = generate_product_costs(order_type, order_id, inquiry_order_id, currency, product_id, entry_id,
                                             cost_types)
        update_inquiry_order_cost_items(consignee_cookie, cost_config)

    # input('Press any key to continue')

    logging.info('--> setOrderQuotation...')
    set_order_quotation(consignee_cookie, {"id": inquiry_order_id, "orderId": order_id})

    # input('Press any key to continue')

    logging.info('--> appointmentAgent...')
    res = find_inquiry_order_by_id(consigner_cookie, {'id': inquiry_order_id}).json()
    selected_order_entries = [entry['orderEntry']['_id'] for entry in res['response']['orderEntries']]
    request_data = generate_appointment_agent_params(selected_order_entries, order_id, inquiry_order_id)
    appointment_agent(consigner_cookie, request_data)


if __name__ == '__main__':
    main()
