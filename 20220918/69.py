class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            # x의 최소 == 2
            # 2로 나눈 범위 부터 찾기 가능
            first = 0
            last = x//2 #나머지 버린 연산
            while first<=last:
                mid = (first+last)//2
                cmp_val=mid*mid
                if x==cmp_val:
                    return mid
                elif x<cmp_val: # need to find leftside
                    last=mid-1
                elif x>cmp_val: #need to find right sie
                    first=mid+1
                # if last binary search
                if first>last:
                    #check value is smaller or bigger
                    if x>cmp_val:
                        return mid
                    elif x<cmp_val:
                        return mid-1

s=Solution()
print(s.mySqrt(x=4))
print(s.mySqrt(x=8))
print(s.mySqrt(x=9))
print(s.mySqrt(x=15))