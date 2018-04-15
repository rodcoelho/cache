#!/usr/bin/env python3

from ttdcache import TTDCache


class RodCache(TTDCache):
    def query_database(self, key):
        return 'holy cow'

    # def algo(self):
    #     self.clear_cache()


c = RodCache(2)
c.get(1)
c.get(2)
c.get(1)
c.get(3)
print(c.cache)
