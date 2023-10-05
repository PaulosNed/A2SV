class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dominant = None
        
        for key in count:
            if count[key] * 2 > len(nums):
                dominant = key
                break
        
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                cnt += 1
                
                if cnt * 2 > i + 1 and (count[dominant] - cnt) * 2 > len(nums[i+1:]):
                    return i
        
        return -1