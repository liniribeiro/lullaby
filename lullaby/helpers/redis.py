import json
from datetime import timedelta

import redis as redis

from lullaby.settings import REDIS_HOST

redis = redis.Redis(host=REDIS_HOST)


def add_to_cache(key, data):
    redis.setex(key, timedelta(minutes=1), value=json.dumps(data))


def get_from_cache(key):
    redis_object = redis.get(key)
    return json.loads(redis_object) if redis_object else None
