class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            match move:
                case "U":
                    x += 1
                case "D":
                    x -= 1
                case "R":
                    y += 1
                case "L":
                    y -= 1

        return x == 0 and y == 0