class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(s, d):
            s = tuple(s)
            d = tuple(d)
            parent1 = find(s)
            parent2 = find(d)
            # print(s, d, parent1, parent2)

            if parent1 == parent2:
                return
            
            if s[0] == d[0] or s[1] == d[1]:
                if rank[parent1] >= rank[parent2]:
                    parent[parent2] = parent1
                    rank[parent1] += rank[parent2]
                    rank[parent2] = 1
                else:
                    parent[parent1] = parent2
                    rank[parent2] += rank[parent1]
                    rank[parent1] = 1

        for stone in stones:
            stone = tuple(stone)
            parent[stone] = stone
            rank[stone] = 1
            
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                union(stones[i], stones[j])
        
        ans = 0
        for key in rank:
            ans += rank[key] - 1
        
        return ans
        