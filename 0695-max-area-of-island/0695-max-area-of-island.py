class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_len = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    max_len = max(max_len, self.dfs(grid, r, c))
        
        return max_len
        
    def dfs(self, grid, r, c):
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        stack = [(r, c)]
        curr_len = 0
        
        while stack:
            cr, cc = stack.pop()
            if 0 <= cr < len(grid) and 0 <= cc < len(grid[0]) and grid[cr][cc]:
                curr_len += 1
                grid[cr][cc] = 0
                
                for direction in directions:
                    stack.append(((cr  + direction[0]), (cc  + direction[1])))
        
        return curr_len