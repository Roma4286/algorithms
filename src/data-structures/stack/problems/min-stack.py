# https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack: list[list[int]] = []

    def push(self, value: int) -> None:
        min_value = min(value, self.stack[-1][1]) if len(self.stack) else value
        self.stack.append([value, min_value])

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        