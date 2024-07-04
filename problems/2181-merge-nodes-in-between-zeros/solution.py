from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        summed_nodes_between_zeros = 0

        head_new = ListNode()
        curr_new = head_new

        while curr is not None:
            if curr.val == 0:
                if summed_nodes_between_zeros > 0:
                    new_node = ListNode(val=summed_nodes_between_zeros)
                    curr_new.next = new_node
                    curr_new = new_node
                    summed_nodes_between_zeros = 0
            else:
                summed_nodes_between_zeros += curr.val
            curr = curr.next

        return head_new.next
