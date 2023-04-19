#!/usr/bin/python3
"""
 MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    The super method.
    MRU we need to store recent values
    """
    def __init__(self):
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """
        Altering the least recently used
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            latest = self.mru[-1]
            del self.cache_data[latest]
            del self.mru[-1]
            print(f'DISCARD:{latest}')
        self.cache_data[key] = item
        self.mru.append(key)

    def get(self, key):
        """
        Fetching the mru
        """
        if key is not None and key in self.cache_data.keys():
            del self.mru[self.mru.index(key)]
            self.mru.append(key)
            return self.cache_data[key]
        return None
