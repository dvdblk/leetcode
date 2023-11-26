from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """Naive"""
        def length(node):
            if node is None:
                return 0
            return 1 + length(node.next)

        len_a = length(headA)
        len_b = length(headB)
        # Get maximum possible intersection length
        intersection_max_length = min(len_a, len_b)

        # Get starting nodes
        curr_a = headA
        if len_a > intersection_max_length:
            for _ in range(len_a-intersection_max_length):
                curr_a = curr_a.next

        curr_b = headB
        if len_b > intersection_max_length:
            for _ in range(len_b-intersection_max_length):
                curr_b = curr_b.next

        # Iterate until they meet
        while curr_a and curr_b:
            if curr_a == curr_b:
                return curr_a
            else:
                curr_a = curr_a.next
                curr_b = curr_b.next