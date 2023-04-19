#!/usr/bin/python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Methods:
            put: to change the elements
            get: assign a key to a value
    """
    def __init__(self):
        super().__init__()
        self.visited = []

    def put(self, key, item):
        """
        Caches the data and removes on a FIFO basis
        The first one in first one out.
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= self.MAX_ITEMS:
            keyitr = self.visited[0]
            del self.cache_data[keyitr]
            self.visited.pop(0)
            print(f'DISCARD:{keyitr}')
        self.visited.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Assign key to a value.
        Key to be present in cache_data
        """
        if key is None and key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
