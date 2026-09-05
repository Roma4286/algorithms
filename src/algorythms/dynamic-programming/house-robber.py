# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i-1])
        return dp[n]

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        step1 = 0
        step2 = nums[0]
        for i in range(2, n + 1):
            curr = max(step2, step1 + nums[i-1])
            step1 = step2
            step2 = curr
        return curr
