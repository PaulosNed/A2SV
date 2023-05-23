class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        name = {}

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
        
        for account in accounts:
            for email in account[1:]:
                parent[email] = email
                rank[email] = 1
                name[email] = account[0]
        
        for account in accounts:
            for i in range(2, len(account)):
                union(account[i], account[i-1])
        
        # print(parent)
        
        ans = defaultdict(list)
        for email in parent:
            rep = find(email)
            ans[rep].append(email)
        
        final = []
        
        for key, val in ans.items():
            curr = [name[key]]
            val.sort()
            curr.extend(val)
            final.append(curr)
        
        return final
            
                