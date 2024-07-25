# Caching System Implementations

This repository contains implementations of various caching systems as part of the alx-backend curriculum. The project involves creating classes that inherit from BaseCaching and implement different caching algorithms. Below are the tasks, learning objectives, and instructions on how to use the caching system implementations.


## Background Context

In this project, you will learn about different caching algorithms and implement them in Python.

## Resources
**Read or watch:**  
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))  
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_(LIFO))  
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))  
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU))  
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Frequently_Used_(LFU))

## Learning Objectives

By the end of this project, you should be able to explain the following concepts to anyone without using Google:
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- The purpose of a caching system
- The limits of a caching system

## Requirements
### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)').
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)').
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)').
- Documentation should not be a single word, but a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).

### Parent Class `BaseCaching`
All your classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")```

## Tasks

### 0. Basic Dictionary

Create a class `BasicCache` that inherits from `BaseCaching` and implements a basic caching system:

- Use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- This caching system doesn't have a limit.

### 1. FIFO Caching

Create a class `FIFOCache` that inherits from `BaseCaching` and implements a FIFO caching system:

- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the first item put in cache (FIFO algorithm).

### 2. LIFO Caching

Create a class `LIFOCache` that inherits from `BaseCaching` and implements a LIFO caching system:

- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the last item put in cache (LIFO algorithm).

### 3. LRU Caching

Create a class `LRUCache` that inherits from `BaseCaching` and implements an LRU caching system:

- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the least recently used item (LRU algorithm).

### 4. MRU Caching

Create a class `MRUCache` that inherits from `BaseCaching` and implements an MRU caching system:

- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the most recently used item (MRU algorithm).

### 5. LFU Caching

Create a class `LFUCache` that inherits from `BaseCaching` and implements an LFU caching system:

- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the least frequently used item (LFU algorithm). If there are multiple items with the same frequency, discard the least recently used item.
