# coding:utf-8
"""
Created on 2018-04-27

@Filename: order_types
@Author: Gui


"""

ORDER_TYPES = {
    'OTOPA': {
        "_id": "56652246d4c6815fc8ef7e8d",
        "name": "Husbandry Matter",
        "code": "OTOPA",
    },

    'OTNB': {
        "_id": "56652246d4c6815fc8ef7e95",
        "name": "Newbuilding",
        "code": "OTNB",
        'defaults': ['PTOF'],
        'suggested': ['PTOF'],
    },
    'OTRV': {
        "_id": "56652246d4c6815fc8ef7e92",
        "name": "Purchase Vessel",
        "code": "OTRV",
        'defaults': ['PTOF'],
        'suggested': ['PTIF', 'PTOF'],
    },
    'OTDV': {
        "_id": "56652246d4c6815fc8ef7e93",
        "name": "Sell Vessel",
        "code": "OTDV",
        'defaults': ['PTIF'],
        'suggested': ['PTIF', 'PTOF'],
    },
    'OTDD': {
        "_id": "56652246d4c6815fc8ef7e94",
        "name": "Drydocking",
        "code": "OTDD",
        'defaults': ['PTIF', 'PTOF'],
        'suggested': ['PTIF', 'PTOF'],
    },
    'OTBK': {
        "_id": "56652246d4c6815fc8ef7e96",
        "name": "Bunkering",
        "code": "OTBK",
        'defaults': ['PTIF', 'PTOF'],
        'suggested': ['PTIF', 'PTOF'],
    },
    'OTCL': {
        "_id": "56652246d4c6815fc8ef7e8f",
        "name": "Local Agency - Loading",
        "code": "OTCL",
        'defaults': ['PTIF', 'PTOF'],
        'suggested': ['PTIF', 'PTOF'],
    },
    'OTCD': {
        "_id": "56652246d4c6815fc8ef7e8e",
        "name": "Local Agency - Discharging",
        "code": "OTCD",
        'defaults': ['PTIF', 'PTOF'],
        'suggested': ['PTIF', 'PTOF'],
    },
    'OTPCL': {
        "_id": "56652246d4c6815fc8ef7e91",
        "name": "Protecting agency - Loading",
        "code": "OTPCL",
        'defaults': ['PTOL'],
        'suggested': ['PTOL'],
    },

    'OTPCD': {
        "_id": "56652246d4c6815fc8ef7e90",
        "name": "Protecting Agency - Discharging",
        "code": "OTPCD",
        'defaults': ['PTOL'],
        'suggested': ['PTOL'],
    },

    'OTMVS': {
        "_id": "5824349077c83eeb44fd1acc",
        "name": "Monitor Vessel Schedule",
        "code": "OTMVS",
    },
    'OTOT': {
        "_id": "56652246d4c6815fc8ef7e97",
        "name": "Others",
        "code": "OTOT",
    },
}
