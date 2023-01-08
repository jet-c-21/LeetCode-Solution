class Solution:
    def isValid(self, s: str) -> bool:
        cto_dict = {')': '(', ']': '[', '}': '{'}
        open_stack = []
        for c in s:
            if c not in cto_dict:
                open_stack.append(c)
                continue

            if open_stack and cto_dict[c] == open_stack[-1]:
                open_stack.pop()
            else:
                return False

        return not open_stack
