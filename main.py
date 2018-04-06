#!/usr/bin/env/ python3

import time, datetime
from pprint import pprint


class NCache:

    def __init__(self, n):
        self.cache = {}
        self.cache_size = n
        # TODO see TODO's below
        # use isinstance() or type() for key/value types
        self.key_type = None
        self.value_type = None

    def __contains__(self, key):
        return key in self.cache

    def add_lru(self, key, value):
        # TODO check key/values for rules
        if len(self.cache) >= self.cache_size and key not in self.cache:
            self.remove_oldest_lru()

        self.cache[key] = {'conventional_time': datetime.datetime.now(), 'unix_time': time.time(), 'value': value}

    def remove_oldest_lru(self):
        oldest = None
        for key in self.cache:
            if oldest is None:
                oldest = key
            elif self.cache[key]['conventional_time'] < self.cache[oldest]['conventional_time']:
                oldest = key
        self.cache.pop(oldest)

    def add_mru(self, key, value):
        # TODO check key/values for rules
        if len(self.cache) >= self.cache_size and key not in self.cache:
            self.remove_newest_mru()

        self.cache[key] = {'conventional_time': datetime.datetime.now(), 'unix_time': time.time(), 'value': value}

    def remove_newest_mru(self):
        newest = None
        for key in self.cache:
            if newest is None:
                newest = key
            elif self.cache[key]['conventional_time'] > self.cache[newest]['conventional_time']:
                newest = key
        self.cache.pop(newest)


if __name__ == '__main__':
    cache_test = NCache(5)
    keyz = [x for x in range(1, 10)]
    valuez = [x for x in range(101, 110)]
    for _, __ in zip(keyz, valuez):
        cache_test.add_mru(_, __)
    pprint(cache_test.cache)

