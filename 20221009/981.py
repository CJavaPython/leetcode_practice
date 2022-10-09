"""
Design a time-based key-value data structure that can store multiple values for
the same key at different time stamps and retrieve the key's value at a certain 
timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the 
value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called 
previously, with timestamp_prev <= timestamp. If there are multiple such 
values, it returns the value associated with the largest timestamp_prev. 
If there are no values, it returns "".
"""

class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)


    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        n = len(arr)

        left = 0
        right = n

        while left < right:
            mid = (left + right) / 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid

        return "" if right == 0 else arr[right - 1][1]

class TimeMap:

    def __init__(self):
        self.dic = dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dic.get(key) ==None:
            self.dic[key] = list()
        self.dic[key].append((timestamp, value))
        # heap may be best solution
        sorted(self.dic[key])

    def get(self, key: str, timestamp: int) -> str:
        # using binary search
        find_area = self.dic.get(key)
        if find_area == None:
            return ""
        left = 0
        right = len(find_area) - 1
        while left< right:
            mid = (left +right) // 2
            if timestamp >= find_area[mid][0]:
                left = mid + 1
            elif timestamp < find_area[mid][0]:
                right = mid
        return find_area[right][1]
class TimeMap:

    def __init__(self):
        self.dic = dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dic.get(key) ==None:
            self.dic[key] = list()
        self.dic[key].append((timestamp, value))
        # heap may be best solution
        sorted(self.dic[key])

    def get(self, key: str, timestamp: int) -> str:
        # using binary search
        find_area = self.dic.get(key)
        if find_area == None:
            return ""
        left = 0
        right = len(find_area) - 1

        while left <= right:
            mid = (left + right) // 2
            if timestamp >= find_area[mid][0]:
                left = mid + 1
            elif timestamp < find_area[mid][0]:
                right = mid - 1

        if timestamp < find_area[right][0]:
            return ""
        return find_area[right][1]

timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))        
print(timeMap.set("foo", "bar2", 4))
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
