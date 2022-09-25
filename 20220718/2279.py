# 현재 가방에도 암석이 차있다
# rock size : 1
# "최대 용량을 가질 수 있는 " 가방의 "최대 개수"
# 즉, 최대한 큰 사이즈부터 더해가야함
from typing import List
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainCapacity=[capacity[i]-rocks[i] for i in range(len(capacity))]
        remainCapacity.sort()
        result=0
        for remain in remainCapacity:
            additionalRocks-=remain
            if additionalRocks<0:
                break
            result+=1
        return result

s = Solution()
print(s.maximumBags(
    capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
))