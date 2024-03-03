from collections import defaultdict
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Hashmap"""
        curr = head
        i = 0
        nodes = defaultdict(lambda: None)
        while curr is not None:
            i += 1
            nodes[i] = curr
            curr = curr.next

        if i > n:
            nodes[i - n].next = nodes[i - n + 2]
        elif i == n:
            return head.next

        return head

     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """two pointers one pass"""
        dummy = ListNode()
        dummy.next = head

        first, second = dummy, dummy

        for _ in range(n+1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next