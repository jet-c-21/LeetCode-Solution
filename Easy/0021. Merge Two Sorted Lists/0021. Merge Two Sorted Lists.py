from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_nd = ListNode()
        curr_nd = dummy_nd
        while list1 and list2:
            if list1.val < list2.val:
                curr_nd.next = list1
                list1 = list1.next
            else:
                curr_nd.next = list2
                list2 = list2.next

            curr_nd = curr_nd.next

        if list1:
            curr_nd.next = list1

        if list2:
            curr_nd.next = list2

        return dummy_nd.next
