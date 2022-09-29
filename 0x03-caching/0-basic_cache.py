#!/usr/bin/python3
"""
BasicCache is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This caching system doesn’t have limit
    """
    def put(self, key, item):
        """
        if doesn’t exist, not do anything
        """
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        if doesn’t exist, return none
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
