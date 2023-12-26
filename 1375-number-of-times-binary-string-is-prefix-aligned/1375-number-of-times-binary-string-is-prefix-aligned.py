class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_val = 0
        idx_cnt = 0
        cnt = 0
        
        for val in flips:
            max_val = max(max_val, val)
            idx_cnt += 1
            
            if idx_cnt == max_val:
                cnt += 1
        
        return cnt
            
            
            