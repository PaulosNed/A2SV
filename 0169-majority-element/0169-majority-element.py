class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        limit = len(nums) // 2
        
        for key in count:
            if count[key] > limit:
                return key