# coding=utf-8
"""
Created on 2017-12-28

@Filename: update_organization_status
@Author: Gui


"""
import logging
import datetime
from epMongo import EPMongo
from bson.objectid import ObjectId

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    now = datetime.datetime.utcnow()
    print(type(now), now)
    epmongo = EPMongo()
    # epmongo = EPMongo(
    #     uri="mongodb://root:gEUMooTG0d%23pd1%24YX@172.16.100.1:30001,172.16.100.11:30001,172.16.120.30:30001",
    #     db_name='epdb-prod')
    with open('shipIds.txt') as f:
        ships = [line.strip() for line in f.readlines()]
    for i, ship_id in enumerate(ships, 1):
        logging.debug((i, ship_id))
        logging.debug(epmongo.update_one("ships", {'_id': ObjectId(ship_id)}, {"$set": {"dateDelete": now}}))
