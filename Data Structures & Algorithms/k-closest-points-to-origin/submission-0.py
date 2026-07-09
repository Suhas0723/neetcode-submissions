import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in points:
            d = math.sqrt((i[0])**2 + (i[1])**2)
            heapq.heappush(max_heap, (-d, tuple(i)))
            if len(max_heap) > k:
                heapq.heappop(max_heap)


        res = []
        while max_heap:
            val = heapq.heappop(max_heap)
            res.append(list(val[1]))
        
        return res
