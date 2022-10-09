# not triple booking
class MyCalendarTwo:
    def __init__(self):
        self.calendar = list()
        self.overlaps = list()

    def book(self, start : int, end : int):
        # first find two booking
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        # if not find in two booking, find one booking
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
        self.calendar.append((start, end))
        return True

from heapq import heappush, heappop
class MyCalendarTwo:
    def __init__(self):
        self.calendar = list()
        self.overlaps = list()

    def book(self, start : int, end : int):
        # first find two booking
        
        return True

obj = MyCalendarTwo()
print(obj.book(10,20))  #True
print(obj.book(50,60))  #True
print(obj.book(10,40))  #True
print(obj.book(5,15))   #False
print(obj.book(5,10))   #True
print(obj.book(25,55))  #True
