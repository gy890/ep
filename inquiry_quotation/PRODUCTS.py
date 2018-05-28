# coding=utf-8
"""
Created on 2018-04-27

@Filename: products
@Author: Gui


"""
requires = 'a.something else about this product.\nb.something else about this product.'
PRODUCTS_CONFIG = {
    "PTIF": {"cargoName": "copper concentrate", "cargoType": "58ff2d492df86f014f0de882", "cargoWeight": 123.456,
             "cargoVolume": 789.123, "shipDraft": "", "requires": requires, "isComplete": False},
    "PTOF": {"cargoName": "copper concentrate", "cargoType": "58ff2d492df86f014f0de882", "cargoWeight": 123.456,
             "cargoVolume": 789.123, "shipDraft": 112.334, "requires": requires, "isComplete": True},
    "PTOL": {"requires": requires, "isComplete": True},
    "PTAGMINPECN": {"requires": requires, "isComplete": True},
    "PTACVAHK": {
        "visa": [{"_id": 0, "nationality": "563886dc1920abd8e88d54ed", "type": "G（Transit)", "number": 1},
                 {"_id": 1, "nationality": "", "type": "", "number": "1"}], "requires": requires, "isComplete": False},
    "PTBWD": {"quantity": 12.323, "requires": requires, "isComplete": True},
    "PTCTM": {"currency": "usd", "amount": 100230, "requires": requires, "isComplete": True},
    "PTCCOFFS":
        {"offChineseCrew": 1, "specialCrew": 2, "offOtherCrew": 3, "requires": requires, "isComplete": True},
    "PTCCONS": {"OriginalLetter": "No", "onChineseCrew": 2, "onOtherCrew": 3, "letters": 4, "requires": requires,
                "isComplete": True},
    "PTFHWTANAS": {"quantity": 3, "requires": requires, "isComplete": True},
    "PTFWSPY": {"quantity": 45.789, "requires": requires, "isComplete": True},
    "PTGABAGE": {"quantity": 123.456, "requires": requires, "isComplete": True},
    "PTFRWKPMT": {"requires": requires, "isComplete": True},
    "PTMACMADJST": {
        "magnetic": [{"_id": 0, "type": "type1", "number": 11, }, {"_id": 1, "type": "type2", "number": ''}],
        "requires": requires, "isComplete": False},
    "PTMEIMBIN": {"requires": requires, "isComplete": True},
    "PTCVD": {"numberOfPeople": 7, "requires": requires, "isComplete": True},
    "PTOLFVSL": {"backShip": "No", "land": [
        {"content": "name1", "oNumber": 1, "oWeight": 2.23, "oLength": 11.22, "oWidth": 1.366, "oHeight": 13.33,
         "_id": 0},
        {"content": "", "oNumber": "", "oWeight": 14, "oLength": "", "oWidth": "", "oHeight": "", "_id": 2}],
                 "companyName": "公司名称", "address": "收货地址", "tel": "联系电话123", "requires": requires,
                 "isComplete": False},
    "PTPSCIA": {"requires": requires, "isComplete": True},
    "PTHLTHCC": {"numberOfPeople": 4, "requires": requires, "isComplete": True},
    "PTRSCAC": {"requires": requires, "isComplete": True},
    "PTSSCEC": {"requires": requires, "isComplete": True},
    "PTYLLOWCC": {"numberOfPeople": 4, "requires": requires, "isComplete": True},
    "PTSLUDGE": {"quantity": 5, "requires": requires, "isComplete": True},
    "PTSP": {"land": [
        {"_id": 0, "status": "Overseas spare parts", "content": "name1", "oNumber": 1, "oWeight": 2.33, "oLength": 3.66,
         "oWidth": 5.66, "oHeight": 3.22},
        {"_id": 1, "status": "Overseas spare parts", "content": "", "oNumber": "", "oWeight": "", "oLength": "",
         "oWidth": "",
         "oHeight": ""}], "requires": requires, "isComplete": False},
    "PTSPRO": {"requires": requires, "isComplete": True},
    "PTSVBKDV": {"requires": requires, "isComplete": True},
    "PTBKQASV": {"requires": requires, "isComplete": True},
    "PTSVCGOT": {"requires": requires, "isComplete": True},
    "PTDRAFTSV": {"requires": requires, "isComplete": True},
    "PTOFFHBKCDSV": {"survey": 7, "requires": requires, "isComplete": True},
    "PTOFFHBKSV": {"survey": 8, "requires": requires, "isComplete": True},
    "PTONHBKCDSV": {"survey": 9, "requires": requires, "isComplete": True},
    "PTONHBKSV": {"survey": 10, "requires": requires, "isComplete": True},
    "PTTSA": {"OriginalLetter": "Yes", "numberOfPeople": 11, "letters": 12, "requires": requires,
              "isComplete": True},
    "PTOT": {"customName": None, "requires": "", "isComplete": True, "serviceName": None},
}

PTOT2 = {"customName": "my name is others", "requires": requires, "isComplete": True, "serviceName": None,
         "productCode": "PTOT"}

ALL_PRODUCTS = {'PTSPRO': 'SPRO', 'PTSLUDGE': 'Sludge', 'PTGABAGE': 'Garbage', 'PTOL': 'Port Captain',
                'PTOT': 'Customized Service', 'PTAGMINPECN': 'AGM Inspection', 'PTFRWKPMT': 'Hot Work Permit',
                'PTMEIMBIN': 'Main Engine Immobilization', 'PTFWSPY': 'Fresh Water Supply',
                'PTFHWTANAS': 'Water Sample Analysis', 'PTMACMADJST': 'Magnetic Compass Adjust',
                'PTACVAHK': 'Apply Visa at HongKong', 'PTHLTHCC': 'Renew Certificate - Health',
                'PTSSCEC': 'Renew Certificate - Ship Sanitation Control Exempt', 'PTOLFVSL': 'Off Land',
                'PTYLLOWCC': 'Renew Certificate - Vaccination', 'PTCVD': 'Medical Service', 'PTCTM': 'Cash To Master',
                'PTSP': 'Spare Part Delivery', 'PTTSA': 'Technicians/ Superintendent Attendance',
                'PTCCONS': 'Crew Change On Signer', 'PTCCOFFS': 'Crew Change Off Signer',
                'PTPSCIA': 'PSC Inspection Assistance', 'PTIF': 'Inward Formality', 'PTOF': 'Outward Formality',
                'PTBWD': 'Bilge Water', 'PTAGT': 'Port Agency Fee', 'PTSVBKDV': 'Survey - Bunker Delivery',
                'PTSVCGOT': 'Survey - Cargo Operation', 'PTRSCAC': 'Renew Certificate - Ship Certificate At Consulate',
                'PTOFFHBKCDSV': 'Survey - Off Hire B+C', 'PTBKQASV': 'Survey - Bunker Quantity',
                'PTONHBKSV': 'Survey - On Hire Bunker', 'PTOFFHBKSV': 'Survey - Off Hire Bunker',
                'PTONHBKCDSV': 'Survey - On Hire B+C', 'PTDRAFTSV': 'Survey - Draft'}
