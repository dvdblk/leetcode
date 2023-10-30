from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations first
        citations.sort()
        # initial h_index is the max value
        h_index = len(citations)

        for i in range(len(citations)):
            # if there are less citations than h_index
            if citations[i] < h_index:
                # reduce the h_index
                h_index -= 1
            else:
                # if there are more citations, all the rest will have more so this is our h_index
                break
        return h_index