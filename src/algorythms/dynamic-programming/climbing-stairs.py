# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1 
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        step1 = 0
        step2 = 1
        for i in range(n):
            curr = step1+step2
            step1 = step2
            step2 = curr
        
        return curr