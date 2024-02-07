from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(n) two passes"""
        # count number of nodes
        n_nodes = 0
        curr = head
        while curr is not None:
            n_nodes += 1
            curr = curr.next

        if n_nodes == 1:
            return None

        # drop middle one
        mid = n_nodes // 2
        curr = head
        for _ in range(mid - 1):
            # traverse to the parent of the middle node
            curr = curr.next
        # set the midparent.next to mid.next
        curr.next = curr.next.next

        return head

    def deleteMiddle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Fast and slow pointers"""
        if head.next is None:
            return None

        dummy_node = ListNode(val=None, next=head)
        slow = fast = dummy_node

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head
