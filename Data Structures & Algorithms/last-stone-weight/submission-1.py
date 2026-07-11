import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)

            if (a == b):
                continue
            else:
                heapq.heappush(heap, -abs(a-b))
            
        if heap:
            return -heap[0]
        else:
            return 0
        