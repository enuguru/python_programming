import redis

redis = redis.Redis(
    host= 'localhost',
    port= '6379')

redis.set('mykey', 'Hello from Python!')
value = redis.get('mykey') 
print(value)

redis.zadd('vehicles', {'car' : 0})
redis.zadd('vehicles', {'bike' : 0})
vehicles = redis.zrange('vehicles', 0, -1)
print(vehicles)
