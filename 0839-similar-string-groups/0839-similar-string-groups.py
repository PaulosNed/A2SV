class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        def connect(n1, n2):
            parent1 = find(n1)
            parent2 = find(n2)
            
            if parent1 == parent2:
                return
            
            if rank[parent1] <= rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
        
        parents = {s:s for s in strs}
        rank = {s:1 for s in strs}
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                
                cnt = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        cnt += 1
                
                if cnt <= 2:
                    connect(strs[i], strs[j])
        
        ans = set()
        for s in strs:
            parent = find(s)
            ans.add(parent)
        
        return len(ans)