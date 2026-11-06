# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points[:k]:
            heapq.heappush(heap, (-(x**2 + y**2), [x, y]))

        for point in points[k:]:
            if -(point[0]**2 + point[1]**2) > heap[0][0]:
                heapq.heapreplace(heap, (-(point[0]**2 + point[1]**2), point))
        
        return [l for _, l in heap]