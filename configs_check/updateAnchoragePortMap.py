# coding=utf-8
"""
Created on 2017-04-05

@Filename: updateAnchoragePortMap
@Author: Gui

update anchorage port_id
"""
from epMongo import EPMongo


def get_ports(epmongo):
    port_documents = epmongo.get_all('ports')
    ports = []
    for port in enumerate(port_documents, 1):
        ports.append((port[1]['_id'], port[1]['anchorages']))
    return ports


def update_anchorages(epmongo, port):
    (port_id, anchorages) = port
    if len(anchorages) != 0:
        for anchorage in anchorages:
            query = {'_id': anchorage}
            update = {'$set': {'port': port_id}}
            print(epmongo.update_one('anchorages', query, update))


def main():
    epmongo = EPMongo()
    ports = get_ports(epmongo)
    for each in enumerate(ports):
        update_anchorages(epmongo, each[1])


if __name__ == '__main__':
    main()
