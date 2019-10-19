import redis
from com.netease.properties import *


class RedisConnection:

    def __init__(self):
        self.conn = redis.StrictRedis(host=redis_host_ip, port=redis_host_port, password=redis_host_password)

    def close(self):
        self.conn.shutdown()

    def putset(self, keyname, obj: str) -> int:
        return self.conn.sadd(keyname, obj)
