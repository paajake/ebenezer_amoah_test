from time import time
from collections import OrderedDict
from typing import Union

CACHE_TYPE = Union[int, str]


class LRUCache:
    """
    This is a class implementation of a Least Recently Used Cache
    with expiry time.

    Attributes:
        capacity (int): This an integer of the maximum number
        of data inputs the cache can store.

        expiry_time (int): This is an integer representation of the
        Cache's expiry time in epoch time.

        cache (OrderedDict): This is an OrderedDict object which actually
        holds the data in the LRU Cache object.
    Examples:
        >>> my_cache = LRUCache(10, 60*10)
        >>> my_cache.is_expired()
        False
        >>> my_cache.put(1,"One")
        >>> my_cache.get(1)
        'One'
        >>> my_cache.get(2)
        -1
        >>> my_cache.get_capacity()
        10
        >>> my_cache.get_size()
        1
    """

    def __init__(self, capacity: int, expiry_secs: int):
        """
        The constructor for the LRUCache class.

        Parameters:
        capacity (int): An integer of the maximum size of the cache.

        expiry_secs (int): The number of seconds the cache should be valid for.
        """

        self.capacity = capacity
        self.expiry_time = int(time()) + expiry_secs
        self.cache: OrderedDict = OrderedDict()

    def get(self, key: CACHE_TYPE) -> CACHE_TYPE:
        """
        This function returns data stored in the cache when given a key.

        Parameters:
            key (CACHE_TYPE): The key of the stored data.

        Returns:
            CACHE_TYPE: Returns the stored data when found.
            int: Returns -1 when the data isn't found or the Cache Object is expired
        """
        if self.is_expired():
            return -1

        value = self.cache.pop(key, None)
        if value is None:
            return -1
        self.cache[key] = value
        return value

    def put(self, key: CACHE_TYPE, value: CACHE_TYPE):
        """
        This function stores data when a data value and key is given.

        Parameters:
            key (CACHE_TYPE): The key of the data to be stored.
            value (CACHE_TYPE): The data to be stored

        Returns:
            None: Returns nothing when data is successfully stored.
            int: Returns -1 when the Cache Object is expired.
        """
        if self.is_expired():
            return -1

        self.cache.pop(key, None)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(False)
        return None

    def is_expired(self) -> bool:
        """
        This function checks if the Cache object is expired.

        Returns:
            bool: Returns True if the Cache object is expired, else returns false.
        """
        if int(time()) > self.expiry_time:
            return True
        return False

    def set_cache_expiry_time(self, exp: int):
        """
        This function sets a new expiry time for the Cache object
        based on the time given in seconds.

        Parameters:
            exp (int): The new time in seconds for the cache to expire.

        Returns:
            None: Returns nothing when successful.
            int: Returns -1 when object is expired.
        """
        if self.is_expired():
            return -1

        self.expiry_time = int(time()) + exp
        return None

    def extend_cache_expiry_time(self, exp: int):
        """
        This function extends expiry time of the Cache object
        by the time given in seconds.

        Parameters:
           exp (int): The extension time in seconds.

        Returns:
           None: Returns nothing when successful.
           int: Returns -1 when object is expired.
        """
        if self.is_expired():
            return -1

        self.expiry_time += exp
        return None

    def get_expiry_time(self) -> int:
        """
        This function fetches the expiry time of the Cache object in epoch time.

        Returns:
           int: integer representation of epoch time.
        """
        return self.expiry_time

    def get_size(self):
        """
        This function fetches the number of current entries in the Cache object.

        Returns:
           int: Number of data items in Cache.
        """
        return len(self.cache)

    def get_capacity(self):
        """
        This function fetches the capacity of the Cache object.

        Returns:
           int: capacity of Cache object.
        """
        return self.capacity


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
