#!/usr/bin/python3
"""
LIFOCache is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """
    LAST_ITEM = ""

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
            lastItem = self.LAST_ITEM
            print("DISCARD:", lastItem)
            self.cache_data.pop(lastItem)
        self.cache_data[key] = item
        self.LAST_ITEM = key

    def get(self, key):
        """
        if doesn’t exist, return none
        """
        if key not in self.cache_data.key():
            return None
        else:
            return self.cache_data[key]
