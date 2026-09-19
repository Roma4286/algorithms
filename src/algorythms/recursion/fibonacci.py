# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:        
        cache = {
            0: 0,
            1: 1
        }

        def recurs(n: int) -> int:
            if n in cache:
                return cache[n]
            
            res = recurs(n-1) + recurs(n-2)
            cache[n] = res
            return res
        
        return recurs(n)