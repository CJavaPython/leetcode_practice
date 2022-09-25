import time
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == float(0):
            return 0
        elif x == float(1):
            return 1
        else:
            # n is integer            
            if n == 0:
                return 1
            elif n > 0:
                if n%2==0:
                    dp=self.myPow(x, n/2)
                    return dp * dp
                else:
                    dp=self.myPow(x, (n-1)/2)
                    return dp * dp * x
            else:
                if (-n)%2==0:
                    dp=self.myPow(x, n/2)
                    return dp*dp
                else:
                    dp=self.myPow(x, (n+1)/2)
                    return dp*dp*(1/x)
s = Solution()
start = time.time()
print(s.myPow(2.00000, -3))
#print(s.myPow(0.00001, 2147483647))
end = time.time()
print("dp solution time : ", end-start)

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == float(0):
            return 0
        elif x == float(1):
            return 1
        else:
            # n is integer            
            if n == 0:
                return 1
            # n is positive
            elif n > 0:
                # x is float
                result=1
                for i in range(n):
                    result*=x
                return result
            # n is negative
            else:
                result=1
                for i in range(-n):
                    result/=x
                return result
s = Solution()
start = time.time()
print(s.myPow(0.00001, 2147483647))
end = time.time()
print("original solution time : ", end-start)
"""