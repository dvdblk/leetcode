from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split(".")
        revisions2 = version2.split(".")

        # zip pads out the shorter version with trailing '0' revisions
        for r1, r2 in zip_longest(revisions1, revisions2, fillvalue=0):
            r1, r2 = int(r1), int(r2)

            if r1 > r2:
                return 1
            elif r1 < r2:
                return -1

        return 0
