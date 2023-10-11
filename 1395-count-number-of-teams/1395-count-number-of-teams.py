class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        dp = [(0, 0) for _ in range(len(rating))]
        
        cnt = 0
        
        for i in range(len(rating) - 2, -1, -1):
            lowerCnt = 0
            higherCnt = 0
            for j in range(i + 1, len(rating)):
                
                if rating[i] > rating[j]:
                    lowerCnt += 1
                    cnt += dp[j][0]
                
                if rating[i] < rating[j]:
                    higherCnt += 1
                    cnt += dp[j][1]
            
            dp[i] = (lowerCnt, higherCnt)
        
        # print(dp)
        return cnt
                
                
        
        