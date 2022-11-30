from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __preorder_recursive(self, node, res):
        if not node:
            return

        res.append(node.val)
        self.__preorder_recursive(node.left, res)
        self.__preorder_recursive(node.right, res)

    def preorder_recursive(self, root):
        res = []
        self.__preorder_recursive(root, res)

        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.preorder_recursive(root)

        res = []
        stack = [root]

        while stack:
            curr_node = stack.pop()
            if curr_node:
                res.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)

        return res
