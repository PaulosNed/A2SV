class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        max_cnt = max(count.values())
        
        return max_cnt > 1