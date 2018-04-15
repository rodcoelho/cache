# Cache

A customizable cache implementation with two options - LRU and MRU.


#### Step 1: Clone

Clone the private repository:

`$ git clone https://github.com/rodcoelho/cache_project.git`


#### Step 2: Setup - Import, instantiate, and customize your cache

First, you will need to create a new object that inherits from TTDCache to override the query method. 
It will look like this:

    from ttdcache import TTDCache       # imports our abstract base cache
    class YourCustomCache(TTDCache):    # create your custom cache that inherits from TTDCache
        def query_database(self, key):  # override the query_database method
            # your code                 # this will tell the object what query to make if key/value is not in cache
                                        # so perhaps something like orm.get_from_database(key)
    c = YourCustomCache(10)             # then instantiate the object
    
Here we've create a cache `c` that has a maximum size of 10 items. The default replacement algorithm is set to 'LRU',
or Least Recently Used, but you can also change the replacement algorithm to MRU by altering self.replacement_algo:
    
    from ttdcache import TTDCache
    class YourCustomCache(TTDCache):
        def query_database(self, key):
    ...
    ...
    c = TTDCache(10)
    self.replacement_algo = 'MRU'       # this changes the replacement algorithm from LRU (default) to MRU
    

#### Optional: Custom Replacement Algorithms

To create a custom replacement algorithm for your cache, it's as easy as creating a new class that inherits from 
TDDCache and redefining the `algo` function. For example:

    from ttdcache import TTDCache
    class YourCustomCache(TTDCache):
        def query_database(self, key):
    ...
    ...
        def algo(self):
            # your code                 # your custom replacement algorithm goes here, like FIFO for example
                                        # this will override the parent class default LRU replacement algorithm
    c = CustomCache(10)
    
You can even change `self.replacement_algo` to a name you like but note that this is not necessary if you are creating
a custom replacement algorithm.


#### How the cache works

Now that your cache is customized and instantiated, let's check to see if a key of interest is in the cache:

    value = c.get('cache_key_10948')
    

What happens?
    
1) `c.get(key)` will check to see if the key is in the cache. If the key is in cache, update 'metadata' and return value. The 'metadata' is unix time of query and a counter for number of queries.

2) If the key is NOT in the cache, it will run `self.query_database(key)` and query the database for the value we are looking for. 

3) Then it will check the cache's size to see there is enough room for more data. If the cache is at capacity, it will make room for
the new data point. Lastly, it will add the key/value pair to the cache and return the value for use. 


