from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """O(n*k) time, O(1) space"""
        dummy = ListNode()
        curr = dummy

        while True:
            smallest_val = 10e5
            smallest_idx = None
            for i, l in enumerate(lists):
                if l and l.val < smallest_val:
                    smallest_idx = i
                    smallest_val = l.val

            if smallest_idx is None:
                break
            smallest = lists[smallest_idx]

            curr.next = smallest
            curr = curr.next
            smallest = smallest.next
            lists[smallest_idx] = smallest

        return dummy.next

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """O(n * log k)"""

        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1 is not None:
                curr.next = l1
            else:
                curr.next = l2

            return dummy.next

        n = len(lists)
        if n == 0:
            return None

        while n > 1:
            for i in range(n // 2):
                l1 = lists[i]
                l2 = lists[n - 1 - i]
                lists[i] = merge(l1, l2)
            n = (n + 1) // 2

        return lists[0]
