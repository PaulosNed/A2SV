class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        validElement = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in validElement:
                    if validElement[i-j] == matrix[i][j]:
                        continue
                    return False
                else:
                    validElement[i-j] = matrix[i][j]
        return True