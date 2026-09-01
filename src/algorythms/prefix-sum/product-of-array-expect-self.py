# https://leetcode.com/problems/product-of-array-except-self
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1]
        for i in range(len(nums)-1):
            result.append(result[-1]*nums[i])
        
        reverse_p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i]*reverse_p
            reverse_p = reverse_p*nums[i]
        
        return result