#!/usr/bin/python3
"""
 LRU Caching 
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
        if key is None or item is None:
            pass           
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            latest = self.mru.pop(-1)
            del self.cache_data[latest]
            print(f'DISCARD:{latest}')
        self.cache_data[key] = item
        self.mru.append(key)

    def get(self, key):
        if key is None and key  not in self.cache_data:
            return None
        self.mru.remove(key)
        self.mru.append(key)
        return self.cache_data[key]
        
