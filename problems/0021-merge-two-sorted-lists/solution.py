from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # init first node
        merged_list = ListNode()
        # keep track of which node is last
        last_ptr = merged_list

        # loop until either one of the lists is empty
        while list1 and list2:
            # find the lower value
            new_val = 0
            if list1.val <= list2.val:
                new_val = list1.val
                list1 = list1.next
            else:
                new_val = list2.val
                list2 = list2.next

            # create and append the lower value to the merged list
            new_node = ListNode(val=new_val)
            last_ptr.next = new_node
            # update last pointer to be the new node
            last_ptr = new_node

        # take care of the rest of the list
        if list1:
            last_ptr.next = list1
        elif list2:
            last_ptr.next = list2

        return merged_list.next