class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c]:
                    if self.dfs(grid1, grid2, r, c):
                        count += 1
        
        return count
        
    def dfs(self, grid1, grid2, r, c):
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        stack = [(r, c)]
        flag = True
        
        while stack:
            cr, cc = stack.pop()
            if 0 <= cr < len(grid2) and 0 <= cc < len(grid2[0]) and grid2[cr][cc]:
                if not grid1[cr][cc]:
                    flag = False
                
                grid2[cr][cc] = 0
                
                for direction in directions:
                    stack.append(((cr  + direction[0]), (cc  + direction[1])))
        return flag