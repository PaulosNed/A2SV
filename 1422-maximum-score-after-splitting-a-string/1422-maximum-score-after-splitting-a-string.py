class Solution:
    def maxScore(self, s: str) -> int:
        count = Counter(s)
        
        
        ans = 0
        count0 = 0
        count1 = count['1']
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                count0 += 1
            
            else:
                count1 -= 1
            
            ans = max(ans, count0 + count1)
        
        return ans