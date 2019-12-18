import unittest
from time import time, sleep

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_get_and_put(self):
        my_cache = LRUCache(10, 60*10)
        for i in range(0, 11):
            self.assertEqual(my_cache.put(i, i), None)

            if i == 10:
                self.assertEqual(my_cache.get(0), -1)

            self.assertEqual(my_cache.get(i), i)

    def test_capacity(self):
        my_cache = LRUCache(10, 60*10)
        for i in range(0, 20):
            self.assertEqual(my_cache.put(i, i), None)
            self.assertEqual(my_cache.get(i), i)

        self.assertEqual(my_cache.get_capacity(), 10)
        self.assertEqual(my_cache.get_size(), 10)

    def test_expiry(self):
        my_cache = LRUCache(10, 1)
        self.assertEqual(my_cache.put(1, 1), None)

        sleep(2)

        self.assertGreater(int(time())+2, my_cache.get_expiry_time())
        self.assertEqual(my_cache.is_expired(), True)
        self.assertEqual(my_cache.get(1), -1)
        self.assertEqual(my_cache.put(2, 2), -1)

    def test_expiry_manipulation(self):
        my_cache = LRUCache(10, 60)

        self.assertGreater(int(time())+120, my_cache.get_expiry_time())
        self.assertEqual(my_cache.extend_expiry_time(150), None)
        self.assertLess(int(time())+120, my_cache.get_expiry_time())

        self.assertEqual(my_cache.set_expiry_time(60), None)
        self.assertGreater(int(time())+120, my_cache.get_expiry_time())


if __name__ == '__main__':
    unittest.main()
