class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions =  {
                   1: [(0,1), (0,-1)],
                   2: [(1,0), (-1,0)],
                   3: [(0,-1), (1,0)],
                   4: [(0,1), (1,0)],
                   5: [(0,-1), (-1,0)],
                   6: [(-1,0), (0,1)]
                  }
        
        visited = set((0, 0))
        
        def isBounded(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(i, j):
            if [i, j] == [len(grid)-1, len(grid[0]) - 1]:
                return True
            
            for r, c in directions[grid[i][j]]:
                nr, nc = i + r, j + c
                if isBounded(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if (-1*r, -1*c) in directions[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True
            
            return False
        
        return dfs(0,0)