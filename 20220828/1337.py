from typing import List
from heapq import heappush, heappushpop, heappop
# more soldiers,
# bigger row, stonger
# find k weakest row
# sorting method
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        count_list = []
        
        for row in mat:
            count = 0
            while count < len(mat[0]):
                if row[count]==0:
                    break
                count+=1
            count_list.append(count)

        result = sorted(range(len(mat)), key = lambda x : count_list[x])
        return result[:k]
        ## 한줄짜리 return 값
        #return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]
        """
        heap = []
        # count 구하기: binary search
        for index, row in enumerate(mat):
            start = 0
            end = len(mat[0]) - 1
            count = 0
            while start < end:
                mid = int((start+end)/2)
                #병사인경우
                if row[mid]==1:
                    start = mid
                #시민인경우
                else:
                    end = mid-1
            # binary search로 찾은 index
            count = start            
            ## sorting method
            heap.append((count, index))
        
            ## heap q method

            if len(heap) == k:
                #만약 push 할 개수가 꽉 찼다면
                #max q 로 정렬, 가장 작은 항목 (== -로 집어넣으니 가장 큰 항목) 제거
                heappushpop(heap, (-count, -index))
            else:
                heappush(heap, (-count, -index))
        weakest_row = []

        while heap:
            weakest_row.append(-heappop(heap)[1])
        return weakest_row[::-1]


        
        return 0
        """
print("1")
s = Solution()
print(s.kWeakestRows(
mat =[[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]],
k=3))