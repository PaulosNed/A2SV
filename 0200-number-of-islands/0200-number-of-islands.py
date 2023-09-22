class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def isBounded(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                return True
            
            return False
        
        def bfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = deque([(r, c)])
            
            while queue:
                row, col = queue.popleft()
                
                for mr, mc in directions:
                    nr, nc = row + mr, col + mc
                    
                    if isBounded(nr, nc) and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"
                
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] = "0"
                    bfs(i,j)
        
        return cnt