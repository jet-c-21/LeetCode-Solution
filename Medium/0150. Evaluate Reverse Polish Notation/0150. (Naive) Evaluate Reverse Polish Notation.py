from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_set = {'+', '-', '*', '/'}
        num_stack = []
        for c in tokens:
            if c not in op_set:
                num_stack.append(int(c))
                continue

            num_r = num_stack.pop()
            num_l = num_stack.pop()
            if c == '+':
                num_stack.append(num_l + num_r)
            elif c == '-':
                num_stack.append(num_l - num_r)
            elif c == '*':
                num_stack.append(num_l * num_r)
            else:
                num_stack.append(int(num_l / num_r))

        return num_stack[0]
