class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        converter = {}
        i = 0
        
        for start, end in equations:
            
            if start not in converter:
                converter[start] = i
                i += 1
            
            if end not in converter:
                converter[end] = i
                i += 1
            
        grid = [[float('inf') for _ in range(len(converter))]  for _ in range(len(converter)) ]
        
        for i in range(len(equations)):
            start, end = equations[i]
            
            grid[converter[start]][converter[end]] = values[i]
            grid[converter[end]][converter[start]] = 1 / values[i]
            
        for k in range(len(grid)):
            for i in range(len(grid)):
                for j in range(len(grid)):
                    
                    if i == j:
                        grid[i][j] = 1
                        continue
                        
                    grid[i][j] = min(grid[i][j], grid[i][k] * grid[k][j])
        
        ans = []
        for start, end in queries:
            if start not in converter or end not in converter:
                ans.append(-1)
                continue
                
            val = grid[converter[start]][converter[end]]
            ans.append(val if val != float(inf) else -1)
        
        return ans
            
            
            
            