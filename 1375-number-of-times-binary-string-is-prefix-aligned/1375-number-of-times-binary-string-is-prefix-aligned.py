class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        flipped = []
        cnt = 0
        
        for i in flips:
            idx = i
            heappush(flipped, -idx)
            
            if len(flipped) == -flipped[0]:
                cnt += 1
        
        return cnt
            
            
            