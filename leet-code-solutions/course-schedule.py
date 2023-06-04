class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for nxt, pre in prerequisites:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        
        queue = deque()
        visited =set()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
                visited.add(i)
        
        
        while queue:
            curr = queue.pop()
            
            for neighbour in graph[curr]:
                indegree[neighbour] -= 1
                
                if not indegree[neighbour]:
                    queue.append(neighbour)
                    visited.add(neighbour)
        
        return len(visited) == numCourses
        