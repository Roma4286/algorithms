# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def iteratively(self, head: ListNode):
        prev = None
        curr = head
        while curr:
            next_note = curr.next
            curr.next = prev
            prev = curr 
            curr = next_note
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        return self.iteratively(head)
        