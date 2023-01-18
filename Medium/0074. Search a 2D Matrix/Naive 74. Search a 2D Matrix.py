from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def search_row():
            top, down = 0, m - 1
            while down >= top:
                mid = (top + down) // 2
                if matrix[mid][0] > target and matrix[mid][n - 1] > target:
                    down = mid - 1
                elif matrix[mid][0] < target and matrix[mid][n - 1] < target:
                    top = mid + 1

                elif matrix[mid][0] <= target <= matrix[mid][n - 1]:
                    return mid
            return -1

        row = search_row()
        if row == -1:
            return False

        def search_col():
            l_idx, r_idx = 0, n - 1
            while r_idx >= l_idx:
                m_idx = (r_idx + l_idx) // 2
                if matrix[row][m_idx] > target:
                    r_idx = m_idx - 1
                elif matrix[row][m_idx] < target:
                    l_idx = m_idx + 1
                else:
                    return m_idx
            return -1

        col = search_col()
        if col == -1:
            return False

        return True
