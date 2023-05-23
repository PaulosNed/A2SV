class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        rank = {}
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]


        def union(s, d):
            parent1 = find(s)
            parent2 = find(d)
            # print(s, d, parent1, parent2)

            if parent1 == parent2:
                return

            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]

        
        for i in range(97, 123):
            parent[chr(i)] = chr(i)
            rank[chr(i)] = 1
        
        for equation in equations:
            if equation[1] == '=':
                union(equation[0], equation[3])
        
        for equation in equations:
            if equation[1] == '!' and find(equation[0]) == find(equation[3]):
                return False
        
        return True
        
        
        