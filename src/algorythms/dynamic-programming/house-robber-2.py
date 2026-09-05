# https://leetcode.com/problems/house-robber-ii/
class Solution:

    def default_rob(self, nums: list[int]) -> int: 
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        step1 = 0
        step2 = nums[0]
        for i in range(2, n + 1):
            curr = max(step2, step1 + nums[i-1])
            step1 = step2
            step2 = curr
        return curr

    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.default_rob(nums[1:]), self.default_rob(nums[:-1]))