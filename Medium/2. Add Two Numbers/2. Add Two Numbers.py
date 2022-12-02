from typing import Optional, List


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        initial = ListNode()
        curr = initial

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            # record new val
            curr.next = ListNode(val)

            # update pointer
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return initial.next


def print_ls_node(ln: ListNode):
    curr = ln
    while curr:
        print(curr.val, end=', ')
        curr = curr.next
    print()


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = Solution().addTwoNumbers(l1, l2)
    print_ls_node(l3)

    print(l3.val)
