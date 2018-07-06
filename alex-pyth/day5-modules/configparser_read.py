# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
print(config.sections())

print(config.read('example.ini'))

print(config.sections())

'''
[]
['example.ini']
['bitbucket.org', 'topsecret.server.com']
'''