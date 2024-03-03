from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_occurences, row_occurences = [], []
        col_occurences = [[0] * 9 for _ in range(9)]

        for row in range(9):
            if row % 3 == 0:
                # reset box occurences if needed (every 3 rows)
                box_occurences = [[0] * 9 for _ in range(3)]

            row_occurences = [0] * 9
            for col in range(9):
                cell = board[row][col]

                if cell != ".":
                    c = int(cell) - 1
                    # Rows
                    if row_occurences[c]:
                        return False
                    row_occurences[c] = 1
                    # Cols
                    if col_occurences[col][c]:
                        return False
                    col_occurences[col][c] = 1
                    # Boxes
                    if box_occurences[col // 3][c]:
                        return False
                    box_occurences[col // 3][c] = 1

        return True
