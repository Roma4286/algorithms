# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []
        self.size_queue = 0
        

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        self.size_queue += 1
        return True
        

    def pop(self) -> int:
        if not self.out_stack:
            self._move()

        self.size_queue -= 1
        return self.out_stack.pop()
        

    def peek(self) -> int:
        if not self.out_stack:
            self._move()

        return self.out_stack[-1]
        
    def empty(self) -> bool:
        return self.size_queue == 0
        
    def _move(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())