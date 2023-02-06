from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_nd = ListNode()
        curr_nd = res_nd
        nd1, nd2 = list1, list2
        while nd1 and nd2:
            curr_nd.next = ListNode()
            curr_nd = curr_nd.next
            if nd1.val < nd2.val:
                curr_nd.val = nd1.val
                nd1 = nd1.next
            else:
                curr_nd.val = nd2.val
                nd2 = nd2.next

        if nd1:
            curr_nd.next = nd1

        if nd2:
            curr_nd.next = nd2

        return res_nd.next
