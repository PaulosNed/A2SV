class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {i:i for i in range(len(s))}
        rank = {i:1 for i in range(len(s))}
        tracker = {i:[s[i]] for i in range(len(s))}
        

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
                for val in tracker[parent2]:
                    heappush(tracker[parent1], val)
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
                for val in tracker[parent1]:
                    heappush(tracker[parent2], val)
        
        for i, j in pairs:
            union(i, j)
        
        # print(tracker, parent)
            
        ans = ""
        for i in range(len(s)):
            rep = find(i)
            curr = heappop(tracker[rep])
            ans += curr
            
        return ans
