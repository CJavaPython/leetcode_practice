"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""
#constraints : arr.length = 10^4
from typing import List
from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result=list()
        if x <= arr[0]:
            for i in range(k):
                result.append(arr[i])
        elif x >= arr[-1]:
            for i in range(len(arr)-1-k, len(arr)):
                result.append(arr[i])
        elif k==len(arr):
            result=arr
        else:
            # find with binary search
            start = 0
            end = len(arr) - 1
            mid = (start + end)//2
            # if left move : True, else : right
            while start<=end:
                if x > arr[mid]:
                    start = mid+1
                elif x < arr[mid]:
                    end = mid-1
                else:
                    break
                mid = (start+end)//2
            if start>end:
                #ascending order if rights
                if abs(x-arr[end])<=abs(x-arr[start]):
                    mid=end
                else:
                    mid=start
            # find k closest one
            result = deque()
            result.append(arr[mid])
            k-=1
            left_mid = mid-1
            right_mid = mid+1
            while k>0:
                if left_mid>=0 and right_mid<=len(arr)-1:
                    #find both
                    if abs(arr[left_mid] - x) <= abs(arr[right_mid]-x):
                        result.appendleft(arr[left_mid])
                        left_mid-=1
                    else:
                        result.append(arr[right_mid])
                        right_mid+=1
                elif right_mid>len(arr)-1:
                    result.appendleft(arr[left_mid])
                    left_mid-=1
                elif left_mid<0:
                    result.append(arr[right_mid])
                    right_mid+=1
                k-=1
            result=list(result)
        return result
s = Solution()
print(s.findClosestElements(arr=[1,2,3,4,5], k=4, x=3))
print(s.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4))
print(s.findClosestElements(arr=[1,1,1,10,10,10], k=1, x=9))
print(s.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9))
print(s.findClosestElements([1, 3], 1, 2))