# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i-c], dp[i])
            dp[i] = dp[i] + 1

        return dp[amount] if dp[amount] != float('inf') else -1