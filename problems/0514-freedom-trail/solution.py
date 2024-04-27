from collections import deque


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """BFS with ring position and key position"""
        visited = set()
        # ring index, key index, number of steps
        queue = deque([(0, 0, 0)])

        while queue:
            ring_idx, key_idx, steps = queue.popleft()
            if key_idx == len(key):
                return steps

            if (ring_idx, key_idx) in visited:
                continue
            visited.add((ring_idx, key_idx))

            if ring[ring_idx] == key[key_idx]:
                queue.append((ring_idx, key_idx + 1, steps + 1))
            else:
                queue.append(((ring_idx + 1) % len(ring), key_idx, steps + 1))
                queue.append(((ring_idx - 1) % len(ring), key_idx, steps + 1))
