#!/usr/bin/python3
"""
LIFOCache is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
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
            lastItem = list(self.cache_data)[len(self.cache_data.items())-1]
            print("DISCARD:", lastItem)
            self.cache_data.pop(lastItem)
        self.cache_data[key] = item

    def get(self, key):
        """
        if doesn’t exist, return none
        """
        if key not in self.cache_data.key():
            return None
        else:
            return self.cache_data[key]
