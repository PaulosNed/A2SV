class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        target = nums[-1]
        ans = 0
        
        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            
            partition = (ceil(curr / target) - 1)
            ans += partition
            target = min(target, curr // (partition + 1))
            
        return ans