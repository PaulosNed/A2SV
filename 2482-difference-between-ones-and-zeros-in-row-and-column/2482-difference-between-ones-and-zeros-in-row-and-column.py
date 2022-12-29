class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        length = len(matrix)
        insideLength = len(matrix[0])
        final = [ [0] * length for _ in range(insideLength)]
        for i in range(length):
            for j in range(insideLength):
                final[j][i] = matrix[i][j]
        return final
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        final = [[0] * len(grid[0]) for _ in range(len(grid))]
        oneRow = [[0] * len(grid)]*len(grid[0])
        zeroRow = [[0] * len(grid)]*len(grid[0])
        oneColumn = [[0] * len(grid[0])]*len(grid)
        zeroColumn = [[0] * len(grid[0])]*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    oneColumn[i][j] += 1
                    oneRow[j][i] += 1
                else:
                    zeroColumn[i][j] += 1
                    zeroRow[j][i] += 1
        oneRow = self.transpose(oneRow)
        zeroRow = self.transpose(zeroRow)
        for i in range(len(final)):
            for j in range(len(final[i])):
                final[i][j] = oneRow[i][j] + oneColumn[i][j] - zeroRow[i][j] - zeroColumn[i][j]
        return final
                
                
                
                