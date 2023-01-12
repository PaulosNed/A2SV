class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for column in range(len(matrix[0])-1,-1,-1):
                if target > matrix[row][column]:
                    break
                if target == matrix[row][column]:
                    return True