# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        end_of_white = 0
        end_of_blue = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[end_of_blue], nums[end_of_white] = nums[end_of_blue], nums[end_of_white],  nums[i]
                end_of_white += 1
                end_of_blue += 1
            elif nums[i] == 1:
                nums[i], nums[end_of_blue] = nums[end_of_blue], nums[i]
                end_of_blue += 1
