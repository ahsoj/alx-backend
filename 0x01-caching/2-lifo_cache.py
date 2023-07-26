#!/usr/bin/env python3
"""LIFO module"""

from collections import OrderedDict
from base_caching import BaseConfig


class LIFOCache(BaseConfig):
    """Last-In First Out cache implementation."""

    def __init__(self) -> None:
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """updating an item from the cache."""
        if not (key is None or item is None):
            if (key not in self.cache_data) and (
                len(self.cache_data) + 1 > BaseConfig.MAX_ITEMS
            ):
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)
