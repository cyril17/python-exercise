# -*- coding: utf-8 -*-

import hashlib

m = hashlib.md5()
m.update(b'hello')
m.update(b'tomorrow')

print(m.digest())    #二进制哈希
#b'&\xe3\x10\xeb@\xac\xca\xbf&\xd4\x7f\xe1\xf0\xcf6\xa5'

m.update(b'you are my family')
print(m.hexdigest())  #16进制哈希
#9436dc56ac5adc7b19dfa38ecbb52eb0

m.update('天王盖地虎'.encode(encoding='utf-8'))
print(m.digest())
#b'\xe3\xba]\xf8/2\xe1]M\x9b\xb8\xa3\x11VW\xcd'


import hmac

h = hmac.new(b'11111',b'22222')

print(h.digest())
print(h.hexdigest())
'''
b'\xf13\x1c)\xc4\x8cp\xef\xfa\x08\xa6oR\xde\x1c5'
f1331c29c48c70effa08a66f52de1c35
'''

g = hmac.new(b'haha','哈哈'.encode(encoding='utf-8'))
print(h.digest())
#b'\xf13\x1c)\xc4\x8cp\xef\xfa\x08\xa6oR\xde\x1c5'