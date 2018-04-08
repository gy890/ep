# coding=utf-8
"""
Created on 2017-12-29

@Filename: updateUsersAccount
@Author: Gui


"""
from bson.objectid import ObjectId
from epMongo import EPMongo


def generate_pipeline(user_id):
    pipeline = [
        {
            "$match": {
                "_id": user_id
            }
        },

        {
            "$lookup": {
                "from": "userpositions",
                "localField": "position",
                "foreignField": "_id",
                "as": "position"
            }
        },

        {
            "$unwind": {
                "path": "$position",
            }
        },

        {
            "$lookup": {
                "from": "usergroups",
                "localField": "position.group",
                "foreignField": "_id",
                "as": "position.group"
            }
        },

        {
            "$unwind": {
                "path": "$position.group",
            }
        },

        {
            "$project": {
                "username": 1,
                "account": "$position.group.account"
            }
        },

    ]
    return pipeline


if __name__ == '__main__':
    epmongo = EPMongo()
    users = epmongo.get_docs_by_query('users', query=None, projection={'_id': 1})
    # print(c, users[0])
    # pipeline = generate_pipeline(users[0]['_id'])
    # docs = epmongo.aggregate('users', pipeline)
    # print(docs)
    # for each in docs:
    #     print(each)
    for each in users:
        pipeline = generate_pipeline(each['_id'])
        print(pipeline)
        for result in (epmongo.aggregate('users', pipeline)):
            print(result)
