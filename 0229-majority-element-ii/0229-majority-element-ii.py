class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        ans = []
        limit = len(nums) // 3
        
        for key in count:
            if count[key] > limit:
                ans.append(key)
        
        return ans