from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # should be O(logn)
        first = 0
        last = len(nums) - 1
        result=0
        while first <= last:
            mid = (first + last) // 2
            if nums[mid]>target:
                last=mid-1

            elif nums[mid]<target:
                first=mid+1
            else:
                result=mid
                break
            # break case
            if nums[mid]<target and first>last:
                result=mid+1
        
        return result
s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5)) #2
print(s.searchInsert(nums = [1,3,5,6], target = 2)) #1
print(s.searchInsert(nums = [1,3,5,6], target = 7)) #4

