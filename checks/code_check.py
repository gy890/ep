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
            # "D:\PycharmProjects\ep",
            ]

    cmd1 = 'git fetch'
    cmd2 = 'git status '
    cmd3 = 'git pull '

    def __init__(self):
        for _, path in enumerate(GitCheck.path, 1):
            subprocess.Popen(GitCheck.cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=path)
            p = subprocess.Popen(GitCheck.cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=path)
            (std, err) = p.communicate()
            std = std.decode('utf-8')
            if 'behind' in std or 'Changes not staged for commit' in std or 'Untracked files' in std or 'Changes to be committed' in std:
                logging.debug('-------------------------------------------')

                # if 'behind' in std:
                #     n = std.split('by')[1].split('commit')[0].strip()
                #
                #     cmd4 = 'git log -{}'.format(n)
                #     p = subprocess.Popen(cmd4, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                #                          cwd=path)
                #     (std, err) = p.communicate()
                #     std = std.decode('utf-8')

                logging.debug('{path}\n{std}'.format(path=path, std=std))

                subprocess.Popen(GitCheck.cmd3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 cwd=path)

                logging.debug('-------------------------------------------')


git_check = GitCheck()