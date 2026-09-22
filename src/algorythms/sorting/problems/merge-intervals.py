# https://leetcode.com/problems/merge-intervals/
import random

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                if result[-1][1] < intervals[i][1]:
                    result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])
                        
        return result
