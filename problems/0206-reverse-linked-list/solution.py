from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        # Fill stack
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next
        # Build reversed list
        result = ListNode()
        last = result
        while stack:
            last.next = ListNode(val=stack.pop())
            last = last.next

        return result.next

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        curr = head

        while curr is not None:
            # Swap result first
            prev = result
            result = curr
            curr = curr.next
            result.next = prev

        return result

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        curr = head

        while curr is not None:
            # Swap curr.next first
            nxt = curr.next
            curr.next = result
            result = curr
            curr = nxt

        return result
