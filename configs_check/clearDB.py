# coding=utf-8
"""
Created on 2017年3月3日

@author: EP-Admin
"""
import argparse
from bson.objectid import ObjectId

from epMongo import EPMongo
import utils

SPACE = '  '


def clear_order_by_order_number(ep, order_number):
    order_id = ep.get_doc_id_by_query('orders', {'order_number': order_number})
    if order_id is not None:
        utils.line()
        print('Remove order_number={order_number}'.format(order_number=order_number))
        print('{count} order(s) removed'.format(count=ep.delete_many_by_query('orders', {'_id': order_id})))
        print('{count} orderentry(s) removed'.format(
            count=ep.delete_many_by_query('orderentries', {'order': order_id})))
        print('{count} productconfig(s) removed'.format(
            count=ep.delete_many_by_query('productconfigs', {'order': order_id})))
        print('{count} event(s) removed'.format(count=ep.delete_many_by_query('events', {'order': order_id})))
        print('{count} feedback(s) removed'.format(
            count=ep.delete_many_by_query('feedbacks', {'order': order_id})))
        print('{count} accessclaim(s) removed'.format(
            count=ep.delete_many_by_query('accessclaims', {'resourceId': str(order_id)})))
        print('{count} message(s) removed'.format(
            count=ep.delete_many_by_query('messages', {'order': order_id})))


def clear_order_by_order_id(ep, order_id, level):
    utils.line()
    print(SPACE * level + 'Remove order_id={order_id}'.format(order_id=order_id))
    print(SPACE * level + '{count} order removed'.format(
        count=ep.delete_many_by_query('orders', {'_id': order_id})))
    print(SPACE * level + '{count} orderentry(s) removed'.format(
        count=ep.delete_many_by_query('orderentries', {'order': order_id})))
    print(SPACE * level + '{count} productconfig(s) removed'.format(
        count=ep.delete_many_by_query('productconfigs', {'order': order_id})))
    print(SPACE * level + '{count} event(s) removed'.format(
        count=ep.delete_many_by_query('events', {'order': order_id})))
    print(SPACE * level + '{count} feedback(s) removed'.format(
        count=ep.delete_many_by_query('feedbacks', {'order': order_id})))
    print(SPACE * level + '{count} accessclaim(s) removed'.format(
        count=ep.delete_many_by_query('accessclaims', {'resourceId': str(order_id)})))
    print(SPACE * level + '{count} message(s) removed'.format(
        count=ep.delete_many_by_query('messages', {'order': order_id, 'type': 'Order'})))
    print(SPACE * level + '{count} inquiryorder(s) removed'.format(
        count=ep.delete_many_by_query('inquiryorders', {'order': order_id})))


def clear_voyage_by_voyage_id(ep, voyage_id, level):
    utils.line()
    print(SPACE * level + 'Remove voyage_id={voyage_id}'.format(voyage_id=voyage_id))
    print(SPACE * level + '{count} voyage(s) removed'.format(
        count=ep.delete_many_by_query('voyagesegments', {'_id': voyage_id})))
    print(SPACE * level + '{count} message(s) removed'.format(
        count=ep.delete_many_by_query('messages', {'voyage': voyage_id, 'type': 'Voyage'})))
    order_ids = ep.get_ids_by_query('orders', {'segment': voyage_id}, '_id')
    level += 1
    for i, order_id in enumerate(order_ids, 1):
        utils.line()
        print(SPACE * level + 'order {number}'.format(number=str(i)))
        clear_order_by_order_id(ep, order_id, level)


def clear_ship_by_ship_id(ep, ship_id, level):
    utils.line()
    print(SPACE * level + 'Remove ship_id={ship_id}'.format(ship_id=ship_id))
    voyage_ids = ep.get_ids_by_query('voyagesegments', {'ship': ship_id}, '_id')
    level += 1
    for i, voyage_id in enumerate(voyage_ids, 1):
        utils.line()
        print(SPACE * level + 'voyage {number}'.format(number=str(i)))
        clear_voyage_by_voyage_id(ep, voyage_id, level)


def clear_user_by_username(ep, username, level):
    utils.line()
    print(SPACE * level + 'Remove user={user}'.format(user=username))
    print(ep.get_doc_by_query('users', {'username': username}))
    position_id = ep.get_doc_by_query('users', {'username': username}).get('position')
    group_id = ep.get_doc_by_query('userpositions', {'_id': position_id}).get('group')
    account_id = ep.get_doc_by_query('usergroups', {'_id': group_id}).get('account')
    organization_id = ep.get_doc_by_query('accounts', {'_id': account_id}).get('organization')
    print(position_id, group_id, account_id, organization_id)
    ep.delete_one_by_query('users', {'username': username})
    ep.delete_one_by_query('userpositions', {'_id': position_id})
    ep.delete_one_by_query('usergroups', {'_id': group_id})
    ep.delete_one_by_query('accounts', {'_id': account_id})
    ep.delete_one_by_query('organizations', {'_id': organization_id})
    ep.delete_one_by_query('accessclaims', {'gid': str(group_id)})


def get_user_by_username(ep, username, level):
    utils.line()
    print(SPACE * level + 'Get user={user}'.format(user=username))
    print(ep.get_doc_by_query('users', {'username': username}))
    position_id = ep.get_doc_by_query('users', {'username': username}).get('position')
    group_id = ep.get_doc_by_query('userpositions', {'_id': position_id}).get('group')
    account_id = ep.get_doc_by_query('usergroups', {'_id': group_id}).get('account')
    organization_id = ep.get_doc_by_query('accounts', {'_id': account_id}).get('organization')
    print('position_id={position_id}, group_id={group_id}, account_id={account_id}, organization={organization_id}'.format(position_id=position_id, group_id=group_id, account_id=account_id, organization_id=organization_id))


