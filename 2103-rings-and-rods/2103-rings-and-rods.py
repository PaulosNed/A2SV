class Solution:
    def countPoints(self, rings: str) -> int:
        tracker = defaultdict(set)
        
        for i in range(1, len(rings), 2):
            tracker[int(rings[i])].add(rings[i-1])
        
        cnt = 0
        for ring in tracker:
            if len(tracker[ring]) == 3:
                cnt += 1
        
        return cnt