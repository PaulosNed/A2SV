class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
        if sum(nums) == 1:
            return 1
        
        elif sum(nums) == 0:
            return 0
        
        cnt = 1
        
        start = 0
        end = 0
        
        while end < len(nums):
            if nums[start] == 0:
                start += 1
                end += 1
            
            elif nums[end] == 0:
                end += 1
            
            else:
                if start == end:
                    end += 1
                    continue
                cnt = cnt * (end - start)
                start = end
                end += 1
        
        return cnt % ((10 ** 9) + 7)
                
            