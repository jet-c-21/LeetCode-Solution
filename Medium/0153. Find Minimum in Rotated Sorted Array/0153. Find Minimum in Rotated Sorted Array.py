from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l_idx, r_idx = 0, len(nums) - 1
        while r_idx >= l_idx:
            if nums[l_idx] < nums[r_idx]:
                res = min(res, nums[l_idx])
                break

            m_idx = (l_idx + r_idx) // 2
            res = min(res, nums[m_idx])
            if nums[m_idx] >= nums[l_idx]:
                l_idx = m_idx + 1  # search right side
            else:
                r_idx = m_idx - 1  # search left side

        return res
