# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)
    
    def get_max(self):
        return self.queue[0]
    
    def pop(self, value):
        if self.queue[0] == value:
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        monotonic_queue = MonotonicQueue()
        for i in range(k):
            monotonic_queue.push(nums[i])
        result = [monotonic_queue.get_max()]
        for i in range(k, len(nums)):
            monotonic_queue.pop(nums[i-k])
            monotonic_queue.push(nums[i])
            result.append(monotonic_queue.get_max())
        
        return result

d = Solution()
print(d.maxSlidingWindow(nums = [5, 3, 4, 2, 8], k = 3))
