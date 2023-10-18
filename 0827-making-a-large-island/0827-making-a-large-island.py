class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        
        def isBound(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                return True
            
            return False
        
        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        def connect(n1, n2):
            parent1 = find(n1)
            parent2 = find(n2)
            
            if parent1 == parent2:
                return
            
            if rank[parent1] >= rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            
        def bfs(r, c):
            
            queue = deque([(r, c)])
            
            while queue:
                
                row, col = queue.popleft()
                connect((r, c), (row, col))
                
                for mr, mc in directions:
                    nr, nc = row + mr, col + mc
                    
                    if isBound(nr, nc) and (nr, nc) not in visited and grid[nr][nc]:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        def findSize(r, c):
            
            cnt = 1
            vis = set()
            
            for mr, mc in directions:
                nr, nc = r + mr, c + mc
                
                if isBound(nr, nc):
                    pr, pc = find((nr, nc))
                    if (pr, pc) not in vis and grid[pr][pc] == 1:
                        vis.add((pr, pc))
                        cnt += rank[(pr, pc)]
            
            return cnt
                    
                    
                    
        max_size = 0
        found = False
        
        parents = {}
        rank = {}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                parents[(i, j)] = (i, j)
                rank[(i, j)] = 1
        
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j]:
                    visited.add((i, j))
                    bfs(i, j)
        
        
        max_len = 0
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    found = True
                    max_len = max(max_len, findSize(i, j))
        
        if not found:
            return len(grid) * len(grid[0])
        
        return max_len