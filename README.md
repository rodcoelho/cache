# Cache

A custom cache implementation with two options - LRU and MRU.


#### Step 1: Setup

`$ git clone https://github.com/rodcoelho/cache_project.git`

Next iteration: `pip3 install ttd-cache`

#### Step 2: Import and instantiate 

Include the following imports:

`from cache_main import CacheLRU, CacheMRU`

To create an LRU Cache (Least Recently Used):
    
    LRU_cache = CacheLRU(n)
    
Where n is the desired size of the cache.

To 
    
    MRU_test = CacheMRU(5)

    for _, __ in zip(keyz, valuez):
        LRU_test.add_to_cache(_, __)
        pprint(LRU_test.cache)
