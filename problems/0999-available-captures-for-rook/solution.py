class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == "R":
                    # find rook first
                    rook = x, y
                    # check all directions from here
                    captures = 0
                    # south
                    for i in range(x, len(board)):
                        if board[i][y] == "p":
                            captures += 1
                            break
                        elif board[i][y] == "B":
                            break
                    # north
                    for i in range(x, -1, -1):
                        if board[i][y] == "p":
                            captures += 1
                            break
                        elif board[i][y] == "B":
                            break
                    # east
                    for i in range(y, len(board[x])):
                        if board[x][i] == "p":
                            captures += 1
                            break
                        elif board[x][i] == "B":
                            break
                    # west
                    for i in range(y, -1, -1):
                        if board[x][i] == "p":
                            captures += 1
                            break
                        elif board[x][i] == "B":
                            break

                    return captures

        return 0