class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def dp(idx, curr):
            if idx >= len(requests):
                if len(set(curr)) == 1 and curr[0] == 0:
                    return 0
                
                return float('-inf')
            
            option1 = dp(idx+1, curr[:])
            
            req = requests[idx]
            curr[req[0]] -= 1
            curr[req[1]] += 1
            
            option2 = 1 + dp(idx+1, curr[:])
            
            curr[req[0]] += 1
            curr[req[1]] -= 1
            
            return max(option1, option2)
            
        curr = [0] * n
        return dp(0, curr)