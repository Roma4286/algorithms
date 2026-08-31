# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        while left != right:
            res = numbers[left]+numbers[right]
            if res == target:
                return [left+1, right+1]
            elif res < target:
                left += 1
            else: 
                right -= 1