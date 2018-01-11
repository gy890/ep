# coding=utf-8
"""
Created on 2018-01-10

@Filename: check_ships
@Author: Gui


"""
import timeit
from epMongo import EPMongo


class CHECK(object):
    def __init__(self):
        with open('check_ships.txt') as f:
            self._ships = [l.strip() for l in f.readlines()]
            # self._epmongo = EPMongo()
        self._epmongo = EPMongo(
            uri="mongodb://root:gEUMooTG0d%23pd1%24YX@172.16.100.1:30001,172.16.100.11:30001,172.16.120.30:30001",
            db_name='epdb-prod')

    @timeit.timeit
    def check_orders(self):
        results = []
        docs = self._epmongo.get_docs_by_query('orders', {}, {'_id': 1, 'ship': 1})
        for i, doc in enumerate(docs, 1):
            if str(doc.get('ship')) in self._ships:
                results.append(doc)
        return results

    @timeit.timeit
    def check_inquiryorders(self):
        results = []
        docs = self._epmongo.get_docs_by_query('inquiryorders', {}, {'_id': 1, 'ship': 1})
        for i, doc in enumerate(docs, 1):
            if str(doc.get('ship')) in self._ships:
                results.append(doc)
        return results

    @timeit.timeit
    def check_voyagesegments(self):
        results = []
        docs = self._epmongo.get_docs_by_query('voyagesegments', {}, {'_id': 1, 'ship': 1})
        for i, doc in enumerate(docs, 1):
            if str(doc.get('ship')) in self._ships:
                results.append(doc)
        return results

    @timeit.timeit
    def check_messages(self):
        results = []
        docs = self._epmongo.get_docs_by_query('messages', {}, {'_id': 1, 'ship': 1})
        for i, doc in enumerate(docs, 1):
            if str(doc.get('ship')) in self._ships:
                results.append(doc)
        return results

    @timeit.timeit
    def check_operationlogs(self):
        results = []
        docs = self._epmongo.get_docs_by_query('operationlogs', {}, {'_id': 1, 'ship': 1})
        for i, doc in enumerate(docs, 1):
            if str(doc.get('ship')) in self._ships:
                results.append(doc)
        return results

    @timeit.timeit
    def check_favships(self):
        results = []
        docs = self._epmongo.get_docs_by_query('favships', {}, {'_id': 1, 'ship': 1})
        for i, doc in enumerate(docs, 1):
            if str(doc.get('ship')) in self._ships:
                results.append(doc)
        return results

    @timeit.timeit
    def check_shipcorrections(self):
        results = []
        docs = self._epmongo.get_docs_by_query('shipcorrections', {}, {'_id': 1, 'ship': 1})
        for i, doc in enumerate(docs, 1):
            if str(doc.get('ship')) in self._ships:
                results.append(doc)
        return results

    @timeit.timeit
    def check_fleets(self):
        results = []
        docs = self._epmongo.get_docs_by_query('fleets', {}, {'_id': 1, 'ships': 1})
        for i, doc in enumerate(docs, 1):
            ships = doc.get('ships')
            for ship in ships:
                if str(ship) in self._ships:
                    results.append((doc, str(ship)))
        return results

    @timeit.timeit
    def check_ownerships(self):
        results = []
        docs = self._epmongo.get_docs_by_query('ownerships', {}, {'_id': 1, 'ships': 1})
        for i, doc in enumerate(docs, 1):
            ships = doc.get('ships')
            for ship in ships:
                if str(ship) in self._ships:
                    results.append((doc, str(ship)))
        return results


if __name__ == '__main__':
    checker = CHECK()
    orders_result = checker.check_orders()
    print('1 orders:', len(orders_result), orders_result)

    inquiryorders_result = checker.check_inquiryorders()
    print('2 inquiryorders:', len(inquiryorders_result), inquiryorders_result)

    voyagesegments_result = checker.check_voyagesegments()
    print('3 voyagesegments:', len(voyagesegments_result), voyagesegments_result)

    messages_result = checker.check_messages()
    print('4 messages:', len(messages_result), messages_result)

    operationlogs_result = checker.check_operationlogs()
    print('5 operationlogs:', len(operationlogs_result), operationlogs_result)

    favships_result = checker.check_favships()
    print('6 favships:', len(favships_result), favships_result)

    shipcorrections_result = checker.check_shipcorrections()
    print('7 shipcorrections:', len(shipcorrections_result), shipcorrections_result)

    fleets_result = checker.check_fleets()
    print('8 fleets:', len(fleets_result), fleets_result)

    ownerships_result = checker.check_ownerships()
    print('9 ownerships:', len(ownerships_result), ownerships_result)
