# -*- coding:utf-8 -*-

import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379,db=5)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)
#pipe.multi()

pipe.set ('name', 'yyy')
time.sleep(50)
pipe.set('role', 'sb')

pipe.execute()