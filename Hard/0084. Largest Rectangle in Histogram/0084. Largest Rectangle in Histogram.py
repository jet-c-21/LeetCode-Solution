from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (index, height)

        for curr_idx, curr_h in enumerate(heights):
            start_idx = curr_idx

            while stack and stack[-1][1] > curr_h:
                past_idx, past_h = stack.pop()
                max_area = max(max_area, past_h * (curr_idx - past_idx))
                start_idx = past_idx  # can extend to left side

            stack.append((start_idx, curr_h))

        for rest_idx, rest_h in stack:
            max_area = max(max_area, rest_h * (len(heights) - rest_idx))

        return max_area
