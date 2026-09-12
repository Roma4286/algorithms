from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass(eq=False)
class Node(Generic[T]):
    var: T
    next: Node | None = None
    prev: Node | None = None

class DoublyLinkedList(Generic[T]): 

    def __init__(self) -> None:
        self.head: Node | None = None
        self.end: Node | None = None

    def push_front(self, var: T) -> bool: 
        if not self.head:
            self.head = self.end = Node(var=var)
            return True

        new_node = Node(var=var, next=self.head)
        self.head.prev = new_node
        self.head = new_node        

        return True
            
    def push_back(self, var: T) -> bool:
        if not self.end:
            self.head = self.end = Node(var=var)
            return True

        new_node = Node(var=var, prev=self.end)
        self.end.next = new_node
        self.end = new_node

        return True

    def pop_front(self) -> None | T:
        if not self.head:
            return None

        if self.head is self.end:
            result = self.head.var

            self.head = self.end = None

            return result

        result = self.head.var

        self.head = self.head.next

        self.head.prev = None

        return result

    def pop_back(self) -> None | T:
        if not self.end:
            return None

        if self.head is self.end:
            result = self.end.var

            self.head = self.end = None

            return result

        
        result = self.end.var

        self.end = self.end.prev

        self.end.next = None

        return result

    def remove(self, node: Node) -> bool:
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node is self.end:
            self.end = node.prev
        else:
            node.next.prev = node.prev

        node.prev = node.next = None
        return True