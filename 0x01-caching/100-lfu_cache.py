#!/usr/bin/env python3
"""LFU caching module"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequency = defaultdict(int)
        self.lru_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                self._discard()

            self.cache_data[key] = item
            self.frequency[key] += 1
            if key in self.lru_order:
                self.lru_order.remove(key)
            self.lru_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None

    def _discard(self):
        """Discard the least frequently used item"""
        min_freq = min(self.frequency.values())
        lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]

        if len(lfu_keys) > 1:
            for key in self.lru_order:
                if key in lfu_keys:
                    lru_key = key
                    break
        else:
            lru_key = lfu_keys[0]

        del self.cache_data[lru_key]
        del self.frequency[lru_key]
        self.lru_order.remove(lru_key)
        print(f"DISCARD: {lru_key}")
