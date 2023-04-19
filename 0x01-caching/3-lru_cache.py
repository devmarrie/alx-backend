#!/usr/bin/python3
"""
 LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    The super method.
    LRU we need to store recent values
    """
    def __init__(self):
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """
        Altering the least recently used
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            latest = self.lru[0]
            del self.cache_data[latest]
            del self.lru[0]
            print(f'DISCARD:{latest}')
        self.cache_data[key] = item
        self.lru.append(key)

    def get(self, key):
        """
        Fetching the LRU
        """
        if key is not None and key in self.cache_data.keys():
            del self.lru[self.lru.index(key)]
            self.lru.append(key)
            return self.cache_data[key]
        return None
