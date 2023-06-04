class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        graph = {}
        visited = set()
        
        for r in range(len(isConnected)):
            neighbours = []
            for c, col in enumerate(isConnected[r]):
                if col:
                    neighbours.append(c)
            graph[r] = neighbours
        
        def dfs(stack):
            nonlocal count
            
            count += 1
            while stack:
                curr = stack.pop()
                
                if curr in visited:
                    continue
                
                stack.extend(graph[curr])
                visited.add(curr)
        for g in graph:
            if g not in visited:
                dfs(graph[g])
            
        return count