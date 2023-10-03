class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        distance = {(0, 0) : grid[0][0]}
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isBound(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                return True
            
            return False
        
        
        heap = [(grid[0][0], 0, 0)]
        max_dis = 0
        
        while heap:
            # print(heap)
            time, x, y = heappop(heap)
            
            if (x, y) in visited:
                continue
                
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return max(grid[x][y], time)
            
            visited.add((x,y))
            distance[(x, y)] = time
            
            for mx, my in directions:
                
                newX, newY = x + mx, y + my
                
                if isBound(newX, newY):
                    heappush(heap, (max(time, grid[newX][newY]), newX, newY))
        
        last = (len(grid) - 1, len(grid[0]) - 1)
        return distance[last]
                    
            
            