from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        res = head
        res_last = res
        prev_val = res_last.val
        curr = res
        while curr is not None:
            if prev_val == curr.val:
                curr = curr.next
                if curr is None:
                    res_last.next = None
            else:
                prev_val = curr.val
                res_last.next = curr
                res_last = curr
                curr = curr.next

        return res

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Less space"""
        curr = head
        while curr and curr.next:
            # if current val is the same as the next one
            if curr.val == curr.next.val:
                # skip to next.next
                curr.next = curr.next.next
            else:
                # otherwise move to the next
                curr = curr.next

        return head
