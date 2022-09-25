from typing import List
#do not have to use library
#in-place(do not use other data structure)
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        two_idx = len(nums)-1
        cur_idx = 0
        while cur_idx <= two_idx:
            if nums[cur_idx] == 0:
                nums[cur_idx], nums[zero_idx] = nums[zero_idx], nums[cur_idx]
                zero_idx+=1
            elif nums[cur_idx] == 2:
                nums[cur_idx], nums[two_idx] = nums[two_idx], nums[cur_idx]
                two_idx-=1
                #check once again
                cur_idx-=1
            cur_idx+=1
            print(nums)
        print(nums)

s = Solution()
s.sortColors([2,0,1])
