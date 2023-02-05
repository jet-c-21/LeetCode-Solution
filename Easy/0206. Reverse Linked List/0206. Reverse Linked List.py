from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_nd, curr_nd = None, head

        while curr_nd:
            next_nd = curr_nd.next

            curr_nd.next = prev_nd
            prev_nd = curr_nd
            curr_nd = next_nd

        return prev_nd
