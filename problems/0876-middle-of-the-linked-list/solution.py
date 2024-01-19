# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # compute length of list
        length = 1
        curr = head
        while curr.next is not None:
            length += 1
            curr = curr.next

        # get the middle node
        mid_node_i = length // 2
        res = head
        for _ in range(mid_node_i):
            res = res.next

        return res

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Fast and slow O(n)"""
        slow = fast = head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


