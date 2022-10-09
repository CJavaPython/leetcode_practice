"""
You are implementing a program to use as your calendar. We can add a new event 
if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e.
, some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents
 a booking on the half-open interval [start, end), the range of real numbers x 
 such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the 
calendar successfully without causing a double booking. Otherwise, return false 
and do not add the event to the calendar.
"""
class MyCalendar:

    def __init__(self):
        self.calendar = dict()

    def book(self, start: int, end: int) -> bool:
        # start <= x
        # x < end
        # start < end <= 10^9
        # need to check double booking
        for i in range(start, end):
            self.calendar[i] = self.calendar.get(i, 0) + 1
            if self.calendar[i] > 1:
                for j in range(start, i+1):
                    self.calendar[j]= self.calendar[j]-1
                    if self.calendar[j] == 0:
                        del self.calendar[j]
                return False
        return True

from collections import deque

class MyCalendar:

    def __init__(self):
        self.calendar = deque()
    # wrong approach : 
    # because, it can not find end
    def book(self, start: int, end: int) -> bool:
        # start <= x
        # x < end
        # start < end <= 10^9
        # need to check double booking
        if len(self.calendar)==0:
            self.calendar.appendleft(end)
            self.calendar.appendleft(start)
            return True
        if end < self.calendar[0]:
            self.calendar.appendleft(end)
            self.calendar.appendleft(start)
            return True
        elif start > self.calendar[len(self.calendar)-1]:
            self.calendar.append(start)
            self.calendar.append(end)
            return True
        else:
            left = 0
            right = len(self.calendar) - 1
            mid = (left + right) // 2
            # find start location
            while left < right:
                if start < self.calendar[mid]:
                    left=mid+1
                elif start > self.calendar[mid]:
                    right=mid
                else:
                    mid = (left+right)//2
                    break
                mid = (left+right)//2
            if end > self.calendar[mid]:
                self.calendar.insert(start,mid)
                self.calendar.insert(end,mid)
                return True
            return False
"""
# sort by left
class MyCalendar():

    def __init__(self):
        self.calendar = []

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid][0]:
                right = mid
            else:
                left = mid + 1
        return left

    def book(self, start : int, end : int):
        idx = self.lowerBsearch(self.calendar, start)
        if idx > 0 and self.calendar[idx-1][1] > start:
            return False
        if idx < len(self.calendar) and end > self.calendar[idx][0]:
            return False
        self.calendar.insert(idx, [start, end])
        return True
"""
class MyCalendar():

    def __init__(self):
        self.calendar = []


    def book(self, start : int, end : int):
        
        left = 0
        right = len(self.calendar)
        while left < right:
            mid = (left + right)//2
            if start <= self.calendar[mid][0]:
                right = mid
            else:
                left = mid + 1
        idx = left
    
        if idx > 0 and self.calendar[idx-1][1] > start:
            return False
        if idx < len(self.calendar) and end > self.calendar[idx][0]:
            return False
        self.calendar.insert(idx, [start, end])
        return True
    

class MyCalendar():
    def __init__(self):
        self.calendar = list()

    def book(self, start : int, end : int):
        for s, e in self.calendar:
            if start < e and end > s:
                return False

        self.calendar.append((start, end))
        return True

class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:

        right = len(self.calendar) 

        if right == 0:
            self.calendar.append((start, end))
            return True

        left = 0
        while left < right:
            mid = left + (right - left)//2
            if self.calendar[mid][1] <= start:
                left = mid + 1
            else:
                right = mid

        if left == len(self.calendar):
            self.calendar.append((start, end))
            return True
                
        if self.calendar[left][0] >= end:
            self.calendar.insert(left, (start, end))
            return True
            
        return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
cal = MyCalendar()
print(cal.book(20,29))  #true
print(cal.book(13,22))  #false
print(cal.book(44,50))  #true
print(cal.book(1,7))    #true
print(cal.book(2,10))   #false
print(cal.book(14,20))  #true
print(cal.book(19, 25)) #false
