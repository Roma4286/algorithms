# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sum = [0]
        for i in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+i)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]

# [0, -2, -2, 1, -4, -2, -3]
