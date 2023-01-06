from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l_idx = 0
        r_idx = len(height) - 1
        while l_idx < r_idx:
            area = (r_idx - l_idx) * min(height[l_idx], height[r_idx])
            res = max(res, area)

            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1

        return res
