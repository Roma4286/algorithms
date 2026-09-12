# https://leetcode.com/problems/lru-cache/
from dataclasses import dataclass

@dataclass(eq=False)
class Node():
    data: int
    next: Node | None = None
    prev: Node | None = None

class DoublyLinkedList(): 

    def __init__(self) -> None:
        self.head: Node | None = None
        self.end: Node | None = None

    def push_back(self, data: int) -> Node:
        if not self.end:
            self.head = self.end = Node(data=data)
            return self.head

        new_node = Node(data=data, prev=self.end)
        self.end.next = new_node
        self.end = new_node

        return self.end

    def pop_front(self) -> None | int:
        if not self.head:
            return None

        if self.head is self.end:
            result = self.head.data

            self.head = self.end = None

            return result

        result = self.head.data

        self.head = self.head.next

        self.head.prev = None

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

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.doubly_linked_list = DoublyLinkedList()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        result = self.cache[key]

        self.doubly_linked_list.remove(result[1])
        new_node = self.doubly_linked_list.push_back(data=key)

        self.cache[key] = [result[0], new_node]

        return result[0]

    def put(self, key: int, value: int) -> None:
        new_node = self.doubly_linked_list.push_back(data=key)

        if key in self.cache:
            self.doubly_linked_list.remove(self.cache[key][1])
        else:
            if self.capacity:
                self.capacity -= 1
            else:
                pop_key = self.doubly_linked_list.pop_front()
                del self.cache[pop_key]

        self.cache[key] = [value, new_node]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)