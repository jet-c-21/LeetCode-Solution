from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_idx, r_idx = 0, 1  # left = buy, right = sell
        res = 0
        while r_idx < len(prices):
            # profitable
            if prices[l_idx] < prices[r_idx]:
                curr_profit = prices[r_idx] - prices[l_idx]
                res = max(res, curr_profit)
            else:
                l_idx = r_idx

            r_idx += 1

        return res
