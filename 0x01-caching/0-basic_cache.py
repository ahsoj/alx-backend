#!/usr/bin/python3
"""BasicCache module"""

from base_caching import BaseConfig


class BasicCache(BaseConfig):
    """Class for basic caching functionality."""

    def put(self, key, item):
        """update an item from the cache."""
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
