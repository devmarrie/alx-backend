#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from the main class
    Attributes:
              key, item
    Methods:
            put(), get()
    """
    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)
    
    def put(self, key, item):
        """
        Assigns key to item
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        Displays the item associated with a key.
        The key should be present in the cache and not None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
