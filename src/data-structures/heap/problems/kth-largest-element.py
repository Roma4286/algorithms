# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:

            if num > heap[0]:
                heapq.heapreplace(heap, num)
        
        return heap[0]