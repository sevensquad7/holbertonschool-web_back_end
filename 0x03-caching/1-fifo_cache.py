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
        MAX_ITEMS = len(self.cache_data)
        if not key or not item:
            return
        if MAX_ITEMS >= BaseCaching.MAX_ITEMS:
            ret_val = list(self.cache_data)[0]
            print('DISCARD: ', ret_val)
            self.cache_data.pop(ret_val)
        
        self.cache_data[key] = item

    def get(self, key):
        """
        if doesn’t exist, return none
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
