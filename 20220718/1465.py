# modulo 10^9 + 7
# constraints : 2 <= h, w <= 10^9
# 1 <= horizontalCuts.length <= min(h-1, 10^5)
# 1 <= verticalCuts.length <= min(w-1, 10^5)
# 1 <= verticalCuts[i] < w
from typing import List
import sys
input=sys.stdin.readline
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        modulo=1000000000+7
        def maxFind(input_list, lastval, firstval=0, maximum=0):
            input_list.append(firstval)
            input_list.append(lastval)
            input_list.sort()
            for i in range(len(input_list)-1):
                maximum=max(maximum, input_list[i+1] - input_list[i])
            return maximum
        hor_max = maxFind(horizontalCuts, h, 0, maximum=0)
        ver_max = maxFind(verticalCuts, w, 0, maximum=0)
        return (hor_max*ver_max)%modulo

s = Solution()
print(s.maxArea(5, 4, [3,1], [1]))