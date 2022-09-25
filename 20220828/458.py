class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        ## find poisonous bucket - exactly one
        # 1. select num of pig to feed poison
        # 2. select bucket to feed pig (pig can be fed some buckets, 두 개 동시에 먹기 가능)
        # 3. wait for some minutes - minutes to Die (can't feeding) / undead pig can use once again
        # 4. repeat
        # 5. return minimum number of pigs to figure out which bucket is poisonous within allotted time
        ## allotted time = (minutestoTest)

        avail_test_case = int(minutesToTest/minutesToDie) + 1
        pigs = 0
        while avail_test_case ** pigs < buckets:
            pigs+=1        
        return pigs

s = Solution()
s.poorPigs(buckets = 4, minutesToDie = 15, minutesToTest = 15)