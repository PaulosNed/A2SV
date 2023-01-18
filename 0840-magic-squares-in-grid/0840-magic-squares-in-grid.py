class Solution:
    def handleRows(self, surrounding, grid, r, c):
        if grid[r][c] not in surrounding:   
            return False
        if set([grid[r][c-1],grid[r][c],grid[r][c+1]]) != surrounding[grid[r][c]]:
            return False
        surrounding.pop(grid[r][c])
        return True
    
    def handleCols(self, surrounding, grid, r, c):
        if grid[r][c] not in surrounding:
            return False
        if set([grid[r-1][c], grid[r][c], grid[r+1][c]]) != surrounding[grid[r][c]]:
            return False
        surrounding.pop(grid[r][c])
        return True
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        rs = 0
        while (rs+2 < len(grid)):
            cs = 0
            while(cs+2 < len(grid[0])):
                surrounding = {1:{1,8,6}, 3:{3,4,8}, 7:{7,2,6} ,9:{9,2,4}}
                if grid[rs+1][cs+1] != 5:
                    cs += 1
                    continue
                if not self.handleCols(surrounding, grid, rs+1, cs):
                    cs += 1
                    continue
                if not self.handleCols(surrounding, grid, rs+1, cs+2):
                    cs += 1
                    continue
                if not self.handleRows(surrounding, grid, rs, cs+1):
                    cs += 1
                    continue
                if not self.handleRows(surrounding, grid, rs+2, cs+1):
                    cs += 1
                    continue
                ans += 1
                cs += 1
            rs += 1
        return ans