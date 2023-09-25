class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        pairs = [(scores[i], ages[i]) for i in range(len(scores))]
        
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))]
        
        for i in range(len(pairs) - 2, -1, -1):
            
            max_val = pairs[i][0]
            for j in range(i+1, len(pairs)):
                if pairs[j][1] >= pairs[i][1]:
                    max_val = max(max_val, pairs[i][0] + dp[j])
                    
            dp[i] = max_val
        
        return max(dp)