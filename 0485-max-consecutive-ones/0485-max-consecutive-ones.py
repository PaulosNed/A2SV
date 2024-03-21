class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        cnt = 0
        
        for num in nums:
            if not num:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
            
            else:
                cnt += 1 
        
        max_cnt = max(max_cnt, cnt)
        return max_cnt