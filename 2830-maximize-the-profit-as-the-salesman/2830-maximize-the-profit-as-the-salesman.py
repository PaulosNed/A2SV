class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        groups = [[] for _ in range(n)]
        for start, end, gold in offers:
            groups[end].append((start, gold))
        
        f = [0] * (n+1)
        for end, x in enumerate(groups):
            f[end+1] = f[end]
            for start, gold in x: 
                f[end+1] = max(f[end+1], f[start] + gold)
                
                
        return f[n]