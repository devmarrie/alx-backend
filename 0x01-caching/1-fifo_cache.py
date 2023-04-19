#!/usr/bin/python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        if len(self.cache_data) >= self.MAX_ITEMS:
            keyitr = next(iter(self.cache_data))
            del self.cache_data[keyitr]
            print(f'DISCARD:{keyitr}')
        self.cache_data[key] = item

    def get(self, key):
        if key is None and key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
