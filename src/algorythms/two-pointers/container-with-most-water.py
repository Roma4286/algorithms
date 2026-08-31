# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right])*(right-left)
            if area > max_area:
                max_area = area
            
            if height[left] >= height[right]:
                right -= 1
            else: 
                left += 1

        return max_area