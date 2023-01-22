import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l_speed, r_speed = 1, max(piles)
        res = r_speed

        while r_speed >= l_speed:
            m_speed = (l_speed + r_speed) // 2

            cost = 0
            for p in piles:
                cost += math.ceil(p / m_speed)

            if cost <= h:
                res = min(res, m_speed)
                r_speed = m_speed - 1
            else:
                l_speed = m_speed + 1

        return res
