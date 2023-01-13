class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[0]*(len(grid[0])-2) for _ in range(len(grid)-2)]
        rs = 0
        cs = 0
        while (rs+2 < len(grid)):
            cs = 0
            while(cs+2 < len(grid[0])):
                currMax = 0
                for r in range(rs,rs+3):
                    for c in range(cs, cs+3):
                        currMax = max(currMax, grid[r][c])
                ans[rs][cs] = currMax
                cs += 1
            rs += 1
        return ans