# https://leetcode.com/problems/koko-eating-bananas/
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def check(k: int) -> bool:
            res = 0
            for i in piles:
                res += -(-i // k)

                if res > h:
                    return False
            
            return True

        left = 1
        right = max(piles)

        min_k = float('inf')

        while left <= right:
            mid = left + (right - left) // 2

            is_can_make_it = check(mid)
            if is_can_make_it:
                min_k = min(min_k, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return min_k