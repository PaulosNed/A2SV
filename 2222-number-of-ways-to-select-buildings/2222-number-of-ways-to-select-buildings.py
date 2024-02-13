class Solution:
    def numberOfWays(self, s: str) -> int:
        
        ps = defaultdict(int)
        
        ps[int(s[0])] += 1
        oneCount = sum(list(map(int, list(s))))
        zeroCount = len(s) - oneCount
        ans = 0
        
        for i in range(1, len(s)):
            num = int(s[i])
            
            if num:
                ans += ps[0] * (zeroCount - ps[0])
            else:
                ans += ps[1] * (oneCount - ps[1])
            
            ps[num] += 1
        
        return ans
                
        
        