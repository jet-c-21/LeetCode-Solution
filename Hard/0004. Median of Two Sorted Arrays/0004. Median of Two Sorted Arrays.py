from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        short_ls, long_ls = nums1, nums2
        if len(short_ls) > len(long_ls):
            short_ls, long_ls = long_ls, short_ls

        short_l_idx, short_r_idx = 0, len(short_ls) - 1
        while True:
            short_m_idx = (short_l_idx + short_r_idx) // 2
            long_m_idx = (half - (short_m_idx + 1)) - 1

            short_lp_max = short_ls[short_m_idx] if short_m_idx >= 0 else float('-inf')
            short_rp_min = short_ls[short_m_idx + 1] if (short_m_idx + 1) < len(short_ls) else float('inf')
            long_lp_max = long_ls[long_m_idx] if long_m_idx >= 0 else float('-inf')
            long_rp_min = long_ls[long_m_idx + 1] if (long_m_idx + 1) < len(long_ls) else float('inf')

            # partition is correct
            if short_lp_max <= long_rp_min and long_lp_max <= short_rp_min:
                # odd
                if total % 2:
                    return min(short_rp_min, long_rp_min)
                # even
                return (max(short_lp_max, long_lp_max) + min(short_rp_min, long_rp_min)) / 2

            elif short_lp_max > long_rp_min:
                short_r_idx = short_m_idx - 1
            else:
                # short right partition min element < long left partition max element
                short_l_idx = short_m_idx + 1

