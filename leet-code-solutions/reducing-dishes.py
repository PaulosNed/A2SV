class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        ps = satisfaction[:]
        
        j = len(ps) - 2
        while j >= 0:
            ps[j] += ps[j+1]
            j -= 1
        
        
        i = 0 
        while i < len(satisfaction) - 1:
            if satisfaction[i] + ps[i + 1] > 0:
                break
            
            i += 1
        
        if i == len(satisfaction) - 1:
            return max(0, satisfaction[i])
        
        ans = 0
        for idx in range(i, len(satisfaction)):
            ans += ((idx - i + 1) * satisfaction[idx])
        
        return ans
        