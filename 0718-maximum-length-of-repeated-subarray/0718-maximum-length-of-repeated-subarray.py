class Solution:
    def findLength(self, user1: List[int], user2: List[int]) -> int:
        n1 = len(user1)
        n2 = len(user2)
        maxx = 0
        dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if user1[i-1] == user2[j-1] :
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                maxx = max(maxx, dp[i][j])
        
        return maxx    