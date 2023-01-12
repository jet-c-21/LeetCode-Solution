from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # with tuple: (temp, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                past_t, past_idx = stack.pop()
                res[past_idx] = i - past_idx
            stack.append((t, i))

        return res
