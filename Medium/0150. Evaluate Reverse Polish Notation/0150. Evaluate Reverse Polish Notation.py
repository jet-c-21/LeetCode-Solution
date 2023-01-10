from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for c in tokens:
            if c == '+':
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif c == '-':
                num_r, num_l = num_stack.pop(), num_stack.pop()
                num_stack.append(num_l - num_r)
            elif c == '*':
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif c == '/':
                num_r, num_l = num_stack.pop(), num_stack.pop()
                num_stack.append(int(num_l / num_r))
            else:
                num_stack.append(int(c))

        return num_stack[0]
