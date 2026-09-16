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
        self.list_of_hash = [None] * table_size
        self.table_size = table_size

    def set(self, key: int | str, data: T) -> bool:
        hash_value = self._hash_function(key)
        if self.has(key):
            head: Node = self.list_of_hash[hash_value]
            while head.key != key:
                head = head.next

            head.data = data

            return True

        new_node = Node(key=key, data=data)
        if self.list_of_hash[hash_value] is None:
            self.list_of_hash[hash_value] = new_node
            return True

        head: Node = self.list_of_hash[hash_value]
        while head.next is not None:
            head = head.next

        head.next = new_node
        return True

    def get(self, key: int | str) -> T:
        if not self.has(key):
            raise KeyError("There is no entry with this key")

        hash_value = self._hash_function(key)

        head: Node = self.list_of_hash[hash_value]
        while head.key != key:
            head = head.next

        return head.data

    def delete(self, key: int | str) -> bool:
        if not self.has(key):
            raise KeyError("There is no entry with this key")

        hash_value = self._hash_function(key)

        head: Node = self.list_of_hash[hash_value]
        if head.key == key:
            self.list_of_hash[hash_value] = head.next
            return True
        
        while head.next.key != key:
            head = head.next

        head.next = head.next.next
        return True        
        
    def has(self, key: int | str) -> bool:
        hash_value = self._hash_function(key)
        if self.list_of_hash[hash_value] is None:
            return False

        head: Node = self.list_of_hash[hash_value]
        while head is not None and head.key != key:
            head = head.next

        if head is None:
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