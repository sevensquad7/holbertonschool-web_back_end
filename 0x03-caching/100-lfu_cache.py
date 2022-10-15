#!/usr/bin/python3
"""
LFUCache is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache Class """

    def __init__(self):
        """
        don’t forget to call the parent init: super().__init__()
        """
        super().__init__()
        self.lfu_order = []
        self.frequency = {}

    def put(self, key, item):
        """
        if doesn’t exist, not do anything
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.lfu_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_value = min(self.frequency.values())
                    min_keys = [k for k in self.frequency
                                if self.frequency[k] == min_value]
                    for i in range(len(self.lfu_order)):
                        if self.lfu_order[i] in min_keys:
                            break
                    del self.cache_data[self.lfu_order[i]]
                    del self.frequency[self.lfu_order[i]]
                    print("DISCARD:", self.lfu_order[i])
                    self.lfu_order.pop(i)
                self.cache_data[key] = item
                self.frequency[key] = 1
            self.lfu_order.append(key)

    def get(self, key):
        """
        if doesn’t exist, return none
        """
        if key in self.cache_data:
            self.lfu_order.remove(key)
            self.lfu_order.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
