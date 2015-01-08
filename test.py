import unittest
import redis
r = redis.Redis(host='localhost', port=6379, db=0)

from redis_objects import rstr


class RStringTest(unittest.TestCase):

    def setUp(self):
        self.key = "msg"
        self.msg = "This is a test message"
        self.rstr_msg = rstr(self.key, self.msg)
        
    def test_print(self):
        self.assertEqual(self.rstr_msg.__str__(), "This is a test message")
        
    def test_incr(self):
        self.assertRaises(redis.exceptions.ResponseError, self.rstr_msg.incr)
        
    def test_incrby(self):
        self.assertRaises(redis.exceptions.ResponseError, self.rstr_msg.incrby, 10)
        
    def test_exists(self):
        self.assertTrue(self.rstr_msg.exists())

    def test_type(self):
        self.assertEqual(self.rstr_msg.type(), "string")

    def test_del(self):
        del(self.rstr_msg)
        self.assertIsNone(r.get(self.key))


if __name__ == '__main__':
    unittest.main()