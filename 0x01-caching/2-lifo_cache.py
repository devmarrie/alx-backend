#!/usr/bin/python3
"""
LIFO Caching
Create a class LIFOCache that inherits from 
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Arguments:
              key, item
    Methods:
            get(), post()
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Alters the cache value
        Based on the LastIn FistOut basis.
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item

    def get(self, key):
        """
        Get the values associated with the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
