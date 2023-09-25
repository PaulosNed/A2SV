class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        ps = 0
        chosen = []
        for i in range(len(satisfaction) - 1, -1, -1):
            if satisfaction[i] + ps > 0:
                chosen.append(satisfaction[i])
                ps += satisfaction[i]
        
        chosen.reverse()
        ans = 0
        for idx, num in enumerate(chosen):
            ans += ((idx + 1) * num)
        
        return ans
            