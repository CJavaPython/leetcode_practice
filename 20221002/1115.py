#20221002
"""
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways 
(out of the kn total ways) to roll the dice so the sum of the face-up numbers 
equals target. Since the answer may be too large, return it modulo 10^9 + 7.
"""

class Solution:
    #DP problem
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        result = 0
        def dp(n):
            answer = 0
            for i in range(1, n):
                answer += dp(n-i)
            return answer            
        

        return result % (10**9+7)

s = Solution()
s.numRollsToTarget(n = 1, k = 6, target = 3)

"""
Constraints:

1 <= n, k <= 30
1 <= target <= 1000
"""