def get_users_by_account_id(ep, account_id, level):
    utils.line()
    print(SPACE * level + 'Get users by account_id={account_id}'.format(account_id=account_id))
    print(ep.get_doc_by_query('accounts', {'_id': account_id}))
    organization_id = ep.get_doc_by_query('accounts', {'_id': account_id}).get('organization')
    group_ids = ep.get_ids_by_query('usergroups', {'account': account_id}, '_id')
    position_ids = []
    for group_id in group_ids:
        ids = ep.get_ids_by_query('userpositions', {'group': group_id}, '_id')
        position_ids.append((group_id, ids))
    # print('[(group, positions)]', position_ids)
    users = []
    for (group_id, positions) in position_ids:
        for position_id in positions:
            user = ep.get_doc_by_query('users', {'position': position_id})
            username = user.get('username')
            user_group = user.get('group')
            date_delete = user.get('dateDelete')
            if date_delete is None:
                date_delete = 'No'
            else:
                date_delete = 'Yes'
            group_flag = ep.get_doc_by_query('usergroups', {'_id': group_id}).get('default')
            user_id = user.get('_id')
            isSuperAdmin = user.get('isSuperAdmin')
            users.append((user_id, username, date_delete, isSuperAdmin, position_id, group_id, group_flag, user_group))
    for i, (user_id, username, date_delete, isSuperAdmin, position_id, group_id, group_flag, user_group) in enumerate(users, 1):
        print(
            '{i} {user_id}, dateDelete={date_delete}, username={username}, isSuperAdmin={isSuperAdmin}, position={position_id}, group={group_id}({flag}), user.group={user_group}, organization={organization_id}'.format(
                i=i, user_id=user_id, username=username, date_delete=date_delete, isSuperAdmin=isSuperAdmin, position_id=position_id,
                group_id=group_id, flag=group_flag, user_group=user_group, organization_id=organization_id))
        # print(ep.update_one('users', {'username': username}, {"$set":{'account': account_id, 'group': group_id}}))


def delete_users_by_account_id(ep, account_id, level):
    utils.line()
    print(SPACE * level + 'Get users by account_id={account_id}'.format(account_id=account_id))
    print(ep.get_doc_by_query('accounts', {'_id': account_id}))
    organization_id = ep.get_doc_by_query('accounts', {'_id': account_id}).get('organization')
    group_ids = ep.get_ids_by_query('usergroups', {'account': account_id}, '_id')
    position_ids = []
    for group_id in group_ids:
        ids = ep.get_ids_by_query('userpositions', {'group': group_id}, '_id')
        position_ids.append((group_id, ids))
    # print('[(group, positions)]', position_ids)
    users = []
    for (group_id, positions) in position_ids:
        for position_id in positions:
            user = ep.get_doc_by_query('users', {'position': position_id})
            username = user.get('username')
            group_flag = ep.get_doc_by_query('usergroups', {'_id': group_id}).get('default')
            user_id = user.get('_id')
            isSuperAdmin = user.get('isSuperAdmin')
            users.append((user_id, username, isSuperAdmin, position_id, group_id, group_flag))
    for i, (user_id, username, isSuperAdmin, position_id, group_id, group_flag) in enumerate(users, 1):
        print(ep.delete_one_by_query('users', {'username': username}))
        print(ep.delete_one_by_query('userpositions', {'_id': position_id}))
        print(ep.delete_one_by_query('usergroups', {'_id': group_id}))
    print(ep.delete_one_by_query('accounts', {'_id': account_id}))
    print(ep.delete_one_by_query('organizations', {'_id': organization_id}))


def main():
    epmongo = EPMongo(uri="mongodb://root:gEUMooTG0d%23pd1%24YX@172.16.100.1:30001,172.16.100.11:30001,172.16.120.30:30001", db_name='epdb-prod')
    # epmongo = EPMongo()
    parser = argparse.ArgumentParser(prog='clear ep db',
                                     description='clear ep db')

    parser.add_argument('c',
                        choices=['clear_order_by_order_number',
                                 'clear_order_by_order_id',
                                 'clear_voyage_by_voyage_id',
                                 'clear_ship_by_ship_id',
                                 'clear_user_by_username',
                                 'get_user_by_username',
                                 'get_users_by_account_id',
                                 'delete_users_by_account_id'],
                        help='commands for clear operations')

    parser.add_argument('d',
                        help='query condition')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    c = args.c
    d = args.d
    print(c, d)
    if c == 'clear_order_by_order_number':
        order_number = d
        clear_order_by_order_number(epmongo, order_number)
    if c == 'clear_order_by_order_id':
        order_id = ObjectId(d)
        clear_order_by_order_id(epmongo, order_id, 0)
    if c == 'clear_voyage_by_voyage_id':
        voyage_id = ObjectId(d)
        clear_voyage_by_voyage_id(epmongo, voyage_id, 0)
    if c == 'clear_ship_by_ship_id':
        ship_id = ObjectId(d)
        clear_ship_by_ship_id(epmongo, ship_id, 0)
    if c == 'clear_user_by_username':
        username = d
        clear_user_by_username(epmongo, username, 0)
    if c == 'get_user_by_username':
        username = d
        get_user_by_username(epmongo, username, 0)
    if c == 'get_users_by_account_id':
        account_id = ObjectId(d)
        get_users_by_account_id(epmongo, account_id, 0)
    if c == 'delete_users_by_account_id':
        account_id = ObjectId(d)
        delete_users_by_account_id(epmongo, account_id, 0)


if __name__ == '__main__':
    main()
