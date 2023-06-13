class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue         
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i].append(j)
         
        def dfs(curr, visited):
            visited.add(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    dfs(neighbour, visited)
            return len(visited)
        
        answer = 1
        for i in range(len(bombs)):
            answer = max(answer, dfs(i, set()))
        
        return answer