#!/usr/bin/python3
"""
 LRU Caching 
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.lru = []
        
    
    def put(self, key, item):
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.lru
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:


        self.cache_data[key] = item