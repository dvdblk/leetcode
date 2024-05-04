from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        n_boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            elif people[r] <= limit:
                r -= 1
            else:
                l += 1
            n_boats += 1

        return n_boats
