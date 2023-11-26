from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n_hops = 0
        if head is None:
            return False

        cur = head
        while n_hops < 1e4:
            cur = cur.next
            if cur is None:
                return False
            n_hops += 1

        return True

    def hasCycle_2pt(self, head: Optional[ListNode]) -> bool:
        """Two pointer (slow, fast)"""
        slow, fast = head, head
        if slow is None:
            return False

        while True:
            # Next slow is the child
            slow = slow.next

            # Next fast is the grandchild (if it exists)
            fast = fast.next
            if fast is not None and fast.next is not None:
                fast = fast.next
            else:
                # if it doesn't exist, return False because we're at the end of the list
                return False

            if fast == slow:
                # if slow and fast meet, there was a cycle
                return True

