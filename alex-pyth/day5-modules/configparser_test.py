# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
'''
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwardx11 = yes

[bitbucket.org]
user = hg

[topsecret.server.com]
host port = 50022
forwardx11 = no
'''




config2 = configparser.ConfigParser()
config2['DEFAULT'] = {'name':'23',
                      'number':'36559067',
                      'sex':'M'}
config2['BIGcyril'] = {}
config2['BIGcyril']['User'] = 'good'
config2['SMALLgsy'] = {}
sec = config2['SMALLgsy']
sec['pc'] = '2017'
config2['DEFAULT']['name'] = 'GSY'

with open('example2.ini','w') as f:
    config2.write(f)
'''
[DEFAULT]
name = GSY
number = 36559067
sex = M

[BIGcyril]
user = good

[SMALLgsy]
pc = 2017


'''