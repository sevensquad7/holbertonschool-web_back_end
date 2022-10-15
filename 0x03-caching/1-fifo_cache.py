#!/usr/bin/python3
"""
FIFOCache is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """
    def __init__(self):
        """
        don’t forget to call the parent init: super().__init__()
        """
        super().__init__()

    def put(self, key, item):
        """
        if doesn’t exist, not do anything
        """
        if key is None or item is None:
            return
        if (
            len(self.cache_data.items()) == BaseCaching.MAX_ITEMS
            and (key not in self.cache_data.keys())
        ):
            firstItem = list(self.cache_data)[0]
            print("DISCARD:", firstItem)
            self.cache_data.pop(firstItem)
        self.cache_data[key] = item
    def get(self, key):
        """
        if doesn’t exist, return none
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
