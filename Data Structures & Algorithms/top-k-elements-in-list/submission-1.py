from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []
        for i in nums:
            freq[i] += 1
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for count, num in heap:
            res.append(num)
    
        return res


        

        


            
        

        