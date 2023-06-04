class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        
        graph = defaultdict(list)
        for dis in dislikes:
            graph[dis[0]].append(dis[1])
            graph[dis[1]].append(dis[0])
        
        groups = defaultdict(int)
        visited = set()
        def dfs(stack, group):
            if not stack:
                return True
            
            for op in stack:
                if op in visited:
                    if groups[op] == group:
                        return False                
                    else:
                        continue
                
                groups[op] = -1 if group == 1 else 1
                visited.add(op)
                if not dfs(graph[op], groups[op]):
                    return False
                
            return True
        
        ans = True
        for key in graph:
            if key not in visited:
                visited.add(key)
                groups[key] = 1
                ans = ans and dfs(graph[key], 1)
        
        return ans
        
        
        
        
        