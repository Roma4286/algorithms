from typing import TypeVar, Generic

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.in_stack: list[T] = []
        self.out_stack: list[T] = []
        self.size_queue = 0

    def enqueue(self, new_element: T) -> bool:
        self.in_stack.append(new_element)
        self.size_queue += 1
        return True

    def dequeue(self) -> T | bool:
        if self.is_empty():
            return False

        if not self.out_stack:
            self._move()

        self.size_queue -= 1
        return self.out_stack.pop()
        
    def peek(self) -> T | bool:
        if self.is_empty():
            return False

        if not self.out_stack:
            self._move()

        return self.out_stack[-1]

    def is_empty(self) -> bool:
        return self.size_queue == 0

    def size(self) -> int:
        return self.size_queue

    def _move(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
