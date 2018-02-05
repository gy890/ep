# coding=utf-8
"""
Created on 2018-01-26

@Filename: guide_zh
@Author: Gui


"""
import logging
import ast
import json
from openpyxl import Workbook


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    with open('zh-Hans-CN.js', 'rb') as f:
        line = f.read().decode('utf-8').strip('module.exports = ').strip(';')
    for k, v in json.loads(line).items():
        print('{}\t{}'.format(k.strip(), v.strip()))


if __name__ == '__main__':
    main()
