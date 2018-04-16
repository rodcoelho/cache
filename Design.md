#### Goal

Create an N-Way, Set-Associative Cache

#### DISCLAIMER

Look at the README before reading this Design file.

#### Design Axioms

1) Use dictionary as a cache for quick queries (log n)
2) Using a single method, do everything 'under the hood': Provide user with a single method that (1) checks the cache for key/value pair (2) queries the database if key/value not present (3) adds key/value to cache (4) and maintains cache at capacity.
3) Allow users to easily customize the replacement algorithm
4) Allow users to easily customize how they query the database 
5) Allow users to change capacity size


#### Crash course for using TTDCache

Let's create an MRU cache that can hold 10,000 key/value pairs.

NOTE: You must override the `query_database` method anytime you instantiate an instance of TTDCache.

    from ttdcache import TTDCache
    class YourCustomCache(TTDCache):
        def query_database(self, key):
                                        # your code for quering a database goes here
            return value                # be sure to return a value
            
            
    c = YourCustomCache(10000)          # instantiate the custom cache with capacity of 10,000 
    
    self.replacement_algo = 'MRU'       # this changes the replacement algorithm from LRU (default) to MRU
    
    value = c.get('key-929040')         # this is the method to check if a key is in cache
                                        # if the key is not in cache, it will get data from the database
                                        # then it will add the key/value pair to the cache
                                        # if the cache is at capacity, room will be created
                                        # finally a value will be returned
    
#### How to create a custom replacement algorithm

    from ttdcache import TTDCache
        class YourCustomCache(TTDCache):
            def query_database(self, key):
                ...                         
                return value                
                
            def algo(self):
                                        # custom replacement algo code goes here
                
    c = YourCustomCache(10000)  
    
    value = c.get('key-000042')        
    
