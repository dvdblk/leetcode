from typing import Optional, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. find middle of the list with tortoise/hare or slow/fast pointers
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        head_second = slow

        # 2. reverse the second half
        prev, curr = None, head_second

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head_second = prev

        # 3. compare first half and second half
        while head_second is not None:
            if head_second.val != head.val:
                return False

            head = head.next
            head_second = head_second.next

        return True
