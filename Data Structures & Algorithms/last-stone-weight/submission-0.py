import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -i)
        
        while len(max_heap) > 1:
            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)

            if a == b:
                continue
            elif a > b:
                heapq.heappush(max_heap, -(a - b))
            else:
                heapq.heappush(max_heap, -(b - a))

        if max_heap:
            return -max_heap[0]
        else:
            return 0