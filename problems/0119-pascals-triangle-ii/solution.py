from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(rowIndex):

            new_row = [1]
            for j in range(i):
                new_row.append(result[j] + result[j+1])

            new_row.append(1)
            result = new_row

        return result