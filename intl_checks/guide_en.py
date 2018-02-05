# coding=utf-8
"""
Created on 2018-01-26

@Filename: guide_en
@Author: Gui


"""
import logging
import ast
import json
from openpyxl import Workbook


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    with open('en-US.js', 'rb') as f:
        lines = [l.decode('utf-8').strip() for l in f.readlines() if
                 l.decode('utf-8').find('{') == -1 and l.decode('utf-8').find('}') == -1]
    for l in lines:
        (a, b) = l.split(':')
        (a, b) = (a.strip(), b.strip())
        print('{}\t{}'.format(a.strip(), b.strip(',').strip("'")))


if __name__ == '__main__':
    main()
