from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # XOR operator : bitwise operation, only one bit is 1
        # all subset's XOR output
        # only one number = own number
        result = sum(nums)
        
        

        
        return result
s = Solution()
s.subsetXORSum(nums = [1,3])
"""
2 XOR 5 XOR 6
010
101
=
111
110
= 
001

5 XOR 1 XOR 6
101
001
=
100
110
=
010
"""
