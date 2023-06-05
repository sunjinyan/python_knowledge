#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import cryptography

# r = redis.Redis(host='47.93.20.75', port=6379,password="Sunjinyan0429")
# r.set('foo', 'Bar')
# print(r.get('foo').decode())



pool = redis.ConnectionPool(host='47.93.20.75', port=6379,password="Sunjinyan0429")

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print(r.get('foo').decode())