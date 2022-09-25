# princess : bottom right 
# knight : top left
# m * n room (+-health room)
# knight health : positive integer 
# demon : - health
# orb : + health

# possible moving direction : right / down
# return minimum knight health

# 1. find all possible path
# 2. find minimum path

from typing import List
import math
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # dungeon size
        x_size = len(dungeon)
        y_size = len(dungeon[0])
        # find maximum health
        max_health = [[-math.inf for _ in range(y_size)] for tmp in range(x_size)]
        for i in range(x_size-1, -1, -1):
            for j in range(y_size-1, -1, -1):
                if i==x_size-1 and j==y_size-1:
                    max_health[i][j] = max(1 - dungeon[i][j],1)
                elif i==x_size-1:
                    max_health[i][j] = max(max_health[i][j+1] - dungeon[i][j], 1)
                elif j==y_size-1:
                    max_health[i][j] = max(max_health[i+1][j] - dungeon[i][j], 1)
                else: #not corner
                    max_health[i][j] = max(min(max_health[i+1][j], max_health[i][j+1]) - dungeon[i][j],1)
        # empty queue case
        return max_health[0][0]
s = Solution()
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))

#### not backtracking?

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # dungeon size
        x_size = len(dungeon)
        y_size = len(dungeon[0])
        # find maximum health
        max_health = [[-math.inf for _ in range(y_size)] for tmp in range(x_size)]
        for i in range(0, x_size):
            for j in range(0, y_size):
                if i==0 and j==0:
                    max_health[i][j] = max(1 - dungeon[i][j],1)
                elif i==0:
                    max_health[i][j] = max(max_health[i][j-1] - dungeon[i][j], 1)
                elif j==0:
                    max_health[i][j] = max(max_health[i-1][j] - dungeon[i][j], 1)
                else: #not corner
                    max_health[i][j] = max(min(max_health[i-1][j], max_health[i][j-1]) - dungeon[i][j],1)
        # empty queue case
        return max_health[0][0]
s = Solution()
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))