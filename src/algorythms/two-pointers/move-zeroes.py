# https://leetcode.com/problems/move-zeroes
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        first_zero = 0
        while nums[first_zero] != 0:
            first_zero += 1
            if first_zero == len(nums):
                return

        for i in range(first_zero+1, len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[first_zero] = nums[i]
                nums[i] = 0
                first_zero += 1