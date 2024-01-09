class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def check_elem(i, j, val) -> bool:
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
                return True
            else:
                return matrix[i][j] == val

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not check_elem(i+1, j+1, matrix[i][j]):
                    return False

        return True

    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:
        """Shortened"""
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True