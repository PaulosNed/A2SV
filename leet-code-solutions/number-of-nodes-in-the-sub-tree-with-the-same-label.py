class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        ans = [0] * n 
        visited =set()
        
            
        def backtrack(root, tracker):
            if root in visited:
                return
            
            visited.add(root)
            before = tracker[labels[root]]
            tracker[labels[root]] += 1
            for neighbour in graph[root]:
                if neighbour not in visited:
                    backtrack(neighbour, tracker)
            
            ans[root] += tracker[labels[root]] - before
                       
        
        backtrack(0, defaultdict(int))
        
        return ans
            
            