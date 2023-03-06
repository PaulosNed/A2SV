class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 1:
            return 0
        elif len(grid[0]) == 2:
            return min(grid[0][1], grid[1][0])
        gridPs = [ [0] * len(grid[0]) for _ in range(2)]
        for r in range(2):
            for c in range(len(grid[0])-1, -1, -1):
                prev = 0 if c + 1 >= len(gridPs[0]) else gridPs[r][c+1]
                gridPs[r][c] += grid[r][c] + prev
        min_ = float("inf")
        r = 0
        c = 1
        while(c < len(gridPs[0]) and gridPs[0][c + 1] > gridPs[1][0] - gridPs[1][c]):
            c += 1
            if c + 1 == len(gridPs[0]):
                return min(gridPs[0][-1], gridPs[1][0] - gridPs[1][-1])
        
        return min(gridPs[0][c], gridPs[1][0] - gridPs[1][c])