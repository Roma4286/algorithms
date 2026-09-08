# https://leetcode.com/problems/remove-nth-node-from-end-of-list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = dummy

        for _ in range(n-1):
            head = head.next

        while head.next:
            head = head.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next