class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        cnt = {}
        prev = {}
        ans = [0] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in prev:
                prev[nums[i]] = i
                cnt[nums[i]] = 1
            
            else:
                ans[i] = prev[nums[i]] - (cnt[nums[i]] * i)
                prev[nums[i]] += i
                cnt[nums[i]] += 1
        
        
        cnt = {}
        prev = {}
        ans2 = [0] * len(nums)
        
        for i in range(len(nums)):
            if nums[i] not in prev:
                prev[nums[i]] = i
                cnt[nums[i]] = 1
            
            else:
                ans2[i] = abs(prev[nums[i]] - (cnt[nums[i]] * i))
                prev[nums[i]] += i
                cnt[nums[i]] += 1
        
        final = []
        for i in range(len(ans)):
            final.append(ans[i] + ans2[i])
        
        return final