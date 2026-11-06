# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        counts = Counter(nums)
        
        for i in counts:

            c = counts[i]
            
            if len(heap) < k:
                heapq.heappush(heap, (c, i))
            elif c > heap[0][0]:
                heapq.heapreplace(heap, (c, i))
        
        return [a for _, a in heap]