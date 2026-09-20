# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_num = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < min_num:
                min_num = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return min_num

        