from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = even_start = head.next
        curr = even
        i = 1
        while curr is not None:
            if i % 2 == 1:
                # odd step
                odd.next = curr.next
                if odd.next is not None:
                    odd = odd.next
            else:
                even.next = curr.next
                even = even.next
            curr = curr.next
            i += 1

        odd.next = even_start
        return head

    def oddEvenList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Slightly revised version of the above. Only three pointers required"""
        if head is None:
            return None

        odd = head
        even = even_start = head.next

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_start
        return head
