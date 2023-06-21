class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for n1, n2 in adjacentPairs:
            graph[n1].append(n2)
            graph[n2].append(n1)
            indegree[n1] += 1
            indegree[n2] += 1
        
        queue = deque([])
        visited = set()
        for key in indegree:
            if indegree[key] == 1:
                queue.append(key)
                visited.add(key)
                break
                
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            
            for nei in graph[curr]:
                indegree[nei] -= 1
                if nei not in visited and indegree[nei] <= 1:
                    queue.append(nei)
                    visited.add(nei)
        
        return ans