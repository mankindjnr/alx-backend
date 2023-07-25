#!/usr/bin/env python3
"""FIFO caching - caching algorithm"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache algorithm class"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.queue.append(key)

            if len(self.queue) > BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None
