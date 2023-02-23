class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        matrix.append([0] * len(matrix[0]))
        for i in range(len(matrix)-1):
            matrix[i].append(0)
            for j in range(len(matrix[i])-1):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2] + self.matrix[row1-1][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)