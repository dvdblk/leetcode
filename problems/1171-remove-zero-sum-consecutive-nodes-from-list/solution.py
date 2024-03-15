from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix_sum = 0
        d = {0: dummy}

        while head:
            prefix_sum += head.val
            d[prefix_sum] = head
            head = head.next

        head = dummy
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            head.next = d[prefix_sum].next
            head = head.next

        return dummy.next
