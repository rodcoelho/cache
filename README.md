# TTDCache

A customizable cache implementation with two options - LRU and MRU - built to alleviate querying a database multiple 
times for the same query, ultimately improving your application's execution time. 


#### Step 1: Clone

Clone the private repository:

`$ git clone https://github.com/rodcoelho/cache_project.git`


#### Step 2: Instantiate and customize your cache settings

First, you will need to create a new object that inherits from TTDCache to override the query_database method. 

VERY IMPORTANT: Currently, the query_database method queries a fake database. Override this method with a function that
queries your database (or calls an API).

A successful instantiation looks like this:

    from ttdcache import TTDCache           # import TTDCache, our abstract base cache
    class YourCustomCache(TTDCache):        # create a custom cache that inherits from TTDCache
        def query_database(self, key):      # VERY IMPORTANT: override the query_database method
            # your code                     # this will tell the object what query to perform
                                            # so perhaps something like value = orm.get_from_database(key)
            return value                    # make sure to return the value
    c = YourCustomCache(10)                 # then instantiate the object for use in production environment
    
Here we've create a cache `c` that has a maximum size of 10 items. The default replacement algorithm is set to 'LRU',
or Least Recently Used, but you can also change the replacement algorithm to MRU, or Most Recently Used, by altering 
self.replacement_algo after you instantiate the cache object:
    
    from ttdcache import TTDCache
    class YourCustomCache(TTDCache):
        def query_database(self, key):
            # your custom query code
    ...
    ...
    c = YourCustomCache(10)
    self.replacement_algo = 'MRU'           # this changes the replacement algorithm from LRU (default) to MRU
    

#### Optional: Custom Replacement Algorithms

To create a custom replacement algorithm for your cache, it's as easy as creating a new class that inherits from 
TDDCache and redefining the `algo` function. For example:

    from ttdcache import TTDCache
    class YourCustomCache(TTDCache):
        def query_database(self, key):
    ...
    ...
        def algo(self):
            # your new replacement algo     # your custom replacement algorithm goes here, like FIFO for example
                                            # this will override the parent class default LRU replacement algorithm
    c = YourCustomCache(10)
    
You can even change `self.replacement_algo` to a name you like but note that this is not necessary if you are creating
a custom replacement algorithm.


#### Optional: Clear cache

What happens if the database is altered? The cache data is compromised. Use the `.clear_cache()` method.

For example, if we used the code in the example above, simply call `c.clear_cache()`.


#### How the cache works

Now that your cache is customized and instantiated, let's check to see how it works.

Assume we used the code in the example above.

    value = c.get('key_10948')
    

What happens if we include this into our production code?
    
1) `c.get(key)` will check to see if the key, `key_10948`, is in the cache. If the key is in cache, it will update
 the 'metadata' and return the value (The 'metadata' is the unix time of the query and a counter for number of queries.
 Unix time and the counter are being collected so that in the future we can alter the replacement algorithm so that 
 we can remove items from the cache by count and by unix time if more than one item have the same count.)

2) If the key is NOT in the cache, it will run `self.query_database(key)` and query the database for the value we are 
looking for. 

3) Then it will check the cache's size to see there is enough room for more data to be added to the cache. 
If the cache is at capacity, it will make room for the new data point. Lastly, it will add the key/value pair to the 
cache and return the value for use. 

