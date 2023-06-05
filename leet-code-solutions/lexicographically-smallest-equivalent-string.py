class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        def find(node):
            if node not in parent:
                return node
            
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        parent = {}
        for letter in s1 + s2:
            parent[letter] = letter
        
        for i in range(len(s1)):
            parent1 = find(s1[i])
            parent2 = find(s2[i])
            
            if parent1 <= parent2:
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2
        
        ans = ""
        for l in baseStr:
            ans += find(l)
            
        return ans
        