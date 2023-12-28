from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # flatten the input matrix
        nums = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                nums.append(mat[i][j])

        # verify new matrix can be constructed
        if r * c != len(nums):
            return mat

        # construct new matrix
        res = []
        a = 0
        for i in range(0, r):
            res.append(nums[i * c : (i + 1) * c])

        return res
