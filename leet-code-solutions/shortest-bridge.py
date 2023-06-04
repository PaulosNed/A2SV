class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                if 0 <= cr < len(grid) and 0 <= cc < len(grid[0]) and grid[cr][cc]:
                    queue.append((cr, cc))
                    visited.add((cr, cc))
                    grid[cr][cc] = 0

                    for direction in directions:
                        stack.append(((cr  + direction[0]), (cc  + direction[1])))

            return
        
        
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        queue = deque([])
        visited = set()
        flag = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and flag:
                    flag = False
                    dfs(i,j)
                    
        
        count = 0
        while queue:
            size = len(queue)
            count += 1
            
            for _ in range(size):
                curr = queue.popleft()
                if grid[curr[0]][curr[1]]:
                    return count - 2
                
                for direction in directions:
                    nxt = (curr[0]-direction[0], curr[1]-direction[1])
                    if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]) and nxt not in visited:
                        queue.append(nxt)   
                        visited.add(nxt)
        
        return count - 2
        