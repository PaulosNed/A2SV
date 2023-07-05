class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 1
        elif len(nums) == 2:
            return 1 if nums[0] == nums[1] else 2
        
        ans1 = []
        flag = False
        for i in range(1, len(nums)):
            if flag and nums[i] - nums[i-1] > 0:
                flag = False
                ans1.append(nums[i])
            
            elif not flag and nums[i] - nums[i-1] < 0:
                flag = True
                ans1.append(nums[i])
        
        ans2 = []
        flag = True
        for i in range(1, len(nums)):
            if flag and nums[i] - nums[i-1] > 0:
                flag = False
                ans2.append(nums[i])
            
            elif not flag and nums[i] - nums[i-1] < 0:
                flag = True
                ans2.append(nums[i])
            
        ans = max(len(ans1), len(ans2))
        return ans + 1
                
            