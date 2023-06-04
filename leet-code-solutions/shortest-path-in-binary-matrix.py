class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue = deque([(0,0)])
        directions = [(0,-1), (0,1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        count = 0
        visited = {(0, 0)}
        while queue:
            count += 1
            size = len(queue)
            total = 0
            for _ in range(size):
                curr = queue.popleft()
                if curr == (len(grid)-1, len(grid) - 1):
                    return count
                for direction in directions:
                    nxt = (curr[0]-direction[0], curr[1]-direction[1])
                    if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid) and nxt not in visited and grid[nxt[0]][nxt[1]] == 0:
                        queue.append(nxt)   
                        visited.add(nxt)
                
        
        return -1