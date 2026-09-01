# https://leetcode.com/problems/subarray-sum-equals-k/
from itertools import accumulate

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        need_numbers = {}
        result = 0

        for i in range(len(prefix_sum)-1, -1, -1):
            if prefix_sum[i] in need_numbers:
                result += need_numbers[prefix_sum[i]]
                
            if prefix_sum[i]-k in need_numbers:
                need_numbers[prefix_sum[i]-k] += 1
            else:
                need_numbers[prefix_sum[i]-k] = 1
            
        return result 
