from pymongo import MongoClient
import os
import redis


MONGOURL = os.environ.get('MONGOURL')

client = MongoClient(MONGOURL)
db = client[MONGOAPP]

# db["meta"].insert_one({"name":"lastTrustedBlock", "value":1162327})
# db["meta"].insert_one({"name":"lastTrustedTransaction", "value":1162327})

# redis

redis_url = os.environ.get('REDISTOGO_URL')

redis_db = redis.from_url(redis_url)

# redis_db.flushdb()
