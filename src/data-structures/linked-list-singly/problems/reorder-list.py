# https://leetcode.com/problems/reorder-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def find_middle(self, head: ListNode):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        next_node = slow.next
        slow.next = None

        return next_node

    def reverse(self, head: ListNode):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node 

        return prev
    
    def merge(self, head1: ListNode, head2: ListNode):
        start = head1

        curr = head1
        head1 = head1.next

        while head1 and head2:
            curr.next = head2
            curr = curr.next
            head2 = head2.next
            if not head1:
                break

            curr.next = head1
            curr = curr.next
            head1 = head1.next

        return start
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        middle = self.find_middle(head)
        reverse_middle = self.reverse(middle)

        head = self.merge(head, reverse_middle)