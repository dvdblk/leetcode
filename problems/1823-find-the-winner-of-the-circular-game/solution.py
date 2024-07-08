class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        class ListNode:
            def __init__(self, val, next):
                self.val = val
                self.next = next

        head = curr = ListNode(1, None)
        for i in range(2, n + 1):
            new = ListNode(i, None)
            curr.next = new
            curr = new
        # loop it and keep track of previous
        curr.next = head
        prev = curr
        curr = head

        for _ in range(n - 1):
            for _ in range(k - 1):
                prev = curr
                curr = curr.next
            # remove curr from: prev -> curr -> next)
            prev.next = curr.next
            curr = curr.next

        return curr.val
