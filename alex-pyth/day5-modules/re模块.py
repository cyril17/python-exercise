# -*- coding: utf-8 -*-


import re

res = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")

print(res)
#{'province': '3714', 'city': '81', 'birthday': '1993'}