#!/usr/bin/env python3
"""
LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache implements least-frequently used caching with eviction.
    """

    def __init__(self):
        """
        Initialize LFUCache with usage tracking and order counter.
        """
        super().__init__()
        self._usage_counts = {}  # key -> access count
        self._order = {}         # key -> insertion/access order
        self._counter = 0        # global order counter

    def _record_access(self, key: str) -> None:
        """
        Record an access for key: increment count and update order.
        """
        # increment access counter
        self._usage_counts[key] = self._usage_counts.get(key, 0) + 1
        # update usage order
        self._order[key] = self._counter
        self._counter += 1

    def put(self, key: str, item) -> None:
        """
        Add or update item in cache; evict least-frequently used if needed.
        """
        if key is None or item is None:
            return

        # updating existing key
        if key in self.cache_data:
            self.cache_data[key] = item
            self._record_access(key)
            return

        # eviction if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # find minimum usage count
            min_count = min(self._usage_counts.values())
            # candidates with minimum count
            candidates = [k for k, cnt in self._usage_counts.items() if cnt == min_count]
            # among candidates, choose least recently used (smallest order)
            key_to_evict = min(candidates, key=lambda k: self._order.get(k, 0))
            # evict
            del self.cache_data[key_to_evict]
            del self._usage_counts[key_to_evict]
            del self._order[key_to_evict]
            print(f"DISCARD: {key_to_evict}")

        # insert new key
        self.cache_data[key] = item
        # initialize usage and record first access
        self._usage_counts[key] = 0
        self._record_access(key)

    def get(self, key: str):
        """
        Retrieve item by key and record usage; return None if missing.
        """
        if key is None or key not in self.cache_data:
            return None
        self._record_access(key)
        return self.cache_data[key]

