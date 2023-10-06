class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = [[] for _ in range(n)]
        distance = [float("inf") for _ in range(n)]
        visited = set()
        
        
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        heap = [(-1, start_node)]
        while heap:
            # print(heap)
            prob, node = heappop(heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            distance[node] = -prob
            
            for nei, neiProb in graph[node]:
                heappush(heap, (prob * neiProb, nei))
        
        return distance[end_node] if distance[end_node] != float("inf") else 0
                
        
        
        