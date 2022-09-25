# simulation problem
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # to reduce time, eliminate useless case
        # if k == 0 : try 0 time and it always smaller than n
        if k==0 or n>=k-1+maxPts: return 1
        # first prob always 1.0
        dp = [1.0] + [0.0] * n
        # dp table : [1.0 , 0.0 , .... , 0.0]
        # dp table means probability of getting point n
        ## ex
        # dp[0] = 1.0
        # dp[1] = 1.0 / maxPts ## select in range (1~maxPts) == 1/maxPts
        # dp[2] = 1.0 / maxPts + dp[1] / maxPts
        # dp[3] = 1.0 / maxPts + dp[2] / maxPts
        # each array's index means the number of probability

        #current probability
        prob = 1.0

        for i in range(1, n+1):
            # dp[i]=sum(dp[max(0,i-W):min(i,K)])*(1/W)
            dp[i]=prob*(1/maxPts)
            # if simulation is not over
            # dp[i] = (dp[i-1] + 1.0) / maxPts
            if i<k:
                prob+=dp[i]
            # if number is bigger than maxPts
            # it cannot reach one hop
            # move from previous value
            if i>=maxPts:
                ## ex)
                # dp[11] = dp[1] + dp[2] + dp[3] + ... + dp[10]
                # dp[12] = dp[2] + dp[3] + ... + dp[10]
                ## ex)
                # dp[20] = dp[10]
                # only maxPts can reach to 20 from i=10
                prob-=dp[i-maxPts]
        # simulation end at k
        # return from k to k+maxPts-1
        return sum(dp[k:])

## problem psuedocode
# while score <= k:
#   score += randomInteger(1, matPts)
# prob = probability that score <= n
# return prob

# monte carlo : iterative simulate, get result range

# ex) if k=1, it must be try 1 time
# ex2) if k=1, n=10, maxPts=10 than it try only once, and that score always <=n
# ex3) if k=1, n=6, maxPts=10 than it try only once, and probability is 6/10
# under 10^(-5) : drop