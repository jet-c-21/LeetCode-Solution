from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx, r_idx = 0, len(nums) - 1

        while r_idx >= l_idx:
            m_idx = (r_idx + l_idx) // 2
            if nums[m_idx] < target:
                l_idx = m_idx + 1
            elif nums[m_idx] > target:
                r_idx = m_idx - 1
            else:
                return m_idx

        return -1
