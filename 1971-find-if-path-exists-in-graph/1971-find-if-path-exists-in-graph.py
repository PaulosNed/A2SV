class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        parent = [i for i in range(n)]
        rank = [1] * n
        
        for s, d in edges:
            parent1 = find(s)
            parent2 = find(d)
            
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
        
        return find(source) == find(destination)
            