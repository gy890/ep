# coding=utf-8
"""
Created on 2017-06-02

@Filename: getPorts
@Author: Gui


"""
from bson.json_util import loads
import epMongo


def get_ports(epmongo, terminals):
    results = epmongo.get_collection('ports')
    dict1 = {}
    invaild_ports = ['test1', 'PROT2']
    for r in results:
        code = loads(r)['code']
        if code not in invaild_ports:
            name = loads(r)['name']
            port_terminals = loads(r)['terminals']
            terminals_list = []
            for terminal_id in port_terminals:
                terminal_dict = {str(terminal_id): terminals[terminal_id][0]}
                terminals_list.append(terminal_dict)
            terminals_list.insert(0, name)
            dict1[code] = terminals_list
    print(len(dict1))
    return dict1


def get_terminals(epmongo):
    results = epmongo.get_collection('terminals')
    dict1 = {}
    for r in results:
        object_id = loads(r)['_id']
        name = loads(r)['name']
        port = loads(r)['port']
        dict1[object_id] = (name, port)
    return dict1

if __name__ == '__main__':
    epmongo = epMongo.EPMongo()
    terminals = get_terminals(epmongo)
    print(terminals)
    print(get_ports(epmongo, terminals))
    for (k, v) in get_ports(epmongo, terminals).items():
        if len(v) == 1:
            print(k)
