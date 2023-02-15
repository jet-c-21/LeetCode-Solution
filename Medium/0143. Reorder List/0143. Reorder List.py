# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2023-02-15
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        s = ''
        curr = self
        while curr:
            s += f"{curr.val} "
            curr = curr.next

        s += f"{curr}"
        return f"[{s}]"


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node
        slow_nd = head
        fast_nd = head.next
        while fast_nd and fast_nd.next:
            slow_nd = slow_nd.next
            fast_nd = fast_nd.next.next

        # print(slow_nd.val)  # 3
        # print(fast_nd)  # None

        # reverse second half
        second_tail = slow_nd.next
        slow_nd.next = None  # split the node list

        prev_nd = None
        curr_nd = second_tail
        while curr_nd:
            next_nd = curr_nd.next

            curr_nd.next = prev_nd
            prev_nd = curr_nd
            curr_nd = next_nd

        second_head = prev_nd
        first_head = head
        while second_head:
            temp1, temp2 = first_head.next, second_head.next
            first_head.next = second_head
            second_head.next = temp1
            first_head, second_head = temp1, temp2


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    Solution().reorderList(n1)
