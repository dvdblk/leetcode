from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """Recursive solution O(n^2) space & time"""
        if numRows == 1:
            # Base case
            return [[1]]
        else:
            # Recursion
            last_rows = self.generate(numRows-1)
            last_row = last_rows[-1]

            # Create new row with 1 as pre/suffix
            new_row = [1]
            for i in range(len(last_row)-1):
                # Sum up the previous row values
                new_row.append(last_row[i] + last_row[i+1])

            new_row.append(1)
            last_rows.append(new_row)
            return last_rows

    def generate_2(self, numRows: int) -> List[List[int]]:
        """Iterative solution O(n^2)"""
        # Include base case in result
        result = [[1]]

        # Iterate over numRows-1 to add the rest
        for i in range(numRows-1):

            new_row = [1]
            for j in range(i):
                # sum up previous row
                new_row.append(result[i][j] + result[i][j+1])

            new_row.append(1)
            result.append(new_row)
        return result


