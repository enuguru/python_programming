
#cat > redis-test.py <<-"_EOF_"
# -*- coding: utf-8 -*-
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
result = r.set('foo', 'bar')
print(result)
#True
result=r.get('foo')
print(result)
#'bar'
#_EOF_
#python redis-test.py
#True
#bar
