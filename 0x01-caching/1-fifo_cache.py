#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseConfig


class FIFOCache(BaseConfig):
    """fifo caching"""

    def __init__(self) -> None:
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """update an item from the cache."""
        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data) > BaseConfig.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_key)

    def get(self, key):
        """retrieve an item by key"""
        return self.cache_data.get(key, None)
