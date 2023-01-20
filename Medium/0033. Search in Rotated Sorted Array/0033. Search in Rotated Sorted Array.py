from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx, r_idx = 0, len(nums) - 1
        while r_idx >= l_idx:
            m_idx = (l_idx + r_idx) // 2
            if target == nums[m_idx]:
                return m_idx

            # left sorted portion
            if nums[m_idx] >= nums[l_idx]:
                if target > nums[m_idx] or target < nums[l_idx]:
                    l_idx = m_idx + 1
                # target less than nums[m_idx] and target greater than nums[l_idx]
                else:
                    r_idx = m_idx - 1
            # right sorted portion
            else:
                if target < nums[m_idx] or target > nums[r_idx]:
                    r_idx = m_idx - 1
                else:
                    l_idx = m_idx + 1

        return -1
