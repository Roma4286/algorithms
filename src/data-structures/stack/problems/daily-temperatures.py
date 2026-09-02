# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            if temperatures[stack[-1]] < temperatures[i]:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    index = stack.pop()
                    result[index] = i - index
            stack.append(i)
        
        return result