# Cache

A custom cache implementation with two options - LRU and MRU.


#### Step 1: Setup

`$ git clone https://github.com/rodcoelho/cache_project.git`

Next iteration: `pip3 install ttd-cache`

#### Step 2: Import and instantiate

Include the following import into your file and instantiate the object:

    from ttdcache import TTDCache
    c = TTDCache(10)
    
Here we've create a cache `c` that has a maximum size of 10 items. The default replacement algorithm is set to 'LRU',
or Least Recently Used, but you can also change the replacement algorithm to MRU by altering self.replacement_algo:
    
    from ttdcache import TTDCache
    c = TTDCache(10)
    self.replacement_algo = 'MRU'


To create a custom replacement algorithm for your cache, it's as easy as creating a new class that inherits from 
TDDCache and redefining the `algo` function. For example:

    from ttdcache import TTDCache
    class CustomCache(TTDCache):
        def algo(self):
            # replacement logic goes here
    ...
    c = CustomCache(10)
    
You can even change `self.replacement_algo` to a name you like but note that this is not necessary.
    
#### Step 3: Last step

After you've imported and instantiated the cache you want - it's almost ready for use.

The last thing to do is define what database you will query if the key/value pair is not in your cache.

    from ttdcache import TTDCache
    class CustomCache(TTDCache):
        def query_database(self, key):
            # query the database and return desired value
    ...
    c = CustomCache(10)

#### Now you are ready to use your cache

Now that your cache is ready, you can check if a key is in the cache:

    value = c.get('cache_key_10948')
    
What will happen is `c.get(key)` will check to see if the key is in the cache. If it is, it will update cache's metadata and 
will return the value. The 'metadata' is unix time of query and a counter for number of queries. If the key is NOT in
the cache, it will run `self.query_database(key)` and query the database for the value we are looking for. Then it will
check the cache's size to see there is enough room for more data. If the cache is at capacity, it will make room for
the new data point. Lastly, it will add the value to the cache and return the value. 


