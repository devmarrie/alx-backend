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
        if key is None or item is None:
            pass           
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            latest = self.lru.pop()
            del self.cache_data[latest]
            print(f'DISCARD:{latest}')
        self.cache_data[key] = item
        self.lru.append(key)

    def get(self, key):
        if key is None and key  not in self.cache_data:
            return None
        self.lru.remove(key)
        self.lru.append(key)
        return self.cache_data[key]
        
