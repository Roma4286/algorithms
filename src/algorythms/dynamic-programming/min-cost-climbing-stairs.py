# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        step1 = step2 = 0
        for i in range(2, len(cost) + 1):
            curr = min(step1 + cost[i - 1], step2 + cost[i - 2])
            step2 = step1
            step1 = curr

        return curr