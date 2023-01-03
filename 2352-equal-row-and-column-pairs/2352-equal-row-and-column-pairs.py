class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        length = len(matrix)
        insideLength = len(matrix[0])
        final = [ [0] * length for _ in range(insideLength)]
        for i in range(length):
            for j in range(insideLength):
                final[j][i] = matrix[i][j]
        return final
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = self.transpose(grid)
        start = 0
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i] == transpose[j]:
                    ans += 1
        return ans