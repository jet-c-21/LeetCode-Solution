from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_ls = []
        node = head
        while node:
            val_ls.append(node.val)
            node = node.next

        node = head
        for i in range(len(val_ls) - 1, -1, -1):
            val = val_ls[i]
            node.val = val
            node = node.next

        return head
