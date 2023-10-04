class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        distance = [float('inf')] * n
        distance[src] = 0
        
        for source, target, weight in flights:
            graph[source].append((target, weight))
            
        @cache
        def dp(node, cnt):
            nonlocal dst
            
            if cnt > k + 1:
                return float('inf')
            
            if node == dst:
                return 0
            
            ans = float('inf')
            for nei, wei in graph[node]:
                ans = min(ans, wei + dp(nei, cnt + 1))
            
            return ans
        
        ans = dp(src, 0)
        
        return ans if ans != float('inf') else -1
                
                