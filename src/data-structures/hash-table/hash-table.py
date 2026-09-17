from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass(eq=False)
class Node(Generic[T]):
    key: int | str
    data: T
    next: Node | None = None

class HashTable(Generic[T]):
    def __init__(self, table_size: int = 100):
        self.table: list[Node | None] = [None] * table_size
        self.table_size = table_size
        self.cellCount = 0

    def set(self, key: int | str, data: T) -> bool:
        _, node = self._find_prev_and_curr_node(key)
        if node:

            node.data = data

            return True

        hash_value = self._hash_function(key)

        self.cellCount += 1
        if self.cellCount / self.table_size >= 0.75:
            self._rehashing()

        new_node = Node(key=key, data=data)
        if self.table[hash_value] is None:
            self.table[hash_value] = new_node

            return True

        head: Node = self.table[hash_value]
        new_node.next = head
        self.table[hash_value] = new_node

        
        return True

    def get(self, key: int | str) -> T:
        _, node = self._find_prev_and_curr_node(key)
        if not node:
            raise KeyError("There is no entry with this key")

        return node.data

    def delete(self, key: int | str) -> bool:
        prev_node, node = self._find_prev_and_curr_node(key)
        if not node:
            raise KeyError("There is no entry with this key")
        
        hash_value = self._hash_function(key)

        if not prev_node:
            self.table[hash_value] = node.next
            self.cellCount -= 1
            return True

        prev_node.next = prev_node.next.next

        self.cellCount -= 1

        return True        
        
    def has(self, key: int | str) -> bool:
        _, node = self._find_prev_and_curr_node(key)

        if node is None:
            return False

        return True

    def _hash_function(self, key: int | str) -> int:
        
        if isinstance(key, int):
            def count_bits(n):
                return (n - 1).bit_length() 

            A = 2654435761 
            hash_val = (key * A) & 0xFFFFFFFF
            return (hash_val >> (32 - count_bits(self.table_size))) % self.table_size

        h = 0
        p = 31
        for char in key:
            h = (h * p + ord(char)) % self.table_size

        return h

    def _rehashing(self):
        self.table_size = self.table_size * 2
        old_table = self.table
        self.table = [None] * self.table_size
        self.cellCount = 0
        for i in old_table:
            if i:
                head: Node = i
                while head:
                    key = head.key
                    data = head.data

                    self.set(key, data)

                    head = head.next

    def _find_prev_and_curr_node(self, key: int | str) -> tuple[Node, Node] | tuple[None, Node] | tuple[None, None]:
        hash_value = self._hash_function(key)
        if self.table[hash_value] is None:
            return None, None

        head: Node = self.table[hash_value]
        if head.key == key:
            return None, head

        while head.next is not None and head.next.key != key:
            head = head.next

        if head.next is None:
            return None, None

        return head, head.next
