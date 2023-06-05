#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

pool = redis.ConnectionPool(host='10.211.55.4', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex')
pipe.set('role', 'sb')

pipe.execute()