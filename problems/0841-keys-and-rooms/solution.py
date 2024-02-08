from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """DFS"""
        # room 0 is always open
        keys = set([0])
        stack = [rooms[0]]

        while stack:
            room = stack.pop()
            for key in room:
                if key not in keys:
                    stack.append(rooms[key])
                    keys.add(key)

        return len(keys) == len(rooms)
