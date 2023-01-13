class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.add((i,j))
        for zero in zeros:
            for c in range(len(matrix[0])):
                matrix[zero[0]][c] = 0
            for r in range(len(matrix)):
                matrix[r][zero[1]] = 0
        
        