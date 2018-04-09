#!/usr/bin/env/ python3

import time
import datetime

from pprint import pprint


class AbstractBaseCache:
    def __init__(self, n):
        self.cache = {}
        self.cache_size = n
        # TODO see TODO's below
        # use isinstance() or type() for key/value types
        self.key_type = None
        self.value_type = None

    # __contains__ allows us to do something like: if x in object --> returns True or False
    def __contains__(self, key):
        return key in self.cache

    def parent_add_in_next_iteration(self):
        # change this function to add_to_cache
        # see this link for next steps - https://stackoverflow.com/a/38262573/9220192
        # goal is to create add_to_cache as a parent for children to inherit from
        pass


class CacheLRU(AbstractBaseCache):
    def add_to_cache(self, key, value):
        # check if cache has anything in it
        if len(self.cache) == 0:
            # cache is empty
            # set key and value type
            self.key_type, self.value_type = type(key), type(value)
            self.cache[key] = {'conventional_time': datetime.datetime.now(), 'unix_time': time.time(), 'value': value}

        else:
            # cache is not empty
            # check if key and value are of correct type
            if type(key) == self.key_type and type(value) == self.value_type:
                # check size
                if len(self.cache) >= self.cache_size and key not in self.cache:
                    self.remove_oldest_lru()
                    self.cache[key] = {'conventional_time': datetime.datetime.now(), 'unix_time': time.time(), 'value': value}

    def remove_oldest_lru(self):
        oldest = None
        for key in self.cache:
            if oldest is None:
                if key is not None:
                    oldest = key
                else:
                    pass
                    # FIXME edge case for if key == None
            elif self.cache[key]['conventional_time'] < self.cache[oldest]['conventional_time']:
                oldest = key
        self.cache.pop(oldest)


class CacheMRU(AbstractBaseCache):
    def add_to_cache(self, key, value):
        # check if cache has anything in it
        if len(self.cache) == 0:
            # cache is empty
            # set key and value type
            self.key_type, self.value_type = type(key), type(value)
            self.cache[key] = {'conventional_time': datetime.datetime.now(), 'unix_time': time.time(), 'value': value}

        else:
            # cache is not empty
            # check if key and value are of correct type
            if type(key) == self.key_type and type(value) == self.value_type:
                # check size
                if len(self.cache) >= self.cache_size and key not in self.cache:
                    self.remove_newest_mru()
                    self.cache[key] = {'conventional_time': datetime.datetime.now(), 'unix_time': time.time(), 'value': value}

    def remove_newest_mru(self):
        newest = None
        for key in self.cache:
            if newest is None:
                if key is not None:
                    oldest = key
                else:
                    pass
                    # FIXME edge case for if key == None
            elif self.cache[key]['conventional_time'] > self.cache[newest]['conventional_time']:
                newest = key
        self.cache.pop(newest)


if __name__ == '__main__':
    keyz = [x for x in range(1, 10)]
    valuez = [x for x in range(101, 110)]

    LRU_test = CacheLRU(5)
    NRU_test = CacheMRU(5)

    for _, __ in zip(keyz, valuez):
        NRU_test.add_to_cache(_, __)
    pprint(NRU_test.cache)

