#!/usr/bin/python3
"""
FIFOCache is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        MAX_ITEMS = len(self.cache_data.items())
        if not key or not item:
            pass
        elif MAX_ITEMS > BaseCaching.MAX_ITEMS:
            ret_val = list(self.cache_data)[0]
            print('DISCARD: ', ret_val)
            self.cache_data.pop(ret_val)
        else:
            self.cache_data[key] = item

    def get(self, key):
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]