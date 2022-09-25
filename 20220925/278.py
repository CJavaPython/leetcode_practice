# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(num):
    if num == 0:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # n version exists
        # want to find wrong versions
        # isBadVersion : find bad version
        # need to minimize "API call"
        # n <= 231 - 1 == binary search?
        first = 0
        last = n
        mid = (first + last) // 2
        while first<last:
            if isBadVersion(mid):
                last = mid
            else:
                first = mid+1
            mid = (first + last) // 2
        return mid
                
s = Solution()
print(s.firstBadVersion(n=1))