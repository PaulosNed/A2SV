class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        def BFS(source):
            
            queue = deque([source])
            visited = {source}
            
            while queue:
                curr = queue.popleft()
                
                if curr != source:
                    ancestor[curr].add(source)
                
                for nei in graph[curr]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            
            return False
        
        graph = defaultdict(list)
        ancestor = defaultdict(set)
        
        for p, c in prerequisites:
            graph[p].append(c)
        
        ans = []
        
        for i in range(numCourses):
            BFS(i)
        
        for s, t in queries:
            ans.append(s in ancestor[t])
        
        return ans
                    