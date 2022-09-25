class Solution:
    def climbStairs(self, n: int):
        # n : remain stairs to reach top
        # available step : 1, 2 step
        # d(n) = d(n-1) + d(n-2)
        dp=[1,1]
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
s = Solution()
print(s.climbStairs(n=2))
print(s.climbStairs(n=3))
print(s.climbStairs(n=38))