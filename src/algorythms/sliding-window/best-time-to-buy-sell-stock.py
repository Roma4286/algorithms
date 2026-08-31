# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profite = 0
        left = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[left]:
                if prices[i]-prices[left] > max_profite:
                    max_profite = prices[i]-prices[left]
            else:
                left = i
        
        return max_profite