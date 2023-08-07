class UnionFind:
    
    def __init__(self, n): 
        self.root = list(range(n))
    
    def union(self, x, y): 
        self.root[self.find(x)] = self.find(y)
    
    def find(self, x):
        if x != self.root[x]: 
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        unionFind = UnionFind(len(source))
        
        for x, y in allowedSwaps: 
            unionFind.union(x, y)
            
        tracker = defaultdict(set)
        for i in range(len(source)):
            tracker[unionFind.find(i)].add(i)
            
        ans = 0
        for indices in tracker.values():
            sourcecnt = Counter([source[i] for i in indices])
            targetcnt = Counter([target[i] for i in indices])
            diff = sourcecnt - targetcnt
            ans += sum(diff.values())
        return ans
