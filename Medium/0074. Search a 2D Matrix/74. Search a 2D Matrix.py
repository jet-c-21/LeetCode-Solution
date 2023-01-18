from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top_idx, bot_idx = 0, m - 1
        while bot_idx >= top_idx:
            row = (top_idx + bot_idx) // 2
            if matrix[row][-1] < target:
                top_idx = row + 1
            elif matrix[row][0] > target:
                bot_idx = row - 1
            else:
                break

        if not bot_idx >= top_idx:
            return False

        row = (top_idx + bot_idx) // 2
        l_idx, r_idx = 0, n - 1
        while r_idx >= l_idx:
            col = (l_idx + r_idx) // 2
            if matrix[row][col] < target:
                l_idx = col + 1
            elif matrix[row][col] > target:
                r_idx = col - 1
            else:
                return True

        return False
