class Solution:
    def minimumSteps(self, s: str) -> int:
        nums = list(map(int, list(s)))
        zeros = nums.count(0)
        
        start = 0
        end = zeros
        cnt = 0
        
        while end < len(nums):
            if nums[end] == 1:
                end += 1
            
            elif nums[start] == 0:
                start += 1
            
            else:
                cnt += end - start
                end += 1
                start += 1
            
        return cnt
            
            
                