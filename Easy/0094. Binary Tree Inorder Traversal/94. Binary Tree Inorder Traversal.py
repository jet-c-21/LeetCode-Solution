# coding: utf-8
"""
author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2022-05-21
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.inorder_recursive(root)

        res = []
        stack = []
        curr_node = root

        while curr_node or stack:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left

            curr_node = stack.pop()
            res.append(curr_node.val)
            curr_node = curr_node.right

        return res

    def inorder_recursive(self, root):
        res = []
        return self.__inorder_recursive(root, res)

    def __inorder_recursive(self, root, res):
        if root is None:
            return

        self.__inorder_recursive(root.left, res)
        res.append(root.val)
        self.__inorder_recursive(root.right, res)

        return res
