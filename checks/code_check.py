# coding=utf-8
"""
Created on 2018-03-13

@Filename: code_check
@Author: Gui


"""
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)


class GitCheck(object):
    path = ["D:\e-ports\ci-helper", "D:\e-ports\ep-consumer-chatting", "D:\e-ports\ep-consumer-portal",
            "D:\e-ports\ep-mid-mongoose", "D:\e-ports\ep-mid-sendmail", "D:\e-ports\ep-mid-session",
            "D:\e-ports\ep-portal", "D:\e-ports\ep-public",
            "D:\e-ports\ep-svc-auth", "D:\e-ports\ep-svc-chatting", "D:\e-ports\ep-svc-epds", "D:\e-ports\ep-svc-event",
            "D:\e-ports\ep-svc-fee", "D:\e-ports\ep-svc-gateway", "D:\e-ports\ep-svc-mailer",
            "D:\e-ports\ep-svc-message", "D:\e-ports\ep-svc-order", "D:\e-ports\ep-svc-public",
            "D:\e-ports\ep-svc-session", "D:\e-ports\ep-svc-storage", "D:\e-ports\ep-svc-user",
            "D:\e-ports\epmodel", "D:\e-ports\epmsg-helper", "D:\e-ports\epui-intl", "D:\e-ports\epui-md",
            "D:\PycharmProjects\ep",
            ]

    cmd = 'git status '

    def __init__(self):
        for _, path in enumerate(GitCheck.path, 1):
            p = subprocess.Popen(GitCheck.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=path)
            (std, err) = p.communicate()
            std = std.decode('gbk')
            if 'up-to-date' not in std:
                logging.debug('-------------------------------------------')
                logging.debug('{path} {std}'.format(path=path, std=std))
                logging.debug('-------------------------------------------')


git_check = GitCheck()
