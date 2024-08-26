class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        totalCnt = set()
        visited = set()
        
        def recurse(node):
            nonlocal totalCnt
            
            if len(graph[node]) == 1:
                totalCnt.add(node)
                
            visited.add(node)
            
            ans = 0
            uniqueChilds = set()
            
            for child in graph[node]:
                if child not in visited:
                    curr = recurse(child)
                    uniqueChilds.add(curr)
                    ans = ans + 1 + curr 
                    
            if len(uniqueChilds) == 1:
                totalCnt.add(node)
            
            return ans
        
        recurse(0)
        return len(totalCnt)