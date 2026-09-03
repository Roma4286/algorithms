from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class Note(Generic[T]):
    data: T
    next: Note | None = None
    
class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Note | None = None

    def push_back(self, data: T) -> bool:
        if not self.head:
            self.head = Note(data=data)
        else:
            note = self._find_last_note()

            new_note = Note(data=data)
            note.next = new_note
        return True

    def push_front(self, data: T) -> bool:
        if not self.head:
            self.head = Note(data=data)
        else:
            new_note = Note(data=data, next=self.head)
            self.head = new_note

        return True

    def pop_front(self) -> bool | T:
        if not self.head:
            return False

        next_note = self.head.next
        result = self.head.data
        del self.head

        self.head = next_note

        return result

    def insert_at(self, index: int, data: T) -> bool:
        note = self.head

        if index == 1:
            new_note = Note(data=data, next=self.head)
            self.head = new_note
            return True

        while index-2:
            if note.next is None:
                return False
            note = note.next
            index -= 1

        next_note = note.next
        new_note = Note(data=data, next=next_note)
        note.next = new_note
        return True


    def remove_at(self, index: int) -> bool:
        note = self.head

        if index == 1:
            self.head = note.next
            del note
            return True

        while index-2:
            if note.next is None:
                return False
            note = note.next
            index -= 1

        removed_note = note.next
        next_note = removed_note.next
        del removed_note
        note.next = next_note
        return True

    def find(self, index: int) -> T | bool:
        if not self.head:
            return False

        note = self.head
        while index-1:
            if note.next is None: 
                return False
            note = note.next
            index -= 1

        return note.data

    def to_array(self) -> list[T]:
        result = []
        note = self.head
        if not note:
            return result

        result.append(note.data)

        while note.next:
            note = note.next
            result.append(note.data)

        return result

    def _find_last_note(self):
        note = self.head
        while note.next:
            note = note.next
        return note


if __name__ == "__main__":
    # --- push_front / push_back ---
    ll = SinglyLinkedList()
    ll.push_back(1)          # список должен быть: [1]
    ll.push_back(2)          # push_back should append to the END -> expected: [1, 2]
    ll.push_back(3)          # expected: [1, 2, 3]
    print("after push_back(1,2,3):", ll.to_array())  # expected [1, 2, 3]

    ll2 = SinglyLinkedList()
    ll2.push_front(10)       # push_front should prepend to the FRONT -> expected: [10]
    ll2.push_front(20)       # expected: [20, 10]
    ll2.push_front(30)       # expected: [30, 20, 10]
    print("after push_front(10,20,30):", ll2.to_array())  # expected [30, 20, 10]

    # --- pop_front ---
    ll3 = SinglyLinkedList()
    for x in [1, 2, 3, 4]:
        ll3.push_back(x)
    print("list before pop_front:", ll3.to_array())  # expected [1, 2, 3, 4]
    removed = ll3.pop_front()  # pop_front should remove and return the FIRST element -> expected removed == 1
    print("removed by pop_front:", removed)           # expected 1
    print("list after pop_front:", ll3.to_array())     # expected [2, 3, 4]

    # --- find ---
    ll4 = SinglyLinkedList()
    for x in [100, 200, 300, 400, 500]:
        ll4.push_back(x)
    print("list for find:", ll4.to_array())  # expected [100, 200, 300, 400, 500]
    print("find(1):", ll4.find(1))  # expected 100
    print("find(3):", ll4.find(3))  # expected 300
    print("find(5):", ll4.find(5))  # expected 500

    # --- insert_at ---
    ll5 = SinglyLinkedList()
    for x in [1, 2, 3, 4]:
        ll5.push_back(x)
    print("list before insert_at:", ll5.to_array())  # expected [1, 2, 3, 4]
    ok = ll5.insert_at(3, 999)  # insert 999 at position 3 -> expected [1, 2, 999, 3, 4]
    print("insert_at(3, 999) returned:", ok)          # expected True
    print("list after insert_at:", ll5.to_array())     # expected [1, 2, 999, 3, 4]

    # --- remove_at ---
    ll6 = SinglyLinkedList()
    for x in [1, 2, 3, 4, 5]:
        ll6.push_back(x)
    print("list before remove_at:", ll6.to_array())  # expected [1, 2, 3, 4, 5]
    ok2 = ll6.remove_at(3)  # remove element at position 3 (value 3) -> expected [1, 2, 4, 5]
    print("remove_at(3) returned:", ok2)               # expected True
    print("list after remove_at:", ll6.to_array())      # expected [1, 2, 4, 5]