from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l_idx, r_idx = 0, len(height) - 1
        l_max, r_max = height[l_idx], height[r_idx]

        while l_idx < r_idx:
            if l_max < r_max:
                l_idx += 1
                water = l_max - height[l_idx]
                if water > 0:
                    res += water
                l_max = max(l_max, height[l_idx])

            else:
                r_idx -= 1
                water = r_max - height[r_idx]
                if water > 0:
                    res += water
                r_max = max(r_max, height[r_idx])

        return res
