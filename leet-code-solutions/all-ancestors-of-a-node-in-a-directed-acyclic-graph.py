class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        ans = [set() for _ in range(n)]
        
        for start, finish in edges:
            graph[start].append(finish)
            indegree[finish] += 1
        
        queue = deque([])
        for i in range(n):
            if not indegree[i]:
                queue.append(i)
        
        while queue:
            curr = queue.pop()
            
            for neighbour in graph[curr]:
                indegree[neighbour] -= 1
                ans[neighbour].add(curr)
                for ans2 in ans[curr]:
                    ans[neighbour].add(ans2)
                
                if not indegree[neighbour]:
                    queue.append(neighbour)
        
        for i in range(len(ans)):
            ans[i] = sorted(ans[i])
        
        return ans
        
            