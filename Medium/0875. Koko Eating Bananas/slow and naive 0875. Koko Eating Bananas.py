import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        k_ls = list(range(1, max_k + 1))
        l_idx, r_idx = 0, len(k_ls) - 1
        k = max_k
        while r_idx >= l_idx:
            m_idx = (l_idx + r_idx) // 2

            cost = 0
            for b in piles:
                cost += math.ceil(b / k_ls[m_idx])

            if cost <= h:
                k = min(k, k_ls[m_idx])
                r_idx = m_idx - 1

            else:
                l_idx = m_idx + 1

        return k


if __name__ == '__main__':
    piles = [312884470]
    h = 312884469
    print(Solution().minEatingSpeed(piles, h))
