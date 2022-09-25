from typing import List
from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if ""doubled" array
        # return "original" array
        # else
        # return empty array

        # if "changed" array length is odd, it is not doubled
        # O(1)
        if len(changed)%2!=0: return list()

        # 1. only sorting
        # time limit
        """
        # n^2
        changed.sort(reverse=True)
        #
        result = list()
        while changed:
            c = changed.pop()
            result.append(c)
            try:
                changed.remove(c*2)
            except ValueError:
                return list()
        return result
        """
        # 2. make it to hashmap
        ## using defaultdict
        
        changed_dict = defaultdict(int)
        # find from not doubled one
        changed.sort()
        ## O(n)
        for c in changed:
            changed_dict[c]+=1

        result = list()

        for c in changed:
            # doubled elements can be 0
            if changed_dict[c] == 0:
                continue
            else:
                if changed_dict[c*2]>0:
                    result.append(c)
                    changed_dict[c]-=1
                    changed_dict[c*2]-=1
                else:
                    return list()
        return result
        ## "Counter" is more efficient

s = Solution()
print(s.findOriginalArray(changed = [1,3,4,2,6,8]))
print(s.findOriginalArray(changed = [6,3,0,1]))
