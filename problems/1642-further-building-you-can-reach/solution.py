from heapq import heapify, heappush, heappushpop
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:
            return 0

        distances = []
        for i in range(len(heights)-1):
            distance = max(0, heights[i+1] - heights[i])
            distances.append(distance)

        ladder_distances = []
        heapify(ladder_distances)
        for i in range(len(distances)):
            if len(ladder_distances) < ladders:
                heappush(ladder_distances, distances[i])
            else:
                smolest = heappushpop(ladder_distances, distances[i])
                if bricks - smolest < 0:
                    return i
                bricks -= smolest

        return i + 1