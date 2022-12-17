class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        insideLength = len(grid[0])
        length = len(grid)
        row = 0
        column = 0
        maxSum = 0
        while(row+2 < length):
            column = 0
            while(column+2 < insideLength):
                temp = sum(grid[row][column:column+3]) + grid[row+1][column+1] + sum(grid[row+2][column:column+3])
                maxSum = max(maxSum, temp)
                column += 1
            row += 1
        return maxSum