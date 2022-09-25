from typing import List
# weak : attack, defense is strictly greater than others
# find weak characters
# attack and defense : 1<= <=10^5
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 1. brute force
        # N^2
        """
        weak = 0
        for i in range(len(properties)):
            for j in range(len(properties)):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    weak += 1 
                    break
        return weak
        """
        
        # 2. sort and brute foce
        # reason of j = i + 1 start : always smaller "attack" in left side
        """
        weak = 0
        properties.sort()
        for i in range(len(properties)):
            for j in range(i+1, len(properties)):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    weak += 1 
                    break
        return weak
        """
        # 또 너냐 구글! + facebook
        # 3. stack        
        properties.sort(key=lambda x: (x[0], -x[1]))
        # [1,1], [1,2] , [2,1], [2,2]
        # -> [1,2], [1,1], [2,2], [2,1]
        print(properties)
        stack = []
        ans = 0
        
        for i in range(len(properties)):
            defense = properties[i][1]
            # [1,7], [2,2], [2,0], [3,10], [4,1]
            # 같은 attack 내에서는 무조건 작아짐
            # defense는 줄어들다가 
            while stack and stack[-1] < defense:
                stack.pop()
                ans += 1
            stack.append(defense)
        return ans
s = Solution()
print(s.numberOfWeakCharacters(properties = [[1,1],[1,2],[2,1],[2,2]]))
