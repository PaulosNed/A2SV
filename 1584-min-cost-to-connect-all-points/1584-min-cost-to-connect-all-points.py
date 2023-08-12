  
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        parent = {i:i for i in range(len(points))}
        rank = {i:1 for i in range(len(points))}
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]


        def union(s, d):
            parent1 = find(s)
            parent2 = find(d)

            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
        
        def isConnected(i, j):
            return find(i) == find(j)

        
        distance = []
        
        for i in range(len(points)):
            x1, y1 = points[i]
            
            for j in range(i + 1, len(points)):
                x2 , y2 = points[j]
                dis = abs(x2 - x1) + abs(y2 - y1)
                distance.append((dis , i, j))
        
        distance.sort()
        cost = 0
        for d , i, j in distance:
            if not isConnected(i, j):
                cost += d
                union(i, j)
        
        return cost
        
                
                
                
        