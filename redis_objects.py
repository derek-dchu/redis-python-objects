import redis
r = redis.Redis(host='localhost', port=6379, db=0)


class RStr:
    def __init__(self, key, string=""):
        self.key = key
        r.set(key, string)

    def __str__(self):
        return r.get(self.key).decode('utf-8')

    def __del__(self):
        r.delete(self.key)

    def exists(self):
        return r.exists(self.key)

    def type(self):
        return r.type(self.key).decode('utf-8')

    def ttl(self):
        return r.ttl(self.key)


class RInt(RStr):
    """
    A class represents an integer (which is always string inside redis) of redis.
    """
    def __init__(self, key, num):
        super(RInt, self).__init__(key, num)

    def __str__(self):
        return r.get(self.key).decode('utf-8')

    def incr(self):
        r.incr(self.key)

    def incrby(self, num):
        r.incr(self.key, num)

    def decr(self):
        r.decr(self.key)

    def decrby(self, num):
        r.decr(self.key, num)