class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6] }
        
        @cache
        def dp(num, rem):
            nonlocal ans
            
            if rem == 0:
                return 1
            
            ans = 0
            for nei in moves[num]:
                ans += dp(nei, rem - 1)
            
            return ans
        
        ans = 0
        for i in range(10):
            ans += dp(i, n - 1)
        
        return ans % (10 ** 9 + 7)
                
                    