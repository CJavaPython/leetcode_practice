#Least Recently Used
#delete using one

from collections import OrderedDict, deque
import math

#ordered dict

class LRUCache:

    def __init__(self, capacity: int):
        #init capacity size
        self.capacity = capacity
        self.cache = OrderedDict()

    #need to time complexity O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            v = self.cache.pop(key)
            self.cache[key] = v
            return v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

#how to...?

class LRUCache:

    def __init__(self, capacity: int):
        #init capacity size
        self.capacity = capacity
        # save index order with key
        self.cache = dict()
        # save value with index order
        self.order = list()

        # save # of removed value from cache
        #self.removed = 0

        # maximum index value
        self.idx = 0

    # need to average time complexity O(1)
    # get method : delete the value
    def get(self, key: int) -> int:
        if self.cache.get(key)==None:
            return -1
        result=0
        for i in range(self.idx, -1, -1):
            if i==self.cache[key]:
                val = self.cache.pop(key)
                # val is index
                result = self.order.pop(self.order[val])
                self.idx-=1
                #self.removed+=1

                ##문제점 : index other values - remove된 이후, 다른 value들을 어떻게 업데이트할 것인지
                #O(n)
                #update other
        return result
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key]=self.idx
            self.order.append(value)
            self.idx+=1
        elif len(self.order)>=self.capacity:
            ##문제점 : index other values - remove된 이후, 다른 value들을 어떻게 업데이트할 것인지
            #O(n)
            self.cache[key]=self.idx
            # remove first value
            self.order.remove(self.order[0])
            self.order.append(value)
        else:
            self.cache[key]=self.idx
            self.order.append(value)
            self.idx+=1

        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lRUCache = LRUCache(2)
print(lRUCache.put(1, 1))
print(lRUCache.put(2, 2))
print(lRUCache.get(1))
print(lRUCache.put(3, 3))
print(lRUCache.get(2))
print(lRUCache.put(4, 4))
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))