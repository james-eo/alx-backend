#!/usr/bin/env python3
"""
Module 3-lru_cache
Defines class LRUCache that inherits from BaseCaching
and implements LRU caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache class
    Implements a caching system with LRU eviction policy
    """

    def __init__(self):
        """ Initialize class instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the
        item value for the key key.
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS, discard the least
        recently used item (LRU algorithm).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest = next(iter(self.cache_data))
                print(f"DISCARD: {oldest}")
                del self.cache_data[oldest]
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
