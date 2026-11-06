# https://leetcode.com/problems/last-stone-weight/
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            
            first_stone = heapq.heappop(heap)
            second_stone = heapq.heappop(heap)
            
            if first_stone != second_stone:
                heapq.heappush(heap, first_stone - second_stone)
        
        return -heapq.heappop(heap) if heap else 0
        