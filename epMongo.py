# coding=utf-8
"""
Created on 2016年12月6日

@author: EP-Admin
"""
import pymongo
from bson.json_util import dumps


class EPError(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


class EPMongo(object):
    # test environment
    # def __init__(self, host="192.168.30.101", port=24017):
    #     client = pymongo.MongoClient(host, port)
    #     self.__dbName = 'epdb-tst'
    #     self.__db = client[self.__dbName]

    # product environment
    # def __init__(self):
    #     uri = "mongodb://root:gEUMooTG0d%23pd1%24YX@172.16.100.1:30001,172.16.100.11:30001,172.16.120.30:30001"
    #     client = pymongo.MongoClient(uri)
    #     print(client)
    #     self.__dbName = 'epdb-prod'
    #     self.__db = client[self.__dbName]

    # def __init__(self, uri="mongodb://172.16.100.104:27017", db_name='epdb-stg'):
    def __init__(self, uri="mongodb://192.168.30.102:29017", db_name='epdb-dev'):
        client = pymongo.MongoClient(uri)
        print(client)
        self.__dbName = db_name
        self.__db = client[self.__dbName]

    def get_collection_names(self):
        return self.__db.collection_names()

    def _check_name(self, collection_name):
        if collection_name not in self.get_collection_names():
            raise EPError('Collection[{0}] not in {1}'.format(collection_name, self.__dbName))
            #             raise EPErr("Collection[%s] not in %s" % (collection_name, self.__dbName))

    def get_collection(self, collection_name):
        self._check_name(collection_name)
        collection = self.__db[collection_name]
        results = []
        for _i, v in enumerate(collection.find()):
            #            print 1, type(v), v
            #            print 2, type(dumps(v)), dumps(v)
            results.append(dumps(v))
        return results

    def get_doc_id_by_query(self, collection_name, query):
        collection = self.__db[collection_name]
        doc = collection.find_one(query)
        if doc:
            return doc.get('_id')
        else:
            return None

    def get_doc_by_query(self, collection_name, query):
        collection = self.__db[collection_name]
        doc = collection.find_one(query)
        return doc

    def get_ids_by_query(self, collection_name, query, key_id):
        collection = self.__db[collection_name]
        find_results = collection.find(query)
        ids = []
        for _i, each in enumerate(find_results, 1):
            ids.append(each[key_id])
        return ids

    def delete_one_by_query(self, collection_name, query):
        collection = self.__db[collection_name]
        return collection.delete_one(query).deleted_count

    def delete_many_by_query(self, collection_name, query):
        collection = self.__db[collection_name]
        return collection.delete_many(query).deleted_count

    def get_all(self, collection_name):
        collection = self.__db[collection_name]
        find_results = collection.find()
        return find_results

    def update_one(self, collection_name, query, update):
        collection = self.__db[collection_name]
        return collection.update_one(query, update).raw_result
