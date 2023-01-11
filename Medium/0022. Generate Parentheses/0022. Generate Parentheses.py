from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        only add open parenthesis if open < n
        only add close parenthesis if closed < open
        valid IIF open == closed == n
        """
        stack = []
        res = []

        def backtrack(open_n, close_n):
            if open_n == close_n == n:
                res.append(''.join(stack))

            if open_n < n:
                stack.append('(')
                backtrack(open_n + 1, close_n)
                stack.pop()

            if close_n < open_n:
                stack.append(')')
                backtrack(open_n, close_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res
