from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums)==0:return False
        subset1 = list()
        subset2 = list()
        while nums:
            max_val = nums.pop(nums.index(max(nums)))
            subset1.append(max_val)
        if len(subset2)==0:
            return False
        return True

s = Solution()
print(s.canPartition([1,5,11,5]))