class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        distance = {(0, 0): 0}
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def isBound(r, c):
            if 0 <= r < len(heights) and 0 <= c < len(heights[0]):
                return True
            
            return False
        
        
        heap = [(0, 0, 0)]
        while heap:
            height, row, col = heappop(heap)
            
            if (row, col) in visited:
                continue
            
            if (row, col) == (len(heights) - 1, len(heights[0]) - 1):
                return height
            
            visited.add((row, col))
            distance[(row, col)] = height
            
            for mr, mc in directions:
                
                newR, newC = row + mr, col + mc
                
                if isBound(newR, newC):
                    diff = abs(heights[newR][newC] - heights[row][col])
                    heappush(heap, (max(diff, height), newR, newC))
        
        # lastR, lastC = len(heights) - 1, len(heights[0]) - 1
        # return distance[(lastR, lastC)]
            
                