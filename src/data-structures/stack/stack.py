from typing import Generic, TypeVar

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.stack: list[T] = []
        self.stack_size: int = 0
    
    def push(self, new_element: T) -> bool:
        self.stack.append(new_element)
        self.stack_size += 1
        return True

    def pop(self) -> T | bool:
        if self.is_empty():
            return False
        self.stack_size -= 1
        return self.stack.pop()

    def peek(self) -> T | bool:
        if self.is_empty():
            return False
        return self.stack[-1]

    def is_empty(self) -> bool:
        return self.stack_size == 0

    def size(self) -> int:
        return self.stack_size