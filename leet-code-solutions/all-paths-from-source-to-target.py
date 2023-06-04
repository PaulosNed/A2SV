class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        
        def dfs(curr):
            if curr and curr[-1] == len(graph) - 1:
                paths.append(curr[:])
                return
            
            for neighbour in graph[curr[-1]]:
                curr.append(neighbour)
                dfs(curr)
                curr.pop()
        
        dfs([0])
        return paths
            