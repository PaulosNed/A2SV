class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for source, target, weight in times:
            graph[source].append((target, weight))
        
        distance = {}
        visited = set()
        
        
        heap = [(0, k)]
        while heap:
            time, node = heappop(heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            distance[node] = time
            
            for nei, wei in graph[node]:
                heappush(heap, (time + wei, nei))
        
        if len(visited) != n:
            return -1
        
        return max(distance.values())
                
            
            
            
        
        