
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', '567')
r.set('one',10)
r.incr('one')
#r.set('foo', 'ramp')
x = r.get('foo')
y = r.get('one')
print(x)
print(y)
