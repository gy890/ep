# coding=utf-8
"""
Created on 2017-12-11

@Filename: update_username_status
@Author: Gui


"""
import logging
import datetime
from epMongo import EPMongo

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    epmongo = EPMongo(
        uri="mongodb://root:gEUMooTG0d%23pd1%24YX@172.16.100.1:30001,172.16.100.11:30001,172.16.120.30:30001",
        db_name='epdb-prod')
    with open('mailers.txt') as f:
        users = [line.strip() for line in f.readlines()]
    now = datetime.datetime.utcnow()
    for i, username in enumerate(users, 1):
        logging.debug((i, username))
        logging.info(epmongo.update_one("users", {'username': username}, {"$set": {'status': "normal"}}))
        # logging.debug(epmongo.update_one("users", {'username': username}, {"$set": {'dateDelete': now}}))
