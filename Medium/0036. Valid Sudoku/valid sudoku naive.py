from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(len(board)):
            seen_num = set()
            for col_num in board[i]:
                if col_num == '.':
                    continue
                if col_num in seen_num:
                    return False
                else:
                    seen_num.add(col_num)

        # check column
        for i in range(len(board)):
            seen_num = set()
            for j in range(len(board[i])):
                row_num = board[j][i]
                if row_num == '.':
                    continue
                if row_num in seen_num:
                    return False
                else:
                    seen_num.add(row_num)

        # check sub-boxes
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                seen_num = set()
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        num = board[a][b]
                        if num == '.':
                            continue
                        if num in seen_num:
                            return False
                        else:
                            seen_num.add(num)

        return True
