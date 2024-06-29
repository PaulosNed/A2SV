class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache()
        def helper(i, j):
            if i == 0:
                return grid[i][j]
            else:
                return grid[i][j] + min(moveCost[grid[i - 1][k]][j] + helper(i - 1, k) for k in range(n))
        
        return min(helper(m - 1, j) for j in range(n))