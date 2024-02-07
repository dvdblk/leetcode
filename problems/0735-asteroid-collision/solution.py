from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Solution if the asteroids were on an orbit or a circular row..."""
        stack = []
        i = 0
        while i < len(asteroids):
            current_asteroid = asteroids[i]
            if not stack:
                stack.append(current_asteroid)
            else:
                collision = current_asteroid < 0 and stack[-1] > 0
                if collision:
                    last_asteroid = stack.pop()
                    if last_asteroid > abs(current_asteroid):
                        stack.append(last_asteroid)
                    elif last_asteroid == abs(current_asteroid):
                        pass
                    else:
                        continue
                else:
                    stack.append(current_asteroid)
            i += 1

        return stack
