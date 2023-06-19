class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        ans = [i for i in range(len(quiet))]
        
        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
        
        queue = deque([])
        visited = set()
        for i in range(len(quiet)):
            if not indegree[i]:
                queue.append(i)
                visited.add(i)
        
        while queue:
            curr = queue.popleft()
            
            for n in graph[curr]:
                if quiet[ans[curr]] < quiet[ans[n]]:
                    ans[n] = ans[curr]
                
                indegree[n] -= 1
                
                if not indegree[n]:
                    queue.append(n)
                    visited.add(n)
        
        return ans