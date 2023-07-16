class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        def BFS(queue, target):
            visited = {queue[0]}
            while queue:
                curr = queue.popleft()
                
                if curr == target:
                    return True
                
                for nei in graph[curr]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            
            return False
        
        graph = defaultdict(list)
        
        for p, c in prerequisites:
            graph[p].append(c)
        
        ans = []
        
        for source, target in queries:
            ans.append(BFS(deque([source]), target))
        
        return ans
                    