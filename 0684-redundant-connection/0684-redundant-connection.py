class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        parent = [i for i in range(len(edges))]
        rank = [1] * len(edges)
        ans = None
        
        for s, d in edges:
            parent1 = find(s-1)
            parent2 = find(d-1)
            
            if parent1 == parent2:
                ans = [s, d]
            
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                parent[d-1] = parent1
            else:
                parent[parent1] = parent2
                parent[s-1] = parent2
        
        return ans