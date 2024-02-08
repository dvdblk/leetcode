class Solution:
    def numSquares(self, n: int) -> int:
        """BFS with memoization"""
        # create a decreasing range of perfect squares
        closest_perfect_square = int(sqrt(n))
        perfect_squares = [i*i for i in range(closest_perfect_square, 0, -1)]

        # BFS queue
        queue = deque()
        visited = set()

        def bfs(agg_sum, level, starting_idx):
            for i in range(starting_idx, len(perfect_squares)):
                new_sum = agg_sum + perfect_squares[i]
                if new_sum == n:
                    return level
                elif new_sum > n:
                    # don't continue into another level from this node
                    pass
                else:
                    # continue to another level from this node
                    queue.append((agg_sum + perfect_squares[i], level+1, i))

            return None

        res = bfs(0, 1, 0)
        while queue:
            new_sum, next_level, i = queue.popleft()

            if (new_sum, next_level, i) not in visited:
                res = bfs(new_sum, next_level, i)
                visited.add((new_sum, next_level, i))

                # immediately return the result if it exists, otherwise continue BFS
                if res is not None:
                    return res

        return res

    def numSquares(self, n: int) -> int:
        """DP bottom-up

        Note: How many perfect squares does it take to reach each element i in range 1 to n? Start from 1 and build up.
        """
        # start with "it takes n squares to reach n"
        dp = [n] * (n+1)
        # it takes 0 squares to reach 0
        dp[0] = 0

        # create an increasing range of perfect squares
        closest_perfect_square = int(sqrt(n))
        perfect_squares = [i*i for i in range(1, closest_perfect_square+1)]

        for i in range(1, n+1):
            for perfect_square in perfect_squares:
                if i < perfect_square:
                    break
                dp[i] = min(dp[i], 1 + dp[i - perfect_square])

        return dp[n]
