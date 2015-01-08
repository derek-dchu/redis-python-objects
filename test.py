import unittest
import redis
r = redis.Redis(host='localhost', port=6379, db=0)

from redis_objects import RStr, RInt


class RStringTest(unittest.TestCase):

    def setUp(self):
        self.key = "msg"
        self.msg = "This is a test message"
        self.rstr_msg = RStr(self.key, self.msg)
        
    def test_print(self):
        self.assertEqual(self.rstr_msg.__str__(), "This is a test message")
             
    def test_exists(self):
        self.assertTrue(self.rstr_msg.exists())

    def test_type(self):
        self.assertEqual(self.rstr_msg.type(), "string")

    def test_del(self):
        del(self.rstr_msg)
        self.assertIsNone(r.get(self.key))


class RIntTest(unittest.TestCase):

    def setUp(self):
        self.key = "num"
        self.num = 100
        self.rint = RInt(self.key, self.num)

    def test_incr(self):
        self.rint.incr()
        self.assertEqual(self.rint.__str__(), "101")

    def test_incrby(self):
        self.rint.incrby(100)
        self.assertEqual(self.rint.__str__(), "200")

    def test_decr(self):
        self.rint.decr()
        self.assertEqual(self.rint.__str__(), "99")

    def test_decrby(self):
        self.rint.decrby(200)
        self.assertEqual(self.rint.__str__(), "-100")


if __name__ == '__main__':
    unittest.main()