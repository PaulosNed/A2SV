class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        
        def find(node):
            if node != rep[node]:
                rep[node] = find(rep[node])
            return rep[node]
        
        rep = [i for i in range(n)]
        minimum = [float("inf")] * n
        rank = [1] * n
        
        for x, y, d in roads:
            parent1 = find(x-1)
            parent2 = find(y-1)
            
            if rank[parent1] >= rank[parent2]:
                rep[parent2] = parent1
                minimum[parent1] = min(minimum[parent1], d, minimum[parent2])
                rank[parent1] += rank[parent2]
            else:
                rep[parent1] = parent2
                minimum[parent2] = min(minimum[parent2], d, minimum[parent1])
                rank[parent2] += rank[parent1]
        
        return minimum[find(0)]
    
        
                