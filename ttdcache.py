#!/usr/bin/env python3

import time
import datetime
from random import randint
from pprint import pprint


class TTDCache:
    def __init__(self, n):
        self.cache = {}
        self.cache_size = n
        self.replacement_algo = 'LRU'

    # __contains__ allows us to do something like: if x in object --> returns True or False
    def __contains__(self, key):
        return key in self.cache

    def get(self, key):

        # if key is in cache, return value and update unix, time, and count
        if key in self.cache:
            value = self.cache[key]['value']
            self.cache[key]['unix'] = time.time()
            self.cache[key]['conventional_time'] = datetime.datetime.now()
            self.cache[key]['count'] += 1
            return value

        # if key not in cache, get from database, save to cache
        else:
            # query database
            value = self.query_database(key)

            # check if cache is at capacity
            if len(self.cache) >= self.cache_size:
                # if at capacity, then call replacement algo function
                self.algo()

            # store key/value in cache
            self.cache[key] = {
                'value': value,
                'unix': time.time(),
                'conventional_time': datetime.datetime.now(),
                'count': 1
            }
            return self.cache[key]['value']

    def query_database(self, key):
        # fake database query
        value = str(randint(0, 10000)) + str(key)
        return value

    def algo(self):
        # if LRU, pop the oldest
        if self.replacement_algo == 'LRU':
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

        # if MRU, pop the newest
        elif self.replacement_algo == 'MRU':
            newest = None
            for key in self.cache:
                if newest is None:
                    if key is not None:
                        newest = key
                    else:
                        pass
                        # FIXME edge case for if key == None
                elif self.cache[key]['conventional_time'] > self.cache[newest]['conventional_time']:
                    newest = key
            self.cache.pop(newest)

