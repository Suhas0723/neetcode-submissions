import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            distance = math.sqrt((i[0])**2 + (i[1])**2)
            heapq.heappush(heap, (-distance, i))

        while len(heap) > k:
            heapq.heappop(heap)

        res = []

        for i in heap:
            res.append(i[1])

        return res         