from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def helper(i, j, w):
            if (
                not (0 <= i < len(board) and 0 <= j < len(board[i]))
                or visited[i][j]
                or w[0] != board[i][j]
            ):
                return False
            elif w == board[i][j]:
                return True
            else:
                visited[i][j] = True
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                result = any(map(lambda x: helper(i + x[0], j + x[1], w[1:]), dirs))
                visited[i][j] = False
                return result

        for i in range(len(board)):
            for j in range(len(board[i])):
                if helper(i, j, word):
                    return True

        return False
