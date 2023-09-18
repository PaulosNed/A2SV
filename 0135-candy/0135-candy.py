class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        def findValue(i):
            if 0 <= i < len(ratings):
                return ratings[i]
            
            return float('inf')
        
        def fillValue(i, val):
            for nei in tracker[i]:
                ans[nei] = max(ans[nei], val)
                fillValue(nei, val + 1)
        
        ans = [1] * len(ratings)
        
        tracker = defaultdict(list)
        toBeFilled = []
        
        for i in range(len(ratings)):
            prev = findValue(i - 1)
            nxt = findValue(i + 1)
            
            if ratings[i] <= prev and ratings[i] <= nxt:
                toBeFilled.append(i)
            
            else:
                if ratings[i] > prev:
                    tracker[i-1].append(i)

                if ratings[i] > nxt:
                    tracker[i+1].append(i)
        
        for idx in toBeFilled:
            fillValue(idx, ans[idx] + 1)
         
        return sum(ans)