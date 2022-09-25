from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        for box in boxTypes:
            truckSize-=box[0]
            if truckSize>=0:
                result+=box[0]*box[1]
            else:
                result+=(box[0]+truckSize)*box[1]
                return result
        return result
s=Solution()
print(s.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))
