class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        colors = {}
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        count = defaultdict(int)
        
        def bfs(start, end):
            
            if start == end:
                count[start] += 1
                return True
            
            for nei in graph[start]:
                
                if nei not in visited:
                    visited.add(nei)
                    if bfs(nei, end):
                        count[start] += 1
                        return True
                
            
            return False
            
        @cache
        def dp(source, node, canHalf):
            
            ans = 0
            
            if canHalf and node in count:
                
                opt1 = 0
                opt2 = (price[node] * count[node])
                
                for nei in graph[node]:
                    
                    if nei == source:
                        continue
                    
                    
                    # print("before", opt1, opt2, node, nei)
                    opt1 += dp(node, nei, True)
                    opt2 += dp(node, nei , False)
                    
                    # print("after", opt1, opt2, node, nei)
                
                ans = max(opt1, opt2)
                return ans
                
            else:
                for nei in graph[node]:
                    
                    if nei == source:
                        continue
                    
                    # print("before", ans, node, nei)
                    ans += dp(node, nei, True)
                    # print("after", ans)
                
                return ans

            
        for start, end in trips:
            visited = set([start])
            bfs(start, end)
        
        toBeReduced = dp(None, 0, True)
        # print(toBeReduced)
        
        total = 0
        for node in count:
            total += (count[node] * (price[node]))
        
        return total - (toBeReduced // 2)
        
        
        
        
        
        
        
        
        # color the graph @Done
        # iterate through trips to find visited nodes
        # blackCnt and whiteCnt for visited nodes only
        # decide which ones to half
        # iterate through trips again and calculate price
        
        