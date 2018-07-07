# -*- coding: utf-8 -*-


import re

res = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")

print(res)
#{'province': '3714', 'city': '81', 'birthday': '1993'}

rem = re.search("[a-z]+d$","abcdA\nsecondline\nthird")
#rem = re.search("[a-z]+d$","abcdA\nsecondline\nthird",flags =re.M)
print(rem)

reb = re.search(r"^a","\nabc\neee",flags=re.MULTILINE)
print(reb)
rec = re.search(r".+","\nabc\neee",flags=re.S)
print(rec)
rer = re.search(r".+","\nabc\neee")
print(rer)

'''
{'province': '3714', 'city': '81', 'birthday': '1993'}
<_sre.SRE_Match object; span=(17, 22), match='third'>
<_sre.SRE_Match object; span=(1, 2), match='a'>
<_sre.SRE_Match object; span=(0, 8), match='\nabc\neee'>
<_sre.SRE_Match object; span=(1, 4), match='abc'>
'''