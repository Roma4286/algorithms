# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        numbers = set(nums)

        result = 1

        for i in numbers:
            if i-1 in numbers:
                continue
            
            res = 1
            while i+1 in numbers:
                res += 1
                i += 1
            
            result = max(result, res)
    
        return result