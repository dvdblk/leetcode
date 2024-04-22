from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """BFS with wraparound (mod 10)"""
        deadends = set(deadends)
        visited, queue = set(), deque([(0, "0000")])

        while queue:
            n_steps, node = queue.popleft()
            if node in visited:
                continue

            visited.add(node)

            if node in deadends:
                continue
            elif node == target:
                return n_steps
            else:
                # for each digit in current node,
                # explore in BFS manner in both directions +1 or -1
                for i in range(4):
                    for step in [-1, 1]:
                        n = (int(node[i]) + step) % 10
                        new_node = node[:i] + str(n) + node[i + 1 :]
                        queue.append((n_steps + 1, new_node))

        return -1
