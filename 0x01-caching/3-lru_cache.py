#!/usr/bin/env python3
"""LRU module"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache implementation."""

    def __init__(self) -> None:
        """Initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """updating an item from the cache."""
        if not (key is None or item is None):
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    lru_key, _ = self.cache_data.popitem(True)
                    print("DISCARD:", lru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
        return

    def get(self, key):
        """Retrieve an item by key."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
